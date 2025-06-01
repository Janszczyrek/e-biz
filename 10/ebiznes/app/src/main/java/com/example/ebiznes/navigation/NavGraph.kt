package com.example.ebiznes.navigation

import androidx.compose.runtime.Composable
import androidx.lifecycle.viewmodel.compose.viewModel
import androidx.navigation.NavHostController
import androidx.navigation.compose.NavHost
import androidx.navigation.compose.composable
import com.example.ebiznes.screen.ProductScreen
import com.example.ebiznes.screen.CategoryScreen
import com.example.ebiznes.screen.CartScreen
import com.example.ebiznes.screen.CartScreenViewModel
import com.example.ebiznes.screen.ProductScreenViewModel

@Composable
fun Navigation(navController: NavHostController) {
    val cartScreenViewModel: CartScreenViewModel = viewModel()
    val productScreenViewModel: ProductScreenViewModel = viewModel()
    NavHost(navController, startDestination = "product") {
        composable("product") {
            ProductScreen(navController, productViewModel = productScreenViewModel, cartViewModel = cartScreenViewModel)
        }
        composable("category") {
            CategoryScreen(navController, productViewModel = productScreenViewModel)
        }
        composable("cart") {
            CartScreen(navController, cartViewModel = cartScreenViewModel)
        }

    }
}