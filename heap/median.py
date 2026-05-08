import heapq

class MedianFinder:
    def __init__(self):
        self.leftHalf = []
        self.rightHalf = []

    def addNum(self, num):
        if not self.leftHalf or num <= -self.leftHalf[0]:
            heapq.heappush(self.leftHalf, -num)
        else:
            heapq.heappush(self.rightHalf, num)
        if len(self.leftHalf) > len(self.rightHalf) + 1:
            heapq.heappush(self.rightHalf, -heapq.heappop(self.leftHalf))
        elif len(self.rightHalf) > len(self.leftHalf):
            heapq.heappush(self.leftHalf, -heapq.heappop(self.rightHalf))

    def findMedian(self):
        if len(self.leftHalf) > len(self.rightHalf):
            return -self.leftHalf[0]
        elif len(self.rightHalf) > len(self.leftHalf):
            return self.rightHalf[0]
        else:
            return (-self.leftHalf[0] + self.rightHalf[0]) / 2.0
