from datetime import datetime
import time


dailytask=[]
importanttask=[]
plannedtask=[]

def timer():

    try:
        hours=float(input("Enter deadline for your task(in hours) :"))
        if hours<0:
            print("Please enter a positive number of hours")
            return
        else:
            timeframe=int(hours*3600)
            for deadline in range(timeframe,0,-1):
                seconds=deadline % 60
                minutes=(deadline/60) % 60
                hours=deadline/3600
                print(f"{hours:.2f}:{minutes:.2f}:{seconds:.2f}")
                time.sleep(1)
            print("You're time is up!")
            print("The goal is uncompleted")
    except ValueError:
        print("Invalid input\n Please enter deadline in hours")

def show_tasks():
    print("----Your Tasks----")
    if len(dailytask)==0 or len(importanttask)==0 or len(plannedtask)==0:
        print("You have no tasks")


def add_task(taskname,deadline,):
    print("----Add a Daily Task----")

    if not taskname or not deadline:
        print("Task name and deadline are required!")
        return
    else:

        task=({"Task":taskname,
               "Deadline":timer(),
               "Type":"Daily",
               "Added Date":datetime.now(),})
        dailytask.append(task)
        print(f"----Your Daily Task----""\n")
        print(f"Task Name: {taskname}")
        print(f"Deadline: {timer()}")
        print(f"Type: {task['Type']}")
        print(f"Added Date: {task['Added Date']}")




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
         importanttask.append(im_task)
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



