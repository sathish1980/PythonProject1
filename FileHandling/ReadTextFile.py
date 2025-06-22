class ReadTextFile():

    """
    Text File
    Excel file --****
    Json file
    Xml File
    CSV File
    """
    filePath = "C:\\Users\\DELL\\PycharmProjects\\PythonProject1\\Input\\Fita.txt"
    OfilePath = "C:\\Users\\DELL\\PycharmProjects\\PythonProject1\\Input\\Output.txt"
    def readFile(self):
        file = open(self.filePath,"r")
        readData = file.read()
        print(readData)
        file.close()
        file1 = open(self.OfilePath,"a")
        print(file1.write(readData))
        file1.close()

obj = ReadTextFile()
obj.readFile()