from Models.Model import Model
from DataBase.Sqlite import Database
import datetime as dt
from Constants.RegExValidations import Patterns
import re


class Message(Model):

    TableName = 'messages'
    PrimaryKey = 'id'
    DateTimePattern = '%Y-%m-%d %H:%M:%S'
    
    def __init__(self, id : int, message : str, datetime : 'dt.datetime', admin_email : str):
        super().__init__(id)
        self.message = message
        self.datetime = datetime
        self.admin_email = admin_email

    def __eq__(self, other):
        if not isinstance(other, Message):
            return False
        else:
            return self.id == other.id and self.message == other.message and\
                 self.datetime == other.datetime and self.admin_email == other.admin_email


    @staticmethod
    def ValidateDateTime(datetime:str):
        """Validate datetime format"""

        if not isinstance(datetime, str):
            raise TypeError("Datetime must be a string")
        else:
            try:
                dt.datetime.strptime(datetime, Message.DateTimePattern)
            except ValueError:
                raise ValueError("Incorrect datetime format")

        return datetime

    @staticmethod
    def ValidateEmail(email:str):
        """Validate email format"""

        if not isinstance(email, str):
            raise TypeError("Email must be a string")
        elif not re.match(Patterns.EMAIL.value, email):
            raise ValueError("Incorrect email format")
        
        return email

    @property
    def message(self):
        return self._message

    @message.setter
    def message(self, message:str):
        if not isinstance(message, str):
            raise TypeError("Message must be a string")
        self._message = message

    @property
    def datetime(self):
        return self._datetime

    @datetime.setter
    def datetime(self, datetime:'dt.datetime'):
        if not isinstance(datetime, dt.datetime):
            raise TypeError("Datetime must be a datetime object")
        self._datetime = datetime

    @property
    def admin_email(self):
        return self._admin_email

    @admin_email.setter
    def admin_email(self, admin_email:str):
        if not isinstance(admin_email, str):
            raise TypeError("Admin email must be a string")

        if not re.match(Patterns.EMAIL.value, admin_email):
            raise ValueError("Admin email must be a valid email")

        self._admin_email = admin_email


    @staticmethod
    def Create(data:dict):
        """Create a new message in database"""

        if 'id' in data:
            raise KeyError("id is not allowed")

        if not 'message' in data:
            raise KeyError("Message is required")
        else:
            data['message'] = str(data['message'])
        
        if not 'datetime' in data:
            raise KeyError("Datetime is required")
        else:
            data['datetime'] = Message.ValidateDateTime(data['datetime'])

        if not 'admin_email' in data:
            raise KeyError("Admin email is required")
        else:
            data['admin_email'] = Message.ValidateEmail(data['admin_email'])

        return Database.Create(Message.TableName, data)

    @staticmethod
    def GetAll():
        """Fetches all messages in the database and return list of messages"""
            
        messages = Database.ReadAll(Message.TableName)

        if type(messages) != list or not len(messages):
            return []

        return [
            Message(
                id=message[0],
                message=message[1],
                datetime=dt.datetime.strptime(message[2], Message.DateTimePattern),
                admin_email=message[3]
            ) for message in messages
        ]

    @staticmethod
    def Get(id: int):
        """Fetches a message from database by id"""

        message = Database.Read(Message.TableName, Message.PrimaryKey, id)
        
        # if error happens or nothing found, return None
        if type(message) != list or not len(message):
            return None

        message = message[0]

        return Message(
            id=message[0],
            message=message[1],
            datetime=dt.datetime.strptime(message[2], Message.DateTimePattern),
            admin_email=message[3]
        )

    @staticmethod
    def Delete(id: int):
        """Delete a message from database by id"""

        Database.Delete(Message.TableName, Message.PrimaryKey, id)

    @staticmethod
    def Update(id: int, data:dict):
        """Update a message in database by id"""

        if 'id' in data:
            raise KeyError("id is not allowed")

        if not 'message' in data:
            raise ValueError("New message is required")
        
        if 'datetime' in data:
            raise KeyError("Datetime is not allowed")
        
        if 'admin_email' in data:
            raise KeyError("Admin email is not allowed")
        
        Database.Update(Message.TableName, Message.PrimaryKey, id, data)

    @staticmethod
    def Exists(id: int):
        """Check if message exists in database by id"""

        return Database.Exists(Message.TableName, Message.PrimaryKey, id)
