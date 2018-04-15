#Main Python 3.6 file
from Functions import getValidIntInput

def showMainMenu(): #Main menu. Likely to change. Here for clean code
    print ( "What do you want to do?" )
    print ( "1. Chain the data" )
    print ( "2. Verify the data" )
    print ( "3. Extract the data" )
    print ( "4. Change configuration" )
    print ( "5. Exit" )

#Main loop starts
while True:
    showMainMenu()
    choice = getValidIntInput(Max=5, Min=1)
        
    if   choice == 1:
        import Chain
        del Chain
        
    elif choice == 2:
        import Verify
        del Verify
        
    elif choice == 3:
        import Extract
        del Extract

    elif choice == 4:
        import ConfigChanger
        del ConfigChanger

    elif choice == 5:
        print ( "Bye!" )
        break




