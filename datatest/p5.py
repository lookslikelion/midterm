import math

start = int(input("Start number: "))
end = int(input("End number: "))
print ("Sum from", start, "to", end, "is",math.trunc((start + end)*(end-start+1)/2))
