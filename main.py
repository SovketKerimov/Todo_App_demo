import flet as ft
from datetime import datetime
from functions import menyu,add_task,important_task


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
    main = Taskmanage()