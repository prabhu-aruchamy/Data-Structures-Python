from datetime import date, timedelta

class work:
    def __init__(self):
        return None

    def workcalc(self,yr,mnth,dte):
        self.dte = dte
        self.mnth = mnth
        self.yr = yr
        tdate = date.today()
        work_started = date(yr, mnth, dte)
        experience = (date.today() - work_started) // timedelta(days=365.2425)
        # print(date.today().month)
        t = date.today().month - mnth
        #d = datetime.striptime()
        print(experience," years",t," months")

w = work()
d = int(input("Enter day: "))
m = int(input("Enter Month: "))
y = int(input("Enter Year: "))
w.workcalc(y,m,d)
# print (experience)