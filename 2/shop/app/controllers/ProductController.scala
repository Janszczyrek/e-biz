package controllers

import javax.inject._
import play.api._
import play.api.mvc._
import play.api.libs.json._
import views.html.index



@Singleton
class ProductController @Inject()(val controllerComponents: ControllerComponents) extends BaseController {
    var products = List("apple", "banana", "orange")

    def get() = Action { implicit request: Request[AnyContent] =>
        Ok(Json.toJson(products))
  }
}