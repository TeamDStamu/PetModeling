import random
import urllib, urllib2, json

#local url
url = 'http://127.0.0.1:3000/petm/insert'

time = 0
auxTime = 0
nextState = 0
currentState = 0
index = 0
randomValue = 0.0
auxPos=0
#listProb = [0,0,0,0,0,0]
listProb = []
'''
actions = []
times = []
'''
maxDict = []

def readDoc():
    arch = open('probabilities.txt','r')
    for line in arch:
        listProb.append(float(line.strip('\n')))

readDoc()

print "Starting"

while True:
    randomValue = random.random()
    currentState = nextState

    #times.append(time)
    auxTime = time;

    if currentState == 0:
        if(randomValue < listProb[2]):
            nextState = 0
            time += 20
        elif(randomValue >= listProb[2] and randomValue < listProb[4]):
            nextState = 1
            time += 5
        else:
            nextState = 2
            time += 10
    elif currentState == 1:
        if(randomValue < listProb[2]):
            nextState = 0
            time += 20
        elif(randomValue >= listProb[2]and randomValue < listProb[3]):
            nextState = 1
            time += 5
        elif(randomValue >= listProb[3] and randomValue < listProb[5]):
            nextState = 1
            time += 10
        else:
            nextState = 3
            time += 3
    elif currentState == 2:
        if(randomValue < listProb[2]):
            nextState = 0
            time += 20
        elif(randomValue >= listProb[2] and randomValue < listProb[4]):
            nextState = 1
            time += 5
        else:
            nextState = 3
            time += 3
    elif currentState == 3:
        if(randomValue < listProb[0]):
            nextState = 0
            time += 20
        elif(randomValue >= listProb[0] and randomValue < listProb[1]):
            nextState = 1
            time += 5
        else:
            nextState = 2
            time += 10

    #actions.append(nextState)
    maxDict.append( { 'action':nextState, 'time':auxTime } )

    if(time >= 1440):
        break

print("Finished")
#print actions
#print times
print (maxDict)
#print len(maxDict)

#json formatting
values = {
    'data' : maxDict
}

data = json.dumps(values)
clen = len(data)

'''

#make post request
req = urllib2.Request(url, data, {'Content-Type': 'application/json', 'Content-Length': clen})
response = urllib2.urlopen(req)
print response.geturl()
print response.info()
the_page = response.read()
print the_page

'''