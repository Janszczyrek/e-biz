import React, { useState } from "react";
import Cookies from "js-cookie";

function Login({ onLoginSuccess }) {
  const [toogleRegister, setToogleRegister] = useState(false);
  const [username, setUsername] = useState("");
  const [password, setPassword] = useState("");
  const [passwordRep, setPasswordRep] = useState("");
  const [error, setError] = useState("");

  const handleRegisterSubmit = async (event) => {
    event.preventDefault();
    if (password !== passwordRep) {
      setError("Passwords do not match!");
      return;
    }
    setError("");

    const formData = new FormData();
    formData.append('username', username);
    formData.append('password', password);

    try {
      const response = await fetch("http://localhost:5000/auth/register", {
        method: "POST",
        body: formData,
      });
      if (response.ok) {
        console.log("Registration successful");
        setToogleRegister(false);
        setUsername("");
        setPassword("");
        setPasswordRep("");
      } else {
        const errorData = await response.json();
        setError(errorData.message || "Registration failed");
      }
    } catch (err) {
      setError("An error occurred during registration.");
      console.error("Registration error:", err);
    }
  };

  if (toogleRegister) {
    return (
      <div>
        <h1>Register</h1>
        {error && <p style={{ color: "red" }}>{error}</p>}
        <form onSubmit={handleRegisterSubmit}>
          <input
            name="username"
            type="text"
            placeholder="Username"
            value={username}
            onChange={(e) => setUsername(e.target.value)}
            required
          />
          <input
            name="password"
            type="password"
            placeholder="Password"
            value={password}
            onChange={(e) => setPassword(e.target.value)}
            required
          />
          <input
            name="password_rep"
            type="password"
            placeholder="Repeat password"
            value={passwordRep}
            onChange={(e) => setPasswordRep(e.target.value)}
            required
          />
          <button type="submit">Register</button>
        </form>
        <div>
          <p>Already have an account?</p>
          <button
            onClick={() => {
              setToogleRegister(!toogleRegister);
              setError("");
              setUsername("");
              setPassword("");
              setPasswordRep("");
            }}
          >
            Login
          </button>
        </div>
      </div>
    );
  }

  const handleLoginSubmit = async (event) => {
    event.preventDefault();
    setError("");

    const formData = new FormData();
    formData.append('username', username);
    formData.append('password', password);

    try {
      const response = await fetch("http://localhost:5000/auth/login", {
        method: "POST",
        body: formData,
        credentials: 'include'
      });

      if (response.ok) {
        setUsername("");
        setPassword("");
        Cookies.set('username', username, { expires: 1 });
        onLoginSuccess();
      } else {
        const errorData = await response.json();
        setError(errorData.message || "Login failed");
      }
    } catch (err) {
      setError("An error occurred during login.");
      console.error("Login error:", err);
    }
  };
  const handleGoogleLogin = async () => {
    window.location.href = "http://localhost:5000/auth/login/google";
  };
  return (
    <div>
      <h1>Login</h1>
      {error && <p style={{ color: "red" }}>{error}</p>}
      <form onSubmit={handleLoginSubmit}>
        <input
          name="username"
          type="text"
          placeholder="Username"
          value={username}
          onChange={(e) => setUsername(e.target.value)}
          required
        />
        <input
          name="password"
          type="password"
          placeholder="Password"
          value={password}
          onChange={(e) => setPassword(e.target.value)}
          required
        />
        <button type="submit">Login</button>
        <button onClick={handleGoogleLogin}>Google login</button>
      </form>
      <div>
        <p>Don't have account?</p>
        <button
          onClick={() => {
            setToogleRegister(!toogleRegister);
            setError("");
            setUsername("");
            setPassword("");
          }}
        >
          Register
        </button>
      </div>
    </div>
  );

}
export default Login;