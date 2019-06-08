class Timer:
    def __init__(self,hours,minutes,seconds):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds
    def __str__(self):
        hours = str(self.hours)
        minutes = str(self.minutes)
        seconds = str(self.seconds)
        if len(hours) == 1:
            hours = "0" + hours
        if len(minutes) == 1:
            minutes = "0" + minutes
        if len(seconds) == 1:
            seconds = "0" + seconds
        # nếu muốn in dưới dạng 00:00:00
        return hours + ':' + minutes + ':' + seconds

    def tick(self, seconds):
        self.seconds +=1
        if self.seconds == 60:
            self.seconds = 0
            self.minutes += 1
        if self.minutes == 60:
            self.minutes = 0
            self.hours += 1
        if self.hours == 24:
            self.reset()
    def reset(self):
        self.hours = 0
        self.minutes = 0
        self.seconds = 0

time = Timer(3,2,57)
time.tick(0)
print(time)