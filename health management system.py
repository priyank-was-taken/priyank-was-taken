def gettime():
    import datetime
    return datetime.datetime.now()

def log():

    who = int(input('''
whom do you want to choose
1 - priyank
2 - floyd
3 - punk
choice : '''))
    if who == 1:
        choice = int(input('''
What do you want to log for?
1 - Diet
2 - Exercise         
choose : '''))
        if choice == 1:
            tell_us = input("what you eat today? ")
            f = open("priyank diet", "a")
                    #"[",gettime(),"]"
            f.write(str([str(gettime())]) + " " + tell_us + "\n")
            f.close()

        elif choice == 2:
            tell_us = input("what exercise do you do today : ")
            f = open("priyank exercise", "a")
            f.write(str([str(gettime())]) + " " + tell_us + "\n")
            f.close()

    elif who == 2:
        choice = int(input('''
What do you want to log for?
1 - Diet
2 - Exercise         
choose : '''))
        if choice == 1:
            tell_us = input("what you eat today? ")
            f = open("floyd diet", "a")
            f.write(str([str(gettime())]) + " " + tell_us + "\n")
            f.close()

        elif choice == 2:
            tell_us = input("what exercise do you do today : ")
            f = open("floyd exercise", "a")
            f.write(str([str(gettime())]) + " " + tell_us + "\n")
            f.close()

    elif who == 3:
        choice = int(input('''
What do you want to log for?
1 - Diet
2 - Exercise         
choose : '''))
        if choice == 1:
                tell_us = input("what you eat today? ")
                f = open("punk diet", "a")
                f.write(str([str(gettime())]) + " " + tell_us + "\n")
                f.close()

        elif choice == 2:
                tell_us = input("what exercise do you do today : ")
                f = open("punk exercise", "a")
                f.write(str([str(gettime())]) + " " + tell_us + "\n")
                f.close()


def retrieve():
    who = int(input('''
whom do you want to choose
1 - priyank
2 - floyd
3 - punk
choice : '''))
    if who == 1:
        choice = int(input('''
What do you want to log for?
1 - Diet
2 - Exercise         
choose : '''))
        if choice == 1:
            f = open("priyank diet", "r")
            print(f.read())
            f.close()

        elif choice == 2:
            f = open("priyank exercise", "r")
            print(f.read())
            f.close()

    elif who == 2:
        choice = int(input('''
What do you want to log for?
1 - Diet
2 - Exercise         
choose : '''))
        if choice == 1:
            f = open("floyd diet", "r")
            print(f.read())
            f.close()

        elif choice == 2:
            f = open("floyd exercise", "r")
            print(f.read())
            f.close()

    elif who == 3:
        choice = int(input('''
What do you want to retrieve for?
1 - Diet
2 - Exercise         
choose : '''))
        if choice == 1:
            f = open("punk diet", "r")
            print(f.read())
            f.close()

        elif choice == 2:
            f = open("punk exercise", "r")
            print(f.read())
            f.close()

print("\n Welcome to health management system")
choose = int(input('''
what you want to do
1 - log
2 - retrieve
Choose 1 or 2 : '''))

if choose == 1:
    log()
elif choose == 2:
    retrieve()
else:
    print("WRONGE STATEMENT")

