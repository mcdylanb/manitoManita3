import random

masterlist = [ 'Dylan', 'Kaitlyn' , 'Moymoy', 'KOA', 'Gustav' , 'Jannin'];

# copies the masterlist into a new list
randomizedML = list(masterlist);


# using shuffles the randomizedML list
random.shuffle(randomizedML);
print("PROCESS:shuffle")

# creates a function to check wheter list a and listb the same
def checkIfUnique(list_a ,list_b):
    answer = False
    for people in range(len(list_a)):
        if (list_a[people] == list_b[people]):
            print("similar crap at: ");
            answer = True
    return answer 


#shuffles until unique
while(checkIfUnique(masterlist, randomizedML)):
    print("ho they same")
    random.shuffle(randomizedML);
        
for people in range(len(masterlist)):
    print(masterlist[people] + ' -> '+ randomizedML[people])
