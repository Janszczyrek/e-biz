package com.example.ebiznes.screen

import androidx.compose.runtime.mutableStateListOf
import androidx.lifecycle.ViewModel
import com.example.ebiznes.data.Product

class ProductScreenViewModel : ViewModel() {


    private var productList = mutableStateListOf(
        Product(
            name = "Wireless Mouse",
            price = 10.5,
            description = "Ergonomic wireless mouse with adjustable DPI.",
            category = "Electronics"
        ),
        Product(
            name = "Water Bottle",
            price = 1.2,
            description = "Insulated stainless steel water bottle, 1L capacity.",
            category = "Home & Kitchen"
        ),
        Product(
            name = "Yoga Mat",
            price = 12.0,
            description = "Non-slip yoga mat with extra cushioning.",
            category = "Fitness"
        ),
        Product(
            name = "Bluetooth Speaker",
            price = 20.0,
            description = "Portable speaker with 12 hours of battery life.",
            category = "Electronics"
        ),
        Product(
            name = "Notebook",
            price = 2.0,
            description = "A5 size, 200 pages, dotted grid, hard cover.",
            category = "Stationery"
        )
    )

    fun addProduct(product: Product) {
        productList.add(product)
    }

    fun removeProduct(product: Product) {
        productList.remove(product)
    }

    fun getProducts(): List<Product> {
        return productList
    }

    fun getUniqueCategories(): List<String> {
        return getProducts()
            .map { it.category }
            .filter { it.isNotBlank() }
            .distinct()
            .sorted()
    }

}
