import json
from Models.Menu import Menu
from Models.Food import Food


class MenusController:

    @staticmethod
    def GetDefaultMenus():
        """Get data from json file and return it as a list of dicts"""

        # get data from json file
        with open(r".\Constants\DefaultMenus.json", "r") as file:
            data = json.load(file)

        return [
            Menu(
                id = i + 1,
                title=menu["title"],
                foods=[
                    Food(
                        id=food["id"],
                        title=food["title"],
                        stock=food["stock"],
                        fixed_price=food["fixed_price"],
                        sale_price=food["sale_price"],
                        description=food["description"],
                        category=food["category"],
                        materials=food["materials"],
                        image=food["image"]
                    )for food in menu["foods"]
                    ],
                date=menu["date"]
            ) for i, menu in enumerate(data)
        ]


    @staticmethod
    def SetDefaultMenus(data:list[dict]):
        """Update default menus json file with data"""
        
        # dump the data to json file
        with open(r".\Constants\DefaultMenus.json", "w") as file:
            json.dump(data, file, indent=4)


    @staticmethod
    def GetDefaultMenu(date: int):
        """Get default menu for the given date"""

        # get data from json file
        with open(r".\Constants\DefaultMenus.json", "r") as file:
            data = json.load(file)

        for menu in data:
            if menu["date"] == date:
                return Menu(
                    id = menu["date"],
                    title=menu["title"],
                    foods=[
                        Food(
                            id=food["id"],
                            title=food["title"],
                            stock=food["stock"],
                            fixed_price=food["fixed_price"],
                            sale_price=food["sale_price"],
                            description=food["description"],
                            category=food["category"],
                            materials=food["materials"],
                            image=food["image"]
                        )for food in menu["foods"]
                        ],
                    date=menu["date"]
                )

        return None


    @staticmethod
    def UpdateMenu(date: int, data: dict):
        """Update a menu in the json file with date equal to date"""
            
        # get data from json file
        with open(r".\Constants\DefaultMenus.json", "r") as file:
            menus = json.load(file)

        # update the data
        for menu in menus:
            if menu["date"] == date:
                menu.update(data)
                break

        # dump the data to json file
        with open(r".\Constants\DefaultMenus.json", "w") as file:
            json.dump(menus, file, indent=4)


    @staticmethod
    def AddFoodToMenu(date: int, food: Food):
        """Update a menu in the json file with date equal to date"""
        
        data = {
            "id": food.id,
            "title": food.title,
            "stock": food.stock,
            "fixed_price": food.fixed_price,
            "sale_price": food.sale_price,
            "description": food.description,
            "category": food.category,
            "materials": food.materials,
            "image": food.image,
        }

        # get data from json file
        with open(r".\Constants\DefaultMenus.json", "r") as file:
            menus = json.load(file)

        # update the data
        for menu in menus:
            if menu["date"] == date:
                menu["foods"].append(data)
                break

        # dump the data to json file
        with open(r".\Constants\DefaultMenus.json", "w") as file:
            json.dump(menus, file, indent=4)


    @staticmethod
    def RemoveFoodFromMenu(date: int, food: Food):
        """Update a menu in the json file with date equal to date"""
        
        # get data from json file
        with open(r".\Constants\DefaultMenus.json", "r") as file:
            menus = json.load(file)

        # update the data
        for menu in menus:
            if menu["date"] == date:
                menu["foods"] = list(filter(lambda x: x["id"] != food.id, menu["foods"]))
                break

        # dump the data to json file
        with open(r".\Constants\DefaultMenus.json", "w") as file:
            json.dump(menus, file, indent=4)


    @staticmethod
    def FoodExistsInMenu(date: int, foodId: int):
        """Check if a food with the given id exists in a menu with the given date"""
        
        # get data from json file
        with open(r".\Constants\DefaultMenus.json", "r") as file:
            menus = json.load(file)

        # check if the food exists in the menu
        for menu in menus:
            if menu["date"] == date:
                for food in menu["foods"]:
                    if food["id"] == foodId:
                        return True
                break

        return False


    @staticmethod
    def DeleteFood(foodId: int):
        """delete a food from all menus in the json file"""

        # get all menus from json file
        with open(r".\Constants\DefaultMenus.json", "r") as file:
            menus = json.load(file)

        # delete food from all menus
        for menu in menus:
            menu['foods'] = list(filter(lambda food: food["id"] != foodId, menu['foods']))

        # update json file with new data
        data = [
            {
                "id": menu["date"],
                "title": menu["title"],
                "foods": menu["foods"],
                "date": menu["date"]
            } for menu in menus
        ]

        MenusController.SetDefaultMenus(data)


    @staticmethod
    def GetAllFoods():
        """Get all foods from all menus"""

        # get all menus from json file
        menus = MenusController.GetDefaultMenus()

        # get all foods from all menus
        foods:list[Food] = []
        for menu in menus:
            for food in menu.foods:
                if not food in foods:
                    foods.append(food)

        return foods


    @staticmethod
    def SetFood(id: int, foodData: dict):
        """Update a food in all menus"""

        # get all menus from json file
        menus = MenusController.GetDefaultMenus()

        # update food in all menus
        for menu in menus:
            for food in menu.foods:
                if food["id"] == id:
                    food.update(foodData)

        # update json file with new data    
        data = [
            {
                "title": menu.title,
                "foods": menu.foods,
                "date": menu.date
            } for menu in menus
        ]

        MenusController.SetDefaultMenus(data)


    @staticmethod
    def GetFood(id: int):
        """Get a food from all menus"""

        # get all menus from json file
        menus = MenusController.GetDefaultMenus()

        # get food from all menus
        for menu in menus:
            for food in menu.foods:
                if food.id == id:
                    return food
