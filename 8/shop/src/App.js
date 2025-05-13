import React, { useState, useEffect } from "react";
import { BrowserRouter, Routes, Route, Link } from "react-router-dom"; // Import Link for navigation
import ProductList from "./Products";
import Cart from "./Cart";
import { CartProvider } from "./Cart";
import Login from "./Login";
import Logout from "./Logout";
import Cookies from 'js-cookie'


function App() {
  const [isLoggedIn, setIsLoggedIn] = useState(!!Cookies.get('user_id'));
  const handleLoginSuccess = (userId, username) => {
    if (userId) {
      Cookies.set('user_id', userId, { expires: 7, path: '/' });
    }
    if (username) {
      Cookies.set('username', username, { expires: 7, path: '/' });
    }
    setIsLoggedIn(true);
  };

  const handleLogout = () => {
    Cookies.remove('user_id', { path: '/' });
    setIsLoggedIn(false);
  };

  useEffect(() => {
    const verifyAuth = async () => {
      try {
        const response = await fetch('http://localhost:5000/auth/check-auth', {
          method: 'GET',
          credentials: 'include',
        });

        if (response.ok) {
          const data = await response.json();
          if (data.isLoggedIn && data.user_id) {
            handleLoginSuccess(data.user_id, data.username);
          } else {
            Cookies.remove('user_id', { path: '/' });
            setIsLoggedIn(false);
          }
        } else {
          Cookies.remove('user_id', { path: '/' });
          setIsLoggedIn(false);
        }
      } catch (error) {
        console.error("Auth check failed:", error);
        Cookies.remove('user_id', { path: '/' });
        setIsLoggedIn(false);
      }
    };
    verifyAuth();
  }, []);

  if (!isLoggedIn) {
    return (
      <Login onLoginSuccess={handleLoginSuccess}/>
    )
  }
  return(
    <CartProvider>
      <BrowserRouter>
          <header>
            <h1>My Shop</h1>
            <nav>
              <Link to="/">Products</Link> | <Link to="/cart">Cart</Link> | <Link to="/logout">Log out {Cookies.get('username')}</Link>
            </nav>
          </header>
          <main>
            <Routes>
              <Route path="/" element={<ProductList />} />
              <Route path="cart" element={<Cart />} />
              <Route path="logout" element={<Logout onLogoutSuccess={handleLogout} />} />
            </Routes>
          </main>
      </BrowserRouter>
    </CartProvider>
  );
}

export default App;
