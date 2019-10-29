import sys
import os

#GLOBAL VARS
topology = open('topology1.txt', 'r')
srcs = []
nexts = []
costs = []
newNode = []
count = 0
dest = None
flag = False
#--------------------------------------------------------------#
# CLASS DECLARATION THAT WILL BE USED AS MY NODE OF MY NETWORK #
#--------------------------------------------------------------#
class Node:
    def __init__(self, src, next, cost):
        self.src = src
        self.next = next
        self.cost = cost
#--------------------------------------------------------------#
# METHODS TO MAKE MY LIFE EASIER AND MODULATE THIS PROGRAM     #
#--------------------------------------------------------------#

# This method will find the cost from the node own table
def findCost(nodeRange, src, dest):
    for i in range(0, nodeRange):
        if newNode[0].src[i] == src and newNode[0].next[i] == dest:
            print("Message from ", src, " to ", dest, " cost " ,newNode[0].cost[i] )
            return True

    return False


# If the Node did not find the Dest in their table will check its neighbors table
def checkNeighbor(nodeRange, src, dest,flag):
    for i in range(0, nodeRange):
        if newNode[0].src[i] == src and newNode[0].next[i] != dest:
            previous_src = newNode[0].src[i]
            neighbor = newNode[0].next[i]
            neighbor_cost = newNode[0].cost[i]
            for j in range(0, nodeRange):
                if newNode[0].src[j] == neighbor and newNode[0].next[j] == dest:
                    print(newNode[0].cost[j])
                    new_cost = (newNode[0].cost[j] + neighbor_cost)
                    newNode[0].src.append(previous_src)
                    newNode[0].next.append(dest)
                    newNode[0].cost.append(new_cost)
                    flag = True
                    return (flag)



#Adding all elements to their respective arrays
for i, line in enumerate(topology):
    src, next, cost = line.strip().split("\t")
    srcs.append(int(src))
    nexts.append(int(next))
    costs.append(int(cost))
    newNode.append(Node(srcs, nexts, costs))

newNode.append(Node(srcs, nexts, costs))
print (newNode[0].src)
print (newNode[0].next)
print (newNode[0].cost)
nodeRange=(len(newNode[0].src))


#For testing purposes
src = 4
dest = 2

flag = findCost(nodeRange,src, dest)
flag = checkNeighbor(nodeRange, src, dest, flag)

print("\n")
print (newNode[0].src)
print (newNode[0].next)
print (newNode[0].cost)
