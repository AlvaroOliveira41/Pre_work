gandalf = [10, 11, 13, 30, 22, 11, 10, 33, 22, 22]
saruman = [23, 66, 12, 43, 12, 10, 44, 23, 12, 17]
gandalf_spell = 0
saruman_spell = 0
gandalf_wins = 0
saruman_wins = 0
i = 0

while i < 10:
    gandalf_spell = gandalf[i]
    saruman_spell = saruman[i]
    if gandalf_spell > saruman_spell:
        gandalf_wins += 1
        print("Gandalf wins")
    elif saruman_spell > gandalf_spell:
        saruman_wins += 1
        print("Saruman wins")
    i += 1
print("\n")
if gandalf_wins > saruman_wins:
    print("Gandalf wins", gandalf_wins, "battles against", saruman_wins, "from Saruman. Gandalf won the war!")
else:
    print("Saruman wins", saruman_wins, "battles against", gandalf_wins, "from Gandalf. Saruman won the war!")