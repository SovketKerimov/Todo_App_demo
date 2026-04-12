from datetime import datetime
import time


dailytask=[]
importask=[]
plannedtask=[]

def convert_to_sec():
    try:
        hours=float(input("Enter deadline for your task(in hours) :"))
        if hours<=0:
           print("Please enter a positive number of hours")
           return None

        if hours>0:
          seconds=int(hours*3600)
        return seconds

    except ValueError:
        print("Invalid input\n Please enter deadline in hours")

def time_frame(seconds):
    while seconds>0:
        days, remainder = divmod(seconds, 86400)
        hours, remainder = divmod(remainder, 3600)
        mins, secs = divmod(remainder, 60)
        print(f"Time left:{days}d and {hours:02d}:{mins:02d}:{secs:02d} ")
        time.sleep(1)
        seconds-=1
    print("You're time is up!")





def show_tasks():

    print("----Your Tasks----")
    if len(dailytask)==0 and len(importask)==0 and len(plannedtask)==0:
        print("You have no tasks yet")
        return

    if dailytask:
        print("---Your Daily Tasks---")
        for i,task in enumerate(dailytask,1):
            print(f"{i}. Task: {task['Task']} | Deadline : {task['Deadline']} | Added date : {task['Added Date']}")

    if importask:
        print("---Your Important Tasks---")
        for i,task in enumerate(importask,1):
            print(f"{i}. Task: {task['Task']} | Deadline : {task['Deadline']} | Added date : {task['Added Date']}")
    if plannedtask:
        print("---Your Planned Tasks---")
        for i,task in enumerate(plannedtask,1):
            print(f"{i}. Task: {task['Task']} | Added date : {task['Added Date']} | Deadline : {task['Deadline']}")

def add_task():
    print("---Add Daily Task---")
    taskname = input("Task name: ")
    if taskname is None:
        print("Task name can't be empty!")
        return

    deadline_sec = int(convert_to_sec())
    if deadline_sec is False:
           return

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
    start=input("Start time ?(y/n):").lower()
    if start=="y":
        time_frame(task["Deadline"])
    else:
        menyu()


def important_task(taskname,deadline):
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
         print(f"Type: {im_task['Type']}")
         print(f"Added Date: {im_task['Added Date']}")
         start=input("Start time ?(y/n):").lower()

         if start=="y":
             time_frame(im_task["Deadline"])

         else:
             menyu()


def menyu():
    while True:
        print("----MAIN----"
            "\n1-My day :"
            "\n2-Important :"
            "\n3-Planned :"
            "\n4-My tasks :"
            "\n5-Quit :"  
            "\n------------")
        try:
          choice=int(input("Enter your choice:"))
          if choice==1:
            add_task()
          elif choice==2:
            important_task()
          elif choice==3:
            pass
          elif choice==4:
            show_tasks()
          elif choice==5:
            print("You are logged out")
            break
          else:
            print("Please enter a valid choice")
        except ValueError:
            print("Please enter a number between (1-6)")
menyu()



