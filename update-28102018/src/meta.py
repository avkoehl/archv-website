## CREATE links file.abc and representatives file
import json

## OBJECTS: input cluster file and adjacency list 
o = open ("../data/intercluster-links.abc", "w")
o2 = open ("../data/representatives.tsv", "w")
x = open ("../data/clusters.tsv", "r")
y = open ("../data/adjacency-list.csv", "r")
clusters_list = []
adjacency_list = []

## FUNCTIONS: 

# get all node ids that match a single input node
def getmatches(node):
    matches = [] #output a list of the matches, without the weights

    for i in range (0, len(adjacency_list)): #search through the adjacency list for the corresponding row
        parts = adjacency_list[i].split(',')[0]
        seed = parts
        allm = []
        if seed == node:
            allm = adjacency_list[i].split(',')[2:]

        for m in allm:
            match = m.split(' ')[0]
            matches.append(match)

    return matches 

# given an input node, return the cluster that contains it
def getcluster(node):
    idx = 0
    for cluster in clusters_list:
        if node in cluster:
            return idx
        idx = idx + 1
    return -1

# given a node, find all of its matches and the clusters that they belong to
def getmatchescluster (node):

    matchescluster = []

    # get all the node ids that it has matched with
    matches = getmatches(node)

    # for each match, find the cluster it belongs to
    for match in matches:
        matchescluster.append (getcluster(match))

    return matchescluster


## MAIN 

# read in the files into adjacency_list and clusters_list
for line in y:
    adjacency_list.append(line.rstrip())
y.close()

for line in x:
    clusters_list.append(line.rstrip())
x.close()

# for each cluster, print out clusters that contain the nodes that nodes in that cluster match with 
nodes = [] 
links = []
for i in range(0, len(clusters_list)):
    print ("processing cluster: ", i)

    node = {}
    link = {} 

    TARGETS = []

    elements = clusters_list[i].split('\t')
    allmatches = []

    max_num_for_cluster = 0
    representative = ""
    for elem in elements:
        icm_num = 0
        matches = getmatchescluster(elem)
        for match in matches:
            if match == i:
                icm_num = icm_num + 1
            allmatches.append(match)
        if icm_num > max_num_for_cluster:
            max_num_for_cluster = icm_num
            representative = elem

    for match in allmatches:
        if match != i:
            TARGETS.append(match)


    targets = set(TARGETS)

    if (targets):
        for t in set(targets):
            link["source"] = i
            link["target"] = t
            link["weight"] = TARGETS.count(t) 
            if link["weight"] > 1:
                links.append(link.copy())

    node["name"] = i
    node["id"] = i
    node["value"] = len(elements)
    node["representative"] = representative
    nodes.append(node.copy())

for node in nodes:
    print (node["name"], node["representative"], file = o2)
for link in links:
    print (link["source"], link["target"], link["weight"], file=o)
