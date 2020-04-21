from message import *
from caesar import *


def testGetMessage():
    expM = 'test'
    expS =  Caesar()
    m = Message('test', expS)
    actM = m.getMessage()
    if expM == actM:
        return 1
    else:
        return 0

def testGetStratCaesar():
    expS =  Caesar()
    m = Message('test', expS)
    res = isinstance(m.getStrat(), Caesar)
    if res:
        return 1
    else: 
        return 0

def testGetStratVig():
    expS =  Vig()
    m = Message('test', expS)
    res = isinstance(m.getStrat(), Vig)
    print(res)
    if res:
        return 1
    else:
        return 0

def incrementResults(result, resultTracker):
    resultTracker[0] += result
    resultTracker[1] += 1
    return resultTracker


def run():
    '''
    run tests on class Mesasge
    '''
    # [passed, total]
    results = [0,0]

    # test getMessage() 
    res0 = testGetMessage()
    incrementResults(res0, results)

    # test getStrat - casesar()
    res1 = testGetStratCaesar()
    incrementResults(res1, results)

    # test getStrat - casesar()
    res2 = testGetStratCaesar()
    incrementResults(res2, results)

    print("Test: message.py tests")
    print("Passed Tests: " + str(results[0]) + "\nTotal Tests: " + str(results[1]))
    print("% passed " + str(results[0] / results[1] * 100))

