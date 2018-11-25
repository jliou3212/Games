allies = 3


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
        print(total, poss_list_fin, i)
    return total_list


print(find_poss(allies))
