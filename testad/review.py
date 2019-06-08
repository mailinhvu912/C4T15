# import math
# def quadro(a,b,c):
#     delta = b**2 - 4*a*c
#     if delta > 0:
#         x1 = (-b + math.sqrt(delta))/ (2*a)
#         x2 = (-b - math.sqrt(delta))/ (2*a)
#         return x1,x2
#     if delta == 0:
#         x = -b /(2*a)
#         return x
#     if delta < 0:
#         return None
# variable = quadro(1,2,1)
# print(variable)

# class Clock:
#     def __init__(self, hours, minutes, seconds):
#         self.hours = hours
#         self.minutes = minutes
#         self.seconds = seconds
#     def __str__(self):
#         hours = str(self.hours)
#         minutes = str(self.minutes)
#         seconds = str(self.seconds)
#         if len(hours) == 1:
#             hours = "0" + hours
#         if len(minutes) == 1:
#             minutes = "0" + minutes
#         if len(seconds) == 1:
#             seconds = "0" + seconds
#         return hours + ':' + minutes + ':' + seconds
#     def tick(self,seconds):
#         self.seconds += 1
#         if self.seconds == 60:
#             self.seconds = 0
#             self.minutes += 1
#         if self.minutes == 60:
#             self.minutes = 0
#             self.hours += 1
#         if self.hours == 24:
#             self.reset()
#     def reset(self):
#         self.hours = 0
#         self.minutes = 0
#         self.seconds = 0
                
# time = Clock(1,6,57)
# time.tick(0)
# print(time)

def gcd(a,b):
    if a > b:
        high = a
        low = b
    if a < b:
        high = b
        low = a
    # if a == b:
    #     return a
    # else: 
    #     return gcd(low, high - low)
    if high%low == 0:
        return low
    else: 
        return gcd(low, high%low)
numbers = gcd(23,34)
print(numbers)

