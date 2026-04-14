from functions import systemmenyu,user_account,sign_up,log_in
from models import Account


class Taskmanage:
    def __init__(self):
        self.tasks=[]



    def log_in(self):
          self.name=input("Enter your name:")
          self.password=input("Enter your password:")

          print(f"You're welcome {self.name}")

    def sign_up(self):

        self.name=input("Enter your name:")
        self.password=input("Enter your password:")
        self.email = input("Enter your email:")
        print(f"We are pleased to see you {self.name}")

if __name__ == "__main__":
    print("-Microsoft To Do App-")
    account = Account()
    taskmanage = Taskmanage()
    while True:
        print("---Main Menu---")
        print("1. Sign Up")
        print("2. Log In")
        print("3. My Account")
        print("4. Exit")
        try:
           choice = input("Choose option: ")

           if choice == "1":
             sign_up()
             systemmenyu()
           elif choice == "2":
            log_in()
            systemmenyu()
           elif choice == "3":
            user_account()
           elif choice == "4":
            print(f"Goodbye {account.name}!")
            break
           else:
              print("Please choose between (1-4)")


        except ValueError:
            print("Please enter a valid option")
