class Shop_Data:
    def __init__(self, new_products=""):
        self.all_products = {}
        self.cart_items_number = 0
        self.cart_items = {}
        self.grocery_products = {
            "101": {
                "name": "Bananas",
                "amount": 100,
                "price": 2.99
            },
            "102": {
                "name": "Apples",
                "amount": 75,
                "price": 3.50
            },
            "103": {
                "name": "Milk",
                "amount": 10,
                "price": 1.99
            },
            "104": {
                "name": "Bread",
                "amount": 20,
                "price": 2.25
            },
            "105": {
                "name": "Eggs",
                "amount": 30,
                "price": 4.75
            },
            "106": {
                "name": "Rice",
                "amount": 50,
                "price": 5.99
            },
            "107": {
                "name": "Pasta",
                "amount": 25,
                "price": 3.25
            },
            "108": {
                "name": "Tomatoes",
                "amount": 40,
                "price": 2.75
            },
            "109": {
                "name": "Potatoes",
                "amount": 80,
                "price": 1.50
            },
            "110": {
                "name": "Chicken",
                "amount": 15,
                "price": 7.99
            },
            "111": {
                "name": "Oranges",
                "amount": 60,
                "price": 4.25
            },
            "112": {
                "name": "Onions",
                "amount": 50,
                "price": 1.75
            },
            "113": {
                "name": "Carrots",
                "amount": 40,
                "price": 2.99
            },
            "114": {
                "name": "Spinach",
                "amount": 20,
                "price": 3.50
            },
            "115": {
                "name": "Cucumbers",
                "amount": 30,
                "price": 1.99
            },
            "116": {
                "name": "Bell Peppers",
                "amount": 35,
                "price": 2.49
            },
            "117": {
                "name": "Broccoli",
                "amount": 20,
                "price": 3.99
            },
            "118": {
                "name": "Lettuce",
                "amount": 15,
                "price": 2.75
            },
            "119": {
                "name": "Strawberries",
                "amount": 10,
                "price": 6.99
            },
            "120": {
                "name": "Blueberries",
                "amount": 8,
                "price": 5.50
            },
            "121": {
                "name": "Avocados",
                "amount": 12,
                "price": 3.99
            },
            "122": {
                "name": "Grapes",
                "amount": 25,
                "price": 4.75
            },
            "123": {
                "name": "Watermelon",
                "amount": 5,
                "price": 7.25
            },
            "124": {
                "name": "Pineapple",
                "amount": 10,
                "price": 5.99
            },
            "125": {
                "name": "Kiwi",
                "amount": 4,
                "price": 1.99
            },
            "126": {
                "name": "Celery",
                "amount": 10,
                "price": 2.50
            },
            "127": {
                "name": "Zucchini",
                "amount": 15,
                "price": 2.25
            },
            "128": {
                "name": "Asparagus",
                "amount": 8,
                "price": 4.50
            },
            "129": {
                "name": "Cauliflower",
                "amount": 12,
                "price": 3.75
            },
        }

        self.cakes = {
            "201": {
                "name": "Chocolate Fudge Cake",
                "amount": 20,
                "price": 25.99
            },
            "202": {
                "name": "Vanilla Bean Cake",
                "amount": 25,
                "price": 29.50
            },
            "203": {
                "name": "Red Velvet Cheesecake",
                "amount": 18,
                "price": 27.99
            },
            "204": {
                "name": "Lemon Blueberry Cake",
                "amount": 15,
                "price": 22.75
            },
            "205": {
                "name": "Strawberry Shortcake",
                "amount": 22,
                "price": 31.25
            },
            "206": {
                "name": "Carrot Cake",
                "amount": 17,
                "price": 26.99
            },
            "207": {
                "name": "Coconut Cream Cake",
                "amount": 14,
                "price": 23.50
            },
            "208": {
                "name": "Pineapple Upside-Down Cake",
                "amount": 16,
                "price": 28.75
            },
            "209": {
                "name": "Marble Cake",
                "amount": 21,
                "price": 30.99
            },
            "210": {
                "name": "Raspberry Chocolate Cake",
                "amount": 19,
                "price": 27.25
            },
            "211": {
                "name": "Chocolate Fudge Cake",
                "amount": 20,
                "price": 25.99
            },
            "212": {
                "name": "Vanilla Bean Cake",
                "amount": 25,
                "price": 29.50
            },
            "213": {
                "name": "Red Velvet Cheesecake",
                "amount": 18,
                "price": 27.99
            },
            "214": {
                "name": "Lemon Blueberry Cake",
                "amount": 15,
                "price": 22.75
            },
            "215": {
                "name": "Strawberry Shortcake",
                "amount": 22,
                "price": 31.25
            },
            "216": {
                "name": "Carrot Cake",
                "amount": 17,
                "price": 26.99
            },
            "217": {
                "name": "Coconut Cream Cake",
                "amount": 14,
                "price": 23.50
            },
            "218": {
                "name": "Pineapple Upside-Down Cake",
                "amount": 16,
                "price": 28.75
            },
            "219": {
                "name": "Marble Cake",
                "amount": 21,
                "price": 30.99
            },
            "220": {
                "name": "Raspberry Chocolate Cake",
                "amount": 19,
                "price": 27.25
            },
            # New cakes
            "221": {
                "name": "Triple Chocolate Cake",
                "amount": 30,
                "price": 35.99
            },
            "222": {
                "name": "Classic Cheesecake",
                "amount": 26,
                "price": 33.50
            },
            "223": {
                "name": "Mango Passionfruit Cake",
                "amount": 18,
                "price": 38.99
            },
            "224": {
                "name": "Hazelnut Praline Cake",
                "amount": 23,
                "price": 40.75
            },
            "225": {
                "name": "Cookies and Cream Cake",
                "amount": 20,
                "price": 36.25
            },
            "226": {
                "name": "Lemon Meringue Cake",
                "amount": 14,
                "price": 37.50
            },
            "227": {
                "name": "Tiramisu Cake",
                "amount": 19,
                "price": 34.99
            },
            "228": {
                "name": "Pistachio Rose Cake",
                "amount": 17,
                "price": 39.25
            },
            "229": {
                "name": "Blueberry Lemon Cake",
                "amount": 22,
                "price": 36.99
            },
            "230": {
                "name": "Salted Caramel Cake",
                "amount": 25,
                "price": 38.50
            },
        }

        self.books = {
            "301": {
                "name": "Cosmos",
                "author": "Carl Sagan",
                "subject": "Astronomy",
                "price": 15.99,
                "rating": 4.7,
                "published_year": 1980
            },
            "302": {
                "name": "A Brief History of Time",
                "author": "Stephen Hawking",
                "subject": "Physics",
                "price": 12.50,
                "rating": 4.6,
                "published_year": 1988
            },
            "303": {
                "name": "The Selfish Gene",
                "author": "Richard Dawkins",
                "subject": "Biology",
                "price": 11.99,
                "rating": 4.5,
                "published_year": 1976
            },
            "304": {
                "name": "The Structure of Scientific Revolutions",
                "author": "Thomas S. Kuhn",
                "subject": "History and Philosophy of Science",
                "price": 14.75,
                "rating": 4.4,
                "published_year": 1962
            },
            "305": {
                "name": "Gödel, Escher, Bach: An Eternal Golden Braid",
                "author": "Douglas Hofstadter",
                "subject": "Computer Science and Mathematics",
                "price": 18.25,
                "rating": 4.8,
                "published_year": 1979
            },
            "306": {
                "name": "The Origin of Species",
                "author": "Charles Darwin",
                "subject": "Biology",
                "price": 13.99,
                "rating": 4.5,
                "published_year": 1859
            },
            "307": {
                "name": "The Elegant Universe",
                "author": "Brian Greene",
                "subject": "Physics",
                "price": 16.50,
                "rating": 4.4,
                "published_year": 1999
            },
            "308": {
                "name": "Sapiens: A Brief History of Humankind",
                "author": "Yuval Noah Harari",
                "subject": "Anthropology",
                "price": 10.99,
                "rating": 4.6,
                "published_year": 2011
            },
            "309": {
                "name": "The Double Helix",
                "author": "James D. Watson",
                "subject": "Biology",
                "price": 9.75,
                "rating": 4.3,
                "published_year": 1968
            },
            "310": {
                "name": "The Quantum Universe",
                "author": "Brian Cox",
                "subject": "Physics",
                "price": 14.25,
                "rating": 4.7,
                "published_year": 2011
            },
        }

        # kanstovari = {
        #               "books": books }

    def show_grocery_list(self):
        """Shows the list of groceries in the shop"""
        print("\n\nProducts in grocery measured in kg/l")
        for product in self.grocery_products:
            print(f"\nID: {product} ", end="     ")
            for k, v in self.grocery_products[product].items():
                if k == "amount":
                    continue
                print(f"{v}", end=": ")

    def show_books_list(self):
        """Shows the list of books in the shop"""
        print("\n\n\tBooks in the store: ")
        for book in self.books:
            print(f"\nID: {book}")
            for k, v in self.books[book].items():
                print(f"{k}: {v}")

    def show_cakes_list(self):
        """Shows the list of cakes in the shop"""
        print("\n\nProducts in grocery measured in kg/l")
        for product in self.cakes:
            print(f"\n ID: {product} ", end="     ")
            for k, v in self.cakes[product].items():
                if k == "amount":
                    continue
                print(f"{v}", end=": ")

    def gather_all(self):
        self.all_products.update(self.grocery_products)
        self.all_products.update(self.cakes)
        self.all_products.update(self.books)

    def isin(self, id_item):
        if id_item in self.all_products:
            return True
        else:
            return False

    def isincart(self, id_item):
        if id_item in self.cart_items:
            return True
        else:
            return False

    def add_item(self, id_pro, given_value):
        """Adds item into the cart"""
        if Shop_Data.isin(self, id_item=id_pro):
            if id_pro not in self.books:
                if id_pro in self.cart_items:
                    self.cart_items[id_pro]["amount"] += given_value
                else:
                    self.cart_items[id_pro] = dict(self.all_products[id_pro])
                    self.cart_items[id_pro]["amount"] = given_value
                    self.cart_items_number += 1
                remaining = self.all_products[id_pro]["amount"] - given_value
                self.all_products[id_pro]["amount"] = remaining
            else:
                self.cart_items[id_pro] = dict(self.all_products[id_pro])
                self.cart_items_number += 1
                self.cart_items[id_pro]["amount"] = given_value
            print(f"'{self.all_products[id_pro]["name"]}' is successfully added to the cart!")

    def remove_item(self, id_pro, given_value):
        """Removes item from the cart"""
        if Shop_Data.isincart(self, id_item=id_pro):
            if id_pro not in self.books:
                self.cart_items[id_pro]["amount"] -= given_value
                self.all_products[id_pro]["amount"] += given_value
                if self.cart_items[id_pro]["amount"] <= 0:
                    del self.cart_items[id_pro]
                    self.cart_items_number -= 1
            else:
                del self.cart_items[id_pro]
                self.cart_items_number -= 1

            print(f"'{self.all_products[id_pro]["name"]}' is successfully removed from the cart!")

    def report(self):
        """Shows the report about what you have in your cart"""
        print(f"\nYou have {self.cart_items_number} type of products")
        for i in self.cart_items:
            print(f"\nID: {i}")
            if i not in self.books:
                for k, v in self.cart_items[i].items():
                    if k == "amount":
                        print(f"{k}: {v} kg")
                    else:
                        print(f"{k}: {v}")
            else:
                for k, v in self.cart_items[i].items():
                    if k == "amount":
                        print(f"{k}: {v}")
                    else:
                        print(f"{k}: {v}")

    def calculate_bill(self):
        total = 0
        if self.cart_items:
            for i in self.cart_items:
                for k, v in self.cart_items[i].items():
                    if k == "price":
                        fee = self.cart_items[i][k] * self.cart_items[i]["amount"]
                        total += fee
            print(f"\n\nYour total bill: ${round(total, 2)}")
        else:
            print("You have nothing in your cart")
