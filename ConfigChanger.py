import string
import Functions

#Read the config file
file = open ( "Config.py", "rb" )
fileData = file.read()
file.close()
fileData = fileData.decode()

#Strip stray \r if any
EndType = "\n" #Unix c:
if fileData.count("\r") > 0:
    EndType = "\n\r" #Windows .-.
    fileData.split("\n")
    fileData = [ string.replace(x, "\r", "") for x in fileData ]

else:
    fileData.split("\n")

print ( "What would you like to change?" )
i = 0
for x in fileData:
    print ( i+1, x, sep=". " ) #Mind the offset
    i += 1

item = Functions.getValidIntInput(Max=i+1,Min=1)-1 #offsets cancel
#let the user change something ^

print ( "What would you like to change", fileData[item].split("=")[0], "to?" )
value = input ( "> " ) #Input can by of almost any type.
#to something ^
print ( "Setting ", fileData[item].split("=")[0], "to ", value, sep="" )
fileData[item] = fileData[item].split("=")[0] + "= " + value
#Man, this is fun

print ( "Anything else?" )
