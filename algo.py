import data2 as data

def node():
    return None
def p():
    return None

class Graph:
    def __init__(self, target_node):
        self.adj_list = {}
        self.target_node = target_node

    # adj_list = {101 : [102,103,104],102 : [103,104],103 : [104,106],104 : [102,103,105]}
    def create(self):

        # Pasting the target node's followers into adj_list
        copied_list = data.data1[self.target_node]["follower"].copy()
        self.adj_list[self.target_node] = copied_list

        # Looping through the list of followers in the target node and add only those nodes
        # in the adj_list which are there in the followers list of the target node
        for index in self.adj_list[self.target_node]:
            copied_list = data.data1[index]["follower"].copy()
            self.adj_list[index] = copied_list
        actual_connections = 0

        # Removing the unnecessary nodes from the adj_list
        for ID in self.adj_list:
            self.adj_list[ID] = list(set(self.adj_list[self.target_node]) & set(self.adj_list[ID]))
            actual_connections += len(self.adj_list[ID])

            # if the main node of the particular list exist in the list itself, then remove the id from that list
            if ID in self.adj_list[ID]:
                a = self.adj_list[ID]
                a.remove(ID)

        return self.adj_list

    def fraudulent_checker(self):
        # this will give the number of total ids
        ids = len(self.adj_list)

        # this will give the actual connections of the adjacency list
        connections = 0
        for ID in self.adj_list:
            connections += len(self.adj_list[ID])

        actual_connections = connections #- len(self.adj_list[self.target_node])

        # total possible connection that can connect in the graph
        length =len(data.data1[self.target_node]["follower"]) #  3
        total_possible = length*(length + 1)#5*4=9
        if total_possible ==0:
            cc=0
        else:
        # this will calculate the clustering coefficient of the graph
            cc = (actual_connections / total_possible) * 100

        # check if the cc > 50
        if not cc > 50:
            print(f"The Social Media ID {self.target_node} is not Fraudulent !! ")

        # if not, then calculate the relative following count of the graph
        # checking the number of total followers and relative follower count according to the age
        else:
            age = data.data1[self.target_node]["age"]
            ef =  ( 1 +(5 / age))**age

            # prints the effective followers and adjacency list of the followers
            print(ef)
            print(ids)

            # condition for the effective followers
            if ef < length:
                print(f"The Social Media ID {self.target_node} is Fraudulent !! ")
            else:
                print(f"The Social Media ID {self.target_node} is not Fraudulent !! ")

        # prints the clustering coefficient
        print(f"The cc is {cc}%")

