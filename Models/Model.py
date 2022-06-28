class Model:

    def __init__(self, id : int):
        self.id : int = id

    @staticmethod
    def Create(data):
        raise NotImplementedError

    @staticmethod
    def Get(id : int):
        raise NotImplementedError

    @staticmethod
    def GetAll():
        raise NotImplementedError

    @staticmethod
    def Exists(id : int):
        raise NotImplementedError

    @staticmethod
    def Update(id : int, data):
        raise NotImplementedError

    @staticmethod
    def Delete(id : int):
        raise NotImplementedError


    #properties

    def getId(self) -> int:
        return self.__id

    def setId(self, id):

        if not isinstance(id, int) or not id >= 0:
            raise TypeError("invalid id")

        self.__id = id

    id = property(fget = getId, fset = setId)