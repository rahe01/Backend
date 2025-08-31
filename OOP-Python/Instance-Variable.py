

class Myclass1:

    
    # Instance Method
    def sum(self):
        sum = self.a + self.b
        return sum
    
    # Constructor Method
    def __init__(self , x ,y):
        self.a = x #instance / object variable
        self.b = y #instance variable



       



s1 = Myclass1(10,250) 

print(s1.sum())