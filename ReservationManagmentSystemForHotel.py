"""
Reservation Management System for
"""



import datetime
from datetime import date


class villa(object):
    """
    Class villa encapsulates the following rented villa characteristics: name of villa, name of personal assistant.
    It also offers functions that inform about the hours that the personal assistant will be on call and the dates that
    the villa will be cleaned and keys will be changed. In addition, it has a function to print the label
    of the gift that is left in the room of each new guest.
    """
    def __init__(self,n,id):
        self.villaName = n

    def setPersonalAssistat(self,pa):
        self.setPersonalAssistat = pa
        print(f"{pa} will be on call from 8.00am to 8.00pm for villa {self.villaName}")

    def cleanAndChangeKey(self, d1, d2):
        print(f"Villa {self.villaName} will be cleaned and keys will be changed on {d1} and {d2}")

    def printGiftLabel(self, s):
        print(f"Welcome at the {self.villaName}, {s} party!")



class vipVilla(villa):
    """
    Class vipVilla inherits from class villa.
    It encapsulates the name of the VIP personal assistant and offers an access function to it.
    """
    def __init__(self,nn,id):
        villa.__init__(self,nn,id)

    def setPersonalAssistant(self, pa):
        self.vipPersAssist = pa
        print(f"{pa} will be on call (7.00am-9.00pm) for villa {self.villaName} and arrange for a personal yacht")



class guest(object):
    """
    Class guest encapsulates the following attributes of a guest: first and last name, number of adults, and number
    of children in the room. It offers an access function to last name and a printing function for the guest object.
    """
    def __init__(self,l1,f1,b,c):
       self.first=l1
       self.last=f1
       self.noofAdults=b
       self.noofChildren=c

    def getLastName(self):
        return self.last

    def __repr__(self):
       return 'Guest: (%s, %s)' % (self.first, self.last)



class reservation(object):
    """
    Class reservation encapsulates the following attributes of a reservation: the name of the reserved villa, checkin date,
    checkout date, reservation ID, a printing function for the reservation class.
    """
    def __init__(self,n,de,le):
         self.checkinDate=de
         self.lengthofStay=le
         self.villaName=n
         self.checkoutDate=de+datetime.timedelta(days=le)

    def getvillaName(self):
             return self.villaName

    def getcheckinDate(self):
            return self.checkinDate

    def getcheckoutDate(self):
            return self.checkoutDate

    def setreservID(self,id):
        self.reservID=id

    def __repr__(self):
       return 'Reservation: (%s, %s, %s, %s)' % (self.checkinDate, self.lengthofStay, self.villaName, self.reservID)


class resort(object):
    """
    Class resort encapsulates the following attributes: a list with the names of the (standard) villas,
    a list with the names of the VIP villas, a guest list, a reservation list and a reservation ID list.
    It also offers access functions to a Guest object, Reservation object, reservation ID and a function that prints all lists.
    """

    vil = ['Elektra', 'Persephone', 'Artemis', 'Kouros']
    vipVil = ['Zeus', 'Alexandrian']
    guestList = []
    reservationList = []
    resIDList = [0]

    def __init__(self):
        print("Welcome to GALLLA!")

    def setGuest(self, g):
        self.guestList.append(g)

    def setReservation(self, r):
        self.reservationList.append(r)

    def getresID(self):
        return self.resIDList[-1]

    def updateResIDList(self):
        i = self.getresID() + 1
        self.resIDList.append(i)
        return (self.resIDList[-1])

    def printLists(self):
        print(f" The guest list is: {self.guestList}")
        print(f" The reservation list is: {self.reservationList}")
        print(f" The resID list is: {self.resIDList}")


# TEST

#guest 1
resort = resort()

guest1 = guest('Adam','Hell',2,1)
resort.setGuest(guest1)
re = reservation('Zeus',date(2019,6,3),5)
resort.setReservation(re)

newid= resort.updateResIDList()
re.setreservID(newid)
if re.getvillaName() == 'Zeus' or re.getvillaName()=='Alexandrian':
    villarese=vipVilla(re.getvillaName(),newid)
else:
    villarese=villa(re.getvillaName(),newid)

villarese.printGiftLabel(guest1.getLastName())
villarese.setPersonalAssistant('Eleni')
villarese.cleanAndChangeKey(re.getcheckinDate(),re.getcheckoutDate())

"""
#Guest 2

sa2=guest('Simon','Marchese',2,1)
rr.setGuest(sa2)
re2=reservation('Artemis',date(2019,7,3),8)
rr.setReservation(re2)
newid2=rr.updateResIDList()
re2.setreservID(newid2)
if re2.getvillaName() == 'Zeus' or re2.getvillaName()=='Alexandrian':
    villarese2=vipVilla(re2.getvillaName(),newid2)
else:
    villarese2=villa(re2.getvillaName(),newid2)
villarese2.printGiftLabel(sa2.getLastName())
villarese2.setPersonalAssistant('Dorian')
villarese2.cleanAndChangeKey(re2.getcheckinDate(),re2.getcheckoutDate())

rr.printLists()

"""






















































