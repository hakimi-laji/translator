from googletrans import Translator
import os
import shutil
from os import path

translator = Translator()


def getName():
    for path, currentDirectory, files in os.walk(os. getcwd()):
        for file in files:
            full = os.path.join(path, file)
            print(file)
            oldName = os.path.splitext(file)[0]
            print(oldName)
            ext = os.path.splitext(file)[1]
            newName = (translator.translate(oldName).text)
            newName = newName.replace("?", ",")
            print(newName)
            trans = os.path.join(path, newName)
            trans = trans + ext
            print(trans)
            os.rename(full, trans)
		
if __name__ == "__main__":
    getName()
