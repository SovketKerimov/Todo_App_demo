from datetime import datetime


tasks=[]

def menyu():
    print("----MAIN----"
        "\n1-My day :"
        "\n2-Important :"
        "\n3-Planned :"
        "\n4-Assigned to me :"
        "\n5-Tasks :"
        "\n------------")





def add_task(schedule):
    choose = int(input("Enter your choice:"))
    time=datetime.now().strftime("%I:%M %p")

    if choose==1:
             tk=input("Enter your task :")
             schedule.append({"Your task is ":tk,"Finished": False,"Time":time})
             print('Task added successfully')


    elif choose==2:
        pass

    elif choose==3:
        pass

    elif choose==4:
        pass

    elif choose==5:
        pass

menyu()
add_task(schedule=tasks)

