package com.example.ebiznes.screen

import androidx.compose.runtime.mutableStateListOf
import androidx.lifecycle.ViewModel
import com.example.ebiznes.data.CartItem
import com.example.ebiznes.data.Product

class CartScreenViewModel: ViewModel() {
    private var cart = mutableStateListOf<CartItem>()

    fun getCart(): List<CartItem> = cart

    fun addToCart(product: Product) {
        val existingItem = cart.find { it.product == product }
        if (existingItem != null) {
            existingItem.quantity += 1
        } else {
            cart.add(CartItem(product, quantity = 1))
        }
    }

    fun removeFromCart(product: Product) {
        val existingItem = cart.find { it.product == product }
        existingItem?.let {
            if (it.quantity > 1) {
                it.quantity -= 1
            } else {
                cart.remove(it)
            }
        }
    }
}

