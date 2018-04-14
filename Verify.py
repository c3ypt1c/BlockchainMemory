import hashlib
import Functions

From = "Stuff to Blockchain"

def FindFiles(path): #Recursive file traverser
    from os import scandir #Slight overhead while being in functions tab
    files = []
    current = scandir(path)
    for x in current:
        currentPath = x.path
        if x.is_file():
            files.append(currentPath)
            print ( "Found a file:", currentPath )
        elif x.is_dir():
            print ( "Found a dir: ", currentPath )
            [ files.append(y) for y in FindFiles(currentPath) ]
        else:
            print ( "Found (skip):", currentPath )
        
    return files


print ( "Building file tree" )
files = FindFiles(From)

#TODO:Starting reading file contents and see if they match 
