import threading
def getValidIntInput(Max=None, Min=None, Default=None ):
    while True:
        try:
            choice = input("> ")
            choice = int ( choice )
        except ValueError:
            if choice == "" and Default:
                return Default
            
            print ( "Your input needs to be a number" )
            continue
        
        if Max != None and choice > Max:
            print ( "Your input needs to be less than", Max )
            continue

        if Min != None and choice < Min:
            print ( "Your input needs to be more than", Min )
            continue
        
        return choice

print ( "How many levels of difficulty do want?(1-5) (2)" )
difficulty = getValidIntInput(Max=5, Min=1, Default=2)


