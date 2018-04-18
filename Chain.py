from itertools import combinations_with_replacement as CombWithReplace
from Functions import FindFiles, getValidIntInput
from string import ascii_letters, digits
from time import time, sleep
from hashlib import sha512
import Config

import threading
from multiprocessing import cpu_count
CoreCount = cpu_count()
del cpu_count

OutputFileNumber = 0
OutputFileName = Config.OutputChainFolder + "/" + str(OutputFileNumber) + ".bkch"
charactars = ascii_letters+digits
del ascii_letters, digits

print ( "How many levels of difficulty do want?(1-5) (2)" )
print ( "Be aware that higher difficulty exponentially slow down progress" )
print ( "(n is the difficulty where 1/(16^n) is the probability of finding the salt)" )
difficulty = getValidIntInput(Max=5, Min=1, Default=2)
#Most computers should be able to complete 1 or 2 rather quickly,
#the rest will depend on how the block chain will work

print ( "Building file tree... (",Config.ApplyChainToFolder,")", sep="" )
files = FindFiles(Config.ApplyChainToFolder)

#TODO: Fix Windows compatibility.

#TODO: Stack certain amount of data into a file.

allFileData = []

for x in files:
    print ( "Adding:", x )
    tempFile = open ( x, "rb" )
    length = str(len(tempFile.read())) #Has to be string to be encoded
    tempFile.close()
    allFileData.append([x, length])
    
Header = "<head>[" + str(OutputFileNumber) + "]"

for x in allFileData:
    Header += "<file>[" + x[0] + "][" + x[1] + "]</file>"

Header += "</head>"

#finished writing the header to the file

OutputFile = open(OutputFileName, "wb" )
OutputFile.write(Header.encode("UTF-8"))
del Header, allFileData
#take as little resources as possible.

Data = b""

for x in files:
    tempFile = open(x, "rb")
    Data += tempFile.read()
    tempFile.close()

#Now find the correct salt.
print ( "Finding the correct salt..." )

start = time()

WorkerDataLock = threading.Lock()
WorkerData = [ None for x in range(CoreCount) ]
Threads = []
found = False
ID = None
length = 0

class worker(threading.Thread): #Will probably be moved to functions
    
    def __init__(self, Data, difficulty, length, ID):
        threading.Thread.__init__(self)
        
    def run(self):
        found = False
        iterations = 0

        TimePassed = time()
        LastIterations = 0

        for salt in CombWithReplace(charactars, length): #They know how long by their ID
            #The iterator will be replaced with byte kind of iterator maybe
            iterations += 1
            
            if sha512(Data+"".join(salt).encode()).hexdigest()[0:difficulty].count("0") == difficulty:
                found = True
                break
            
            if time() - TimePassed > 1:
##                #These will be used as reports later :)
##                print ( "Current salt:", "".join(salt) )
##                print ( "ΔIterations: ", iterations - LastIterations )
##                print ( "ΔIter/ΔTime: ", round((iterations - LastIterations) / 1, 2), "Iterations/Second" )
##                LastIterations = iterations
                WorkerDataLock.acquire()
                HasToExit = WorkerData[ID]
                WorkerDataLock.release()
                if HasToExit:
                    break
                
                TimePassed = time()
                
        WorkerDataLock.acquire()
        HasToExit = WorkerData[ID]
        if not HasToExit: #Prevents thread from overwriting kill signal
            if found:
                WorkerData[ID] = "".join(salt)
            else:
                WorkerData[ID] = None
            
        WorkerDataLock.release()


while not found:
    WorkerDataLock.acquire()
    
    for salt in WorkerData:
        
        if salt is None:
            ID = WorkerData.index(None)
            thread = worker(Data, difficulty, length, ID)
            WorkerData[ID] = False #So no true ;)
            thread.start()
            Threads.append(thread)
            length += 1
            
        elif salt:
            found = True
            WorkerData = [ True for x in WorkerData ]
            break
            
    WorkerDataLock.release()
    sleep(0.5) #Check every half a second

end = time()

print ( "Found salt: ", salt )
digest = sha512(Data+salt.encode()).hexdigest()
print ( "Which gives:", digest[:30] + "..." + digest[len(digest)-30:] )
print ( "It took:    ", round ( end - start, 2 ), "seconds")
##print ( "Hash/Second:", round ( iterations / ( end - start ), 2 ) )

OutputFile.write(Data)
OutputFile.write(str("<salt>"+salt+"</salt><difficulty>"+str(difficulty)+"</difficulty>").encode())
OutputFile.close()


