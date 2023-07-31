import sys

# Create Parent Class
class User():
    def __init__(self,first_name,last_name,age,gender):
        # Initilialize User Details
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.gender = gender

    def user_details(self):
        # Print User Details
        print(f'First Name: {self.first_name}')
        print(f'Last Name: {self.last_name}')
        print(f'Age: {self.age}')
        print(f'Gender: {self.gender}')



class Bank(User):
    def __init__(self,first_name,last_name,age,gender):
        # We use the super() method to inherit everything from User init
        super().__init__(first_name,last_name,age,gender)
        # Basically telling it that first_name from User = first_name here
        # We can now use the bank class to process the info instead of user + create new values
        self.balance = 0
    
    def deposit(self):
        amount = int(input("Please enter how much you'd like to deposit: "))
        self.balance += amount
        print(f'Your new balance is: ${self.balance}')
    
    def withdraw(self):
        amount = int(input("Please enter how much you'd like to withdraw: "))
        if amount > self.balance:
            print(f'Insufficient Funds | Balance Available: ${self.balance}')
        else:
            self.balance -= amount
            print(f'Your new balance is: ${self.balance}')
    
    def view_balance(self):
        self.user_details()
        print(f'Your current balance is: ${self.balance}')


Neelam = Bank("Henil","Bhavsar","19","Male")

def main():

    running = True
    # How can we get it so that users create their first and last names and access their account, do we need conditionals? idk!
    user_entry = input("Welcome to Legacy Bank, press D to deposit, W to withdraw or C to check balance: ").lower()
    while running:
        
        possible_responses = ['w','d','c']

        if user_entry not in possible_responses:
            print('Invalid entry, please try again!')
            user_entry = input("Welcome to Legacy Bank, press D to deposit, W to withdraw or C to check balance: ").lower()
            
        if user_entry in possible_responses:

            if user_entry == 'w':
                Neelam.withdraw()
            
            elif user_entry == 'd':
                Neelam.deposit()
            
            elif user_entry == 'c':
                Neelam.view_balance()
            
            exit_prompt = input("Is there anything else we can do for you today? Y/N: ").lower()

            exit_prompts = ['y','n']
            
            if exit_prompt not in exit_prompts:
                print("Invalid entry! Please type in Y or N only!")
                exit_prompt = input("Is there anything else we can do for you today? Y/N: ").lower()
            
            if exit_prompt in exit_prompts:
            
                if exit_prompt == 'n':
                    print("Thank you for banking with us today, we hope to see you again soon!")
                    running = False
                
                elif exit_prompt == 'y':
                    user_entry = input("Press D to deposit, W to withdraw or C to check balance: ").lower()
            
            

            

                
main()



