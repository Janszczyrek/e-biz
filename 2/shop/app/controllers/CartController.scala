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
class CartController @Inject()(val controllerComponents: ControllerComponents, val productController: ProductController) extends BaseController {

    val products = productController.products
    var cart = new ListBuffer[ProductClass]()

    implicit val productsJson = Json.format[ProductClass]

    def get() = Action { implicit request: Request[AnyContent] =>
          if (cart.isEmpty) {
            NoContent
        } else {
            Ok(Json.toJson(cart))
        }
  }
    // def getById(id: Int) = Action { implicit request: Request[AnyContent] =>
    //     val product = products.find(_.id == id)
    //     if (product.isEmpty) {
    //         NotFound
    //     } else {
    //         Ok(Json.toJson(product))
    //     }
    // }
    def addById(id:Int) = Action { implicit request: Request[AnyContent] =>
        products.find(_.id == id) match {
            case Some(product) =>
            cart += product
            Ok(Json.toJson(product))
            case None =>
            NotFound
        }
    }
    def edit() = Action { implicit request: Request[AnyContent] =>
        val content = request.body
        val jsonObject = content.asJson
        val updatedCart: Option[List[Int]] = jsonObject.flatMap( 
            Json.fromJson[List[Int]](_).asOpt 
            )
        updatedCart match {
            case Some(newCart) =>
                cart = newCart.flatMap(id => products.find(_.id == id)).to(ListBuffer)
            Ok(Json.toJson(cart))
            case None =>
            BadRequest
        }
    }
    def deleteById(id: Int) = Action { implicit request: Request[AnyContent] =>
        val index = cart.indexWhere(_.id == id)
        if (index == -1) {
            NotFound
        } else {
            cart.remove(index)
            Ok(Json.toJson(cart))
        }
    }
}