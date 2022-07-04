import os
import requests
import datetime


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
    def GetFromDirectory(directory: str):
        """Copy the image form the directory in the image resources and return the new directory"""

        if os.path.isfile(directory):
            
            # copy the image to BaseDir
            
            name = os.path.basename(directory)
            destination = os.path.join(Image.BaseDir, name)

            if os.path.isfile(destination):
                # change the destination name to a unique one
                # split the name to name and extension
                name, extension = os.path.splitext(name)

                # create a new name
                name = name + "_" +  datetime.datetime.now().strftime("%Y%m%d%H%M%S") + extension

                destination = os.path.join(Image.BaseDir, name)

            os.system(f"copy {directory} {destination}")

            return destination

        else:
            return None
