from flask import Blueprint, request, jsonify, session, redirect, url_for, make_response, current_app
from werkzeug.security import generate_password_hash, check_password_hash
import os
import jwt
from datetime import datetime, timedelta

from ..database import get_db
from ..extensions import oauth

auth_bp = Blueprint('auth', __name__, url_prefix='/auth')

@auth_bp.route('/register', methods= ['POST'])
def register():
    username = request.form.get('username')
    password = request.form.get('password')
    db = get_db()
    error = None

    if not username:
        error = 'Username is required.'
    elif not password:
        error = 'Password is required.'
    
    if error is None:
        existing_user = db.execute(
            "SELECT id FROM users WHERE username = ?", (username,)
        ).fetchone()

        if existing_user is not None:
            error = f"User {username} is already registered."
        else:
            try:
                db.execute(
                    "INSERT INTO users (username, password) VALUES (?, ?)",
                    (username, generate_password_hash(password)),
                )
                db.commit()
            except db.Error as e:
                error = f"Database error: {e}"
                return jsonify({"error": error}), 500
            else:
                return jsonify({"message": "User registered successfully!"}), 201 # 201 

    return jsonify({"error": error}), 400
    
@auth_bp.route('/login', methods=['POST'])
def login():
    username = request.form.get('username')
    password = request.form.get('password')
    db = get_db()
    error = None
    if not username:
        error = 'username is required.'
    elif not password:
        error = 'Password is required.'
    if error is None:
        user_row = db.execute(
            "SELECT * FROM users WHERE username = ?",
            (username,)
        ).fetchone()
        if user_row is None or not check_password_hash(user_row[2], password): 
            error = 'Incorrect username or password.'
        else:
            session.clear()
            session['user_id'] = user_row[0] 
            session['username'] = user_row[1]
            print(user_row[0])
            response_data = {"message": "Login successful!", "user_id": user_row[0]}
            resp = make_response(jsonify(response_data), 200)
            return resp

    return jsonify({"error": error}), 400
@auth_bp.route('/logout', methods=['POST'])
def logout():
    session.clear()
    return jsonify({"message": "Logged out successfully!"}), 200


@auth_bp.route('/login/google')
def login_google():
    redirect_uri = url_for('auth.authorize_google', _external=True)
    nonce = os.urandom(16).hex()
    print(f"Generated redirect_uri for Google: {redirect_uri}")
    session['google_auth_nonce'] = nonce
    google = oauth.create_client('google')
    return google.authorize_redirect(redirect_uri,nonce=nonce)

@auth_bp.route('/google/callback')
def authorize_google():
    google_client = oauth.create_client('google')
    token = google_client.authorize_access_token()
    nonce = session.pop('google_auth_nonce', None)
    if not nonce:
        return jsonify({"error": "Nonce missing from session or already used."}), 400
    userinfo = google_client.parse_id_token(token, nonce=nonce) 
    session['user_id'] = userinfo['sub']
    session['username'] = userinfo['email']
    return redirect('http://localhost:3000')
@auth_bp.route('/check-auth', methods=['GET'])
def check_auth_status():
    if 'user_id' in session:
        return jsonify({"isLoggedIn": True, "user_id": session['user_id'],"username": session['username']}), 200
    else:
        return jsonify({"isLoggedIn": False}), 401