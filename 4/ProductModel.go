package main

type (
    product struct {
        ID       int    `json:"id"`
        Name     string `json:"name"`
        Price    int    `json:"price"`
        Category string `json:"category"`
    }
)

var (
    products = map[int]*product{
        1: {ID: 1, Name: "Product A", Price: 100, Category: "Category 1"},
        2: {ID: 2, Name: "Product B", Price: 200, Category: "Category 2"},
    }
    auto_increment = 3
)