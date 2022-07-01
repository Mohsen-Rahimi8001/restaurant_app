from Models.Model import Model
from Models.Food import Food
from Models.User import User
from DataBase.Sqlite import Database
import datetime as dt


class Comment(Model):

    TableName = 'comments'
    PrimaryKey = 'id'
    DateTimePattern = "%Y-%m-%d %H:%M:%S"
    DatePattern = "%Y-%m-%d"

    def __init__(self, id: int, comment: str, datetime:str, user_id: int, food_id: int):
        super().__init__(id)
        self.comment = comment
        self.datetime = datetime
        self.user_id = user_id
        self.food_id = food_id

    def __eq__(self, other: 'Comment') -> bool:
        if not isinstance(other, Comment):
            return False
        
        return self.id == other.id and self.comment == other.comment and self.datetime == other.datetime and\
                self.user_id == other.user_id and self.food_id == other.food_id
    
    def __repr__(self):
        return f'Comment(id={self.id}, comment={self.comment}, datetime={self.datetime}, user_id={self.user_id}, food_id={self.food_id})'

    @staticmethod
    def ValidateDateTime(datetime:str) -> str:
        """Validates the datetime of the comment
        :param datetime: The datetime of the comment
        :return: datetime if it is valid, raises proper error otherwise
        """
        try:
            dt.datetime.strptime(datetime, Comment.DateTimePattern)
        except ValueError:
            raise ValueError("Incorrect data format, should be 'Year-Month-Day Hour:Minute:Second'")

        return datetime

    @staticmethod
    def ValidateDate(date:str):
        """Validates the date of the comment
        :param date: The date of the comment
        :return: date if it is valid, raises proper error otherwise
        """
        try:
            dt.datetime.strptime(date, Comment.DatePattern)
        except ValueError:
            raise ValueError("Incorrect data format, should be 'Year-Month-Day'")

        return date

    @staticmethod
    def ValidateUserId(user_id: int) -> int:
        """Validates the user id of the comment
        :param user_id: The user id of the comment
        :return: user_id if it is valid, raises proper error otherwise
        """
        if not isinstance(user_id, int):
            raise TypeError('User id must be an integer')
        elif user_id < 0:
            raise ValueError("User id cannot be negative")
        elif not User.Exists(user_id):
            raise KeyError("User id does not exist")

        return user_id

    @staticmethod
    def ValidateFoodId(food_id: int) -> int:
        """Validates the food id of the comment
        :param food_id: The food id of the comment
        :return: food_id if it is valid, raises proper error otherwise
        """
        if not isinstance(food_id, int):
            raise TypeError('Food id must be an integer')
        elif food_id < 0:
            raise ValueError("Food id cannot be negative")
        elif not Food.Exists(food_id):
            raise KeyError("Food id does not exist")

        return food_id

    @property
    def comment(self) -> str:
        return self._comment
    
    @comment.setter
    def comment(self, new_comment: str):
        if not isinstance(new_comment, str):
            raise TypeError("comment must be a string")

        self._comment = new_comment

    @property
    def datetime(self) -> 'dt.datetime':
        return self._date
    
    @datetime.setter
    def datetime(self, new_date: str):
        # save dt.datetime object of the datetime string in this property
        self._date = Comment.ValidateDateTime(new_date)

    @property
    def user_id(self) -> int:
        return self._user_id
    
    @user_id.setter
    def user_id(self, new_user_id: int):
        self._user_id = Comment.ValidateUserId(new_user_id)
    
    @property
    def food_id(self) -> int:
        return self._food_id

    @food_id.setter
    def food_id(self, new_food_id: int):
        self._food_id = Comment.ValidateFoodId(new_food_id)

    @staticmethod
    def Create(data:dict):
        """Creates a new row in comments table"""
        assert isinstance(data, dict)

        if 'id' in data:
            raise RuntimeError("id cannot be specified when creating a new comment")

        if 'comment' not in data:
            raise KeyError("comment is required")
        else: 
            data['comment'] = str(data['comment'])

        if 'datetime' not in data:
            raise KeyError("datetime is required")
        else:
            data['datetime'] = Comment.ValidateDateTime(data['datetime'])
        
        if 'user_id' not in data:
            raise KeyError("user_id is required")
        else:
            data['user_id'] = Comment.ValidateUserId(data['user_id'])

        if 'food_id' not in data:
            raise KeyError("food_id is required")
        else:
            data['food_id'] = Comment.ValidateFoodId(data['food_id'])

        return Database.Create(Comment.TableName, data)

    @staticmethod
    def Get(id:int) -> 'Comment':
        """Gets a comment from the database"""
        data = Database.Read(Comment.TableName, Comment.PrimaryKey, id)
        
        # if error happens or nothing found, return None
        if type(data) != list or not len(data):
            return None
        else:
            data = data[0]

        return Comment(
            id = data[0],
            comment = data[1],
            datetime = data[2],
            user_id = data[3],
            food_id = data[4]
            )

    @staticmethod
    def GetAll() -> list['Comment']:
        """Gets all comments from the database"""
        data = Database.ReadAll(Comment.TableName)

        if type(data) != list or not len(data):
            return []

        return [Comment(
            id=row[0],
            comment=row[1],
            datetime=row[2],
            user_id=row[3],
            food_id=row[4]
        ) for row in data]

    @staticmethod
    def GetAllByFood(food_id:int) -> list['Comment']:
        """Gets all comments of food with food_id from the database"""
        data = Database.ReadAll(Comment.TableName)

        if type(data) != list or not len(data):
            return []
        
        # filter the data by food_id
        data = filter(lambda row: row[4] == food_id, data)

        return [Comment(
            id=row[0],
            comment=row[1],
            datetime=row[2],
            user_id=row[3],
            food_id=row[4]
        ) for row in data]

    @staticmethod
    def GetAllByUser(user_id:int) -> list['Comment']:
        """Gets all comments of user with user_id from the database"""
        data = Database.ReadAll(Comment.TableName)

        if type(data) != list or not len(data):
            return []
        
        # filter the data by user_id
        data = filter(lambda row: row[3] == user_id, data)

        return [Comment(
            id=row[0],
            comment=row[1],
            datetime=row[2],
            user_id=row[3],
            food_id=row[4]
        ) for row in data]

    @staticmethod
    def GetAllByDate(date:str) -> list['Comment']:
        """Gets all comments that posted in the date from the database"""

        date = Comment.ValidateDate(date)
        data = Database.ReadAll(Comment.TableName)

        if type(data) != list or not len(data):
            return []
        
        # filter the data by datetime
        data = filter(lambda row: row[2].split()[0] == date, data)

        return [Comment(
            id=row[0],
            comment=row[1],
            datetime=row[2],
            user_id=row[3],
            food_id=row[4]
        ) for row in data]

    @staticmethod
    def GetAllByDateRange(start_date:str, end_date:str) -> list['Comment']:
        """Gets all the comments between start_date and end_date (including start and excluding end) in database"""
        
        # validate dates
        start_date = Comment.ValidateDate(start_date)
        end_date = Comment.ValidateDate(end_date)

        data = Database.ReadAll(Comment.TableName)

        if type(data) != list or not len(data):
            return []
        
        # filter the data by date
        data = filter(
            lambda row: dt.datetime.strptime(row[2], Comment.DateTimePattern) >=
            dt.datetime.strptime(start_date, Comment.DatePattern) and
            dt.datetime.strptime(row[2], Comment.DateTimePattern) < 
            dt.datetime.strptime(end_date, Comment.DatePattern), data)
        
        return [Comment(
            id=row[0],
            comment=row[1],
            datetime=row[2],
            user_id=row[3],
            food_id=row[4]
        ) for row in data]

    @staticmethod
    def Exists(id:int) -> bool:
        """Checks if the comment with id exists"""
        if not isinstance(id, int) or id < 0:
            raise ValueError("id must be a positive integer")
        
        return Database.Exists(Comment.TableName, Comment.PrimaryKey, id)

    @staticmethod
    def Delete(id:int):
        """Deletes the comment with id from the database"""
        if not isinstance(id, int) or id < 0:
            raise ValueError("id must be a positive integer")
        
        Database.Delete(Comment.TableName, Comment.PrimaryKey, id)

    @staticmethod
    def Update(id:int, data:dict):
        """Updates the comment with id in the database"""
        assert isinstance(data, dict)

        if not isinstance(id, int) or id < 0:
            raise ValueError("id must be a positive integer")

        if 'comment' in data:
            data['comment'] = str(data['comment'])

        if 'datetime' in data:
            data['datetime'] = Comment.ValidateDateTime(data['datetime'])
        
        if 'user_id' in data:
            data['user_id'] = Comment.ValidateUserId(data['user_id'])
        
        if 'food_id' in data:
            data['food_id'] = Comment.ValidateFoodId(data['food_id'])

        Database.Update(Comment.TableName, Comment.PrimaryKey, id, data)
