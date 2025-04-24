import React, { useState, useEffect } from 'react';
import Payment from './Payment';
import axios from 'axios';

function ProductList() {
  const [cart, setCart] = useState([]);
  const [productsData, setProductsData] = useState([]);
  const [isLoading, setIsLoading] = useState(true);

  useEffect(() => {
    async function fetchProducts() {
      try {
        const response = await axios.get('http://localhost:1323/products');
        setProductsData(response.data);
        setIsLoading(false);
      } catch (err) {
        setIsLoading(false);
      }
    }
    fetchProducts();
  }, []);

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
            <button onClick={() => { setCart([...cart, product]); console.log(cart) }} >Add to cart</button>
          </li>
        ))}
      </ul>
      <Payment cart={cart} />
    </div>
  );
}

export default ProductList;