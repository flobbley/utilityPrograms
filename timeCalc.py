import datetime
import pickle
import os

global clearVar
syst = os.name
if syst == 'nt':
    clearVar = "cls"
else:
    clearVar = "clear"

class day:
    def __init__(self, date, hours, money, wage):
        self.date = date
        self.hours = hours
        self.money = money
        self.activities = {}
        self.wage = wage
        
class timeTracker:
    def __init__(self):
        self.days = []
        self.wage = 45
        
    def load(self):
        try:
            with open('timeTrack','rb') as f:
                oldDays = pickle.load(f)
            self.days = oldDays.days
            self.wage = oldDays.wage
        except FileNotFoundError:
            self.days = []
            self.wage = 45

    def save(self):
        with open('timeTrack','wb') as f:
            pickle.dump(self,f,protocol=2)

    def addDate(self, date):
        newDay = day(date, 0, 0, self.wage)
        self.days.append(newDay)

    def addTime(self, dateIndex): #put the hours into object with date
        while True:
            os.system(clearVar)
            print('How many hours did you work today?')
            print('Enter 00 to go back')
            hours = input()
            if hours == '00':
                break
            try:
                hours = int(hours)
            except ValueError:
                print('Invalid Entry')
            self.days[dateIndex].hours = hours
            self.days[dateIndex].money = hours*self.days[dateIndex].wage
            input('Hours entered\n')
            break

    def addActivities(self, date):
        while True:
            os.system(clearVar)
            print('What is the job number?')
            print('Enter 00 to go back')
            jobNo = input()
            if jobNo == '00':
                break
            print('What did you do today?')
            activities = input()
            activities = activities.lower()
            if jobNo not in self.days[-1].activities:
                self.days[-1].activities[jobNo] = []
            self.days[-1].activities[jobNo].append(activities)
            input('Activities entered\n')
            break
        
    def moneyAdder(self):
        os.system(clearVar)
        total = 0
        daysWorked = 0
        hoursWorked = 0
        for paid in self.days:
            daysWorked += 1
            hoursWorked += paid.hours
            total += paid.money
        print("Days Worked", daysWorked)
        print("Hours Worked", hoursWorked)
        print("Money Made:", "$"+str(total))
        input()

    def checkDate(self):
        validResponse = ['y','n']
        print('Which date? yyyy-mm-dd')
        checkDate = input()
        for i in range(len(self.days)-1,-1,-1):
            if self.days[i].date == checkDate:
                checkDate = self.days[i]
                break
        while True:
            os.system(clearVar)
            print(checkDate.date)
            print("Hours Worked:", checkDate.hours)
            print("Money Made:", checkDate.money)
            print("Activities Performed:")
            for job in checkDate.activities:
                print(job)
                print(checkDate.activities[job])
            print("Would you like to edit? y/n")
            edit = input()
            if edit == 'y':
                os.system(clearVar)
                print(checkDate.date)
                print("1. Hours Worked:", checkDate.hours)
                print("2. Activities Performed:")
                for job in checkDate.activities:
                    print(job)
                    print(checkDate.activities[job])
                print("00. Go Back")
                print('What would you like to edit? enter number of option')
                action = input()
                if action == '1':
                    self.addTime(i)
                    break
                elif action == '2':
                    self.addActivity(i)
                    break
                elif action == '00':
                    break
            else:
                break

    def changeWage(self):
        while True:
            os.system(clearVar)
            print("What is the new hourly wage?")
            print("Enter 00 to go back") 
            wage = input()
            if wage == '00':
                break
            else:
                try:
                    wage = int(wage)
                    self.wage = wage
                    print("wage succesfully changed")
                    input()
                    break
                except ValueError:
                    print("Invalid Input")

    def search(self):
        while True:
            os.system(clearVar)
            print("How do you want to search?")
            print("1. Job Number (faster)")
            print("2. Activity (slower)")
            print("00. Go Back")
            action = input()
            if action == '00':
                break
            elif action == '1':
                while True:
                    print('Please enter job number: ')
                    print("Enter 00 to go back")
                    num = input()
                    os.system(clearVar)
                    if num == '00':
                        break
                    else:
                        findListDates = []
                        findListActivities = []
                        for i in range(len(self.days)-1,-1,-1):
                            if num in self.days[i].activities:
                                findListDates.append(self.days[i].date)
                                findListActivities.append(self.days[i].activities[num])
                        for i in range(0,len(findListDates)):
                            print(findListDates[i])
                            print(findListActivities[i])
                                                          
            elif action == '2':
                while True:
                    print('Please enter an activity: ')
                    print("Enter 00 to go back")
                    act = input()
                    os.system(clearVar)
                    act = act.lower()
                    if act == '00':
                        break
                    else:
                        findListDates = []
                        findListJobNo = []
                        for i in range(len(self.days)-1,-1,-1):
                            for JobNo in self.days[i].activities:
                                if act in self.days[i].activities[JobNo]:
                                    findListDates.append(self.days[i].date)
                                    findListJobNo.append(JobNo)
                        for i in range(0,len(findListDates)):
                            print(findListDates[i])
                            print(findListJobNo[i])
        
                    
timeTrack = timeTracker()
timeTrack.load()

##monday = day('2020-05-04', 8, 360, 45)
##tuesday = day('2020-05-05', 8, 360, 45)
##wednesday = day('2020-05-06', 8, 360, 45)
##thursday = day('2020-05-07', 8, 360, 45)
##friday = day('2020-05-08', 8, 360, 45)
##monday1 = day('2020-05-11', 8, 360, 45)
##
##monday1.activities = {'45880':['slope stability','settlement'],'42131':['soil borings']}
##friday.activities = {'45880':['slope stability'],'42131':['soil borings']}

today = str(datetime.date.today())#check current date

lastDate = timeTrack.days[-1]#check last date entered

if today != lastDate.date: #if current date is not the same as last date entered, reset hours to zero
    timeTrack.addDate(today)
    timeTrack.save()
    print('Added today to the List!')
    input()

while True:
    os.system(clearVar)
    print('Time Tracker')
    print('\nWhat would you like to do?')
    print('1. Add Time to Today')
    print('2. Add Activities to Today')
    print('3. Check Money Made All Time')
    print('4. Check Date')
    print('5. Search Activities')
    print('6. Change Wage')
    print('7. Exit')
    action = input()
    if action == '1':
        timeTrack.addTime(-1)
        timeTrack.save()
    elif action == '2':
        timeTrack.addActivities(-1)
        timeTrack.save()
    elif action == '3':
        timeTrack.moneyAdder()
    elif action == '4':
        timeTrack.checkDate()
        timeTrack.save()
    elif action == '5':
        timeTrack.search()
    elif action == '6':
        timeTrack.changeWage()
        timeTrack.save()
    elif action == '7':
        print("Goodbye!")
        input()
        break

