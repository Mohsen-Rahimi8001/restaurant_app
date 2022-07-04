import json
from Models.Menu import Menu


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
                foods=menu["foods"],
                date=menu["date"]
            ) for i, menu in enumerate(data)
        ]


    @staticmethod
    def SetDefaultMenus(data:list[dict]):
        """Update default menus json file with data"""
        
        # dump the data to json file
        with open(r".\Constants\DefaultMenus.json", "w") as file:
            json.dump(data, file, indent=4)

