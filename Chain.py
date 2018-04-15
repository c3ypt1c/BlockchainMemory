import threading
import itertools
import Functions
import Config

print ( "How many levels of difficulty do want?(1-5) (1)" )
print ( "Beaware that higher number exponentionally slow down your computer" )
difficulty = Functions.getValidIntInput(Max=5, Min=1, Default=2)

print ( "Building file tree..." )
files = Functions.FindFiles(Config.ApplyChainToFolder)

# hack hack





