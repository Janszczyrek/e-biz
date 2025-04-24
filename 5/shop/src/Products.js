import React, { useState, useEffect, useContext } from 'react';
import { CartContext } from './Cart';
import axios from 'axios';

function ProductList() {
  const [productsData, setProductsData] = useState([]);
  const [isLoading, setIsLoading] = useState(true);
  const { setCart } = useContext(CartContext);

  useEffect(() => {
    async function fetchProducts() {
      try {
        const response = await axios.get('/products');
        setProductsData(response.data);
        setIsLoading(false);
      } catch (err) {
        setIsLoading(false);
      }
    }
    fetchProducts();
  }, []);

  const addToCart = (productToAdd) => {
    setCart(prevCart => {
      const existingProductIndex = prevCart.findIndex(item => item.product.id === productToAdd.id);

      if (existingProductIndex > -1) {
        const updatedCart = [...prevCart];
        updatedCart[existingProductIndex] = {
          ...updatedCart[existingProductIndex],
          quantity: updatedCart[existingProductIndex].quantity + 1
        };
        return updatedCart;
      } else {
        return [...prevCart, { product: productToAdd, quantity: 1 }];
      }
    });
  };

  if (isLoading) {
    return <div>Loading products...</div>;
  }
  return (
    <div>
      <h1>Products</h1>
      <ul>
        {productsData.map(product => (
          <li key={product.id}>
            {product.name} - ${product.price}
            <button onClick={() => { addToCart(product) }} >Add to cart</button>
          </li>
        ))}
      </ul>
    </div>
  );
}

export default ProductList;