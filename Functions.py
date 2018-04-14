def getValidIntInput(Max=None, Min=None, Default=None ):
    while True: #getting valid intiger input based on max and min
        try:    #while also allowing for a default option to be
            choice = input("> ") #specified.
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

def FindFiles(path, loud=False): #Recursive file traverser
    from os import scandir #Slight overhead while being in functions tab
    files = []
    current = scandir(path)
    for x in current:
        currentPath = x.path
        if x.is_file():
            files.append(currentPath)
            if loud: print ( "Found a file:", currentPath )
        elif x.is_dir():
            if loud: print ( "Found a dir: ", currentPath )
            [ files.append(y) for y in FindFiles(currentPath) ]
        else:
            if loud: print ( "Found?(skip):", currentPath )
        
    return files
