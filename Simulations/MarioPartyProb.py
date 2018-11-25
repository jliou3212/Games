def find_poss(allies):
    poss_list = [0] * allies
    poss_count = 2 ** allies
    total_list = []
    for i in range(1, poss_count + 1):
        total = 0
        poss_list_fin = []
        counter = 1
        # swaps the count of one number in list
        for j in range(1, allies+1):
            if i % counter == 0:
                poss_list[allies-j] += 1
            counter *= 2
        # converts the even/odd numbers to 1/2
        for j in poss_list:
            if j % 2 == 0:
                poss_list_fin.append(1)
            else:
                poss_list_fin.append(2)
        for j in poss_list_fin:
            total += j
        total_list.append(total)
        total_list.sort()
    return total_list

# below is the declaration of all needed variables
# TODO: consider rewriting input statements for user ease
poss_init = []
outcome_min = int(input('Enter the desired outcome(min): '))
outcome_max = int(input('Enter the desired outcome(max): '))
chance_ttl = 0
for i in range(6):
    poss_init.append(int(input('Enter the initial dice roll possibilities(' + str(i+1) + '): ')))
allies = int(input('Enter the amount of allies you have: '))
allies_poss = find_poss(allies)


# TODO: calculate chance with allies rolls in addition to original
for i in poss_init:
    chance = 0
    # sing for singular dice element
    poss_sing = []
    for j in allies_poss:
        poss_sing.append(i + j)
    for j in poss_sing:
        if outcome_min <= j <= outcome_max:
            chance += (1 / len(allies_poss))
    print(chance, i)
    chance_ttl += chance


chance_ttl = chance_ttl / 6
# final print statement to determine chance
print('Percentage chance is %' + str(chance_ttl * 100))
