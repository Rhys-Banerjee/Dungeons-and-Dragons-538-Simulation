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
    simulations = []
    for i in range(0,10000):
        once = rollDie()
        AdDis = advWithDis()
        DisAd = disWithAdv()
        if once > AdDis and once > DisAd:
            simulations.append("Once")
        elif AdDis > once and AdDis > DisAd:
            simulations.append("Advantage of Disadvantage")
        elif DisAd > once and DisAd > AdDis:
            simulations.append("Disadvantage of Advantage")
    maxCount = 0
    res = simulations[0] 
    for i in simulations: 
        freq = simulations.count(i) 
        if freq > maxCount: 
            maxCount = freq 
            res = i 
    message = """The method which returned the highest amount is %s. In a simulation of 10000 trials, the frequency of the various methods were as follows:
    Once: %d
    Advantage of Disadvantage: %d
    Disadvantage of Advantage: %d""" % (str(res), simulations.count("Once"), simulations.count("Advantage of Disadvantage"), simulations.count("Disadvantage of Advantage"))
    return message

if __name__ == "__main__":
    print(simulate())