error id: 
file://<WORKSPACE>/app/controllers/ProductController.scala
empty definition using pc, found symbol in pc: 
empty definition using semanticdb
|empty definition using fallback
non-local guesses:
	 -

Document text:

```scala
package controllers

import javax.inject._
import play.api._
import play.api.mvc._
import play.api.libs.json._



@Singleton
class ProductController @Inject()(val controllerComponents: ControllerComponents) extends BaseController {
    var products = List("apple", "banana", "orange")

    def get() = Action { implicit request: Request[AnyContent] =>
        Ok(Json.toJson(products))
  }
    def getById(id: Int) = Action { implicit request: Request[AnyContent] =>
        if (id < 0 || id >= products.length) {
            NotFound
        } else {
            Ok(Json.toJson(products(id)))
        }
    }
}
```

#### Short summary: 

empty definition using pc, found symbol in pc: 