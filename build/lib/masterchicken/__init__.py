from csvreader import *


class mathcal:
    def __init__(self):
        self.__init__()
        self.num1 = None
        self.num2 = None

    # Subtract Numbers
    def subtract_num(self, num1, num2):
        self.num1 = num1
        self.num2 = num2
        return num1 - num2

    # Add Numbers
    def add_num(self, num1, num2):
        self.num1 = num1
        self.num2 = num2
        return num1 + num2

    # Multiply Numbers
    def multiply_num(self, num1, num2):
        self.num1 = num1
        self.num2 = num2
        return num1 * num2

    # Divide Numbers
    def divide_num(self, num1, num2):
        self.num1 = num1
        self.num2 = num2
        return num1 / num2


pass


def read_csv(file_location):
    Required_File = Open()
    Required_File.open_file(file_location)

