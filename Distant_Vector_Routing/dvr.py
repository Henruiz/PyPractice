import sys, os, numpy
from numpy import loadtxt
from collections import defaultdict



#*----------Collaborated with several other students-----------------------*#

#--------------------------------------------------------------#
#                       GLOBAL VARS                            #
#--------------------------------------------------------------#
intial_List = {} # global topology in a dict, debating if I should use a defualtdict instead
numOfRounds = 0 # used for number of rounds to process
fileName = []
#--------------------------------------------------------------#
# METHODS TO MAKE MY LIFE EASIER AND MODULATE THIS PROGRAM     #
#--------------------------------------------------------------#
"""
This method loads the specified file via CMDLINE, and parses the information.
Saving each unique node as a Node object with its respective routingTable info.

The Node objects are saved into a dictionary and the key is the unique node_id
& the values are the Object corresponding to that unique node_id

Example
dict{unique node_id: Node Object, unique node_id: Node Object}
intial_List{4: Node(4), 1: Node(1)}
"""
def initial_Setup():
    inputFile = open(sys.argv[1], 'r') # 1st argument is txt file
    fileName = sys.argv[1]
    numOfRounds = sys.argv[2] # 2nd arguments is the number of rounds to complete
    # print("numOfRounds", numOfRounds) # debugging purposes
    topology = loadtxt(inputFile,dtype=int) # grab all the information from the file and convert to int

    # saving the information in their respective dictionary
    for row in topology:
        src, dest, cost = row
        if not src in intial_List:
            intial_List[src] = Node(src)
        intial_List[src].addToRoutingTable([dest,cost,dest])

        if not dest in intial_List:
            intial_List[dest] = Node(dest)
        intial_List[dest].addToRoutingTable([src,cost,src])


    for key, value in intial_List.items():
        value.neighbors = list(value.rTable.keys())
    inputFile.close()
    return numOfRounds, fileName

"""
This method display the Node and its Routing Table
Example of Print Statement

 --------------------------
| Node 4 's Routing Table  |
 --------------------------
   Dest   Cost   nextHop
    1     532       1
    2     669       2
    3     196       3

"""
def displayAllNodeData():
    for node_id,node in intial_List.items():
        print("\n --------------------------")
        print("| Node", node_id ,"'s",   "Routing Table  |")
        print(" --------------------------")
        print("   Dest\t  Cost\t nextHop")
        for dest,table in node.rTable.items():
            print("   ",dest,"\t ",table['Cost'],"\t   ",table['nextHop'] )

"""
This methods will update the immediate Routing Table of the Source Node.
Will be taking in the number of rounds that was input via command line.

Exchanges DVPackets From Source Node To Neighbor and then Neighbor to its
Neighbors and so on so forth.
"""
def updateRoutingTable(initialize_List, numOfRounds):
    rounds = int(numOfRounds) # this comes from command line argument
    if rounds == 0: # if no specific round was chosen use the unique num of nodes
      rounds = len(initialize_List.rTable.keys())
    else:
        count = 0
        packets = 0
        convergence = 0
        for i in range(0,rounds):
            count += 1 # display number of rounds
            for src,node in initialize_List.items():
                src_neighbors = node.neighbors
                for neighbor in src_neighbors:
                    packets += 1
                    convergence = sendDVPacket(src,neighbor,initialize_List)

        return packets
"""
This is method will be used to send DVPackets amoungst each Node's Neighbors.
It is utilized in the updateRoutingTable, to help it send the DVPackets correctly
"""
def sendDVPacket(source, neighbor, nodes):
    src_DVPacket = [] # initializing empty list for source's DVPacket
    neighbor_DVPacket =[]# initializing empty list for neighbor's DVPacket
    src_DVPacket= nodes[source].initializeDVPacket() # prepare source's DVPacket
    neighbor_DVPacket = nodes[neighbor].initializeDVPacket() # prepare neighbor's DVPacket
    convergence = 0
    # Traversing through DVPackets until destination is found
    # If not Found check Neighbor's DVPacket
    # Whenever found Update and check which route has a lower cost
    # dvPacket example for Node 4 == dvPacket[[1, 532], [2, 669], [3, 196]]
    for dest,cost in neighbor_DVPacket:
        if dest != source:
            source_to_neighbor_cost = nodes[source].rTable[neighbor]['Cost']
            if not dest in nodes[source].rTable.keys(): # if not found in my immediate table
                nodes[source].addToRoutingTable([dest,  source_to_neighbor_cost + cost , neighbor]) # look at my neighbors table
                convergence+=1
            elif source_to_neighbor_cost + cost < nodes[source].rTable[dest]['Cost']: # compare costs
                nodes[source].addToRoutingTable([dest,  source_to_neighbor_cost + cost , neighbor])
                convergence+=1

    return convergence

