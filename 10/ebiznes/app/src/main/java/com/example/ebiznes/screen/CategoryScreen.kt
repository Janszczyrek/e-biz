package com.example.ebiznes.screen

import androidx.compose.foundation.layout.padding
import androidx.compose.foundation.lazy.LazyColumn
import androidx.compose.foundation.lazy.items
import androidx.compose.material.icons.Icons
import androidx.compose.material.icons.filled.Home
import androidx.compose.material.icons.filled.List
import androidx.compose.material.icons.filled.Menu
import androidx.compose.material.icons.filled.Settings
import androidx.compose.material.icons.filled.ShoppingCart
import androidx.compose.material3.ExperimentalMaterial3Api
import androidx.compose.material3.Icon
import androidx.compose.material3.MaterialTheme
import androidx.compose.material3.NavigationBar
import androidx.compose.material3.NavigationBarItem
import androidx.compose.material3.Scaffold
import androidx.compose.material3.Text
import androidx.compose.material3.TopAppBar
import androidx.compose.runtime.Composable
import androidx.compose.ui.Modifier
import androidx.lifecycle.viewmodel.compose.viewModel
import androidx.navigation.NavController
import com.example.ebiznes.components.CategoryEntry
import com.example.ebiznes.components.ProductEntry

@OptIn(ExperimentalMaterial3Api::class)
@Composable
fun CategoryScreen(navController: NavController,
                    productViewModel: ProductScreenViewModel = viewModel()) {
    Scaffold(
        topBar = {
            TopAppBar(
                title = { Text("Categories") }
            )
        },
        bottomBar = {
            NavigationBar {
                val routes = listOf(
                    Icons.Default.Menu to "product",
                    Icons.Default.List to "category",
                    Icons.Default.ShoppingCart to "cart"
                )
                routes.forEach { it ->
                    val (icon, screen) = it
                    NavigationBarItem(
                        icon = {
                            Icon(
                                icon,
                                tint = MaterialTheme.colorScheme.onBackground,
                                contentDescription = null
                            )
                        },
                        selected = navController.currentDestination?.route == "category",
                        onClick = {
                            if (navController.currentDestination?.route != screen) {
                                navController.navigate(screen)
                            }
                        }
                    )
                }
            }
        },
        content = { padding ->
            LazyColumn(
                Modifier.padding(padding)
            ) {
                items(productViewModel.getUniqueCategories()) { category ->
                    CategoryEntry(category)
                }
            }
        }
    )
}