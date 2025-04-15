class Product:
    def __init__(self, name, price, stock, category):
        self.name = name
        self.price = price
        self.stock = stock
        self. category=category
        self. reviews=[]
        

    def update_stock(self, quantity):
        if self.stock >= quantity:
            self.stock -= quantity
            return True
        return False    
        
    def add_reviews (self, review): 
       self. reviews. append(review) 
        
class Customer:
    def __init__(self, name, email,address):
        self.name = name
        self. email=email
        self. address=address
        self.cart = ShoppingCart()

    def add_to_cart(self, product, quantity):
        return self.cart.add_product(product, quantity)

    def remove_from_cart(self, product):
        return self.cart.remove_product(product)


class ShoppingCart:
    def __init__(self):
        self.items = {}

    def add_product(self, product, quantity):
        if product.update_stock(quantity):
            self.items[product] = self.items.get(product, 0) + quantity
            return True
        return False

    def remove_product(self, product):
        if product in self.items:
            product.stock += self.items[product]
            del self.items[product]
            return True
        return False

    def apply_discount(self, percentage):
        return sum(product.price * qty * (1 - percentage / 100) for product, qty in self.items.items())


class Order:
    def __init__(self, customer):
        self.customer = customer
        self.total_price = customer.cart.apply_discount(0)

    def process_order(self):
        total = self.customer.cart.apply_discount(0)  # Calculate final total before clearing
        self.customer.cart.items.clear()
        return f"Order processed for {self.customer.name}. Total: ${total:.2f}"
        
    def make_payment (self, method="Credit card "): 
         return f" Payment is successfully received by using {method}"
         
    # Example usage
product1 = Product("Laptop", 1000, 5,'anjad@gamil.com','Multan')
print(product1. add_reviews ())    
product2 = Product("Phone", 500, 10)
print(product2. add_reviews ())
customer = Customer("Muqtasid Khan")
customer.add_to_cart(product1, 1)
customer.add_to_cart(product2, 2)
order = Order(customer)
print(order.process_order())
print(order.make_payment ()) 
