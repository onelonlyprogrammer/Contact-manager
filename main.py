import eel
FILENAME ="contacts.txt"
contactList = {}

#Contact class
class contact:
    name = "undefined"
    phone = "undefined"
    email = "undefined"
    address = "undefined"

    def formatString(self): 
        return self.name + ", " + self.phone + ", " + self.email + ", " + self.address
    
    def __init__(self, name, phone, email, address):
        self.name = name
        self.phone = phone
        self.email = email
        self.address = address

    def __str__(self):
        return self.name + ", " + self.phone + ", " + self.email + ", " + self.address

#Writes contacts to file in proper format
def writeToFile(contacts):
    with open(FILENAME, "w") as file:
        for x, y in contacts.items():
            file.write(str(y) + "\n")

def readFromFile():
    global contactList
    ret = {}
    with open(FILENAME, "r") as file:
        for f in file:
            f = f.strip("\n").split(", ")
            p = contact(f[0], f[1], f[2], f[3])
            contactList[p.name] = p

@eel.expose
def findContact(s):
    if s.upper() == "ALL":
        for x, y in contactList.items():
            print(y)
    elif s in contactList:
        return contactList[s].formatString()
    else:
       return "Could not find " + s

@eel.expose
def addContact(key, phone, email, address): 
    if key.upper() == "ALL":
        print("All is not a valid name")
        return
    p = contact(key, phone, email, address)
    contactList[key] = p
    writeToFile(contactList)

@eel.expose
def deleteContact(todelete):
    if todelete in contactList:
        contactList.pop(todelete)
        writeToFile(contactList)
        return todelete + " succesfully deleted"
    else:
        return "Could not find " + todelete

try:
    readFromFile()
except FileNotFoundError:
    print("creating " + FILENAME)
    with open(FILENAME, "w"):
        pass

eel.init("web")
eel.start("index.html")

