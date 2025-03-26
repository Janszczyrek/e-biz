package models

final case class NewProductClass(name: String, price: Double, description: String, category: Option[Int] = None)
