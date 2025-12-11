class Graph:
    def __init__(self, no_of_vertices):
        self.mat = [[0] * no_of_vertices for row in range(no_of_vertices)]
        
    def add_edge(self, row, col):
        self.mat[row][col] = 1
        self.mat[col][row] = 1
    
    def display_graph(self):
        for row in self.mat:
            print(' '.join(map(str, row)))
            
class GraphUsingList:
    def __init__(self, no_of_vertices):
        self.mat = [[] * no_of_vertices for row in range(no_of_vertices)]

    def add_edge(self, i, j):
        self.mat[i].append(j)
        self.mat[j].append(i)
        
    def display_graph(self):
        for i in range(len(self.mat)):
            print(i, end=':-> ')
            for j in self.mat[i]:
                print(j, end='-> ')
            print(None)
    
graph = Graph(4)
# print(graph.mat)
# graph = GraphUsingList(4)

graph.add_edge(0, 1)
graph.add_edge(0, 2)
graph.add_edge(1, 2)
graph.add_edge(2, 3)

print('Adjacency Matrix Representation: ')

'''
    Adjacency Matrix: 
        0 1 1 0
        1 0 1 0
        1 1 0 1
        0 0 1 0
'''

# print('Adjacency List Representation: ')

'''
    Adjacency List Representation: 
            0:-> 1-> 2-> None
            1:-> 0-> 2-> None
            2:-> 0-> 1-> 3-> None
            3:-> 2-> None
'''
graph.display_graph()