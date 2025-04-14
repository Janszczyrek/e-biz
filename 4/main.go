package main

import (
	"net/http"
	"strconv"
	
	"github.com/labstack/echo/v4"
)

func main() {
	e := echo.New()
	e.GET("/products",getProducts)
	e.GET("/products/:id",getProduct)
	e.POST("/products",createProduct)
	e.PUT("/products/:id",updateProduct)
	e.DELETE("/products/:id",deleteProduct)
	e.Logger.Fatal(e.Start(":1323"))
}

type (
	product struct {
		ID   int    `json:"id"`
		Name string `json:"name"`
		Price int `json:"price"`
		Category string `json:"category"`
	}
)
var (
	products = map[int]*product{
	1: {ID: 1, Name: "Product A", Price: 100, Category: "Category 1"},
	2: {ID: 2, Name: "Product B", Price: 200, Category: "Category 2"},
	}
	auto_increment  = 3
)
func getProducts(c echo.Context) error {
	return c.JSON(http.StatusOK, products)
}
func getProduct(c echo.Context) error {
	id, _ := strconv.Atoi(c.Param("id"))
	return c.JSON(http.StatusNotFound, products[id])
}
func createProduct(c echo.Context) error {
		p := &product{
		ID: auto_increment,
	}
	if err := c.Bind(p); err != nil {
		return c.JSON(http.StatusBadRequest, map[string]string{"message": "Invalid input"})
	}
	products[p.ID] = p
	auto_increment++
	return c.JSON(http.StatusCreated, p)
}

func deleteProduct(c echo.Context) error {
	id, _ := strconv.Atoi(c.Param("id"))
	delete(products, id)
	return c.NoContent(http.StatusNoContent)
}
func updateProduct(c echo.Context) error {
	p := new(product)
	if err := c.Bind(p); err != nil {
		return err
	}
	id, _ := strconv.Atoi(c.Param("id"))
	products[id].Name = p.Name
	products[id].Price = p.Price
	products[id].Category = p.Category
	return c.JSON(http.StatusOK, products[id])
}