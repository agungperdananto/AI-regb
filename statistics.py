from math import sqrt

def mean(data):
    return sum(data)/len(data)

def std(data):
    return sqrt(sum([(x - mean(data))**2 for x in data]) / (len(data)-1))