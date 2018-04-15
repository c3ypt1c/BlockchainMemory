import threading
import itertools
import hashlib
import Functions
import Config
import string
from time import time

import multiprocessing
CoreCount = multiprocessing.cpu_count()
del multiprocessing

OutputFileNumber = 0
OutputFileName = Config.OutputChainFolder + "/" + str(OutputFileNumber) + ".bkch"
charactars = string.ascii_letters+string.digits

print ( "How many levels of difficulty do want?(1-5) (1)" )
print ( "Beaware that higher number exponentionally slow down your computer" )
difficulty = Functions.getValidIntInput(Max=5, Min=1, Default=1)

print ( "Building file tree... (",Config.ApplyChainToFolder,")", sep="" )
files = Functions.FindFiles(Config.ApplyChainToFolder)

#TODO: Fix Windows compatibility.

#TODO: Stack certain amount of data into a file.

#Full file structure:
#<head>[order]<file>[filePath][lengh of data]</file></head>[DATA]<hash>sha512</hash>

allFileData = []

for x in files:
    print ( "Adding:", x )
    tempFile = open ( x, "rb" )
    lengh = str(len(tempFile.read())) #Has to be string to be encoded
    tempFile.close()
    allFileData.append([x, lengh])
    
Header = "<head>[" + str(OutputFileNumber) + "]"

for x in allFileData:
    Header += "<file>[" + x[0] + "][" + x[1] + "]</file>"

Header += "</head>"

#finished writing the header to the file

OutputFile = open(OutputFileName, "wb" )
OutputFile.write(Header.encode("UTF-8"))
OutputFile.close()
del Header, allFileData
#take as little resources as possible.

Data = b""

for x in files:
    tempFile = open(x, "rb")
    Data += tempFile.read()
    tempFile.close()

#Now find the correct salt.
print ( "Finding the correct salt..." )
lengh = 0
found = False
start = time()
iterations = 0
while not found:
    lengh += 1
    for salt in itertools.combinations_with_replacement(charactars, lengh):
        #The iterator will be replaced with data kind of iterator.
        iterations += 1
        if hashlib.sha512(Data+"".join(salt).encode()).hexdigest()[0:difficulty].count("0") == difficulty:
            found = True
            break

end = time()
trueSalt = "".join(salt) 

print ( "Found salt: ", trueSalt )
print ( "Which gives:", hashlib.sha512(Data+trueSalt.encode()).hexdigest() )
print ( "It took:    ", round ( end - start ), "seconds")
print ( "Hash/Second:", round ( iterations / ( end - start ) ) )

OutputFile = open(OutputFileName, "wb" )
OutputFile.write(Data)
OutputFile.write(str("<salt>"+trueSalt+"</salt>)").encode())
OutputFile.close()


