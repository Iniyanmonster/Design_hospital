class User:
    def __init__(self,patientname):
        self.patientname=patientname

    def database(self):
        list1=[]

        if len(list1)==0:
            password = input("create password:")
            d = self.patientname
            g = password
            list1.append([d,g])
            return list1
        else:

            for i in range(len(list1)):
                if self.patientname not in list1[[i][0]]:
                    password=input("create password:")
                    d=self.patientname
                    g=password
                    list1.append([d,g])
                    return list1
                else:
                    password = input("enter password:")
                    if password==list1[1][i]:
                        return "login successful"
                    else:
                        return "invalid password"

class doctor:

    def timingdoc(self):
        list1=[]
        day = {"General_medicine": ['Monday', 'Thursday'], "Pediatrician": ["Tuesday", "Friday"],"Cardiology": ["Wednesday", "Saturday"]}
        time = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        list1.append(day)
        list1.append(time)
        return list1

class patient(User,doctor):

    def updateinformation(self):
        self.slotbook()

    def applicable_insurance(self):
        Type=bool(input("Did you apply insurance? Enter True or False:"))
        if Type==True:
            return "insurance applied"
        else:
            return "insurance not applied"


    def availability(self):
        specialisation = input("Enter the specialisation:")

        if specialisation in self.timingdoc()[0]:
            daytime = self.slotbook()

            if  daytime[0] in self.timingdoc()[1] and daytime[1] in self.timingdoc()[0][specialisation]:
                return "your slot is booked on {} 'o'clock in the day of {}".format(daytime[0],daytime[1])
            else:
                return "No slots are available"

    def show_details(self):
        list1=[]
        list1.append(self.patientname)
        if self.availability()=="your slot is booked":
            list1.append(self.availability())

        return list1
    def slotbook(self):
        list1=[]
        time =input("Enter the time slot for appointment:")
        day =input("Enter the day for appointment:")
        list1.append(time)
        list1.append(day)
        return list1


class doctorassistant(patient,doctor):


    def insurancecheck(self):
        par=self.applicable_insurance()
        if par=="insurance applied":
            return True
        else:
            return False




obj=patient(input("enter patient name:"))
obj2=patient(input("enter patient name:"))

print(obj.database())
print(obj.database())
#print(obj.show_details())
#print(obj.availability())






