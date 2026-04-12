from datetime import datetime
import time


dailytask=[]
importask=[]
plannedtask=[]

def timer():
    try:

        hours=float(input("Enter deadline for your task(in hours) :"))
        if hours<=0:
            print("Please enter a positive number of hours")
            return False
        seconds=int(hours*3600)
        return seconds

    except ValueError:
        print("Invalid input\n Please enter deadline in hours")

def time_frame(seconds):
    while seconds>0:
        mins,secs=divmod(seconds,60)
        hours,mins=divmod(mins,60)
        days,hours=divmod(hours,24)
        print(f"Time left:{days} days and {hours:.2f}:{mins:.2f}:{secs:.2f} ")
        time.sleep(1)
        seconds-=1
    print("You're time is up!")





def show_tasks():

    print("----Your Tasks----")
    if len(dailytask)==0 and len(importask)==0 and len(plannedtask)==0:
        print("You have no tasks")
    return None
for task in dailytask and importask and plannedtask:
    print(f"Your Daily Task: {dailytask}")
    print(f"Imported Task: {importask}")
    print(f"Planned Task: {plannedtask}")

def add_task():
    print("---Add Daily Task---")
    taskname=input("Enter your daily task :")
    timeframe=timer()
    if not timeframe:
        return
    task=({"Task":taskname,
           "Deadline":timer(),
           "Type":"Daily",
           "Added Date":datetime.now().strftime("%d %b %Y, %H:%M"),})
    dailytask.append(task)
    print("\n----Your Daily Task----""\n")
    print(f"Task Name: {taskname}")
    print(f"Deadline(sec): {time_frame}: ")
    print(f"Type: {task['Type']}")
    print(f"Added Date: {task['Added Date']}")
    start=input("Start time ?(y/n):").lower()
    if start=="y":
        time_frame(deadline)
    else:
        menyu()


def important_task(taskname,deadline):
     print("----Add an Important Task----")
     if not taskname or not deadline:
         print("Task name and deadline are required!")
         return
     else:
         im_task=({"Task":taskname,
                   "Deadline":deadline,
                   "Type":"Important",
                   "Added Date":datetime.now(),})
         importask.append(im_task)
         print(f"----Your Important Task----""\n")
         print(f"Task Name: {taskname}")
         print(f"Type: {im_task['Type']}")
         print(f"Added Date: {im_task['Added Date']}")



def menyu():
    while True:
        print("----MAIN----"
            "\n1-My day :"
            "\n2-Important :"
            "\n3-Planned :"
            "\n4-Assigned to me :"
            "\n5-My tasks :"
            "\n6-Quit :"  
            "\n------------")
        try:
          choice=int(input("Enter your choice:"))
          if choice==1:
            add_task()
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
        except ValueError:
            print("Please enter a number between (1-6)")
menyu()



