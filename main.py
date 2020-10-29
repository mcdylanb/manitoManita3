import random

masterlist = [ 'Dylan', 'Kaitlyn' , 'Moymoy', 'KOA', 'Gustav' , 'Jannin'];

# prints the original list
for x in range(len(masterlist)):
    print (masterlist[x]);


# copies the masterlist into a new list
randomizedML = list(masterlist);

# debugging  purposes
print (randomizedML)
print (masterlist)

# using shuffles the randomizedML list
random.shuffle(randomizedML);
print("PROCESS:shuffle")

# debugging  purposes
print (randomizedML)
print (masterlist)

# prints manito manita parnters
for people in range(len(masterlist)):
    print(masterlist[people] + randomizedML[people])
