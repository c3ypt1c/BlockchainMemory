import threading
import itertools
import hashlib
import Functions
import Config

print ( "How many levels of difficulty do want?(1-5) (1)" )
print ( "Beaware that higher number exponentionally slow down your computer" )
difficulty = Functions.getValidIntInput(Max=5, Min=1, Default=2)

print ( "Building file tree..." )
files = Functions.FindFiles(Config.ApplyChainToFolder)

#Create the required tracker file.

#Stack certain amount of data into a file.

#Generate an appropriate salt so that sha512 can
#generate a set amount of 0's at the start (will need
#use threading to acheve best performance).

#Full file structure:
#<head>[order]<file>[filePath]lengh of data]</file></head>[DATA]<hash>sha512</hash>





