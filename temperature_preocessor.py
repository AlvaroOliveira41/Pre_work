temp_C = [33, 66, 65, 0, 59, 60, 62, 64, 70, 76, 80, 81, 80, 83, 90, 79, 61, 53, 50, 49, 53, 48, 45, 39]
limit_highest_temp = []
new_temp = 0
celsius = 0
temp_F = []

for i, temp in enumerate(temp_C):
    if temp >= 70:
        limit_highest_temp.append(temp)
    if temp == False:
        new_temp = (temp_C[i + 1] + temp_C[i - 1]) / 2
        temp_C[i] = int(new_temp)
    temp_F.append(int(temp_C[i] * 1.8 + 32))
    print(i, "hours", temp_C[i], "Celsius degrees.", temp_F[i], "Fahrenheit degrees.")
if len(limit_highest_temp) >= 4:
    print("There are more than 4 hour/temp above 70Cº")
if max(limit_highest_temp) > 80:
    print("Highest than 80Cº")

import statistics
mean_temperature = statistics.mean(temp_C)
if mean_temperature > 60:
    print("Mean temperature is over 60Cº")
print("The mean of the daily temperature is % s" %int(statistics.mean(temp_C)))

from statistics import stdev
print("The standard deviation of the daily temperature is % s" %int(stdev(temp_C)))
print(temp_F)

from itertools import chain
res = sum(chain(temp_C, temp_F)) / len(list(chain(temp_F, temp_F)))
print("The Average of both lists is : " + str(int(res)))