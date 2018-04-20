from hashlib import sha512
import Config
from Functions import FindFiles

print ( "Building file tree..." )
files = FindFiles(Config.ApplyChainToFolder)

#Full file structure:
#<head>[order]<file>[filePath][lengh of data]</file></head>[DATA]<hash>sha512</hash>
