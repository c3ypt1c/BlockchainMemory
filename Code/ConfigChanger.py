from Functions import inputs

#Read the config file
file = open ( "Config.py", "rb" )
fileData = file.read()
file.close()
fileData = fileData.decode()

#Strip stray \r if any
EndType = "\n" #Unix c:
if fileData.count("\r") > 0:
    EndType = "\n\r" #Windows .-.
    fileData = fileData.split("\n")
    fileData = [ string.replace(x, "\r", "") for x in fileData ]

else:
    fileData = fileData.split("\n")

while True:
    print ( "What would you like to change?" )
    i = 0
    for x in fileData:
        if x.count("=") == 1:
            print ( i+1, x, sep=". " ) #Mind the offset
        i += 1

    item = inputs.getValidIntInput(Max=i+1,Min=1)-1 #offsets cancel
    #let the user change something ^
    varableName = fileData[item].split("=")[0].replace(" ", "")

    print ( "What would you like to change", varableName, "to?" )
    value = input ( "> " ) #Input can by of almost any type.
    #to something ^
    print ( "Setting", varableName, "to", value )
    fileData[item] = fileData[item].split("=")[0] + "= " + value
    #Man, this is fun

    print ( "Anything else? (N)" )
    if not inputs.getYesNo(Default=False): #Find if the user wants to change anything else
        break

file = open ( "Config.py", "wb") #Save changes
[ file.write((x+EndType).encode()) for x in fileData ]
file.close()
