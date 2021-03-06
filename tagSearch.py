#C:\Users\harni\Downloads\graph.gpickle
import networkx as nx
list_of_related_tags=[]
def find_related_tags(given_tag):
    #load the graph
    G=nx.read_gpickle("graph.gpickle")

    # get neighbors
    related=list(G.neighbors(given_tag))
    neigh_weighted=[]
    #get weights
    for ele in related:
      weight=G[given_tag][ele]['weight']
      neigh_weighted.append([ele,weight])
    # sort according to weights
    sorted_neigh=sorted(neigh_weighted,key=lambda x:x[1])
    #list_of_related_tags=[]

    # get the tag list
    for tag in sorted_neigh:
      list_of_related_tags.append(tag[0])
    # create a string that stores all tags in list

    result=" || ".join(list_of_related_tags)
    # return the string
    return result
def best_ten():
    ten_best=list_of_related_tags[:11]
    return ten_best





