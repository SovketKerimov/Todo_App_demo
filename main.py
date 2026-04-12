from functions import menyu


class Taskmanage:
    def __init__(self):
        self.tasks=[]

class Account:
    def __init__(self):
        self.name=None
        self.password=None
        self.email=None

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
        print("3. Exit")
        try:
           choice = input("Choose option: ")

           if choice == "1":
             account.sign_up()
             menyu()
           elif choice == "2":
            account.log_in()
            menyu()
           elif choice == "3":
            print("Goodbye!")
            break
           else:
              print("Please choose between (1-3)")
              menyu()
        except ValueError:
            print("Please enter a valid option")
