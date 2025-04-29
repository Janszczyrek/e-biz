import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service as ChromeService


BASE_URL = "http://localhost:3000"


def get_driver():
    options = webdriver.ChromeOptions()
    service = ChromeService(executable_path='/usr/bin/chromedriver')
    driver = webdriver.Chrome(service=service, options=options)
    driver.implicitly_wait(5)
    return driver


class ShopTests(unittest.TestCase):

    def setUp(self):
        self.driver = get_driver()
        self.driver.get(BASE_URL)

    def tearDown(self):
        self.driver.quit()

    def test_navigation_to_cart(self):
        driver = self.driver
        cart_button = driver.find_element(By.XPATH, "//a[@href='/cart']")
        cart_button.click()
        cart_header = driver.find_element(
            By.XPATH, "//h1[contains(text(), 'Cart')]")
        self.assertTrue(cart_header.is_displayed())

    def test_navigation_to_products(self):
        driver = self.driver
        cart_button = driver.find_element(By.XPATH, "//a[@href='/cart']")
        product_button = driver.find_element(By.XPATH, "//a[@href='/']")
        self.assertTrue(cart_button.is_displayed())
        cart_button.click()
        self.assertTrue(product_button.is_displayed())
        cart_header = driver.find_element(
            By.XPATH, "//h1[contains(text(), 'Cart')]")
        self.assertTrue(cart_header.is_displayed())
        product_button.click()
        products_header = driver.find_element(
            By.XPATH, "//h1[contains(text(), 'Products')]")
        self.assertTrue(products_header.is_displayed())

    def test_page_load(self):
        driver = self.driver
        self.assertIn("React App", driver.title)

    def test_product_page_load(self):
        driver = self.driver
        product_list = driver.find_element(By.XPATH, "//ul[li]")
        self.assertTrue(product_list.is_displayed())

    def test_product_list(self):
        driver = self.driver
        product_list = driver.find_element(By.XPATH, "//ul[li]")
        products = product_list.find_elements(By.TAG_NAME, "li")
        self.assertGreater(len(products), 0, "Product list is empty")
        for product in products:
            self.assertTrue(product.is_displayed(), "Product is not displayed")
            self.assertIn("$", product.text,
                          "Product price is not displayed correctly")
            button = product.find_element(By.TAG_NAME, "button")
            self.assertTrue(button.is_displayed(),
                            "Add to Cart button is not displayed")

    def test_add_to_cart(self):
        driver = self.driver
        product_list = driver.find_element(By.XPATH, "//ul[li]")
        products = product_list.find_elements(By.TAG_NAME, "li")
        self.assertGreater(len(products), 0, "Product list is empty")
        button = products[0].find_element(By.TAG_NAME, "button")
        button.click()
        cart_button = driver.find_element(By.XPATH, "//a[@href='/cart']")
        cart_button.click()
        cart_products = driver.find_elements(By.XPATH, "//ul[li]")
        self.assertGreater(len(cart_products), 0, "Cart is empty")
        for cart_product in cart_products:
            self.assertIn("$", cart_product.text,
                          "Product price is not displayed correctly")

    def test_cart(self):
        driver = self.driver
        product_list = driver.find_element(By.XPATH, "//ul[li]")
        products = product_list.find_elements(By.TAG_NAME, "li")
        self.assertGreater(len(products), 0, "Product list is empty")
        for product in products:
            button = product.find_element(By.TAG_NAME, "button")
            button.click()
        cart_button = driver.find_element(By.XPATH, "//a[@href='/cart']")
        cart_button.click()
        cart = driver.find_element(By.XPATH, "//ul[li]")
        cart_products = cart.find_elements(By.TAG_NAME, "li")
        self.assertEqual(len(cart_products), len(products),
                         "Cart does not contain the correct number of products")
        for cart_product in cart_products:
            self.assertTrue(cart_product.is_displayed(),
                            "Product is not displayed in cart")
            self.assertIn("$", cart_product.text,
                          "Product price is not displayed correctly")
            
    def test_empty_cart(self):
        driver = self.driver
        cart_button = driver.find_element(By.XPATH, "//a[@href='/cart']")
        cart_button.click()
        cart = driver.find_element(By.XPATH, "//ul")
        self.assertEqual(
            len(cart.find_elements(By.TAG_NAME, "li")), 0,
            "Cart is not empty")
        total = driver.find_element(By.XPATH, "//p[contains(text(), 'Total')]")
        self.assertIn("Total Amount: $0", total.text,
                      "Total price is not displayed correctly")

    def test_cart_presistance(self):
        driver = self.driver
        product_list = driver.find_element(By.XPATH, "//ul[li]")
        products = product_list.find_elements(By.TAG_NAME, "li")
        self.assertGreater(len(products), 0, "Product list is empty")
        button = products[0].find_element(By.TAG_NAME, "button")
        button.click()
        cart_button = driver.find_element(By.XPATH, "//a[@href='/cart']")
        cart_button.click()
        cart = driver.find_element(By.XPATH, "//ul[li]")
        cart_products = cart.find_elements(By.TAG_NAME, "li")
        self.assertGreater(len(cart_products), 0, "Cart is empty")
        product_button = driver.find_element(By.XPATH, "//a[@href='/']")
        product_button.click()
        cart_button = driver.find_element(By.XPATH, "//a[@href='/cart']")
        cart_button.click()
        cart = driver.find_element(By.XPATH, "//ul[li]")
        cart_products = cart.find_elements(By.TAG_NAME, "li")
        self.assertGreater(len(cart_products), 0, "Cart is empty")

    def test_total(self):
        driver = self.driver
        product_list = driver.find_element(By.XPATH, "//ul[li]")
        products = product_list.find_elements(By.TAG_NAME, "li")
        self.assertGreater(len(products), 0, "Product list is empty")
        price = 0
        for product in products:
            button = product.find_element(By.TAG_NAME, "button")
            price += float(product.text.split("$")[1].split("Add")[0])
            button.click()
        cart_button = driver.find_element(By.XPATH, "//a[@href='/cart']")
        cart_button.click()
        cart = driver.find_element(By.XPATH, "//ul[li]")
        cart_products = cart.find_elements(By.TAG_NAME, "li")
        self.assertGreater(len(cart_products), 0, "Cart is empty")
        total = driver.find_element(By.XPATH, "//p[contains(text(), 'Total')]")
        self.assertIn(str(price), total.text,
                      "Total price is not displayed correctly")

    def test_total_on_product_increment(self):
        driver = self.driver
        product_list = driver.find_element(By.XPATH, "//ul[li]")
        products = product_list.find_elements(By.TAG_NAME, "li")
        self.assertGreater(len(products), 0, "Product list is empty")
        button = products[0].find_element(By.TAG_NAME, "button")
        button.click()
        price = float(products[0].text.split("$")[1].split("Add")[0])
        cart_button = driver.find_element(By.XPATH, "//a[@href='/cart']")
        cart_button.click()
        cart_product = driver.find_element(By.XPATH, "//ul[li]")
        increment_button = cart_product.find_element(
            By.XPATH, "//button[contains(text(), '+')]")
        for i in range(10):
            increment_button.click()
            total = driver.find_element(
                By.XPATH, "//p[contains(text(), 'Total')]")
            self.assertIn(str(price*(i+2)), total.text,
                          "Price not updated correctly")

    def test_total_on_product_decrement(self):
        driver = self.driver
        product_list = driver.find_element(By.XPATH, "//ul[li]")
        products = product_list.find_elements(By.TAG_NAME, "li")
        self.assertGreater(len(products), 0, "Product list is empty")
        button = products[0].find_element(By.TAG_NAME, "button")
        price = float(products[0].text.split("$")[1].split("Add")[0])
        for i in range(10):
            button.click()
        cart_button = driver.find_element(By.XPATH, "//a[@href='/cart']")
        cart_button.click()
        cart_product = driver.find_element(By.XPATH, "//ul[li]")
        decrement_button = cart_product.find_element(
            By.XPATH, "//button[contains(text(), '-')]")
        for i in range(10):
            decrement_button.click()
            total = driver.find_element(
                By.XPATH, "//p[contains(text(), 'Total')]")
            self.assertIn(str(price*(9-i)), total.text,
                          "Price not updated correctly")

    def same_product_multiple_times(self):
        driver = self.driver
        product_list = driver.find_element(By.XPATH, "//ul[li]")
        products = product_list.find_elements(By.TAG_NAME, "li")
        self.assertGreater(len(products), 0, "Product list is empty")
        button = products[0].find_element(By.TAG_NAME, "button")
        for _ in range(100):
            button.click()
        cart_button = driver.find_element(By.XPATH, "//a[@href='/cart']")
        cart_button.click()
        cart = driver.find_element(By.XPATH, "//ul[li]")
        cart_products = cart.find_elements(By.TAG_NAME, "li")
        self.assertEqual(len(cart_products), 1,
                         "Cart does not contain the correct number of products")
        count = cart_products[0].text.split("x")[1]
        self.assertEqual(
            int(count), 100, "Product count in cart is not correct")

    def test_increment(self):
        driver = self.driver
        product_list = driver.find_element(By.XPATH, "//ul[li]")
        products = product_list.find_elements(By.TAG_NAME, "li")
        self.assertGreater(len(products), 0, "Product list is empty")
        button = products[0].find_element(By.TAG_NAME, "button")
        button.click()
        cart_button = driver.find_element(By.XPATH, "//a[@href='/cart']")
        cart_button.click()
        cart_product = driver.find_element(By.XPATH, "//ul[li]")
        increment_button = cart_product.find_element(
            By.XPATH, "//button[contains(text(), '+')]")
        for i in range(10):
            increment_button.click()
            count = cart_product.text.split("x")[1].split("+")[0]
            self.assertEqual(int(count), i + 2,
                             "Product count in cart is not correct")

    def test_decrement(self):
        driver = self.driver
        product_list = driver.find_element(By.XPATH, "//ul[li]")
        products = product_list.find_elements(By.TAG_NAME, "li")
        self.assertGreater(len(products), 0, "Product list is empty")
        button = products[0].find_element(By.TAG_NAME, "button")
        for i in range(10):
            button.click()
        cart_button = driver.find_element(By.XPATH, "//a[@href='/cart']")
        cart_button.click()
        cart_product = driver.find_element(By.XPATH, "//ul[li]")
        decrement_button = cart_product.find_element(
            By.XPATH, "//button[contains(text(), '-')]")
        for i in range(9):
            decrement_button.click()
            count = cart_product.text.split("x")[1].split("+")[0]
            self.assertEqual(
                int(count), 9-i, "Product count in cart is not correct")

    def test_decrement_stops_at_1(self):
        driver = self.driver
        product_list = driver.find_element(By.XPATH, "//ul[li]")
        products = product_list.find_elements(By.TAG_NAME, "li")
        self.assertGreater(len(products), 0, "Product list is empty")
        button = products[0].find_element(By.TAG_NAME, "button")
        button.click()
        button.click()
        cart_button = driver.find_element(By.XPATH, "//a[@href='/cart']")
        cart_button.click()
        cart_product = driver.find_element(By.XPATH, "//ul[li]")
        decrement_button = cart_product.find_element(
            By.XPATH, "//button[contains(text(), '-')]")
        decrement_button.click()
        count = cart_product.text.split("x")[1].split("+")[0]
        self.assertEqual(int(count), 1, "Product count in cart is not correct")
        decrement_button.click()
        self.assertEqual(int(count), 1, "Product count in cart is not correct")

    def test_decrement_and_increment(self):
        driver = self.driver
        product_list = driver.find_element(By.XPATH, "//ul[li]")
        products = product_list.find_elements(By.TAG_NAME, "li")
        self.assertGreater(len(products), 0, "Product list is empty")
        button = products[0].find_element(By.TAG_NAME, "button")
        button.click()
        cart_button = driver.find_element(By.XPATH, "//a[@href='/cart']")
        cart_button.click()
        cart_product = driver.find_element(By.XPATH, "//ul[li]")
        increment_button = cart_product.find_element(
            By.XPATH, "//button[contains(text(), '+')]")
        decrement_button = cart_product.find_element(
            By.XPATH, "//button[contains(text(), '-')]")
        increment_button.click()
        count = cart_product.text.split("x")[1].split("+")[0]
        self.assertEqual(int(count), 2, "Product count in cart is not correct")
        decrement_button.click()
        count = cart_product.text.split("x")[1].split("+")[0]
        self.assertEqual(int(count), 1, "Product count in cart is not correct")

    def test_remove(self):
        driver = self.driver
        product_list = driver.find_element(By.XPATH, "//ul[li]")
        products = product_list.find_elements(By.TAG_NAME, "li")
        self.assertGreater(len(products), 0, "Product list is empty")
        button = products[0].find_element(By.TAG_NAME, "button")
        button.click()
        cart_button = driver.find_element(By.XPATH, "//a[@href='/cart']")
        cart_button.click()
        cart_product = driver.find_element(By.XPATH, "//ul[li]")
        remove_button = cart_product.find_element(
            By.XPATH, "//button[contains(text(), 'Remove')]")
        remove_button.click()
        cart_products = driver.find_elements(By.XPATH, "//ul[li]")
        self.assertEqual(len(cart_products), 0,
                         "Cart is not empty after removing product")
        total = driver.find_element(By.XPATH, "//p[contains(text(), 'Total')]")
        self.assertIn("Total Amount: $0", total.text,
                      "Total didn't reset to 0$.")

    def test_empty_cart_payment(self):
        driver = self.driver
        wait = WebDriverWait(driver, 5)
        cart_button = driver.find_element(By.XPATH, "//a[@href='/cart']")
        cart_button.click()
        pay_button = driver.find_element(
            By.XPATH, "//button[contains(text(), 'Pay Now')]")
        pay_button.click()
        try:
            alert = wait.until(EC.alert_is_present())
            alert_text = alert.text
            alert.accept()
            self.assertIn("Invalid payment amount", alert_text)
        except Exception:
            self.fail("Payment confirmation alert/message did not appear.")

    def test_empty_card_payment(self):
        driver = self.driver
        wait = WebDriverWait(driver, 5)
        product_list = driver.find_element(By.XPATH, "//ul[li]")
        products = product_list.find_elements(By.TAG_NAME, "li")
        self.assertGreater(len(products), 0, "Product list is empty")
        button = products[0].find_element(By.TAG_NAME, "button")
        button.click()
        cart_button = driver.find_element(By.XPATH, "//a[@href='/cart']")
        cart_button.click()
        pay_button = driver.find_element(
            By.XPATH, "//button[contains(text(), 'Pay Now')]")
        pay_button.click()
        try:
            alert = wait.until(EC.alert_is_present())
            alert_text = alert.text
            alert.accept()
            self.assertIn("Invalid card number", alert_text)
        except Exception:
            self.fail("Payment confirmation alert/message did not appear.")

    def test_successful_card_payment(self):
        driver = self.driver
        wait = WebDriverWait(driver, 5)
        product_list = driver.find_element(By.XPATH, "//ul[li]")
        products = product_list.find_elements(By.TAG_NAME, "li")
        self.assertGreater(len(products), 0, "Product list is empty")
        button = products[0].find_element(By.TAG_NAME, "button")
        button.click()
        cart_button = driver.find_element(By.XPATH, "//a[@href='/cart']")
        cart_button.click()
        card_number = driver.find_element(
            By.XPATH, "//input[@id='cardNumber']")
        card_number.send_keys("1234567812345678")
        pay_button = driver.find_element(
            By.XPATH, "//button[contains(text(), 'Pay Now')]")
        pay_button.click()
        try:
            alert = wait.until(EC.alert_is_present())
            alert_text = alert.text
            alert.accept()
            self.assertIn("Payment successful", alert_text)
        except Exception:
            self.fail("Payment confirmation alert/message did not appear.")


if __name__ == "__main__":
    unittest.main()