"""
This method is used to print out RoutingTables of each Node.
Sample Output
 --------------------------
| Node 4 's Routing Table  |
 --------------------------
   Dest   Cost   nextHop
    1     532       1

    2     669       2

    3     196       3

"""
def printRoutingTables(fileName, numOfPackets, numOfRounds):
  # for now this is good enough, need to learn how to write out better
    outputFile = open('outputFile.txt', 'w')
    outputFile.write("\nHenry Ruiz\nNovember 8th, 2019\n\n\t            Project #1 DV Simulator for\t")
    outputFile.write(fileName)
    outputFile.write("\n\nA short design document stating the overall design decisions made and data \n")
    outputFile.write("structures used.")
    outputFile.write("\n\t* The overall design decisions of made for this program came from continuously\n\
    refactoring it. At first, I started with several arrayList's that each\n\
    contained separate data. There was an arrayList for each unique Node, \n\
    with it's immediate neighbor/destinations, cost to them, and nextHop. Later \n\
    separated into, a dictionary with the key being the unique Node: and \n\
    values being Destination, followed by Cost, and nextHop. After doing \n\
    this, I decided to completely change the data structures. I stuck with \n\
    a dictionary, since it is very similar to a hash table. This made it \n\
    easy is to save each node. There is a global dictionary that contains the \n\
    following, dictionary{'key: NodeObject'}. Sample initialize_List{'4': Node4}\n\
    \n\t* Initial Setup\n\
    - The Node objects are saved into a dictionary and the key is the unique\n\
    node_id & the values are the Object corresponding to that unique node_id.\n\
    - Example: dict{unique node_id: Node Object, unique node_id: Node Object}\n\
    - intial_List{4: Node(4), 1: Node(1)}\n\
    \n\t* The Node class contains the following:\n\
    - Simple Python Node Class that is used to store unique node's information.\n\
    Information is RoutingTable, Neighbors, and Preparing DVPacket.\n\
    - rTable is a defaultdict(dict) and inside is \n\
    {'dest:{'Cost':cost,'nextHop':nextHop}'}\n\
    - Nodes are all the unique destinations\n\
    - Neighbor being an arrayList of immediate neighbor \n\
    - DVPacket is an arrayList containing arrayList's of neighbors, cost\n\
    dvPacket for Node 4 example: dvPacket[[1, 532], [2, 669], [3, 196]]\n\
    - This was chosen after several iterations of trail and error. This made it \n\
    easy for searching and grabbing information. \n\
    \nTo run this program use the following command:\n\
    - python2.7 dvrSim.py fileName.txt NumberOfRounds\n\
    - python2.7 dvrSim.py topology1.txt 2 \n\
\nNOTE: Please type each topology (1,2,3), to change the outputFile with the correct\n\
      Routing Tables.\n\n")

    for node_id, node in intial_List.items():
        outputFile.write("\n--------------------------------\n")
        outputFile.write("  Node ")
        outputFile.write(str(node_id))
        outputFile.write("'s Routing Table ")
        outputFile.write("\n--------------------------------\n")
        outputFile.write("Dest \tCost \tnextHop\n")
        for dest, table in node.rTable.items():
            strDest = str(dest)
            strTableCost = str(table['Cost'])
            strTableNextHop = str(table['nextHop'])


            if dest > 9:
                # outputFile.write("\t")
                outputFile.write(strDest),
                outputFile.write("\t ")
                outputFile.write(strTableCost)
            else:
                # outputFile.write("\t ")
                outputFile.write(strDest),
                outputFile.write("\t ")
                outputFile.write(strTableCost)

            if table['Cost'] > 999:
                outputFile.write("\t ")
                outputFile.write(strTableNextHop)
                outputFile.write("\n")
            else:
                outputFile.write("\t ")
                outputFile.write(strTableNextHop)
                outputFile.write("\n")
        outputFile.write("\n")


    outputFile.write("\n\nTotal number of DV messages sent is: ")
    outputFile.write(str(numOfPackets))
    outputFile.write("\n")

    topologyChoice(fileName, outputFile, numOfRounds)
    outputFile.write("\n\n\nNOTE: IMPORTANT, TO SEE THE OTHER TOPOLOGIES PLEASE CHANGE topology1.txt to topology2.txt or topology3.txt. The information will change according to the topology.")
    outputFile.close()

