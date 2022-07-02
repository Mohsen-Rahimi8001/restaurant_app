from enum import Enum

class Patterns(Enum):
    # Regex for validating email
    EMAIL = '^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-_]+\.[a-zA-Z0-9]+$'
    # a valid prefix and 9 more digits
    PHONE = '^(?:00989|\+9809|9|09)\d{9}$'
    # ten digits
    SOCIAL_NUMBER = '^\d{10}$'
    # at least one lowercase letter, one uppercase letter, one digit, one special character, 
    # and characters between 8 and 255 characters
    PASSWORD = "^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[!\"#$%&'()"
    "*+,-.\/:;<=>?@[\]^_`{|}~])[A-Za-z\d!\"#$%&'()*+,-.\/:;<=>?@[\]^_`{|}~]{8,255}$"
