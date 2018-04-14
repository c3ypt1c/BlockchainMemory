#Main Python 3.6 file

class Files:
    pass

class Functions():
    import Chain
    import Verify
    import Extract

def MainMenu(): #Main menu. Likely to change. Here for clean code
    print ( "What do you want to do?" )
    print ( "1. Chain the data" )
    print ( "2. Verify the data" )
    print ( "3. Extract the data" )

#Main loop starts
while True:
    MainMenu()
    choice = input ( "> " )[0] #We only need the first number
    try:
        choice = int ( choice )
    except ValueError:
        print ( "Your input needs to be a number" )
        continue #restarts the loop

    if choice < 1 and choice > 3:
        print ( "Please select a number between 1 and 3" )
        continue #restarts the loop
        
    break
    ##For debug, the break remains
    if choice == 1:
        Functions.Chain()
    elif choice == 2:
        Functions.Verify()
    elif choice == 3:
        Functions.Extract()




