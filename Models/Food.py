from Models.Model import Model
from DataBase.Sqlite import Database


class Food(Model):

    def __init__(self, id:int, title:str, stock:int, sale_price:int, fixed_price:int,\
         description:str, category:str, materials:str, image:str) -> None:
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
    
    @property
    def stock(self):
        return self._number
    
    @stock.setter
    def stock(self, new_number:int):
        if isinstance(new_number, int):
            self._number = new_number
        else:
            raise TypeError("stock must be an integer")

    @property
    def sale_price(self):
        return self._sale_price
    
    @sale_price.setter
    def sale_price(self, new_sale_price:int):
        if isinstance(new_sale_price, int):
            self._sale_price = new_sale_price
        else:
            raise TypeError("sale_price must be an integer")
    
    @property
    def fixed_price(self):
        return self._fixed_price

    @fixed_price.setter
    def fixed_price(self, new_fixed_price:int):
        if isinstance(new_fixed_price, int):
            self._fixed_price = new_fixed_price
        else:
            raise TypeError("fixed_price must be an integer")

    @property
    def image(self):
        return self._image
    
    @image.setter
    def image(self, new_image:str):
        if not isinstance(new_image, str):
            raise TypeError("image must be a string")

        self._image = new_image

    @staticmethod
    def Create(data:dict):
        Database.Create('foods', data)

    @staticmethod
    def Get(id:int):
        feched_data = Database.Read('foods', 'id', id)
        
        if feched_data is None:
            return None
        
        feched_data = feched_data[0]

        return Food(
            id = feched_data[0],
            title = feched_data[1],
            stock = feched_data[2],
            fixed_price = feched_data[3],
            sale_price = feched_data[4],
            description = feched_data[5],
            category = feched_data[6],
            materials = feched_data[7],
            image = feched_data[8]
        )


    @staticmethod
    def Exists(id:int):
        return Database.Exists('foods', 'id', id)
    
    @staticmethod
    def Update(id:int, data:dict):
        Database.Update('foods', 'id', id, data)

    @staticmethod
    def Delete(id:int):
        Database.Delete('foods', 'id', id)
