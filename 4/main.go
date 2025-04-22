package main

import (
	"github.com/labstack/echo/v4"
)

func main() {
	if err := InitDB("products.db"); err != nil {
		panic(err)
    }
	e := echo.New()
	e.GET("/products",getProducts)
	e.GET("/products/:id",getProduct)
	e.POST("/products",createProduct)
	e.PUT("/products/:id",updateProduct)
	e.DELETE("/products/:id",deleteProduct)
	e.Logger.Fatal(e.Start(":1323"))
}