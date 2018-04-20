class inputs:
    def getValidIntInput(Max=None, Min=None, Default=None, arrow="> ", defaultString="" ):
        #Getting valid intiger input based on max and min
        #while also allowing for a default option to be
        #specified.
        #None is No limit or Nothing.
        #Throws TypeError if wrong type is inputted
        allowedType = type( int( ) )
        
        if not (Max is None or allowedType == type(Max) ):
            raise TypeError ( "Invalid Max type: " + str( type( Max ) ) )

        if not (Min is None or allowedType == type(Min) ):
            raise TypeError ( "Invalid Min type: " + str( type( Min ) ) )

        if not (Default is None or allowedType == type(Default) ):
            raise TypeError ( "Invalid Default type: " + str( type( Default ) ) )

        #The rest will throw their own errors with correct responces.
        
        while True: 
            try:    
                choice = input( str( arrow ) ) 
                choice = int( choice )
                
            except ValueError:
                if choice == str( defaultString ): #If the choice is defaultString
                    if not Default is None:
                        return Default #Give the default input if Default is set
                
                    else: #Otherwise...
                        print ( "Your input cannot be blank" )

                else:
                    print ( "Your input needs to be a number" )
                    
                continue
            
            if Max is None and Min is None:
                return choice

            elif Max is None or Min is None:
                if Max is None:
                    if choice < Min: 
                        print ( "Your input needs to be more than", Min )
                        continue


                elif Min is None: #Double check paranoia
                    if choice > Max: #will be safe as choice will always ba a number
                        print ( "Your input needs to be less than", Max )
                        continue


                else:
                    raise OSError( "Someone is tampering with the code as it is ran!" )


            else:
                if choice > Max: #will be safe as choice will always ba a number
                    print ( "Your input needs to be less than", Max )
                    continue

                if choice < Min: 
                    print ( "Your input needs to be more than", Min )
                    continue

            
            return choice

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

            

def FindFiles(path, loud=False, bannedChars=False, allowedChars=False):                        
    from os import scandir #Recursive file traverser (false means default)
    #TypeError is thrown on incorrect input type
    #Slight overhead while being in functions tabal
    acceptedVars = type(set())

    #Testing if the incoming varables are the correct type.
    if not ( type( bannedChars ) == acceptedVars or bannedChars is False):
        raise TypeError ( "Invalid bannedChars type: " + str ( type( bannedChars ) ) )
    
    if not ( type( allowedChars ) == acceptedVars or allowedChars is False):
        raise TypeError( "Invalid allowedChars type: " + str ( type( allowedChars ) ) )
        
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
