import numpy as np
import random
import matplotlib.pyplot as plt

################## DEFINE STUFF ############################
# used for testing
data = np.loadtxt('E:/Python Projects/Pokemon IV Calculator/testStats.txt', dtype = int)
stats1 = data[:, 0]
stats2 = data[:, 1]


class pokemon(object):
    def __init__ (self, stats):
        self.stats = stats


def perfectIVCount(list):
    perfectCounter = 0
    for iv in list:
        if iv == 31:
            perfectCounter += 1
    return(perfectCounter)

def genderFunction():
    genderVariable = random.randint(0, 1)
    if genderVariable == 1:
        genderVariable = 'Male'
    elif genderVariable == 0:
        genderVariable = 'Female'

    return(genderVariable)


startMaleStats = {'HP': stats1[0],
                     'ATK': stats1[1],
                     'DEF': stats1[2],
                     'SPA': stats1[3],
                     'SPD': stats1[4],
                     'SPE': stats1[5],
                     'Gender': 'Male'}
startFemaleStats = {'HP': stats2[0],
                     'ATK': stats2[1],
                     'DEF': stats2[2],
                     'SPA': stats2[3],
                     'SPD': stats2[4],
                     'SPE': stats2[5],
                     'Gender': 'Female'}

offspringStats = {'HP': 0,
                     'ATK': 0,
                     'DEF': 0,
                     'SPA': 0,
                     'SPD': 0,
                     'SPE': 0,
                     'Gender': 'N/A'}

perfectStats = {'HP': 31,
                     'ATK': 31,
                     'DEF': 31,
                     'SPA': 31,
                     'SPD': 31,
                     'SPE': 31,
                     'Gender': 'Female'}

# set methods as variables (think of methods as a return... returns something but you must set it to a variable before you can use it)
maleAllStats = pokemon(startMaleStats)
femaleAllStats = pokemon(startFemaleStats)
offspringAllStats = pokemon(offspringStats)
perfectStats = pokemon(perfectStats)

# extract stat names and values of male and female
statNames = list(perfectStats.stats.keys())
maleIVs = list(maleAllStats.stats.values())
femaleIVs = list(femaleAllStats.stats.values())
offspringIVs = list(offspringAllStats.stats.values())
perfectIVs = list(perfectStats.stats.values())

destinyKnot = False
eggCount = 0

"""
while destinyKnot == False:
    DK = input('Do you have destiny knot? [y/n] > ')
    if DK == 'y':
        destinyKnot == True
        break
    elif DK  =='n':
        destinyKnot == True
        break
    else:
        print('Please input a valid input')
"""

#for i in range(3):
while offspringIVs != perfectIVs and maleIVs != perfectIVs and femaleIVs != perfectIVs:

    if perfectIVCount(maleIVs) < 4 and perfectIVCount(femaleIVs) < 4:
        DK = 'n'
    else:
        DK = 'y'

    print(DK)

    selectedIV = np.sort(random.sample(range(6),3 if DK == 'n' else 5)) # 3 if default, 5 with destiny knot
    notSelectedIV = np.sort(list(set(range(6)) - set(selectedIV))) # this gets the list of notSelectedIV's indices by the ones that are not in selectedIV
#    print('stats index', selectedIV, 'passed down')
#    print('stat index', notSelectedIV, 'randomized')

#    print('Going into breeding, male IVs are', maleIVs)
#    print('Going into breeding, female IVs are',femaleIVs)
    #print('Going into breeding, offspring IVs are',offspringIVs)
    print('-----------------------------------')
    for selected, val in enumerate(selectedIV):
        offspringIVs[val] = random.choice((maleIVs[val],femaleIVs[val]))
        if offspringIVs[val] == maleIVs[val]:
            print('Chosen from male IVs')
            
        else:
            print('Chosen from female IVs')
            
        
        print("Replaced stat", val+1, "with", offspringIVs[val])
        print('-----------------------------------')
    
    for notSelected, notVal in enumerate(notSelectedIV):
        offspringIVs[notVal] = random.randint(0, 31)
        print('Randomized number is', offspringIVs[notVal], "going into stat", notVal+1)

    # generate a gender for the offspring
    offspringGender = genderFunction()
#    print(offspringGender)
    
    for listIndex, stats in enumerate(offspringIVs):
        if stats == 'Male' or stats == 'Female' or stats == 'N/A':
            offspringIVs[listIndex] = offspringGender
        else:
            continue

    print(offspringIVs)

    # condition so that it breaks out of the while loop without replacing the parents
    if offspringIVs == perfectIVs:
        break
    

    if perfectIVCount(offspringIVs) > perfectIVCount(maleIVs) and offspringGender == 'Male':
        maleStats = dict(zip(statNames, offspringIVs))
        maleAllStats = pokemon(maleStats)
        maleIVs = list(maleAllStats.stats.values())

        print("Replaced male pokemon")


    elif perfectIVCount(offspringIVs) > perfectIVCount(femaleIVs) and offspringGender == 'Female':
        femaleStats = dict(zip(statNames, offspringIVs))
        femaleAllStats = pokemon(femaleStats)
        femaleIVs = list(femaleAllStats.stats.values())

        print("Replaced female pokemon")

    
    elif perfectIVCount(offspringIVs) == perfectIVCount(maleIVs) and perfectIVCount(offspringIVs) == perfectIVCount(femaleIVs):
        for count, ivs in enumerate(offspringIVs):
            if maleIVs[count] != 0 and femaleIVs[count] != 0:
                break
            if ivs > maleIVs[count] or ivs > femaleIVs[count]:
                lowerNum = min(maleIVs[count], femaleIVs[count])
                if lowerNum == maleIVs[count] and offspringGender == 'Male':
                    maleStats = dict(zip(statNames, offspringIVs))
                    maleAllStats = pokemon(maleStats)
                    maleIVs = list(maleAllStats.stats.values())
                    print("Lower number is from male and is replaced")
                    break
                elif lowerNum == femaleIVs[count] and offspringGender == 'Female':
                    femaleStats = dict(zip(statNames, offspringIVs))
                    femaleAllStats = pokemon(femaleStats)
                    femaleIVs = list(femaleAllStats.stats.values())
                    print("Lower number is from male and is replaced")
                    break
                else:
                    break
        
          

    print("Resulting Eggs are: ")
    print('Male: ', maleIVs, ' and has', perfectIVCount(maleIVs), '31s')
    print('Female: ', femaleIVs, ' and has', perfectIVCount(femaleIVs), '31s')
    print('-----------------------------------')

    eggCount += 1
    
if eggCount == 0:
    print('You already have a max IV female pokemon!')
else:
    print("Congrats! The child pokemon has max IV! It took ", eggCount,"number of eggs")
#print(maleIVs)
#print(femaleIVs)
#print(offspringIVs)
   


print("test")