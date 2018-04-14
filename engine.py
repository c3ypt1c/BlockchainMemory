

def MainMenu():
    print ( "What do you want to do?" )
    print ( "1. Chain the data" )
    print ( "2. Verify the data" )
    print ( "3. Extract the data" )
    
while True:
    MainMenu()
    choice = input ( "> " )[0]
    try:
        choice = int ( choice )
    except:
        print ( "Your input needs to be a number" )
        continue

    if choice < 1 and choice > 3:
        print ( "Please select a number between 1 and 3" )

    break
