from datetime import datetime


class DateTools:

    DateStringFormat = "%y-%m-%d"


    @staticmethod
    def GetDateStrFormat(year : str, month : str, day : str) -> str:
        """convert date to DateTools format"""

        return f'{year}-{month}-{day}'


    @staticmethod
    def GetDateObject(year : str, month : str, day : str) -> datetime:
        """returns date object from date data"""

        return datetime(int(year), int(month), int(day))


    @staticmethod
    def ConvertDateObjectToStr(dateObj : datetime) -> str:
        return dateObj.strftime(DateTools.DateStringFormat)


    @staticmethod
    def ConvertStrToDateObject(dateStrFormat) -> datetime:
        return datetime.strptime(dateStrFormat, DateTools.DateStringFormat)


    @staticmethod
    def GetToday() -> str:
        """return today date in str format"""

        return  DateTools.ConvertDateObjectToStr(datetime.now())


    @staticmethod
    def Compare(leftSide, rightSide) -> int:
        """
        compares to date in str format
        if left > right returns -1
        if left < right returns 1
        if left = right returns 0
        """

        left = DateTools.ConvertStrToDateObject(leftSide)
        right = DateTools.ConvertStrToDateObject(rightSide)

        if left > right:
            return -1
        elif left < right:
            return 1
        else:
            return 0
