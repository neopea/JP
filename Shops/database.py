from tinydb import TinyDB, Query
import base64

class product_handler:
    def __init__(self):
        self.db = TinyDB('product.json')
        self.Product = Query()
    
    def add_product(self, name, description, image_path, expiration_date, price, quantity_available, category):
        """Add a new product to the database."""
        with open(image_path, "rb") as image_file: 
            encoded_string = base64.b64encode(image_file.read()).decode('utf-8') 
        self.db.insert({
            'name': name,
            'description': description,
            'expiration_date': expiration_date,
            'price': price,
            'quantity_available': quantity_available,
            'category': category
        })

    def update_product_quantity(self, product_name, change_quantity):
        """Update the quantity of a specific product."""
        # Search for the product by name
        product = self.db.get(self.Product.name == product_name)

        if product:
            # Update the quantity by adding the change_quantity
            new_quantity = product['quantity_available'] + change_quantity
            self.db.update({'quantity_available': new_quantity}, self.Product.name == product_name)
        else:
            print(f"Product '{product_name}' not found.")


    def get_product(self, product_name):
        """Retrieve product information by name."""
        product = self.db.get(self.Product.name == product_name)
        if product:
            return product
        else:
            print(f"Product '{product_name}' not found.")
            return None

    def get_all_products(self):
        """Retrieve all products from the database."""
        return self.db.all()


class order_handler():
    def __init__(self):
        self.db = TinyDB('order.json')
        self.Product = Query()

    def add_record(self, name , quantity , time):
        self.db.insert({
            "name" : name ,
            "quantity" : quantity, 
            "pick up time" : time
        })

    def delete_record(self , name):
        self.db.remove(self.Product.name == name)

    def get_all_record(self):
        return self.db.all()


class restaurant_handler():
    def __init__(self):
        self.db = TinyDB('restaurant.json')
        self.Product = Query()

    def add_record(self, restaurant_name,coordinates, location , restaurant_type):
        # Create a new restaurant record
        new_record = {
            'restaurant_name': restaurant_name,
            'coordinates': coordinates ,
            'location' : location , 
            'type' : restaurant_type
        }
        
        # Insert the new record into the TinyDB
        self.db.insert(new_record)
        print(f"Record added: {new_record}")

    def get_record(self, restaurant_name):
        # Query the TinyDB for a restaurant by name
        result = self.db.search(self.Product.restaurant_name == restaurant_name)
        if result:
            return result  # Return the found records
        else:
            return None  # Return None if no records found


class con_handler:
    def __init__(self):
        self.db = TinyDB('convenient.json')
        self.Product = Query()

    def add_record(self, restaurant_name,coordinates, location):
        # Create a new restaurant record
        new_record = {
            'con_name': restaurant_name,
            'coordinates': coordinates ,
            'location' : location , 
        }
        
        # Insert the new record into the TinyDB
        self.db.insert(new_record)
        print(f"Record added: {new_record}")

    def get_record(self, restaurant_name):
        # Query the TinyDB for a restaurant by name
        result = self.db.search(self.Product.con_name == restaurant_name)
        if result:
            return result  # Return the found records
        else:
            return None  # Return None if no records found

    
# Example usage
if __name__ == '__main__':
    #testing case 
    print('hi')


