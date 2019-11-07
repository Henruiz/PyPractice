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
def checkNeighbor(nodeRange, src, dest, flag):
    if flag == False:
        for i in range(0, nodeRange):
            if newNode[0].src[i] == src and newNode[0].next[i] != dest:
                previous_src = newNode[0].src[i]
                neighbor = newNode[0].next[i]
                neighbor_cost = newNode[0].cost[i]
                for j in range(0, nodeRange):
                    if newNode[0].src[j] == neighbor and newNode[0].next[j] == dest:
                        new_cost = (newNode[0].cost[j] + neighbor_cost)
                        print("\nFound path and updated table ")
                        print("Message from ", previous_src, " to ", dest, " cost " , new_cost)
                        newNode[0].src.append(previous_src)
                        newNode[0].next.append(dest)
                        newNode[0].cost.append(new_cost)
                        newNode[0].src.append(dest)
                        newNode[0].next.append(previous_src)
                        newNode[0].cost.append(new_cost)
                        flag = True
                        return (flag)
    else:
        print ("Already in the table ")
        return flag


def readFile():
    #Adding all elements to their respective arrays
    for i, line in enumerate(topology):
        src, next, cost = line.strip().split("\t")
        if src not in srcs:
            srcs.append(int(src))
            nexts.append(int(next))
            costs.append(int(cost))
        if dest not in srcs:
            srcs.append(int(next))
            nexts.append(int(src))
            costs.append(int(cost))

        content = topology.readlines()
    content [line.strip() for line in content]
    newNode.append(Node(srcs, nexts, costs))
    print(content)








readFile()
nodeRange=(len(newNode[0].src))

#For testing purposes
src = 4
dest = 0

flag = findCost(nodeRange,src, dest)
flag = checkNeighbor(nodeRange, src, dest, flag)

print (newNode[0].src)
print (newNode[0].next)
print (newNode[0].cost)

for i in range(0, nodeRange):
    print(newNode[0].src[i])
