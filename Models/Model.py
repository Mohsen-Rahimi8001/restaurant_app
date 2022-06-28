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
    def Exists(id : int):
        raise NotImplementedError

    @staticmethod
    def Update(id : int, data):
        raise NotImplementedError

    @staticmethod
    def Delete(id : int):
        raise NotImplementedError
