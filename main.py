import random

# just realized manito manita is not exchanging gift person to person but passing it on to another person untill it returns into a circle
masterlist = [ 'Dylan', 'Kaitlyn' , 'Moymoy', 'KOA', 'Gustav' , 'Jannin'];

# prints the original list
for x in range(len(masterlist)):
    print (masterlist[x]);


randomizedML = list(masterlist);

print (randomizedML)
print (masterlist)
# using random.shuffle
random.shuffle(randomizedML);
print("PROCESS:shuffle")

# prints the randomized list
for x in range(len(randomizedML)):
    print (randomizedML[x]);

print (randomizedML)
print (masterlist)




# prints manito manita parnters
for people in range(len(masterlist)):
    print(masterlist[people] + randomizedML[people])
