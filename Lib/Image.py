import os
import requests
import datetime
from PyQt5 import QtCore, QtGui, QtWidgets


class Image:

    BaseDir = r".\Resources\Images"


    @staticmethod
    def GetFromUrl(url:str, name:str):
        """Get an image from the given url, save it to the given name, and return the directory of the image"""

        directory = os.path.join(Image.BaseDir, name)

        if os.path.isfile(directory):
            # change the directory name to a unique one
            
            # split the name to name and extension
            name, extension = os.path.splitext(name)
            
            # create a new name
            name = name + "_" +  datetime.datetime.now().strftime("%Y%m%d%H%M%S") + extension
            
            directory = os.path.join(Image.BaseDir, name)

        try:
            # Get the image from the url
            response = requests.get(url)

            if response.status_code == 200:
            
                with open(directory, "wb") as f:
                    f.write(response.content)
            
                return directory
            
            else:
                return None

        except Exception as e:
            return None


    @staticmethod
    def GetFromDirectory(path: str):
        """Copy the image form the directory in the image resources and return the new directory"""

        if os.path.dirname(path) == Image.BaseDir:
            if os.path.isfile(path):
                return directory

        if os.path.isfile(path):
            
            # copy the image to BaseDir
            
            name = os.path.basename(path)
            destination = os.path.join(Image.BaseDir, name)

            if os.path.isfile(destination):
                
                # check if two images has the same content
                with open(path, "rb") as f:
                    if f.read() == open(destination, "rb").read():
                        return destination

                # change the destination name to a unique one
                # split the name to name and extension
                name, extension = os.path.splitext(name)

                # create a new name
                name = name + "_" +  datetime.datetime.now().strftime("%Y%m%d%H%M%S") + extension

                destination = os.path.join(Image.BaseDir, name)

            os.system(f"copy {path} {destination}")

            return destination

        else:
            return None


    @staticmethod
    def Browse(window : QtWidgets.QMainWindow):
        """opens a browse dialog and returns selected path"""

        return QtWidgets.QFileDialog.getOpenFileName(window, "Open File", ".\\", "Image Files (*.png *.jpg *.bmp *.gif)")[0]