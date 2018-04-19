def getValidIntInput(Max=None, Min=None, Default=None ):
    while True: #getting valid intiger input based on max and min
        try:    #while also allowing for a default option to be
            choice = input("> ") #specified.
            choice = int ( choice )
        except ValueError:
            if choice == "" and (not Default is None):
                return Default #Give the default input
            
            elif choice == "" and Default is None:
                print ( "Your input cannot be blank" )

            else:
                print ( "Your input needs to be a number" )
                
            continue
        
        if choice > Max: #will be safe as choice will always ba a number
            print ( "Your input needs to be less than", Max )
            continue

        if choice < Min: 
            print ( "Your input needs to be more than", Min )
            continue
        
        return choice

def FindFiles(path, loud=False, bannedChars=False, allowedChars=False):                        
    from os import scandir #Recursive file traverser (false means default)
    #Slight overhead while being in functions tabal
    acceptedVars = "<class 'set'>"

    #Testing if the incoming varables are the correct type.
    passed = type(bannedChars) == acceptedVars or bannedChars is False
    #Wrong bannedChar Type
    passed = passed and type(allowedChars) == acceptedVars or allowedChars is False
    #Wrong acceptedVar Type

    if passed:
        
        if not bannedChars:
            from string import whitespace, punctuation
            bannedChars = set ( whitespace + punctuation ) #Disallowed chars
            
        if allowedChars:
            bannedChars -= allowedChars #Custom allowed chars
            
        else:
            bannedChars -= set ( ".-+=!\"£$%^&*()_,?" ) #Allowed chars by default
            
            
        files = []
        current = scandir(path)
        
        for x in current:
            currentPath = x.path
            
            if x.is_file():
                files.append(currentPath)
                
                if loud:
                    print ( "Found a file:", currentPath )
                
            elif x.is_dir():
                if loud:
                    print ( "Found a dir: ", currentPath )
                    
                [ files.append(y) for y in FindFiles(currentPath, bannedChars=bannedChars, allowedChars=allowedChars) ]
                
            else:
                if loud: print ( "Found?(skip):", currentPath )            
            
        return files

def getYesNo(Default=None, Inputs=["Y","N"]): #For getting yes or no answers
    Inputs = [ x.lower() for x in Inputs ] #Allow lowercase
    while True:
        choice = input ( Inputs[0]+"/"+Inputs[1]+"> ").lower() #Make everything the same case
        
        if choice == "" and (not Default is None):
            return Default

        if choice == Inputs[0]:
            return True

        if choice == Inputs[1]:
            return False

        print ( "Please enter", Inputs[0], "or", Inputs[1] )
        
