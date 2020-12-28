# import random
# def rollDie():
#     value = randint(1,20)
#     return value
# def advantageWithDis():
#     pass
# def highestRoll():
#     #functionality for single roll
#     #functionality for adv of dis
#     #functionality for dis of adv
#     pass

# rollDie

import random
def findExpected(value, n):
    x = value*((1/20)**n)
    return x
    return accum
def average(lst):
    return sum(lst) / len(lst)
def rollDie():
    return random.randint(1,20)
def advantage():
    first = rollDie()
    second = rollDie()
    if first > second:
        return first
    return second
def disadvantage():
    first = rollDie()
    second = rollDie()
    if first < second:
        return first
    return second
def advWithDis():
    first = disadvantage()
    second = disadvantage()
    if first > second:
        return first
    return second
def disWithAdv():
    first = advantage()
    second = advantage()
    if first < second:
        return first
    return second

def simulate():
    once_raw = []
    AdDis_raw = []
    DisAd_raw = []
    for i in range(0,30):
        once = rollDie()
        once_value = findExpected(once, 1)
        once_raw.append(once_value)
        AdDis = advWithDis()
        AdDis_value = findExpected(AdDis, 4)
        AdDis_raw.append(AdDis_value)
        DisAd = disWithAdv()
        DisAd_value = findExpected(DisAd,4)
        DisAd_raw.append(DisAd_value)
    maxCount = 0
    once_avg = average(once_raw)
    AdDis_avg = average(AdDis_raw)
    DisAd_avg = average(DisAd_raw)

    ret = []
    ret.append(once_avg)
    ret.append(AdDis_avg)
    ret.append(DisAd_avg) 
    # message = """The method which returned the highest amount is %s. In a simulation of 10000 trials, the frequency of the various methods were as follows:
    # Once: %d
    # Advantage of Disadvantage: %d
    # Disadvantage of Advantage: %d""" % (str(res), simulations.count("Once"), simulations.count("Advantage of Disadvantage"), simulations.count("Disadvantage of Advantage"))
    return ret

if __name__ == "__main__":
    print(simulate())