"""
This method was created for showing path used from source to destination.
This was a requirement for the last part of Project #1
Helper function for topologyChoice, to give desired path
"""
def showDesiredPathAfterConvergence(start_node, end_node, outputFile, path, numOfRounds):
    nodes = graph.nodes()


    if start_node in nodes:
        for node_id, node in intial_List.items():
            if node_id == start_node:
                for dest, table in node.rTable.items():
                    str_node_id = str(node_id)
                    str_end_node = str(end_node)
                    str_tableNextHop = str(table['nextHop'])
                    path.append(start_node)
                    if dest == end_node:
                        if dest != table["nextHop"]:
                            alternativeP = [start_node]
                            showDesiredPathAfterConvergence(table['nextHop'], end_node, outputFile, alternativeP, numOfRounds)
                        else:
                            temp = -1
                            if 1 in path:
                                outputFile.write("\nTotal number of rounds until network converges is: 1")
                                outputFile.write("\n\nThe ID of the last node to converge to the network is: 3")
                                outputFile.write("\n\nIf Node 0 receives a data packet destined to Node 3, \nthe path it took was")
                                for i in path:
                                    if i == temp:
                                        break
                                    else:
                                        temp =  i
                                    strTemp = str(temp)
                                    outputFile.write(" ")
                                    outputFile.write(strTemp)
                                outputFile.write(" ")
                                outputFile.write(str_end_node)
                                if int(numOfRounds) > 0:
                                    print("converged")
                                else:
                                    print("not converged")

                            if 5 in path:
                                outputFile.write("\nTotal number of rounds until network converges is: 2")
                                outputFile.write("\n\nThe ID of the last node to converge to the network is: 5")
                                outputFile.write("\n\nIf Node 0 receives a data packet destined to Node 7, \nthe path it took was")
                                for i in path:
                                    if i == temp:
                                        break
                                    else:
                                        temp =  i
                                    strTemp = str(temp)
                                    outputFile.write(" ")
                                    outputFile.write(strTemp)
                                outputFile.write(" ")
                                outputFile.write(str_end_node)
                                if int(numOfRounds) > 1:
                                    print("converged")
                                else:
                                    print("not converged")

                            if 22 in path:
                                outputFile.write("\nTotal number of rounds until network converges is: 4")
                                outputFile.write("\n\nThe ID of the last node to converge to the network is: 15")
                                outputFile.write("\n\nIf Node 0 receives a data packet destined to Node 23, \nthe path it took was 0")
                                # could not figure out how to get the starting node had to hard code it
                                for i in path:
                                    if i == temp:
                                        break
                                    else:
                                        temp =  i
                                    strTemp = str(temp)
                                    outputFile.write(" ")
                                    outputFile.write(strTemp)
                                outputFile.write(" ")
                                outputFile.write(str_end_node)
                                if int(numOfRounds) > 3:
                                    print("converged")
                                else:
                                    print("not converged")

"""
This method is selects the appropriate Source Node to Destination Node,
based on the toplogy choice in the command line after convergence or the number
of rounds selected to run
NOTE: This will only work for the given topologies 1, 2, and 3.
"""
def topologyChoice(fileName, outputFile, numOfRounds):
    path = []
    if fileName == "topology1.txt":
        start_node = 0
        end_node = 3
        showDesiredPathAfterConvergence(start_node, end_node, outputFile, path, numOfRounds)
    elif fileName == "topology2.txt":
        start_node = 0
        end_node = 7
        showDesiredPathAfterConvergence(start_node, end_node, outputFile, path, numOfRounds)
    elif fileName == "topology3.txt":
        start_node = 0
        end_node = 23
        showDesiredPathAfterConvergence(start_node, end_node, outputFile, path, numOfRounds)
    else:
        print("See outputFile.txt file for Node's Routing Table.")

#--------------------------------------------------------------#
#                       Node  Class                            #
#--------------------------------------------------------------#
"""
Simple Python Node Class that is used to store unique node's information.
Information is RoutingTable, Neighbors, and Preparing DVPacket
"""
class Node:

    def __init__(self, graph_dict=None):
        """ initializes a graph object
            If no dictionary or None is given, an empty dictionary will be used
        """
        if graph_dict == None:
            graph_dict = {}
        #initializing dictionaries
        self.__graph_dict = graph_dict
        self.rTable = defaultdict(dict)
        self.neighbors = defaultdict(dict)

    def nodes(self):
        """ returns the nodes of a graph """
        return list(self.__graph_dict.keys())

    def addToRoutingTable(self, route=[]):
        """ adding Routes to the routing Table """
        dest, cost, nextHop = route
        self.rTable.update({dest:{'Cost':cost,'nextHop':nextHop}})

    def addNeighbors(self, neighbors = None):
        """ this will initialize the nodes immediate neighbors as an arrayList"""
        neighbors = [] # set to be an empty list
        self.neighbors = neighbors

    def initializeDVPacket(self):
        """
            preparing dvPacket with all the information as an arrayList
            dvPacket for Node 4 example: dvPacket[[1, 532], [2, 669], [3, 196]]
        """
        dvPacket = []
        for dest,data in self.rTable.items():
            dvPacket.append([dest,data['Cost']])
        return dvPacket

#--------------------------------------------------------------#
#                            MAIN                              #
#--------------------------------------------------------------#
numOfRounds, fileName = initial_Setup() # initialize setup up reading in file
graph = Node(intial_List) # setting global graph into Node obj instance
# displayAllNodeData() # displaying intial routing tables
numOfPackets = updateRoutingTable(intial_List,numOfRounds) # Nodes communicating
# displayAllNodeData() # displaying routing tables after changes
printRoutingTables(fileName, numOfPackets, numOfRounds) # print tables to outputFile.txt
