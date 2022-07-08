from Models.Model import Model
from DataBase.Sqlite import Database
from Lib.Image import Image
import os


class Food(Model):
    
    TableName = 'foods'
    PrimaryKey = 'id'
    DefaultImage = r'.\Resources\Images\food_default.png'

    def __init__(self, id:int, title:str, stock:int, fixed_price:int, sale_price:int,\
         description:str, category:str, materials:str, image:str=None) -> None:
        """
        Constructor for Food class
        :param id: The id of the food
        :param title: The title of the food
        :param stock: Available stock of the food
        :param sale_price: The sell price of the food
        :param fixed_price: The buy price of the food
        :param description: The description of the food
        :param category: The category of the food
        :param materials: The materials used to create the food
        :param image: Directory of the picture of the food
        """
        super().__init__(id)
        self.title = title
        self.stock = stock
        self.sale_price = sale_price
        self.fixed_price = fixed_price
        self.description = description
        self.category = category
        self.materials = materials
        self.image = image
    
    def __eq__(self, other: 'Food') -> bool:
        """
        Overrided equality operator
        :param other: The other food to compare with
        :return: True if the two foods are equal, False otherwise
        """
        if not isinstance(other, Food):
            return False

        return self.id == other.id and self.title == other.title and self.stock == other.stock and\
               self.sale_price == other.sale_price and self.fixed_price == other.fixed_price and\
               self.description == other.description and self.category == other.category and\
               self.materials == other.materials and os.path.samefile(self.image, other.image)

    @staticmethod
    def ValidateStock(stock:int):
        """Validates the stock of the food
        :param stock: The stock of the food
        :return: stock if the stock is valid, raises proper error otherwise
        """
        if not isinstance(stock, int):
            raise TypeError('Stock must be an integer')
        elif stock < 0:
            raise ValueError("Stock cannot be negative")
        
        return stock

    @staticmethod
    def ValidateImage(image:str):
        """Validates the image of the food
        :param image: The image of the food
        :return: image if the image is valid, raises proper error otherwise
        """
        if image is None:
            return Food.DefaultImage
        if not isinstance(image, str):
            raise TypeError('Image must be a string')
        elif not os.path.isfile(image):
            return Food.DefaultImage
        
        return image

    @staticmethod
    def ValidatePrice(price:int):
        """Validates the price of the food
        :param price: The price of the food
        :return: price if the price is valid, raises proper error otherwise
        """
        if not isinstance(price, int):
            raise TypeError('Price must be an integer')
        elif price < 0:
            raise ValueError("Price cannot be negative")
        
        return price

    @property
    def stock(self):
        return self._stock
    
    @stock.setter
    def stock(self, new_number:int):
        self._stock = Food.ValidateStock(new_number)
        
    @property
    def sale_price(self):
        return self._sale_price
    
    @sale_price.setter
    def sale_price(self, new_sale_price:int):
        self._sale_price = Food.ValidatePrice(new_sale_price)
    
    @property
    def fixed_price(self):
        return self._fixed_price

    @fixed_price.setter
    def fixed_price(self, new_fixed_price:int):
        self._fixed_price = Food.ValidatePrice(new_fixed_price)

    @property
    def image(self):
        return self._image
    
    @image.setter
    def image(self, new_image:str):
        self._image = Food.ValidateImage(new_image)

    @staticmethod
    def Create(data:dict):
        """Create a row in the database with the given data"""
        if not isinstance(data, dict):
            raise TypeError("data must be a dictionary")

        if 'image' in data:
            try:
                data['image'] = Image.GetFromDirectory(Food.ValidateImage(data['image']))
            except FileNotFoundError or TypeError:
                data['image'] = Food.DefaultImage
        else:
            data['image'] = Food.DefaultImage

        if 'title' not in data:
            raise KeyError("title is required")
        else:
            data['title'] = str(data['title'])

        if 'stock' not in data:
            data['stock'] = 1
        else:
            data['stock'] = Food.ValidateStock(data['stock'])

        if 'sale_price' not in data:
            raise KeyError("sale_price is required")
        else:
            data['sale_price'] = Food.ValidatePrice(data['sale_price'])
        
        if 'fixed_price' not in data:
            raise KeyError("fixed_price is required")
        else:
            data['fixed_price'] = Food.ValidatePrice(data['fixed_price'])
        
        if 'category' not in data:
            data['category'] = ""
        else:
            data['category'] = str(data['category'])
        
        if 'materials' not in data:
            data['materials'] = ""
        else:
            data['materials'] = str(data['materials'])

        lastRowId = Database.Create(Food.TableName, data)
        return lastRowId



    @staticmethod
    def Get(id:int):
        """Get a food from the database with the given id"""
        fetched_data = Database.Read(Food.TableName, Food.PrimaryKey, id)
        
        # if error happens or nothing found, return None
        if type(fetched_data) != list or not len(fetched_data):
            return None

        fetched_data = fetched_data[0]

        return Food(
            id = fetched_data[0],
            title = fetched_data[1],
            stock = fetched_data[2],
            fixed_price = fetched_data[3],
            sale_price = fetched_data[4],
            description = fetched_data[5],
            category = fetched_data[6],
            materials = fetched_data[7],
            image = fetched_data[8]
        )


    @staticmethod
    def Exists(id:int):
        """Checks if a food with the given id exists"""
        return Database.Exists(Food.TableName, Food.PrimaryKey, id)
    
    @staticmethod
    def Update(id:int, data:dict):
        """Update a row in the database with the given data"""

        if 'image' in data:
            try:
                data['image'] = Image.GetFromDirectory(Food.ValidateImage(data['image']))
            except FileNotFoundError or TypeError:
                data.pop('image')

        if 'title' in data:
            data['title'] = str(data['title'])

        if 'stock' in data:
            data['stock'] = Food.ValidateStock(data['stock'])
        
        if 'sale_price' in data:
            data['sale_price'] = Food.ValidatePrice(data['sale_price'])
        
        if 'fixed_price' in data:
            data['fixed_price'] = Food.ValidatePrice(data['fixed_price'])
        
        if 'category' in data:
            data['category'] = str(data['category'])
        
        if 'materials' in data:
            data['materials'] = str(data['materials'])

        Database.Update(Food.TableName, Food.PrimaryKey, id, data)

    @staticmethod
    def Delete(id:int):
        """Delete a row in the database with the given id"""
        Database.Delete(Food.TableName, Food.PrimaryKey, id)

    @staticmethod
    def GetAll():
        """Get all foods from the database"""
        fetched_data = Database.ReadAll(Food.TableName)

        if type(fetched_data) != list or not len(fetched_data):
            return []

        return [Food(
            id = row[0],
            title = row[1],
            stock = row[2],
            fixed_price = row[3],
            sale_price = row[4],
            description = row[5],
            category = row[6],
            materials = row[7],
            image = row[8]
        ) for row in fetched_data]



    def addToStock(self, number : int):
        """add number to food stock"""

        self.stock += number
        Food.Update(self.id, {"stock" : self.stock})


    def reduceStock(self, number: int):
        """reduce stock value by number"""

        if self.stock - number > 0:

            self.stock += number
            Food.Update(self.id, {"stock": self.stock})