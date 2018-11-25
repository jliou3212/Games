poss = []
outcome_min = int(input('Enter the desired outcome(min): '))
outcome_max = int(input('Enter the desired outcome(max): '))
chance_ttl = 0

for i in range(6):
    poss.append(int(input('Enter the 6 initial dice possibilities(' + str(i+1) + '): ')))
allies = int(input('Enter the amount of allies you have'))
allies_poss = 2 ** allies

for i in poss:
    chance = 1 / len(poss)
    if outcome_min <= i <= outcome_max:
        chance_ttl += chance

print('Percentage chance is %' + str(chance_ttl * 100))
