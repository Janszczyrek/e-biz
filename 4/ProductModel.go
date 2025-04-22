package main

import (
    "gorm.io/driver/sqlite"
    "gorm.io/gorm"
)

var db *gorm.DB

type (
    product struct {
        gorm.Model
        Name       string `json:"name"`
        Price      int    `json:"price"`
        Category   string `json:"category"`
    }
)

func InitDB(databasePath string) error {
    var err error
    db, err = gorm.Open(sqlite.Open(databasePath), &gorm.Config{})
    if err != nil {
        return err
    }

    err = db.AutoMigrate(&product{})
    if err != nil {
        return err
    }

    var count int64
    db.Model(&product{}).Count(&count)
    if count == 0 {
        initialProducts := []product{
            {Name: "Product A", Price: 100, Category: "Category 1"},
            {Name: "Product B", Price: 200, Category: "Category 2"},
        }
        if result := db.Create(&initialProducts); result.Error != nil {
            return result.Error
        }
    }

    return nil
}
func GetAllProducts() ([]product, error) {
    var products []product
    result := db.Find(&products)
    return products, result.Error
}

func GetProductByID(id uint) (*product, error) {
    var p product
    result := db.First(&p, id)
    if result.Error != nil {
        return nil, result.Error
    }
    return &p, nil
}

func CreateProduct(p *product) error {
    result := db.Create(p)
    return result.Error
}

func UpdateProduct(id uint, p *product) error {
    result := db.Model(&product{}).Where("id = ?", id).Updates(p)
    if result.RowsAffected == 0 {
        return gorm.ErrRecordNotFound
    }
    return result.Error
}

func DeleteProduct(id uint) error {
    result := db.Delete(&product{}, id)
    return result.Error
}