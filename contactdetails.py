conct={}
def add(conct):
    name=input("enter the contact name: ")
    number=input("enter the contact number: ")
    conct[name]=number
def delete(conct):
    name=input("Enter the contact name to be deleted")
    del conct[name]
def display(conct):
    print(conct)
def search(conct):
    name=input("Enter the contact name to be searched")
    if name in conct:
        print(conct[name])
    else:
        print("Contact not found")
def update(conct):
    name=input("Enter the name to be updated")
    if name in conct:
        num=input("Enter the number to be updated")
        conct[name]=num
    else:
        a=input("Name not present\nWould you like to add it to the list\ny/n ")
        if a=="y":
            add(conct)
        else:
            pass
print("CONTACT DETAILS\n\n")
n=int(input("1.add new contact\n2.delete\n3.display\n4.search\n5.update\n6.Exit\nYour choice: "))
while n<6:
    if n==1:
        add(conct)
    elif n==2:
        delete(conct)
    elif n==3:
        display(conct)
    elif n==4:
        search(conct)
    elif n==5:
        update(conct)
    else:
        exit()
    n=int(input("1.add new contact\n2.delete\n3.display\n4.search\n5.update\n6.Exit\nYour choice: "))