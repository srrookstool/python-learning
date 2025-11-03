from abc import ABC, abstractmethod
import math
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass
    @abstractmethod
    def perimeter(self):
        pass
    def describe(self):
        return f"This is a {self.__class__.__name__}"
    @staticmethod
    def validate_positive(value, name):
        if value > 0:
            return True
        else:
            print(f"{name} must be positive!")
            return False
class Circle(Shape):
    def __init__(self, radius):
        if self.validate_positive(radius, "Radius"):
            self.radius = radius
    def area(self):
        return (self.radius ** 2) * 3.14159
    def perimeter(self):
        return self.radius * 2 * 3.14159
class Rectangle(Shape):
    def __init__(self, width, height):
        if self.validate_positive(width, "Width") and self.validate_positive(height,"Height"):
            self.width = width
            self.height = height
    def area(self):
        return self.width * self.height
    def perimeter(self):
        return (self.width + self.height) * 2
class Triangle(Shape):
    def __init__(self, side1, side2, side3):
        if self.validate_positive(side1, "Side 1") and self.validate_positive(side2, "Side 2") and self.validate_positive(side3, "Side 3"):
            self.side1 = side1
            self.side2 = side2
            self.side3 = side3
    def area(self):
        s = (self.side1 + self.side2 + self.side3) / 2
        return math.sqrt(s * (s - self.side1) * (s - self.side2) * (s -
        self.side3))
    def perimeter(self):
        return self.side1 + self.side2 + self.side3
class ShapeCollection:
    def __init__(self):
        self.shapes = []
    def add_shape(self, shape):
        self.shapes.append(shape)
    def total_area(self):
        total=0
        for shape in self.shapes:
            total += shape.area()
        return total
    def total_perimeter(self):
        total=0
        for shape in self.shapes:
            total += shape.perimeter()
        return total
# Test your code
if __name__ == "__main__":
    # Create shapes
    circle = Circle(5)
    rectangle = Rectangle(4, 6)
    triangle = Triangle(3, 4, 5)
    # Test individual shapes
    print("Individual Shapes:")
    for shape in [circle, rectangle, triangle]:
        print(f" {shape.describe()}")
        print(f" Area: {shape.area():.2f}")
        print(f" Perimeter: {shape.perimeter():.2f}")
    # Test collection (polymorphism!)
    collection = ShapeCollection()
    collection.add_shape(circle)
    collection.add_shape(rectangle)
    collection.add_shape(triangle)
    print(f"\nCollection Totals:")
    print(f" Total Area: {collection.total_area():.2f}")
    print(f" Total Perimeter: {collection.total_perimeter():.2f}")
    # Test validation
    print("\nTesting validation:")
    try:
        bad_circle = Circle(-5)
    except:
        print(" Correctly rejected negative radius")

class Pizza:
    price_list = {'small': 10, 'medium': 15, 'large': 20}
    topping_price = 2
    def __init__(self, size, toppings):
       self.size = size
       self.toppings = toppings
    def calculate_price(self):
        return self.price_list[self.size] + (len(self.toppings) * self.topping_price)
    def __str__(self):
        return f"{self.size} pizza with {len(self.toppings)} toppings"
    @classmethod
    def create_margherita(cls, size):
        return Pizza(size,['cheese','tomato','basil'])
    @classmethod
    def create_pepperoni(cls, size):
        return Pizza(size,['cheese','pepperoni'])
    @classmethod
    def create_veggie(cls, size):
        return Pizza(size,['cheese','mushrooms','peppers','onions'])
    @staticmethod
    def validate_size(size):
        if size in ["small","medium","large"]:
            return True
        else: return False
class PizzaOrder:
    total_orders = 0
    def __init__(self):
        # TODO: Increment total_orders
        # TODO: Generate order_id like "ORDER_001"
        # TODO: Initialize pizzas list
        PizzaOrder.total_orders += 1
        self.order_id = f"ORDER_{str(self.total_orders).zfill(3)}"
        self.pizzas = []
    def add_pizza(self, pizza):
        self.pizzas.append(pizza)
    def get_total(self):
        sum = 0
        for pizza in self.pizzas:
            sum += pizza.calculate_price()
        return sum
    @classmethod
    def get_total_orders(cls):
        return cls.total_orders
    def __str__(self):
        return f"Order {self.order_id} - Total: ${self.get_total()}"
