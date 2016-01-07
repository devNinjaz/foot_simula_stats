#!/usr/bin/python
import math

class Statistic_obj:
    def __init__ (self, data):
        self.data = data
        self.maximum = find_max(data)
        self.minimum = find_min(data)
        self.median = find_median(data)
        self.average = find_average(data)
        self.variance = find_variance(data)
        self.standard_deviation = find_standard_deviation(data)
    
    def show_data(self):
        print str(self.data)

    def __str__ (self):
        msg2 = "average: " + str("%.3f" % self.average)
        msg3 = "median: " + str(self.median)
        msg4 = "min: " + str(self.minimum)
        msg5 = "max: " + str(self.maximum)
        msg6 = "variance: " + str("%.3f" % self.variance)
        msg7 = "standard deviation: " + str("%.3f" % self.standard_deviation)
        return msg2 + "\n" + msg3 + "\n" + msg4 + "\n" + msg5 + "\n" + msg6 + "\n" + msg7

def find_average(data):
    sum = 0.0
    for dragon in data:
        sum += dragon

    return sum / len(data)

def find_median(data):
    if len(data) % 2 != 0:
        return data[len(data)/2]
    else:
        return (data[len(data)/2 - 1] + data[len(data)/2]) / 2

def find_min(data):
    data.sort()
    return data[0]

def find_max(data):
    data.sort()
    return data[-1]

def find_variance(data):
    N = len(data)
    avg = find_average(data)
    summ = 0.0
    for dragon in data:
       summ = summ + (dragon - avg) * (dragon - avg) 
    return summ * (1.0 / (N - 1))

def find_standard_deviation(data):
    return math.sqrt(find_variance(data))
