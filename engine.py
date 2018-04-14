#Main Python 3.6 file
import Functions

def MainMenu(): #Main menu. Likely to change. Here for clean code
    print ( "What do you want to do?" )
    print ( "1. Chain the data" )
    print ( "2. Verify the data" )
    print ( "3. Extract the data" )

#Main loop starts
while True:
    MainMenu()
    choice = Functions.getValidIntInput(Max=3, Min=1)
        
    if  choice == 1:
        import Chain
        del Chain
        
    elif choice == 2:
        import Verify
        del Chain
        
    elif choice == 3:
        import Extract
        del Extract




