#Vertex class
class Vertex:
    def __init__(self, key):
        self.id = key
        self.connected_to = {}
    #Add neighbors    
    def add_neighbor(self, nbr, weight=0):
        self.connected_to[nbr] = weight
     
    #return all keys in connected to dict    
    def get_connections(self):
        self.connected_to.keys()
    
    #Return id    
    def get_id(self):
        return self.id
      
    #Return weight   
    def get_weight(self, nbr):
        return self.connected_to[nbr]
        
    def __str__(self):
        return str(self.id) + ' connected to: ' + str([x.id for x in self.connected_to])
        
#Graph class, represented as an adjacency list
class Graph:
    
    def __init__(self):
        self.vert_list = {}
        self.num_vert = 0
        
    #Add vertex at index key
    def add_vertex(self, key):
        self.num_vert += 1
        new_vertex = Vertex(key)
        self.vert_list[key] = new_vertex
        return new_vertex
       
   #Return vertex at index n
    def get_vertex(self, n):
        #Looks through keys in vert_list
        if n in self.vert_list:
            return self.vert_list[n]
        else:
            return None
    
    #Add an edge between two vertices
    def add_edge(self, f, t, cost=0):
        #f = from vertex
        #t = to
        #cost = weight
        if f not in self.vert_list:
            nv = self.add_vertex(f)
        if t not in self.vert_list:
            nv = self.add_vertex(t)
            
        self.vert_list[f].add_neighbor(self.vert_list[t], cost)
        
    #Reutns all vertices
    def get_vertices(self):
        return self.vert_list.keys()
    
    #make an iterattable object
    def __iter__(self):
        return iter(self.vert_list.values())
    
    def __contains__(self, n):
        return n in self.vert_list

#Rivalry class
class Rivalry:
    def __init__(self, boy1, boy2):
        self.boy1 = boy1
        self.boy2 = boy2
        
    @staticmethod
    def fromList(le):
        if len(le) !=2:
            raise Exception('Invalid boy line entry')
        return Rivalry(le[0], le[1])
        
    def __str__(self):
        return "Rivalry(boy1: {}, boy2: {})".format(self.boy1, self.boy2)
        
    def __repr__(self):
        return self.__str__()
        
#Boy class
class Boy:
    def __init__(self, index, boy):
        self.index = index
        self.boy = boy
        
    @staticmethod
    def fromList(le):
        if len(le) !=2:
            raise Exception('Invalid boy')
        return Boy(le[0], le[1])
        
    def __str__(self):
        return "Rivalry(index: {}, boy: {})".format(self.index, self.boy)
        
    def __repr__(self):
        return self.__str__()

def make_graph(boys, rivalries):    
  #Add each boy as a vertex
    g = Graph()
    for i in range(len(boys)):
        g.add_vertex(boys[i])
    #Add each rivalry as an edge, using boy1 as a 'from' vertex and boy2 as a 'to' vertex    
    for i in range(len(rivalries)):
        boy1 = rivalries[i].boy1
        boy2 = rivalries[i].boy2
        g.add_edge(boy1, boy2)
        
    return g
        

def bfs(graph_to_search, start, end):
    queue = [[start]]
    visited = set()
    while queue:
        # Gets the first path in the queue
        path = queue.pop(0)

        # Gets the last node in the path
        vertex = path[-1]

        # Checks if we got to the end
        if vertex == end:
            return path
        # We check if the current node is already in the visited nodes set in order not to recheck it
        elif vertex not in visited:
            # enumerate all adjacent nodes, construct a new path and push it into the queue
            neighbors = vertex.connected_to
            #for current_neighbour in graph_to_search.get_vertex(vertex).get_connections():
            for current_neighbour in  neighbors:
                new_path = list(path)
                new_path.append(current_neighbour)
                queue.append(new_path)

            # Mark the vertex as visited
            visited.add(vertex)
    
#Checks each edge to see that it goes between a Babyface and Heel   
def edge_check(boys, rivalries, babyfaces, heels):
    valid_edges = False
    for rivalry in rivalries:
        if rivalry.boy1 in babyfaces:
            if rivalry.boy2 in heels:
            #then this connection is valid
                valid_edges = True
            else: 
                valid_edges = False
        elif rivalry.boy1 in heels:
            if rivalry.boy2 in babyfaces:
                valid_edges = True
            else: 
                valid_edges = False
    return valid_edges

#*****************************
#Get info from text file
lines = []
with open('boys.txt', 'r') as file:
    line = file.readline()
    while line:
        #Stick current line into new list
        cur_line = line.split()
        if len(cur_line) > 0:
            lines.append(cur_line)
        line = file.readline()

#Now that we have all the data, we can parse and format it
if len(lines[0]) != 1:
    raise Exception('invalid formatting for number of boys on line 1')
#first line
num_boys = int(lines[0][0]) 
# print("Number of boys:")
# print(num_boys)
boys = [boy[0] for boy in lines[1:(num_boys+1)]]

#From the number of rivalries to the end
#print("Rivalries:")
rivalries = lines[(2+num_boys):]
# print(rivalries)

# print("Boys")
# print(boys)
    
#Make a list of Rivalry objects
#rivalries = [Rivalry.fromList(riv) for riv in rivalries]
 
#Test data    
#boys = ['Ace', 'Duke', 'Jax', 'Biggs', 'Stone']
rivalries = [['Ace', 'Duke'], ['Ace', 'Biggs'], ['Jax', 'Duke'], ['Stone', 'Biggs'], ['Stone', 'Duke'], ['Biggs', 'Jax']]

#print(rivalries)
rivalries = [Rivalry.fromList(riv) for riv in rivalries]

#Make the graph
g = make_graph(boys, rivalries)

#Get set of distances
babyfaces=[]
heels=[]
start = g.get_vertex(boys[0])
babyfaces.append(start.id)
#d = 0
for vertex in g:
    target = g.get_vertex(vertex.id)
    #Call bfs on this vertex to get its distance from Start
    if start!=target:
        #d +=1
        path = bfs(g, start, target)
        if path is not None:
            d = len(path)
        else:
            d = -1
        #print"Dist from %s to %s", (start.id, target.id)
        if d %2 == 0:
             babyfaces.append(vertex.id)
        else:
             heels.append(vertex.id)
#Check that edges go bewtween babyfaces and heels and not two of the same group    
valid_edges = edge_check(boys, rivalries, babyfaces, heels)
if valid_edges == True:
    print("This is valid!")
    print("babyfaces:")
    print(babyfaces)
    print("Heels")
    print(heels)
else:
    print("No, it is not possible to designate this list of boys as one or the other with the given rivalries")
    
        

