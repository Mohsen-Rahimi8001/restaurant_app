from datetime import datetime


class DateTools:

    DateStringFormat = "%y-%m-%d"


    @staticmethod
    def GetDateStrFormat(year : str, month : str, day : str) -> str:
        """convert date to DateTools format"""

        return f'{year-month-day}'


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