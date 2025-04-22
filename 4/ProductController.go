package main

import (
	"net/http"
	"strconv"
	"github.com/labstack/echo/v4"
)

func getProducts(c echo.Context) error {
	products, err := GetAllProducts()
	if err != nil {
		return err
	}
	return c.JSON(http.StatusOK, products)
}
func getProduct(c echo.Context) error {
	id, _ := strconv.Atoi(c.Param("id"))
	product, err := GetProductByID(uint(id))
	if err != nil {
		return err
	}
	return c.JSON(http.StatusOK, product)
}
func createProduct(c echo.Context) error {
	p := new(product)
	if err := c.Bind(p); err != nil {
		return err
	}
	if err := CreateProduct(p); err != nil {
		return err
	}
	return c.JSON(http.StatusCreated, p)
}

func deleteProduct(c echo.Context) error {
	id, _ := strconv.Atoi(c.Param("id"))
	if err := DeleteProduct(uint(id)); err != nil {
		return err
	}
	return c.NoContent(http.StatusNoContent)
}
func updateProduct(c echo.Context) error {
	id, _ := strconv.Atoi(c.Param("id"))
	p := new(product)
	if err := c.Bind(p); err != nil {
		return err
	}
	if err := UpdateProduct(uint(id), p); err != nil {
		return err
	}
	return c.JSON(http.StatusOK, p)
}