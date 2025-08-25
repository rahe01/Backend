
class Myclass:
    
    a= 10
    b=20
    
    def addTwo(self):
        
        sum = self.a + self.b
        
        print("Sum of a and b is: ", sum)
        
        



my_obj = Myclass()

my_obj.addTwo()

print(my_obj.a)
print(my_obj.b)