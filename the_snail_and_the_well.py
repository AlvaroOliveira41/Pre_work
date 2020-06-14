day = 0
well_height = 125
daily_distance = 30
nightly_distance = 20
snail_position = 0

while snail_position < well_height:
    snail_position += int(daily_distance) - int(nightly_distance)
    day += 1
    print("Day", day, "=", snail_position, "cm")
    if snail_position > well_height:
        break

print("It will take", day, "days for the snail to come out of the well.")
print("\n")
day = 0
well_height = 125
advance_cm = [30, 21, 33, 77, 44, 45, 23, 45, 12, 34, 55]
nightly_distance = 20
snail_position = 0
snail_rises = 0

while advance_cm:
  snail_rises = (advance_cm.pop(0))
  snail_position += snail_rises - nightly_distance
  day += 1
  print("Day", day, "=", snail_position, "cm")
  if snail_position > well_height:
    break

print("It will take", day, "days for the snail to come out of the well.")
print("\n")
day = 0
well_height = 125
advance_cm = [30, 21, 33, 77, 44, 45, 23, 45, 12, 34, 55]
nightly_distance = 20
snail_position = 0
snail_rises = 0
average_progress = 0
max_displacement = 0
min_displacement = 0
list_advanced_cm = []
displacement = [10, 21, 45, 126, 231, 361]

while advance_cm:
  snail_rises = advance_cm[day]
  list_advanced_cm.append(snail_rises)
  snail_position += snail_rises - nightly_distance
  average_progress += snail_position
  day += 1
  print("Day", day, "=", snail_position, " - average:", average_progress)
  if snail_position > well_height:
    break
print("\n")
max_displacement = max(list_advanced_cm)
min_displacement = min(list_advanced_cm)
print("\n")
print("It will take", day, "days for the snail to come out of the well. And the average progress is:", average_progress/day)
print(max_displacement, min_displacement)
print("\n")
from statistics import stdev
print("The Standard Deviation of advance_cm is % s" %(stdev(displacement)))
print("\n")
import statistics
print("The Variance of the advance_cm is % s" %(statistics.variance(displacement)))