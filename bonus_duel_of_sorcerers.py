POWER = {
    'Fireball': 50,
    'Lightning bolt': 40,
    'Magic arrow': 10,
    'Black Tentacles': 25,
    'Contagion': 45
}

gandalf = ['Fireball', 'Lightning bolt', 'Lightning bolt', 'Magic arrow', 'Fireball',
           'Magic arrow', 'Lightning bolt', 'Fireball', 'Fireball', 'Fireball']
saruman = ['Contagion', 'Contagion', 'Black Tentacles', 'Fireball', 'Black Tentacles',
            'Lightning bolt', 'Magic arrow', 'Contagion', 'Magic arrow', 'Magic arrow']
draws = 0
gandalf_wins = 0
saruman_wins = 0
gandalf_power = 0
saruman_power = 0
i = 0
gandalf_average_deviation = []
saruman_average_deviation = []

while i < len(gandalf):
    print("\n")
    print("Gandalf", gandalf[i], " x ",  saruman[i], "Saruman")
    print("Gandalf", POWER[gandalf[i]], " x ", POWER[saruman[i]], "Saruman")
    gandalf_average_deviation.append(POWER[gandalf[i]])
    saruman_average_deviation.append(POWER[saruman[i]])
    if POWER[gandalf[i]] > POWER[saruman[i]]:
        gandalf_wins += 1
        saruman_wins = 0
        print("Gandalf wins!")
        if gandalf_wins >= 3:
            print("Gandalf won the duel!")
            break
    elif POWER[gandalf[i]] < POWER[saruman[i]]:
        saruman_wins += 1
        gandalf_wins = 0
        print("Saruman wins!")
        if saruman_wins >= 3:
            print("Saruman won the duel!")
            break
    else:
        print("Battle draw")
    i += 1

from statistics import stdev
print("The Standard Deviation of Gandalf is % s" %(stdev(gandalf_average_deviation)))
print("The Standard Deviation of Saruman is % s" %(stdev(saruman_average_deviation)))
import statistics
print("The Variance of Gandalf is % s" %(statistics.mean(gandalf_average_deviation)))
print("The Variance of Saruman is % s" %(statistics.mean(saruman_average_deviation)))