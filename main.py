import flet as ft
from datetime import datetime
from functions import menyu,add_task,important_task
from ast import main

class Account:
    def __init__(self,name,email,password):
        self.name=name
        self.password=password
        self.email=email

    def open(self,name,email,password):
          name=input("Enter your name:")
          email=input("Enter your email:")
          password=input("Enter your password:")
          self.name=name
          self.email=email
          self.password=password
          print(f"You're welcome {name}")

    def signup(self,name,email,password):

        name_u=input("Enter your name:")
        password_u=input("Enter your password:")
        print(f"We are pleased to see you {name_u}")
        self.name=name
        self.password=password
        self.email=email
if __name__ == "__main__":
    main()