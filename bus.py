stops = [(10, 0), (4, 1), (3, 5), (3, 4), (5, 1), (1, 5), (5, 8), (4, 6), (2, 3)]
stop_numbers = 0
passagers_in = 0
passagers_out = 0
total_passagers = 0
occupation = []
i = 0

stop_numbers = len(stops)
print("The total stop numbers is: ", stop_numbers)
for each_stop in stops:
    total_passagers += each_stop[0]
    print(each_stop[0], "passagers in")
    total_passagers -= each_stop[1]
    print(each_stop[1], "passagers out")
    print("Total passagers is: ", total_passagers)
    occupation.append(total_passagers)
    print("\n")

print(occupation)
print(max(occupation))

from statistics import stdev
print("The Standard Deviation of occupation is % s" %(stdev(occupation)))
import statistics
print("The Variance of occupation is % s" %(statistics.mean(occupation)))