class OrderManager:
    @staticmethod
    def create_order_from_string(order_string):
        """Parse string like 'large pepperoni, small margherita'"""
        order = PizzaOrder()
        for pizza in order_string.split(","):
            split = pizza.split()
            if split[1] == "margherita":
                order.add_pizza(Pizza.create_margherita(split[0]))
            elif split[1] == "pepperoni":
                order.add_pizza(Pizza.create_pepperoni(split[0]))
            elif split[1] == "veggie":
                order.add_pizza(Pizza.create_veggie(split[0]))
        # TODO: Split by comma
        # TODO: For each item, parse size and type
        # TODO: Use appropriate factory method
        # TODO: Return complete order
        return order
    @staticmethod
    def format_receipt(order):
        # TODO: Create nice receipt with:
        # Order ID
        # List of pizzas
        # Total price
        print("=== RECEIPT ===")
        print(f"Order: {order.order_id}")
        print("Items:")
        for pizza in order.pizzas:
            print(f" {pizza} - ${pizza.calculate_price()}")
        print(f"Total: ${order.get_total()}")
        return("==============")
# Test your code
if __name__ == "__main__":
    # Test factory methods
    pizza1 = Pizza.create_margherita("large")
    pizza2 = Pizza.create_pepperoni("medium")
    pizza3 = Pizza.create_veggie("small")
    print("Individual Pizzas:")
    for pizza in [pizza1, pizza2, pizza3]:
        print(f" {pizza} - ${pizza.calculate_price()}")
    # Test order
    order1 = PizzaOrder()
    order1.add_pizza(pizza1)
    order1.add_pizza(pizza2)
    print(f"\n{order1}")
    # Test order from string
    print("\nOrder from string:")
    order2 = OrderManager.create_order_from_string(
    "large pepperoni, small margherita, medium veggie"
    )
    print(OrderManager.format_receipt(order2))
    print(f"\nTotal orders created: {PizzaOrder.get_total_orders()}")
    
class Duration:
    def __init__(self, hours=0, minutes=0, seconds=0):
        # TODO: Validate minutes and seconds (0-59)
        # TODO: Store values
        # Hint: Convert overflow (e.g., 90 seconds = 1 min 30 sec)
        while seconds >= 60:
            minutes +=1
            seconds = (seconds - 60)
        while minutes >=60:
            hours +=1
            minutes = (minutes - 60)
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds
    @property
    def total_seconds(self):
        return (self.hours * 3600) + (self.minutes * 60) + self.seconds
    def __str__(self):
        string = ""
        if self.hours > 0:
            string += f"{self.hours}h "
        if self.minutes > 0:
            string += f"{self.minutes}m "
        if self.seconds > 0:
            string += f"{self.seconds}s"
        return string
    def __repr__(self):
        # TODO: Return "Duration(h, m, s)"
        return f"Duration({self.hours}, {self.minutes}, {self.seconds})"
    def __add__(self, other):
        return Duration(0,0,self.total_seconds + other.total_seconds)
    def __sub__(self, other):
        s = (self.total_seconds - other.total_seconds)
        if s < 0:
            return Duration(0,0,0)
        else: return Duration(0,0,s)
    def __mul__(self, multiplier):
        return Duration(0,0,self.total_seconds * multiplier)
    def __eq__(self, other):
        if self.total_seconds == other.total_seconds:
            return True
        else: return False
    def __lt__(self, other):
        if self.total_seconds < other.total_seconds:
            return True
        else: return False
    def __le__(self, other):
        if self.total_seconds <= other.total_seconds:
            return True
        else: return False
# Test your code
if __name__ == "__main__":
    # Create durations
    d1 = Duration(1, 30, 45)
    d2 = Duration(0, 45, 30)
    d3 = Duration(2, 15, 0)
    print("Durations:")
    print(f" d1 = {d1}")
    print(f" d2 = {d2}")
    print(f" d3 = {d3}")
    # Test arithmetic
    print("\nArithmetic:")
    print(f" d1 + d2 = {d1 + d2}")
    print(f" d3 - d1 = {d3 - d1}")
    print(f" d2 * 3 = {d2 * 3}")
    # Test comparisons
    print("\nComparisons:")
    print(f" d1 == d2? {d1 == d2}")
    print(f" d1 < d3? {d1 < d3}")
    print(f" d2 <= d1? {d2 <= d1}")
    # Test sorting
    durations = [d3, d1, d2]
    durations.sort()
    print("\nSorted durations:")
    for d in durations:
        print(f" {d}")
    # Test overflow
    print("\nOverflow test:")
    d4 = Duration(0, 90, 90) # Should become 1h 31m 30s
    print(f" Duration(0, 90, 90) = {d4}")
    # Test repr
    print(f"\nRepr: {repr(d1)}")