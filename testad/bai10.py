class Counter:
    def __init__(self,count=0):
        self.count = count
    def __str__(self):
        return str(self.count)
    def tick(self):
        self.count +=1
    def reset(self):
        self.count = 0

counter = Counter(3)
# nếu đã cho count=0 ngay từ đầu, không cần cung cấp tham số ở Counter()
counter.tick()
# counter.reset()
print(counter)