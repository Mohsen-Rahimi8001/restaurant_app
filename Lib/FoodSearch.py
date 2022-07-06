import difflib
from Models.Food import Food
from enum import Enum
from numbers import Real 


class FoodSearch:


    class By(Enum):
        """Enum for search by"""

        TITLE = (1, 'title')
        DESCRIPTION = (2, 'description')
        CATEGORY = (3, 'category')
        MATERIALS = (4, 'materials')


    @staticmethod
    def GetSimilarity(string1:str, string2:str) -> float:
        """Rates the similarity between two strings 
        and return a float number between 0 and 1"""

        return difflib.SequenceMatcher(None, string1.lower(), string2.lower()).ratio()


    @staticmethod
    def ValidateInputs(string:str, by:By, similarity:float):
        """Validates the inputs"""

        if not isinstance(string, str):
            raise TypeError('Search query must be a string')
        
        if not isinstance(by, FoodSearch.By):
            raise TypeError(f'unsupported search by {by}')

        if not isinstance(similarity, Real):
            raise TypeError('similarity must be a float')

        if similarity > 1 or similarity < 0:
            raise ValueError('similarity must be between 0 and 1')


    @staticmethod
    def find(by:By, string:str, similarity:float = 0.7) -> list[Food]:
        """Finds foods by the given string"""

        FoodSearch.ValidateInputs(string, by, similarity)

        foods = Food.GetAll()
        
        result = []
        for food in foods:
            if FoodSearch.GetSimilarity(getattr(food, by.value[1]), string) > similarity:
                result.append(food)
        
        return result


    @staticmethod
    def find_by_all(data:dict[str,str|tuple], similarity:float = 0.7) -> list[Food]:
        """Search for all foods similar to data"""

        assert isinstance(similarity, Real), 'similarity must be a float'

        if 'price' in data:
            price = data['price']
            data.pop('price')
        else:
            price = None

        result = []
        
        foods = Food.GetAll()
        
        for food in foods:
            
            number = 0
            score = 0

            if 'category' in data:
                number += 1
                score += FoodSearch.GetSimilarity(data['category'], food.category)
            if 'title' in data:
                number += 1
                score += FoodSearch.GetSimilarity(data['title'], food.title)
            if 'description' in data:
                number += 1
                score += FoodSearch.GetSimilarity(data['description'], food.description)
            if 'materials' in data:
                number += 1
                score += FoodSearch.GetSimilarity(data['materials'], food.materials)
            
            score /= number

            if score > similarity:
                result.append(food)

            score = 0
            number = 0

        # filter by price
        if price is not None:
            result = list(filter(lambda p : price[0] < p < price[1], result))

        return result
    

    @staticmethod
    def price_between(min:float, max:float) -> list[Food]:
        """Finds foods with a sale price between min and max"""

        assert isinstance(min, Real) and isinstance(max, Real), "min and max must be floats"

        foods = Food.GetAll()

        result = []

        for food in foods:
            if food.sale_price >= min and food.sale_price <= max:
                result.append(food)

        return result
