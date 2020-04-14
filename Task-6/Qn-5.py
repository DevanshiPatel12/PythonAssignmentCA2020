# Create a Time class and initialize it with hours and minutes.
# Make a method addTime which should take two time object and add them. E.g.- (2 hour and 50 min)+(1 hr and 20 min) is (4 hr and 10 min)
# Make a method displayTime which should print the time.
# Make a method DisplayMinute which should display the total minutes in the Time. E.g.- (1 hr 2 min) should display 62 minute.

class Time:
    def __init__(self, hours, minutes):
        self.hours = hours
        self.minutes = minutes

    def addTime(time1, time2):
        if time1.minutes + time2.minutes > 60:
            new_hours = time1.hours + time2.hours + 1
            new_minutes = (time1.minutes + time2.minutes) - 60
        else:
            new_hours = time1.hours + time2.hours
            new_minutes = time1.minutes + time2.minutes
        t = Time(new_hours,new_minutes)
        return t

    def displayTime(self):
        print(self.hours, "hours", self.minutes, "minutes")

    def displayMinutes(self):
        print("Total minutes are : ", self.hours * 60 + self.minutes)

t1 = Time(2,50)
t2 = Time(1,20)
t3 = Time.addTime(t1,t2)
t3.displayTime()
t3.displayMinutes()
