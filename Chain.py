import threading
import itertools
import hashlib
import Functions
import Config

print ( "How many levels of difficulty do want?(1-5) (1)" )
print ( "Beaware that higher number exponentionally slow down your computer" )
difficulty = Functions.getValidIntInput(Max=5, Min=1, Default=2)

print ( "Building file tree... (",Config.ApplyChainToFolder,")" )
files = Functions.FindFiles(Config.ApplyChainToFolder)

#Create the file.
OutputFileNumber = 0
OutputFileName = Config.OutputChainFolder + "/" + str(OutputFileNumber) + ".bkch"

#TODO: Fix Windows compatibility.

#Stack certain amount of data into a file.

#Generate an appropriate salt so that sha512 can
#generate a set amount of 0's at the start (will need
#use threading to acheve best performance) (will be
#implemeted later).

#Full file structure:
#<head>[order]<file>[filePath][lengh of data]</file></head>[DATA]<hash>sha512</hash>

i = 0 #File number
allFileData = []

for x in files:
    tempFile = open ( x, "rb" )
    lengh = str(len(tempFile.read())) #Has to be string to be encoded
    tempFile.close()
    allFileData.append([x, lengh])
    
Header = "<head>[" + str(i) + "]"

for x in allFileData:
    Header += "<file>[" + x[0] + "][" + x[1] + "]</file>"

Header = "</head>"

Data = b""

for x in files:
    tempFile = open(x, "rb")
    Data += tempFile.read()
    tempFile.closer()

#Now find the correct hash.






