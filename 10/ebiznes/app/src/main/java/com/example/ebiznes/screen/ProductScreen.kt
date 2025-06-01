package com.example.ebiznes.screen

import androidx.compose.foundation.layout.Arrangement
import androidx.compose.foundation.layout.Column
import androidx.compose.foundation.layout.Row
import androidx.compose.foundation.layout.Spacer
import androidx.compose.foundation.layout.fillMaxWidth
import androidx.compose.foundation.layout.height
import androidx.compose.foundation.layout.navigationBarsPadding
import androidx.compose.foundation.layout.padding
import androidx.compose.foundation.layout.size
import androidx.compose.foundation.lazy.LazyColumn
import androidx.compose.foundation.lazy.items
import androidx.compose.foundation.shape.CircleShape
import androidx.compose.material.icons.Icons
import androidx.compose.material.icons.filled.Add
import androidx.compose.material.icons.filled.Home
import androidx.compose.material.icons.filled.List
import androidx.compose.material.icons.filled.Menu
import androidx.compose.material.icons.filled.Settings
import androidx.compose.material.icons.filled.ShoppingCart
import androidx.compose.material3.Button
import androidx.compose.material3.Card
import androidx.compose.material3.CardDefaults
import androidx.compose.material3.ExperimentalMaterial3Api
import androidx.compose.material3.FloatingActionButton
import androidx.compose.material3.Icon
import androidx.compose.material3.IconButton
import androidx.compose.material3.MaterialTheme
import androidx.compose.material3.ModalBottomSheet
import androidx.compose.material3.NavigationBar
import androidx.compose.material3.NavigationBarItem
import androidx.compose.material3.OutlinedButton
import androidx.compose.material3.OutlinedTextField
import androidx.compose.material3.R
import androidx.compose.material3.Scaffold
import androidx.compose.material3.Text
import androidx.compose.material3.TopAppBar
import androidx.compose.material3.TopAppBarState
import androidx.compose.material3.rememberModalBottomSheetState
import androidx.compose.runtime.Composable
import androidx.compose.runtime.getValue
import androidx.compose.runtime.mutableStateOf
import androidx.compose.runtime.remember
import androidx.compose.runtime.setValue
import androidx.compose.ui.Alignment
import androidx.compose.ui.Modifier
import androidx.compose.ui.graphics.Color
import androidx.compose.ui.res.painterResource
import androidx.compose.ui.text.font.FontWeight
import androidx.compose.ui.unit.dp
import androidx.lifecycle.ViewModel
import androidx.lifecycle.viewmodel.compose.viewModel
import androidx.navigation.NavController
import com.example.ebiznes.components.ProductEntry
import com.example.ebiznes.data.Product

@OptIn(ExperimentalMaterial3Api::class)
@Composable
fun ProductScreen(
    navController: NavController,
    productViewModel: ProductScreenViewModel = viewModel(),
    cartViewModel: CartScreenViewModel
) {
    val bottomSheetState = rememberModalBottomSheetState()
    var showBottomSheet by remember { mutableStateOf(false) }
    Scaffold(topBar = {
        TopAppBar(
            title = { Text("Products") },
            actions = {
                IconButton(onClick = { showBottomSheet = true }) {
                    Icon(
                        Icons.Default.Add,
                        contentDescription = "Dodaj produkt"
                    )
                }
            })
    }, bottomBar = {
        NavigationBar {
            val routes = listOf(
                Icons.Default.Menu to "product",
                Icons.Default.List to "category",
                Icons.Default.ShoppingCart to "cart"
            )
            routes.forEach { it ->
                val (icon, screen) = it
                NavigationBarItem(icon = {
                    Icon(
                        icon,
                        tint = MaterialTheme.colorScheme.onBackground,
                        contentDescription = null
                    )
                }, selected = navController.currentDestination?.route == "product", onClick = {
                    if (navController.currentDestination?.route != screen) {
                        navController.navigate(screen)
                    }
                })
            }
        }
    }, content = { padding ->
        LazyColumn(
            Modifier.padding(padding)
        ) {
            items(productViewModel.getProducts()) { product ->
                ProductEntry(product) { cartViewModel.addToCart(it) }
            }
        }
    })
    if (showBottomSheet) {
        ModalBottomSheet(
            onDismissRequest = {
                showBottomSheet = false
            },
            sheetState = bottomSheetState
        ) {
            AddProductBottomSheetContent(
                onProductAdd = { product ->
                    productViewModel.addProduct(product)
                    showBottomSheet = false
                },
                onDismiss = {
                    showBottomSheet = false
                }
            )
        }
    }
}

@Composable
fun AddProductBottomSheetContent(
    onProductAdd: (Product) -> Unit,
    onDismiss: () -> Unit
) {
    var name by remember { mutableStateOf("") }
    var description by remember { mutableStateOf("") }
    var price by remember { mutableStateOf("") }
    var category by remember { mutableStateOf("") }

    Column(
        modifier = Modifier
            .fillMaxWidth()
            .padding(16.dp)
            .navigationBarsPadding(),
        verticalArrangement = Arrangement.spacedBy(16.dp)
    ) {
        Text(
            text = "Add new product",
            style = MaterialTheme.typography.headlineSmall,
            modifier = Modifier.padding(bottom = 8.dp)
        )

        OutlinedTextField(
            value = name,
            onValueChange = { name = it },
            label = { Text("Name") },
            modifier = Modifier.fillMaxWidth(),
            singleLine = true
        )

        OutlinedTextField(
            value = description,
            onValueChange = { description = it },
            label = { Text("Description") },
            modifier = Modifier.fillMaxWidth(),
            maxLines = 3
        )

        OutlinedTextField(
            value = price,
            onValueChange = { price = it },
            label = { Text("Price") },
            modifier = Modifier.fillMaxWidth(),
            singleLine = true
        )

        OutlinedTextField(
            value = category,
            onValueChange = { category = it },
            label = { Text("Category") },
            modifier = Modifier.fillMaxWidth(),
            singleLine = true
        )

        Row(
            modifier = Modifier.fillMaxWidth(),
            horizontalArrangement = Arrangement.spacedBy(8.dp)
        ) {
            OutlinedButton(
                onClick = onDismiss,
                modifier = Modifier.weight(1f)
            ) {
                Text("Cancel")
            }

            Button(
                onClick = {
                    if (name.isNotBlank() && price.isNotBlank()) {
                        val priceDouble = price.toDoubleOrNull() ?: 0.0
                        val product = Product(
                            name = name,
                            description = description,
                            price = priceDouble,
                            category = category
                        )
                        onProductAdd(product)
                    }
                },
                modifier = Modifier.weight(1f),
                enabled = name.isNotBlank() && price.isNotBlank()
            ) {
                Text("Add")
            }
        }
        Spacer(modifier = Modifier.height(32.dp))
    }
}