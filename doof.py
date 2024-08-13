class Adder:
    def __init__(self):
        self.total = 0
        
    def add(self, number):
        self.total += number

adder = Adder()
adder.add(1)
print(adder.total)  # Output: 1
