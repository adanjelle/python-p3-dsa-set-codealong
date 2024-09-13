class MySet:
    def __init__(self, enumerable=None):
        self.dictionary = {}
        if enumerable is None:
            enumerable = []
        for value in enumerable:
            self.dictionary[value] = True

    # Method to check if a value exists in the set
    def has(self, value):
        return value in self.dictionary

    # Method to add a value to the set
    def add(self, value):
        self.dictionary[value] = True
    def delete(self, value):
     self.dictionary.pop(value, None)
    