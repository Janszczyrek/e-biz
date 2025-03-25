package controllers

import javax.inject._
import play.api._
import play.api.mvc._
import play.api.libs.json._
import views.html.index
import models.ProductClass
import models.NewProductClass
import scala.collection.mutable.ListBuffer
import play.api.Mode.Prod

@Singleton
class ProductController @Inject()(val controllerComponents: ControllerComponents) extends BaseController {
    var products = new ListBuffer[ProductClass]()
    products += new ProductClass(0, "Product 1", 100.0, "Description 1")
    products += new ProductClass(1, "Product 2", 200.0, "Description 2")
    products += new ProductClass(2, "Product 3", 300.0, "Description 3")
    products += new ProductClass(3, "Product 4", 400.0, "Description 4")

    implicit val productsJson = Json.format[ProductClass]
    implicit val newProductsJson = Json.format[NewProductClass]

    def get() = Action { implicit request: Request[AnyContent] =>
          if (products.isEmpty) {
            NoContent
        } else {
            Ok(Json.toJson(products))
        }
  }
    def getById(id: Int) = Action { implicit request: Request[AnyContent] =>
        val product = products.find(_.id == id)
        if (product.isEmpty) {
            NotFound
        } else {
            Ok(Json.toJson(product))
        }
    }
    def add() = Action { implicit request: Request[AnyContent] =>
        val content = request.body
        val jsonObject = content.asJson
        val newProduct: Option[NewProductClass] = jsonObject.flatMap( 
            Json.fromJson[NewProductClass](_).asOpt 
            )
        newProduct match {
            case Some(newItem) =>
            val nextId = products.map(_.id).max + 1
            val toBeAdded = ProductClass(nextId, newItem.name, newItem.price, newItem.description)
            products += toBeAdded
            Created(Json.toJson(toBeAdded))
            case None =>
            BadRequest
        }
    }
    def put(id: Int) = Action { implicit request: Request[AnyContent] =>
        val content = request.body
        val jsonObject = content.asJson
        val updatedProduct: Option[NewProductClass] = jsonObject.flatMap( 
            Json.fromJson[NewProductClass](_).asOpt 
            )
        updatedProduct match {
        case Some(updated) =>
        val toBeUpdated = ProductClass(id, updated.name, updated.price, updated.description)
        products = products.map {
            case product if product.id == id => toBeUpdated
            case otherProduct => otherProduct
        }
        Ok(Json.toJson(toBeUpdated))
        case None =>
            BadRequest
        
        }
    }
    def delete(id: Int) = Action { implicit request: Request[AnyContent] =>
        products.find(_.id == id) match {
            case Some(product) =>
            products -= product
            Ok(Json.toJson(product))
            case None =>
            NotFound
        }
    }
}