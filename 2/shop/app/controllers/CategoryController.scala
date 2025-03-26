package controllers

import javax.inject._
import play.api._
import play.api.mvc._
import play.api.libs.json._
import views.html.index
import models.CategoryClass
import models.NewCategoryClass
import scala.collection.mutable.ListBuffer
import play.api.Mode.Prod

@Singleton
class CategoryController @Inject()(val controllerComponents: ControllerComponents) extends BaseController {
    var categories = new ListBuffer[CategoryClass]()
    categories += new CategoryClass(0, "Category 1", "Description 1")
    categories += new CategoryClass(1, "Category 2", "Description 2")
    categories += new CategoryClass(2, "Category 3", "Description 3")

    implicit val categoriesJson = Json.format[CategoryClass]
    implicit val newCategoriesJson = Json.format[NewCategoryClass]

    def get() = Action { implicit request: Request[AnyContent] =>
          if (categories.isEmpty) {
            NoContent
        } else {
            Ok(Json.toJson(categories))
        }
  }
    def getById(id: Int) = Action { implicit request: Request[AnyContent] =>
        val category = categories.find(_.id == id)
        if (category.isEmpty) {
            NotFound
        } else {
            Ok(Json.toJson(category))
        }
    }
    def add() = Action { implicit request: Request[AnyContent] =>
        val content = request.body
        val jsonObject = content.asJson
        val newCategory: Option[NewCategoryClass] = jsonObject.flatMap( 
            Json.fromJson[NewCategoryClass](_).asOpt 
            )
        newCategory match {
            case Some(newCat) =>
            val nextId = categories.map(_.id).max + 1
            val toBeAdded = CategoryClass(nextId, newCat.name, newCat.description)
            categories += toBeAdded
            Created(Json.toJson(toBeAdded))
            case None =>
            BadRequest
        }
    }
    def put(id: Int) = Action { implicit request: Request[AnyContent] =>
        val content = request.body
        val jsonObject = content.asJson
        val updatedCategory: Option[NewCategoryClass] = jsonObject.flatMap( 
            Json.fromJson[NewCategoryClass](_).asOpt 
            )
        updatedCategory match {
        case Some(updatedCat) =>
        val toBeUpdated = CategoryClass(id, updatedCat.name, updatedCat.description)
        categories = categories.map {
            case category if category.id == id => toBeUpdated
            case otherCategory => otherCategory 
        }
        Ok(Json.toJson(toBeUpdated))
        case None =>
            BadRequest
        
        }
    }
    def delete(id: Int) = Action { implicit request: Request[AnyContent] =>
        categories.find(_.id == id) match {
            case Some(category) =>
            categories -= category
            Ok(Json.toJson(category))
            case None =>
            NotFound
        }
    }
}