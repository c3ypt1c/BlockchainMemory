##import threading
from itertools import combinations_with_replacement as CombWithReplace
from hashlib import sha512
from Functions import FindFiles, getValidIntInput
import Config
from string import ascii_letters, digits
from time import time

##import multiprocessing
##CoreCount = multiprocessing.cpu_count()
##del multiprocessing

OutputFileNumber = 0
OutputFileName = Config.OutputChainFolder + "/" + str(OutputFileNumber) + ".bkch"
charactars = ascii_letters+digits
del ascii_letters, digits

print ( "How many levels of difficulty do want?(1-5) (2)" )
print ( "Beaware that higher difficulty exponentionally slow down progress" )
print ( "(n is the difficulty where 1/(16^n) is the probability of finding the" )
print ( "salt)" )
difficulty = getValidIntInput(Max=5, Min=1, Default=2)
#Most computers should be able to complete 3 or 4 rather quickly,
#the rest will depend on how the blockchain will work

print ( "Building file tree... (",Config.ApplyChainToFolder,")", sep="" )
files = FindFiles(Config.ApplyChainToFolder)

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
    for salt in CombWithReplace(charactars, lengh):
        #The iterator will be replaced with data kind of iterator.
        iterations += 1
        if sha512(Data+"".join(salt).encode()).hexdigest()[0:difficulty].count("0") == difficulty:
            found = True
            break

end = time()
trueSalt = "".join(salt) 

print ( "Found salt: ", trueSalt )
print ( "Which gives:", sha512(Data+trueSalt.encode()).hexdigest() )
print ( "It took:    ", round ( end - start ), "seconds")
print ( "Hash/Second:", round ( iterations / ( end - start ) ) )

OutputFile = open(OutputFileName, "wb" )
OutputFile.write(Data)
OutputFile.write(str("<salt>"+trueSalt+"</salt>)").encode())
OutputFile.close()


