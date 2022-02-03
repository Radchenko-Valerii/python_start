
class mobila:
    def __init__(self, brand, model, price, color):
        self.brand = brand
        self.model = model
        self.price = price
        self.color = color
    def getAll(self):
        print(self.brand, self.model, self.price, self.color)