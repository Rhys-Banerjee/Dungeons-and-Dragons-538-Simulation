"""
Attempt to solve the FiveThirtyEight "Riddler." Utilizing Random module. Returns number for each type of roll.
"""

import random
def rollDie():
    return random.randint(1,20)

def average(lst):
    return sum(lst) / len(lst)

def advantage(lst):
    first = lst[0]
    second = lst[1]
    if first > second:
        return first
    return second

def disadvantage(lst):
    first = lst[0]
    second = lst[1]
    if first < second:
        return first
    return second

def advWithDis(lst):
    first_roll = lst[0]
    second_roll = lst[1]
    first = disadvantage(first_roll)
    second = disadvantage(second_roll)
    if first > second:
        return first
    return second

def disWithAdv(lst):
    first_roll = lst[0]
    second_roll = lst[1]
    first = advantage(first_roll)
    second = advantage(second_roll)
    if first < second:
        return first
    return second
    

def separate(values):
    way1 = []
    way2 = []
    way2.append([])
    way2.append([])
    way3 = []
    way3.append([])
    way3.append([])
    way1.append(values[0:2])
    way1.append(values[2:4])
    way2[0].append(values[0])
    way2[0].append(values[2])
    way2[1].append(values[1])
    way2[1].append(values[3])
    way3[0].append(values[0])
    way3[0].append(values[3])
    way3[1].append(values[1])
    way3[1].append(values[2])
    ret = []
    ret.append(way1)
    ret.append(way2)
    ret.append(way3)
    return ret
def four_random():
    lst = []
    for i in range(0,4):
        x = rollDie()
        lst.append(x)
    return lst

def simulate():
    lst = four_random()
    avg = []
    values = separate(lst)
    value1 = values[0]
    values2 = values[1]
    values3 = values[2]
    #once
    avg.append(average(lst))
    #advantage of disadvantage
    aod = []
    aod.append(advWithDis(value1))
    aod.append(advWithDis(values2))
    aod.append(advWithDis(values3))
    avg.append(average(aod))
    #disadvantage of advantage
    doa = []
    doa.append(disWithAdv(value1))
    doa.append(disWithAdv(values2))
    doa.append(disWithAdv(values3))
    avg.append(average(doa))
    return avg

def final():
    raw = []
    raw.append([])
    raw.append([])
    raw.append([])
    ret = []
    for i in range(0,320000):
        lst = simulate()
        raw[0].append(lst[0])
        raw[1].append(lst[1])
        raw[2].append(lst[2])
    ret.append(average(raw[0]))
    ret.append(average(raw[1]))
    ret.append(average(raw[2]))
    return ret

def message():
    lst = final()
    message = """In a simulation of 160,000 trials, the average expected roll for each method were as follows:
    One Roll: %d
    Advantage of Disadvantage: %d
    Disadvantage of Advantage: %d"""%((lst[0]), (lst[1]), (lst[2]))
    return message

print(final())
