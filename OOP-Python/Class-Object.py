

class Myclass1:

    a = 10
    b = 20

    def sum(self):
        sum = self.a + self.b
        return sum
    
    # Constructor Method
    def __init__(self):
        sum =self.a + self.b
        print(f"Sum is {sum}")



s1 = Myclass1() 

print(s1.sum())