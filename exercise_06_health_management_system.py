def getdate():
    """Return current date/time"""
    import datetime
    return datetime.datetime.now()


def add1():
    print("a for Exercise\nb for Diet\n")
    choice1 = input("what do you Want To Add\n")
    print("Yash - type(a1)\nRahi - type(a2)\n")
    choice2 = input("a1 or a2\n")
    if choice1 == 'a' and choice2 == 'a1':
        with open("yash_exercise","a") as ch1:
            ch1.write(input("Mention Todays Date AND Day\n"))

            in1 = int(input("Enter how many items :\n"))
            for me in range(0,in1):
                ch1.write(input("Enter Exercise That you have done:\n"))
            print("Exercise Added Successfully\n")

    elif choice1 == 'a' and  choice2 == 'a2':
        with open("rahi_exercise","a") as ch2:
            ch2.write(input("Mention Todays Date AND Day\n"))

            in2 = int(input("Enter how many items :\n"))
            for me in range(0,in2):
                ch2.write(input("Enter Exercise That you have done:\n"))
          
            print("Exercise Added Successfully\n")

    elif choice1 == 'b' and  choice2 == 'a1':
        with open("yash_diet","a") as ch11:
            ch11.write(input("Mention Todays Date AND Day\n"))

            in11 = int(input("Enter how many items :\n"))
            for me in range(0,in11):
                ch11.write(input("Enter Diet which you have taken Today:\n"))
          
            
            print("Diet Added Successfully\n")

    elif choice1 == 'b' and  choice2 == 'a2':
        with open("rahi_diet","a") as ch22:
            ch22.write(input("Mention Todays Date AND Day\n"))

            in22 = int(input("Enter how many items :\n"))
            for me in range(0,in22):
                ch22.write(input("Enter Diet which you have taken Today:\n"))
          
            print("Diet Added Successfully\n")

def get1():
    print("a for Exercise\nb for Diet\n")
    choice1 = input("what do you Want To Add\n")
    print("Yash - type(a1)\nRahi - type(a2)\n")
    choice2 = input("a1 or a2\n")

    if choice1 == 'a' and choice2 == 'a1':
        with open("yash_exercise") as ch1:
            
            print(ch1.read())
            print("Yash_exercise read Successfully\n")

    elif choice1 == 'a' and  choice2 == 'a2':
        with open("rahi_exercise") as ch2:
            # in2 = input("Enter :\n")
            print(ch2.read())
            
            print("rahi_exercise read Successfully\n")

    elif choice1 == 'b' and  choice2 == 'a1':
        with open("yash_diet") as ch11:
            # in11 = input("Enter :\n")
            print(ch11.read())
            print("yash_Diet read Successfully\n")

    elif choice1 == 'b' and  choice2 == 'a2':
        with open("rahi_diet") as ch22:
            # in22 = input("Enter :\n")
            print(ch22.read())
            print("rahi_Diet read Successfully\n")
print("HEALTH MANAGEMENT SYSTEM\n")
print("What do you want (1 for add) or (2 for get)\n")  
m1 = int(input("1 or 2\n"))  
if m1 == 1: 
    add1()
else:
    get1()              



                
        






