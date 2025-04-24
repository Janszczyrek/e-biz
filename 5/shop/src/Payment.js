import React from 'react';
import { useState, useContext } from 'react';
import axios from "axios";
import { CartContext } from './Cart';

function Payment() {
    const { cart } = useContext(CartContext);
    const total = cart.reduce((acc, item) => {
        const price = Number(item?.product?.price) || 0;
        const quantity = Number(item?.quantity) || 0;
        return acc + (price * quantity);
    }, 0);
    const [cardNumber, setCardNumber] = useState('');
    const pay = () => {
        axios.post('/payment', {
            total: total,
            card_number: cardNumber
        })
        .then(response => {
            alert(response.data.message);
        })
        .catch(error => {
            alert(error.response.data.message);
        });
    }
    return (
        <div>
            <h2>Payment</h2>
            <p>Total Amount: ${total.toFixed(2)}</p>
            <label>Card Number:</label>
            <input type="text" id="cardNumber" placeholder="Enter card number" onChange={e => setCardNumber(e.target.value)}/>
            <button onClick={pay}>Pay Now</button>
        </div>
    );
}




export default Payment;