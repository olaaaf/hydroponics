from threading import Timer
import datetime

class Schedule:
    def __init__(self, sch:dict, start_function, stop_function):
        self.schedule = sch
        self.start = start_function
        self.stop = stop_function
        self.running = True    
    
    def get_seconds():
        now = datetime.datetime.now()
        return (now - now.replace(hour=0, minute=0, second=0, microsecond=0)).total_seconds()
    
    def get_weekday():
        days = ["mon", "tue", "wed", "thu", "fri", "sat", "sun"]
        return days[datetime.datetime.today().weekday()]
    
    def next(self):
        days = ["mon", "tue", "wed", "thu", "fri", "sat", "sun"]
        weekday_num = datetime.datetime.today().weekday()
        
        i = weekday_num
        seconds = Schedule.get_seconds()
        surplus = 0
        #Start the pump
        #self.start()
        for i in range(weekday_num, 7 + weekday_num):
            weekday = self.schedule[days[overflow(i, 0, 6)]]
            surplus = 86400 * (weekday_num - i)
            if i > weekday_num:
                surplus += (86400 - seconds)
            for t in weekday:
                start, stop = [int(x) for x in t.split('-')]
                start += surplus
                stop += surplus
                if (stop < seconds):
                    continue
                difference = start - seconds
                
                self.running = True
                if (difference < 0):
                    self.running = False
                    self.stop()
                    self.timer = Timer(stop - seconds, self.toggle)
                else:
                    self.start()
                    self.timer = Timer(difference, self.toggle)
                    
                self.timer.start()
                return True
        return False

    
    def turn_off(self):
        if isinstance(self.timer, Timer.__class__):
            self.timer.cancel()
        self.stop()
        self.running = False
    
    def toggle(self):
        if self.running:
            self.stop()
        else:
            self.start()
        self.running = not self.running
        self.next()
    
    def update_schedule(self, sch:dict):
        self.schedule = sch
        self.next()

def overflow(x, start, stop):
    if x > stop:
        return (x % (stop - start)) + start
    return x
    