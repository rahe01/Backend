

class Myclass1:

    a = 10
    b = 20

    def sum(self , c):
        sum = self.a + self.b +c
        return sum
    
    # Constructor Method
    def __init__(self,c):
        sum =self.a + self.b+c
        print(f"Sum is {sum}")



s1 = Myclass1(10) 

print(s1.sum(100))