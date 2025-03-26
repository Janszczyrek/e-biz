package models

final case class ProductClass(id: Int, name: String, price: Double, description: String, category: Option[Int] = None)
