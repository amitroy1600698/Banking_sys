# Parent class : user
# Hold details about an user
# Has a function to show user details
# Child class : Bank
# Store details about the a/c balance
# Allows for deposits, witdraw, view balance

class user:
    def __init__(self, name, age, gender):
        self.__name = name
        self.__age = age
        self.__gender = gender
  
    def show_details(self):
            print('Personal Detail')
            print('=====================')
            print('Name :',self.__name)
            print('Age :',self.__age)
            print('Gender :',self.__gender)
            print('=====================')
            
class Bank(user):
    def __init__(self, name, age,gender):
        super().__init__(name,age,gender)
        self.__balance = 0
        self.__pin = int
        
    def get_pin(self):
        return self.__pin
    
    def set_pin(self,new):
        if type(new) == int:
            self.__pin = new
            print('Pin Update Successfully')
        else:
            print('Wrong Input !!')

    def create_pin(self):
        self.__pin = int(input('Enter your 4 digit pin\n'))
        print('Pin set Successfully')
        
    def deposit(self,amount):
        temp1 = int(input('Enter your 4 digit pin\n'))
        if temp1 == self.__pin:
            self.amount = amount
            self.__balance = self.__balance + self.amount
            print('Your Balance has been updated, ₹',self.__balance)
        else:
            print('Invalid Pin')
        
    def withdraw(self,amount):
        temp2 = int(input('Enter your 4 digit pin\n'))
        if temp2 == self.__pin:
            self.amount = amount
            self.__balance = self.__balance - self.amount
            print('Your Balance has been updated, ₹',self.__balance)
        else:
            print('Invalid Pin')
        
    def view_balance(self):
        temp = int(input('Enter your 4 digit pin\n'))
        if temp == self.__pin:
            print('Your Current Balance is, ₹',self.__balance)
        else:
            print('Invalid Pin')
        
            
    
    

