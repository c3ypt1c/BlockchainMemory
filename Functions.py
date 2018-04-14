def getValidIntInput(Max=None, Min=None, Default=None ):
    while True:
        try:
            choice = input("> ")
            choice = int ( choice )
        except ValueError:
            if choice == "" and type(Default) == type(1):
                return Default #Give the default input
            
            elif choice == "" and Default == None:
                print ( "Your input cannot be blank" )

            else:
                print ( "Your input needs to be a number" )
            continue
        
        if type(Max) == type(1) and choice > Max:
            print ( "Your input needs to be less than", Max )
            continue

        if type(Min) == type(1) and choice < Min:
            print ( "Your input needs to be more than", Min )
            continue
        
        return choice
