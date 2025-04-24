import { BrowserRouter, Routes, Route, Link } from "react-router-dom"; // Import Link for navigation
import ProductList from "./Products";
import Cart from "./Cart";
import { CartProvider } from "./Cart";

function App() {
  return (
    <CartProvider>
      <BrowserRouter>
          <header>
            <h1>My Shop</h1>
            <nav>
              <Link to="/">Products</Link> | <Link to="/cart">Cart</Link>
            </nav>
          </header>
          <main>
            <Routes>
              <Route path="/" element={<ProductList />} />
              <Route path="cart" element={<Cart />} />
            </Routes>
          </main>
      </BrowserRouter>
    </CartProvider>
  );
}

export default App;
