import random
import datetime

print("WECOME TO TAJ HOTEL")
def detail():
    name =input("enter the name")
    phone=int(input("enter the phone number"))
    address=input("enter the address")
    aadhar_card=int(input("enter the aadhar_card"))
detail()

def Home():
    print("1 Booking")
    print(" 2 Rooms Info")
    print("3 Room Service(Menu Card)")
    print(" 4 Payment")
    print(" 5 Record")
    print("0 Exit")
Home()

name = []
phno = []
add = []
checkin = []
checkout = []
room = []
price = []
rc = []
p = []
roomno = []
custid = []
day = []

i=0

def Booking():
        global i
        print(" BOOKING ROOMS")
        print(" ")
         
        while 1:
            n = str(input("Name: "))
            p1 = str(input("Phone No.: "))
            a = str(input("Address: "))
             
            if n!="" and p1!="" and a!="":
                name.append(n)
                add.append(a)
                break
                 
            else:
                 print("\tName, Phone no. & Address cannot be empty..!!")

num=int(input("enter the num")) 
if num == 1:
    print("Booking ")
elif num == 2:
    print(" Room Info")
elif num == 3:
    print("Room Service(menu card)")
elif num == 4:
    print(" Payment")
elif num == 5:
    print(" Record")
else:
    exit()

def date(c):
     
    if c[2] >= 2019 and c[2] <= 2020:
         
        if c[1] != 0 and c[1] <= 12:
             
            if c[1] == 2 and c[0] != 0 and c[0] <= 31:
                 
                if c[2]%4 == 0 and c[0] <= 29:
                    pass
                 
                elif c[0]<29:
                    pass
                 
                else:
                    print("Invalid date\n")
                    name.pop(i)
                    phno.pop(i)
                    add.pop(i)
                    checkin.pop(i)
                    checkout.pop(i)
                    Booking()

cii=str(input("Check-In: "))
checkin.append(cii)
cii=cii.split('/')
ci=cii
ci[0]=int(ci[0])
ci[1]=int(ci[1])
ci[2]=int(ci[2])
date(ci)
          
coo=str(input("Check-Out: "))
checkout.append(coo)
coo=coo.split('/')
co=coo
co[0]=int(co[0])
co[1]=int(co[1])
co[2]=int(co[2])

if co[1]<ci[1] and co[2]<ci[2]:
    print("\n\tErr..!!\n\tCheck-Out date must fall after Check-In\n")
    name.pop(i)
    add.pop(i)
    checkin.pop(i)
    checkout.pop(i)
    Booking()
elif co[1]==ci[1] and co[2]>=ci[2] and co[0]<=ci[0]:
    print("\n\tErr..!!\n\tCheck-Out date must fall after Check-In\n")
    name.pop(i)
    add.pop(i)
    checkin.pop(i)
    checkout.pop(i)
    Booking()
else:
    pass

date(co)
d1 = datetime.datetime(ci[2],ci[1],ci[0])
d2 = datetime.datetime(co[2],co[1],co[0])
d = (d2-d1).days
day.append(d)

print("----SELECT ROOM TYPE----")
print(" 1. Standard Non-AC")
print(" 2. Standard AC")
print(" 3. 3-Bed Non-AC")
print(" 4. 3-Bed AC")
print(("\t\tPress 0 for Room Prices"))

num=int(input("enter the num"))
if num==0:
    print(" 1. Standard Non-AC - Rs. 3500")
    print(" 2. Standard AC - Rs. 4000")
    print(" 3. 3-Bed Non-AC - Rs. 4500")
    print(" 4. 3-Bed AC - Rs. 5000")
    ch=int(input("->"))
    if ch==1:
        room.append('Standard Non-AC')
        print("Room Type- Standard Non-AC") 
        price.append(3500)
        print("Price- 3500")
    elif ch==2:
        room.append('Standard AC')
        print("Room Type- Standard AC")
        price.append(4000)
        print("Price- 4000")
    elif ch==3:
        room.append('3-Bed Non-AC')
        print("Room Type- 3-Bed Non-AC")
        price.append(4500)
        print("Price- 4500")
    elif ch==4:
        room.append('3-Bed AC')
        print("Room Type- 3-Bed AC")
        price.append(5000)
        print("Price- 5000")
    else:
        print(" Wrong choice..!!")

rn = random.randrange(40)+300
cid = random.randrange(40)+10

while rn in roomno or cid in custid:
    rn = random.randrange(60)+300
    cid = random.randrange(60)+10
    rc.append(0)
    p.append(0)

cii=str(input("Check-In: "))
checkin.append(cii)
cii=cii.split('/')
ci=cii
ci[0]=int(ci[0])
ci[1]=int(ci[1])
ci[2]=int(ci[2])
date(ci)

coo=str(input("Check-Out: "))
checkout.append(coo)
coo=coo.split('/')
co=coo
co[0]=int(co[0])
co[1]=int(co[1])
co[2]=int(co[2])
p1 = str(input("Phone No.: "))
if p1 not in phno:
    phno.append(p1)
elif p1 in phno:
    for n in range(0,i):
        if p1== phno[n]:
            if p[n]==1:
                phno.append(p1)
elif p1 in phno:
    for n in range(0,i):
        if p1== phno[n]:
            if p[n]==0:
                print("\tPhone no. already exists and payment yet not done..!!")
                name.pop(i)
                add.pop(i)
                checkin.pop(i)
                checkout.pop(i)
                Booking()
        print("")
        print("\t\t\t*ROOM BOOKED SUCCESSFULLY*\n")