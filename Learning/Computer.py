class Computer:

    def __init__(self, name):
        self.name = name

    def __str__(self):
        return 'Computer: ' + self.name

    def say_hello(self):
        print("I'am computer, called " + self.name)