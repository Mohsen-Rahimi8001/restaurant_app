from Lib.Messages import Messages
import re

class UserValidator:

    @staticmethod
    def ValidateName(name : str, inputName : str = "name") -> bool:

        if not name:
            Messages.push(Messages.Type.ERROR, f"{inputName} can't be empty")
            return False

        if not name.isalpha():
            Messages.push(Messages.Type.ERROR, f"{inputName} can contain only letters")
            return False

        return True


    @staticmethod
    def ValidateEmail(email : str, inputName : str = "Email") -> bool:

        if not email:
            Messages.push(Messages.Type.ERROR, f"{inputName} can't be empty")
            return False

        pattern = re.compile("([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+")
        if not re.fullmatch(pattern, email):
            Messages.push(Messages.Type.ERROR, f"invalid {inputName}")
            return False
        return True


    @staticmethod
    def ValidatePhoneNumber(phone_number : str, inputName : str = "Phone Number") -> bool:

        if not phone_number:
            Messages.push(Messages.Type.ERROR, f"{inputName} can't be empty")
            return False

        if len(phone_number) < 10:
            Messages.push(Messages.Type.ERROR, f"invalid {inputName}")
            return False

        startPart = phone_number[:-9]
        endPart = phone_number[-9:]

        if startPart not in {"09", "9", "+9809", "00989"}:
            Messages.push(Messages.Type.ERROR, f"invalid {inputName}")
            return False

        if not endPart.isdigit():
            Messages.push(Messages.Type.ERROR, f"invalid {inputName}")
            return False

        return True


    @staticmethod
    def ValidateSocialNumber(socialNumber : str, inputName : str = "Social Number") -> bool:

        if not socialNumber:
            Messages.push(Messages.Type.ERROR, f"{inputName} can't be empty")
            return False

        if len(socialNumber) != 10 or not socialNumber.isdigit():
            Messages.push(Messages.Type.ERROR, f"{inputName} must be ten digits")
            return False

        return True


    @staticmethod
    def ValidatePassword(password : str, inputName : str = "Password") -> bool:

        if not password:
            Messages.push(Messages.Type.ERROR, f"{inputName} can't be empty")
            return False

        pattern = re.compile("^(?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?=.*[!@#$%^&*?/])(?=.*[a-zA-Z]).{8,}$")
        if not re.fullmatch(pattern, password):
            Messages.push(Messages.Type.ERROR, f"{inputName} must contain at least 1 digit, 1 capital letter, 1 symbol \n and it must be at least 8 digits")
            return False

        return True


    @staticmethod
    def ValidatePasswordVerification(password : str, passwordVerification : str, inputName : str = "password verification") -> bool:

        if not passwordVerification:
            Messages.push(Messages.Type.ERROR, f"{inputName} can't be empty")
            return False

        if password != passwordVerification:
            Messages.push(Messages.Type.ERROR, f"{inputName} must be identical to password")
            return False

        return True