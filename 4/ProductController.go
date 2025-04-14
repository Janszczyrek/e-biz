
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