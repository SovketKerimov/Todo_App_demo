from datetime import datetime


dailytask=[]
imptask=[]

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

    def signup(self,name,password):

        name=input("Enter your name:")
        password=input("Enter your password:")
        print(f"We are pleased to see you {name}")
        self.name=name
        self.password=password

def add_task(taskname,deadline,):
    print("----Add a Daily Task----")
    if not taskname or not deadline:
        print("Task name and deadline are required!")
        return
    else:
        task=({"Task":taskname,
                   "Deadline":deadline,
                   "Type":"Daily",
                   "Added Date":datetime.now(),})
        dailytask.append(task)
        print(f"----Your Daily Task----""\n")
        print(f"Task Name: {taskname}")
        print(f"Deadline: {deadline}")
        print(f"Type: {task['Type']}")
        print(f"Added Date: {task['Added Date']}")




def important_task(taskname,deadline):

     imptask.append({"Important task":taskname,"Deadline":deadline})
     print("Your important task has been added""\n"f"------\nThe Task is {taskname}\n------")




def menyu():
    while True:
        print("----MAIN----"
            "\n1-My day :"
            "\n2-Important :"
            "\n3-Planned :"
            "\n4-Assigned to me :"
            "\n5-Tasks :"
            "\n6-Quit :"  
            "\n------------")
        choice=int(input("Enter your choice:"))
        if choice==1:
            pass
        elif choice==2:
            pass
        elif choice==3:
            pass
        elif choice==4:
            pass
        elif choice==5:
            pass
        elif choice==6:
            print("You are logged out")
            break
        else:
            print("Please enter a valid choice")

menyu()



