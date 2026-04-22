from datetime import datetime
from deadlinesystem import convert_to_sec,timer,show_time
import time
import threading

from models import Session, Account
accounts=[]
dailytask=[]
importask=[]
plannedtask=[]



def planned_task():
    print("--Your Planned Tasks--")
    taskname=input("Task name: ")
    if taskname=="":
        print("Task name can't be empty!")
        return
    deadline_sec =int(convert_to_sec())
    pl_task=({"Task":taskname,})
    if deadline_sec:
        pl_task=({"Task":taskname,
                  "Deadline":deadline_sec,
                  "Type":"Planned",
                  "Added Date":datetime.now().strftime("%d %b %Y, %H:%M"),})
        plannedtask.append(pl_task)
    print("\n----Your Daily Task----""\n")
    print(f"Task Name: {taskname}")
    print(f"Deadline(hour(s)): {deadline_sec//3600} hour(s)")
    print(f"Type: {pl_task['Type']}")
    print(f"Added Date: {pl_task['Added Date']}")



def show_tasks():

    print("----Your Tasks----")
    if len(dailytask)==0 and len(importask)==0 and len(plannedtask)==0:
        print("You have no tasks yet")
        return

    if dailytask:
        print("---Your Daily Tasks---")
        for i,task in enumerate(dailytask,1):
            time_display=show_time(task['Deadline'])
            print(f"{i}. Task: {task['Task']} | Deadline : {time_display} | Added date : {task['Added Date']}")

    if importask:
        print("---Your Important Tasks---")
        for i,task in enumerate(importask,1):
            time_display=show_time(task['Deadline'])
            print(f"{i}. Task: {task['Task']} | Deadline : {time_display} | Added date : {task['Added Date']}")
    if plannedtask:
        print("---Your Planned Tasks---")
        for i,task in enumerate(plannedtask,1):
            time_display=show_time((task['Deadline']))
            print(f"{i}. Task: {task['Task']} | Deadline : {time_display} | Added date : {task['Added Date']} ")

def add_task():
    print("---Add Daily Task---")
    taskname = input("Task name: ")
    if taskname is None:
        print("Task name can't be empty!")
        return
    deadline_sec = convert_to_sec()

    if deadline_sec:
        # Start the background process
        wait_time = deadline_sec - time.time()
        t = threading.Thread(target=timer, args=(taskname, wait_time), daemon=True)
        t.start()

    task=({"Task":taskname,
           "Deadline":deadline_sec,
           "Type":"Daily",
           "Added Date":datetime.now().strftime("%d %b %Y, %H:%M"),})
    dailytask.append(task)
    print("\n----Your Daily Task----""\n")
    print(f"Task Name: {taskname}")
    print(f"Deadline(sec): {deadline_sec//3600} hour(s)")
    print(f"Type: {task['Type']}")
    print(f"Added Date: {task['Added Date']}")

def important_task():
     print("----Add an Important Task----")
     taskname=input("Task name: ")
     if not taskname:
         print("Task name can't be empty!")
         return
     deadline_sec = convert_to_sec()
     if deadline_sec is None:
         return
     else:
         im_task=({"Task":taskname,
                   "Deadline":deadline_sec,
                   "Type":"Important",
                   "Added Date":datetime.now().strftime("%d %b %Y, %H:%M"),})
         importask.append(im_task)
         print(f"----Your Important Task----""\n")
         print(f"Task Name: {taskname}")
         print(f"Deadline(sec): {deadline_sec // 3600} hour(s)")
         print(f"Type: {im_task['Type']}")
         print(f"Added Date: {im_task['Added Date']}")

def systemmenyu():
    while True:
        print("----MENU----"
              "\n1-My day :"
              "\n2-Important :"
              "\n3-Planned :"
              "\n4-My tasks :"
              "\n5-Quit :"
              "\n------------")
        try:
            choice = int(input("Enter your choice:"))
            if choice == 1:
                add_task()
            elif choice == 2:
                important_task()
            elif choice == 3:
                planned_task()
            elif choice == 4:
                show_tasks()
            elif choice == 5:
                 print("You are logged out")
                 break
            else:
                 print("Please enter a valid choice")
        except ValueError:
                 print("Please enter a number between (1-6)")

def log_in():
    global our_user
    name=input("Enter your name:")
    if name.strip()=="":
        print("Please enter a valid name")
        log_in()
    password=input("Enter your password:")
    for x in accounts:
        if x.name==name and x.password==password:
            name=x.name.capitalize()
            Session.our_user = x
            print(f"Welcome our dear user : {name}!")
            return True
    print("Please enter a correct username and password")
    print("If you do not have an account create a new one")
    return False

def sign_up():
  global our_user
  try:
    name=input("Enter your name:")
    if name.strip()=="":
      print("Please enter a valid name")
      sign_up()
    else:
      password=input("Enter your password:")
      if password.strip()=="":
            print("Please enter a valid password")
            password = input("Enter your password:")
            print("Please try again")
            sign_up()
      else:
         while True:
            if password == name:
                print("Password can not be same as name")
                password = input("Enter your password:")
            elif len(password) < 8:
                print("Password must be 8 or more characters long")
                password = input("Enter your password:")
            else:
                email = input("Enter your email:")
                if email.strip()=="":
                    print("Please enter a valid email")
                    sign_up()
                else:
                    new_user = Account()
                    new_user.name = name
                    new_user.password = password
                    new_user.email = email

                    accounts.append(new_user)  # Now accounts actually has data
                    Session.our_user = new_user
                    print(f"Nice to see you : {name}")
                    systemmenyu()


  except ValueError:
      print("Please try again")
      sign_up()
def user_account():
  global our_user
  try:
    if not Session.our_user:
        print("You are not logged in")
        return Account

    user=Session.our_user
    print("---My Account---")
    print(f"Your username is :{user.name}")
    print(f"Your email : {user.email}")
  except ConnectionError:
      print("You are not logged in")