package main

import (
	"net/http"
	"github.com/labstack/echo/v4/middleware"
	"github.com/labstack/echo/v4"
)

type Product struct {
	ID    int     `json:"id"`
	Name  string  `json:"name"`
	Price float64 `json:"price"`
}
type Payment struct {
	ID     int     `json:"id"`
	Total float64 `json:"total"`
	Card_number   string  `json:"card_number"`
}
func main() {
	products := []Product{
		{ID: 1, Name: "Apple", Price: 10.0},
		{ID: 2, Name: "Banana", Price: 20.0},
		{ID: 3, Name: "Mango", Price: 30.0},
	}
	e := echo.New()
	e.Use(middleware.CORS())
	e.Use(middleware.CORSWithConfig(middleware.CORSConfig{
	AllowOrigins: []string{"http://localhost:3000"},
	AllowHeaders: []string{echo.HeaderOrigin, echo.HeaderContentType, echo.HeaderAccept},
	}))
	e.GET("/products", func(c echo.Context) error {
		return c.JSON(http.StatusOK, products)
	})
	e.POST("/payment", func(c echo.Context) error {
		payment := Payment{}
		if err := c.Bind(&payment); err != nil {
			return c.JSON(http.StatusBadRequest, map[string]string{
				"message": "Invalid payment data"})
		}
		if payment.Total <= 0 {
			return c.JSON(http.StatusBadRequest, map[string]string{
				"message": "Invalid payment amount"})
		}
		if payment.Card_number == "" {
			return c.JSON(http.StatusBadRequest, map[string]string{
				"message": "Invalid card number"})
			}
		return c.JSON(http.StatusOK, map[string]string{
			"message": "Payment successful"})
	})
	e.Logger.Fatal(e.Start(":1323"))
}