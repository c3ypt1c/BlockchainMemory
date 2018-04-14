import hashlib
import Config
from Functions import FindFiles

From = "Stuff to Blockchain"

print ( "Building file tree..." )
files = FindFiles(Config.ApplyChainToFolder)

#TODO:Starting reading file contents and see if they match 
