import os
import re

class dtsxReader:
    basepath = 'D:\Proj_Excel\SSIS'
    fileList = []

    def __init__(self):
        # List path of file
        self.listFilePath()

        # Read data in file
        self.readDTSXFile()
        

    def listFilePath(self):
        for entry in os.listdir(self.basepath):
            if os.path.isfile(os.path.join(self.basepath, entry)):
                self.fileList.append(entry)

    def readDTSXFile(self):
        for filePAth in self.fileList:
            with open(self.basepath + "/" + filePAth, mode="r") as f:
                data = f.read()
                print(data)
                
        

# Run!
dtsxReader()
