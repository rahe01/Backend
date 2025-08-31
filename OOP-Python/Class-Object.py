

"""class Myclass1:

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

print(s1.sum())"""


#behaviour / method
"""
register()
login()
logout()

data / attributes

name = "Rahe"
email = "rahatrahe01@gmail.com"
password = 01254
"""

class User:

    def __init__(self ,userid, fullname , email , password):
        self.userid = userid
        self.name = fullname
        self.email = email
        self.__password = password #private attribute encapculation 


    def login(self , email, password):
        
        if self.email != email:
            print("Incorrect email")

        if self.__password != password:
            print("Incorrect password")

        elif self.email == email and self.__password == password:
            print("Login successful")
            self.greet()

        else:
            print("Invailid email or password")


    def update_password(self , old_pass , new_pass):
        
        if self.__password == old_pass:
            self.__password = new_pass
            print("Password change successful")
        
        else:
            print("Invailid old pass")




    def logout(self):
        print("Logout successful")


    def greet(self):
        print(f"Welcome Mr. {self.name}")


    def dashboard(self):
        print("user dashboard")


"""
user = User(1,"Rahe" , "rahatrahe01@gmail.com" , "123")
user1 = User(2,"Moon" , "rahatrahe01@gmail.com" , "123")
user2 = User(3,"Afifa" , "rahatrahe01@gmail.com" , "102dfdfdff")



user1.login("rahatrahe01@gmail.com" , "123")


old_pass = input("Enter your pass")
new_pass = input("Enter your pass")

user.update_password(old_pass, new_pass)


"""




# Inheritance

class Admin(User):
    
    def delete_user(self , user_id):
        print(f"User {user_id} Deleted")


# polymorphison

    def dashboard(self):
        print("Admin dashboard")


admin = Admin(4 , "Rahat","rahatrahe01@gmail.com" , "123")

print(admin.name)
admin.greet()
admin.delete_user(10)
admin.login("rahatrahe01@gmail.com" ,"123")


admin.name = "admin rahe"
print(admin.name)

admin.dashboard()