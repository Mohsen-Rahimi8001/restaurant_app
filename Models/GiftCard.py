from Models.Model import Model
from DataBase.Sqlite import Database
import datetime as dt


class GiftCard(Model):

    PrimaryKey = 'id'
    TableName = 'gift_cards'

    def __init__(self, id:int, start_date:str, expiration_date:str, amount:int, sent:bool, code:str=None) -> None:
        """
        :param id: The id of the gift card
        :param code: The code of the gift card
        :param start_date: Use the format Year-Month-Day
        :param expiration_date: Use the format Year-Month-Day
        :param amount: The amount of the gift card in percent
        """
        super(GiftCard, self).__init__(id)
        self.id = id
        self.code = code
        self.start_date = start_date
        self.expiration_date = expiration_date
        self.amount = amount
        self.sent = sent
    

    def __str__(self):
        return f'GiftCard({self.id},{self.code},{self.start_date},{self.expiration_date},{self.sent})'
    
    def __repr__(self):
        return f'GiftCard({self.id},{self.code},{self.start_date},{self.expiration_date},{self.sent})'

    def __eq__(self, other):
        if isinstance(other, GiftCard):
            return self.id == other.id and self.code == other.code and self.start_date == other.start_date and self.expiration_date == other.expiration_date
        else:
            return False

    @staticmethod
    def GetDefaultCode() -> str:
        """Returns the current system datetime as the default code"""
        return dt.datetime.now().strftime("%Y%m%d%H%M%S")
    
    @staticmethod
    def ValidateStartDate(startDate:str):
        """
        :param startDate: The start date of the gift card
        :return: datatime object of startDate if the start date is valid, False otherwise
        """
        try:
            return dt.datetime.strptime(startDate, "%Y-%m-%d")
        
        except ValueError:
            return False
    
    @staticmethod
    def ValidateExpirationDate(expirationDate:str, startDate:dt.datetime) -> 'dt.datetime | bool':
        """
        :param expirationDate: The expiration date of the gift card
        :return: datatime object of expirationDate if the expiration date is valid, False otherwise
        """
        try:
            expirationDate = dt.datetime.strptime(expirationDate, "%Y-%m-%d")

            if expirationDate < startDate:
                return False

            return expirationDate
        
        except ValueError:
            return False

    @staticmethod
    def ValidationCode(code:str):
        """Return the code if it is valid else raise an error"""
        if code is None:
            # default code is generated by the system time
            return GiftCard.GetDefaultCode()
        
        elif not isinstance(code, str):
            raise TypeError("invalid code")
        
        else:
            return code

    @staticmethod
    def ValidationAmount(amount:int):
        """Return the amount if it is valid else raise an error"""
        if amount is None:
            raise ValueError("amount can not be None")
        
        elif not isinstance(amount, int):
            raise TypeError("amount must be an integer")
        
        elif amount < 0 or amount > 100:
            raise ValueError("amount must be between 0 and 100")
        
        else:
            return amount

    @property
    def code(self):
        return self._code
    
    @code.setter
    def code(self, new_code:str):
        self._code = GiftCard.ValidationCode(new_code)

    @property
    def expiration_date(self):
        return self._expiration_date

    @expiration_date.setter
    def expiration_date(self, new_expiration_date:str):
        expiration_date_dt = self.ValidateExpirationDate(new_expiration_date, self.start_date)
        if expiration_date_dt:
            self._expiration_date = expiration_date_dt
        else:
            raise ValueError("invalid expiration date (maybe it's before start date or it's not in format Year-Month-Day)")

    @property
    def start_date(self):
        return self._start_date
    
    @start_date.setter
    def start_date(self, new_start_date:str):
        start_date_dt = self.ValidateStartDate(new_start_date)
        if start_date_dt:
            self._start_date = start_date_dt
        else:
            raise ValueError('Invalid date format. Use this format "Year-Month-Day". or logic error (maybe start date is before now)')

    @property
    def amount(self):
        return self._amount
    
    @amount.setter
    def amount(self, new_amount:int):
        self._amount = GiftCard.ValidationAmount(new_amount)

    @staticmethod
    def Create(data:dict) -> int:
        """Add a new GiftCard to the database."""
        
        if 'id' in data:
            raise ValueError("id can not be set")
        
        data['sent'] = 0

        if 'code' not in data or not data['code']:
            data['code'] = GiftCard.GetDefaultCode()

        # check if the code is already in the database
        elif GiftCard.ExistsByKey('code', data['code']):
            raise ValueError("code already exists")

        # amount validation
        if 'amount' in data:
            GiftCard.ValidationAmount(data['amount'])
        
        # start time validation
        if 'start_date' in data:
            start_date_dt = GiftCard.ValidateStartDate(data['start_date'])
            if not start_date_dt:
                raise ValueError('Invalid date format. Use this format "Year-Month-Day".\
                     or logic error (maybe start date is before now)')
        
        # expiration time validation
        if 'expiration_date' in data:
            if not GiftCard.ValidateExpirationDate(data['expiration_date'], start_date_dt):
                raise ValueError("invalid expiration date (maybe it's \
                    before start date or it's not in format Year-Month-Day)")

        return Database.Create(GiftCard.TableName, data)
        
    @staticmethod
    def Get(id:int) -> 'GiftCard':
        """Get a GiftCard from the database."""
        fetched_row = Database.Read(GiftCard.TableName, GiftCard.PrimaryKey, id)
        
        if not type(fetched_row) == list or not len(fetched_row):
            return None

        fetched_row = fetched_row[0]

        return GiftCard(
            id=fetched_row[0], 
            code=fetched_row[1], 
            start_date=fetched_row[2], 
            expiration_date=fetched_row[3], 
            amount=fetched_row[4], 
            sent=fetched_row[5]
            )

    @staticmethod
    def GetAll() -> list['GiftCard']:
        """Get all GiftCards from the database."""

        GiftCard.DeleteExpiredGiftCards()

        fetched_rows = Database.ReadAll(GiftCard.TableName)
        
        giftCards = []

        for row in fetched_rows:
            giftCards.append(GiftCard(
                id=row[0],
                code=row[1],
                start_date=row[2],
                expiration_date=row[3],
                amount=row[4],
                sent=row[5]
                ))

        return giftCards

    @staticmethod
    def Exists(id: int) -> bool:
        """Check if a GiftCard exists in the database."""
        return Database.Exists(GiftCard.TableName, GiftCard.PrimaryKey, id)
    
    @staticmethod
    def ExistsByKey(key:str, value):
        """Check if a GiftCard exists in the database."""
        return Database.Exists(GiftCard.TableName, key, value)

    @staticmethod
    def Update(id:int, data:dict) -> None:
        """Update a GiftCard in the database."""
        
        if not data:
            raise ValueError("data is empty")
        
        if not type(id) == int or id < 0:
            raise ValueError("invalid id")

        row_to_be_updated = Database.Read(GiftCard.TableName, GiftCard.PrimaryKey, id)

        if not row_to_be_updated:
            raise ValueError("id does not exist")
        else:
            row_to_be_updated = row_to_be_updated[0]

        id = row_to_be_updated[0]
        code = row_to_be_updated[1]

        if 'id' in data:
            raise ValueError("id cannot be updated")

        # check if the code is already in the database
        if 'code' in data:
            GiftCard.ValidationCode(data['code'])
            if code != data['code'] and GiftCard.ExistsByKey('code', data['code']):
                raise ValueError("code already exists")

        # amount validation
        if 'amount' in data:
            GiftCard.ValidationAmount(data['amount'])

        # start time validation
        if 'start_date' in data:
            start_date_dt = GiftCard.ValidateStartDate(data['start_date'])
            if not start_date_dt:
                raise ValueError('Invalid date format. Use this format "Year-Month-Day".\
                     or logic error (maybe start date is before now)')
        
        # expiration time validation
        if 'expiration_date' in data:
            if not GiftCard.ValidateExpirationDate(data['expiration_date'], start_date_dt):
                raise ValueError("invalid expiration date (maybe it's before start date or it's not in format Year-Month-Day)")

        Database.Update(GiftCard.TableName, GiftCard.PrimaryKey, id, data)

    @staticmethod
    def Delete(id:int) -> None:
        """Delete a GiftCard from the database."""
        Database.Delete(GiftCard.TableName, GiftCard.PrimaryKey, id)

    @staticmethod
    def GetByKey(key:str, value) -> list['GiftCard']:
        """Gets all the GiftCards that match the given key and value."""
        fetched_data = Database.Read(GiftCard.TableName, key, value)

        if not type(fetched_data) == list or not len(fetched_data):
            return None

        giftCards = []
        for row in fetched_data:
            giftCards.append(GiftCard(
                id=row[0],
                code=row[1],
                start_date=row[2],
                expiration_date=row[3],
                amount=row[4],
                sent=row[5]
                ))

        return giftCards

    @staticmethod
    def DeleteExpiredGiftCards():
        """Delete all the expired GiftCards in the database"""
        
        all_gift_cards = Database.ReadAll(GiftCard.TableName)
        
        for gift_card in all_gift_cards:
            expiration_date_dt = dt.datetime.strptime(gift_card[3], '%Y-%m-%d')
            if expiration_date_dt < dt.datetime.now():
                GiftCard.Delete(gift_card[0])
