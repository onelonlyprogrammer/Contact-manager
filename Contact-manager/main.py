import eel
import crypt
FILENAME = "contacts.txt"
contactList = {}

#Encodeing object
cipher = crypt.AESCipher("Key")

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
    with open(FILENAME, "wb") as file:
        for x, y in contacts.items():
            file.write(cipher.encrypt(str(y)))
            file.write("\n".encode("utf-8"))

#Reads contacts and append them to contactList
def readFromFile():
    global contactList
    with open(FILENAME, "rb") as file:
        for f in file:
            f = str(cipher.decrypt(f)).strip("b").strip("'").split(", ")
            p = contact(f[0], f[1], f[2], f[3])
            contactList[p.name] = p

@eel.expose
#Takes string and returns contact if found
def findContact(query):
    ret = []
    if query.upper() == "ALL":
        for x, y in contactList.items():
            ret.append(y.formatString())
    elif query in contactList:
        ret.append(contactList[query].formatString())
    else:
       ret.append("Could not find " + query)
    return ret

@eel.expose
#Takes list of four arguments, turns them into contact object and appends contact to contact List
def addContact(con):
    if len(con) != 4:
        return "Invalid contact. Please input four items"
    if con[0].upper == "ALL":
        return "All is not a valid name"
    contactList[con[0]] = contact(con[0], con[1], con[2], con[3])
    writeToFile(contactList)
    return con[0] + " successfully added"

@eel.expose
#Takes string and searches for matching string and deletes corresponding contact
def deleteContact(todelete):
    if todelete in contactList:
        writeToFile(contactList.pop(todelete))
        return todelete + " succesfully deleted"
    else:
        return "Could not find " + todelete

try:
    readFromFile()
except FileNotFoundError:
    print("creating " + FILENAME)
    with open(FILENAME, "wb"):
        pass

eel.init("web")
#For starting eel
"""Comment wnen using gui.py"""#eel.start("index.html")
