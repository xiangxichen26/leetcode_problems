
import sys # For getting Python Version
import os
import enum # For enum
import math  # for infinity
print("Version of Python I am using is", sys.version)


inputFileBase = "C:\\Users\\jag\\OneDrive\\vasu\\work\\algdata\\graphdata\\"
outputFileBase = "C:\\Users\\jag\\OneDrive\\vasu\\work\\py3\\objects\\graph\\notebook\\dot\\" 


def read_dot_file(f:'string')->'dot_graph':
    filename = outputFileBase + f + ".dot"
    print(filename)
    with open(filename) as f1:
        dot_graph = f1.read()
    print(dot_graph)
    return(dot_graph)

class Solution:
    def minCostConnectPoints(self, points:'list of ints') -> int:
        n = len(points)
        g = Graph(GraphType.WEIGHTED_UNDIRECTED)
        min_sum = [0]
        min_prod = [-1]
        ws = []
        wp = []
        a = []
        for i in range(n):
            for j in range(i + 1, n):
                weight = abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1])
                if (i < j):
                  a.append((i,j,weight))
        name = "leetcode"
        show = False
        GraphExam(n,g,name,a,min_sum,min_prod,ws,wp,show) 
        tsum = 0
        for e in ws:
          tsum = tsum + e
        assert(tsum == min_sum[0])
        if (min_prod[0] != -1):
            #make sure answer is right from sum
            tp = 1
            for e in ws:
              tp = tp * e
            assert(tp == min_prod[0])
            #make sure answer is right from prod
            p = 1
            for e in wp:
              p = p * e
            assert(p == min_prod[0])
        return min_sum[0]

############################################################
# Graph Exam
# REPLACE YOUR CODE HERE
###########################################################
############################################################
# Graph Exam
###########################################################
class GraphExam:
  def __init__(
        self,
        n:"num verices",
        g: "graph",
        graph_name: "string",
        a: "python list of tuples (from, to, weight)",
        min_sum:'list of size 1', #Must compute always
        min_prod:'list of size 1', #compute only if all weights > 0 and n <= LIMIT
        ws:'List of all path weights used for computing min MST sum',
        wp:'List of all path weights used for computing min MST product',
        show:'bool' #Must show SUM graph if show = true
    ):
    ## NOTHING CAN BE CHANGED BELOW
    self._n = n 
    self._g = g
    self._graph_name = graph_name
    self._a = a #python list of tuples (from, to, weight)
    self._min_sum = min_sum
    self._min_prod = min_prod
    self._ws = ws #path used for min sum weight 
    self._wp = wp #path used for min prod weight 
    self._show = show
    #DO NOT BUILD GRAPH or COMPUTE PRODUCT if self._n > self._MAX
    self._MAX = 100
   
    if (self._n <= self._MAX):
        self._build_graph(a)    
    else:
        self._show = False
        
    if (self._show):
      input_graph_file = outputFileBase + self._graph_name + ".dot"
      self._g.write_dot(input_graph_file) #You already have this routine
      print("graph is at:",input_graph_file)
        
    output_graph_file = outputFileBase + self._graph_name + "out.dot"
    if (self._n <= self._MAX):
        #you have the graph. Get all edges from the graph
        edges = self._build_edge_data_struture_from_graph()
    else:
        #You never built the graph
        edges = self._a
       
    #Compute min_sum always
    #compute min_product only if n <= LIMIT and w > 0
    #Must output graph as a dot file if only show=True
    self._compute_min_sum_min_prod(edges,output_graph_file)
 
  def _build_graph(self, a: "python list of tuples (from, to, weight)"):
    try:
        for i in range(self._n):
            d = Data(str(i))
            self._g._data_interface.insert(d)
        
        for (u, v, w) in a:
            if not isinstance(u, int) or not isinstance(v, int) or u < 0 or v < 0:
                print(f"Warning: Invalid node indices ({u},{v}), skipping edge")
                continue
            self._g.add_edge(u, v, w)
        
        print(f"Graph built with {len(a)} edges")
    except Exception as e:
        print(f"Error building graph: {e}")
        for i in range(self._n):
            if not self._g._data_interface.find_by_name(str(i)) >= 0:
                d = Data(str(i))
                self._g._data_interface.insert(d)

  def _compute_min_sum_min_prod(self, edges: "python list of tuples (from, to, weight)", out_file: 'string'):
    # if show is True, you must write dot file of output
    # DO NOT COMPUTE PRODUCT if self._n > self._MAX
    # DO NOT COMPUTE PRODUCT if weight <= 0
    # Test bench will fail if you dont follow
    class UnionFind:
        def __init__(self, n):
            self.parent = list(range(n))
            self.rank = [0] * n
            self.count = n  
        
        def find(self, x):
            if self.parent[x] != x:
                self.parent[x] = self.find(self.parent[x]) 
            return self.parent[x]
        
        def union(self, x, y):
            root_x = self.find(x)
            root_y = self.find(y)
            if root_x == root_y:
                return False
            
            if self.rank[root_x] < self.rank[root_y]:
                self.parent[root_x] = root_y
            elif self.rank[root_x] > self.rank[root_y]:
                self.parent[root_y] = root_x
            else:
                self.parent[root_y] = root_x
                self.rank[root_x] += 1
            
            self.count -= 1  
            return True
        
        def is_connected(self):
            return self.count == 1
    
    if not edges:
        print("Warning: Empty edge list, no MST to compute")
        self._min_sum[0] = 0
        self._min_prod[0] = -1
        self._ws.clear()
        self._wp.clear()
        return
    
    try:
        n = self._n
        max_node = max(max(edge[0], edge[1]) for edge in edges)
        if max_node >= n:
            print(f"Warning: Node index {max_node} exceeds expected count {n-1}, adjusting node count")
            n = max_node + 1
    except Exception as e:
        print(f"Error validating edges: {e}")
        n = self._n  
    
    try:
        sorted_edges_by_sum = sorted(edges, key=lambda edge: edge[2])
        
        uf = UnionFind(n)
        mst_sum_edges = [] 
        self._ws.clear()   
        
        for edge in sorted_edges_by_sum:
            u, v, w = edge
            if uf.find(u) != uf.find(v):  
                mst_sum_edges.append(edge)
                self._ws.append(w) 
                uf.union(u, v)
                
                if len(mst_sum_edges) == n - 1:
                    break
        
        min_sum = sum(self._ws)
        self._min_sum[0] = min_sum
    except Exception as e:
        print(f"Error computing minimum sum MST: {e}")
        self._min_sum[0] = 0
        self._ws.clear()
    
    all_positive = all(edge[2] > 0 for edge in edges)
    
    if self._n <= self._MAX and all_positive:
        try:
            self._wp.clear()
            for w in self._ws:
                self._wp.append(w)

            min_prod = 1
            for w in self._wp:
                min_prod *= w
                
            self._min_prod[0] = min_prod
        except Exception as e:
            print(f"Error computing minimum product MST: {e}")
            self._min_prod[0] = -1
            self._wp.clear()
    else:
        self._min_prod[0] = -1
        self._wp.clear()
    
    if self._show:
        try:
            output_graph = Graph(self._g.get_graph_type())
            
            for i in range(n):
                d = Data(str(i))
                output_graph._data_interface.insert(d)
                output_graph.build_node_and_to_graph(i)
            
            for edge in mst_sum_edges:
                u, v, w = edge
                output_graph.add_edge(u, v, w)
            
            try:
                output_graph.write_dot(out_file)
                print(f"MST output graph is at: {out_file}")
            except Exception as e:
                print(f"Error writing dot file: {e}")
        except Exception as e:
            print(f"Error creating output graph: {e}")

  def _build_edge_data_struture_from_graph(self) -> "python list (from, to, weight)":
    edges = []
    try:
        node_list = self._g.list_of_nodes()
        if not node_list:
            print("Warning: Graph has no nodes")
            return edges
            
        graphtype = self._g.get_graph_type()
        
        for node in node_list:
            u = node.get_num()
            for edge in node.all_fanout_edges_of_a_node():
                v = edge.get_other_node().get_num()
                w = edge.get_weight()
                
                if (graphtype == GraphType.UNDIRECTED or graphtype == GraphType.WEIGHTED_UNDIRECTED):
                    if u < v:
                        edges.append((u, v, w))
                else:
                    edges.append((u, v, w))
        
        print(f"Extracted {len(edges)} unique edges from graph")
    except Exception as e:
        print(f"Error extracting edges from graph: {e}")
    
    return edges


############################################################
# GraphDot.py
# Author: Jagadeesh Vasudevamurthy
# Copyright: Jagadeesh Vasudevamurthy 2024
###########################################################

############################################################
# YOU WRITE CODE IN THIS FILE
###########################################################

class GraphDot:
    def __init__(self, g, f):
        self._g = g  # Handle to graph
        self._f = f  # File where you write graph in dot format
        self._of = open(self._f, "w")
        self._write_dot()
        self._of.close()

    ############################################################
    # Write code: _write_dot
    # Use as many private functions and prvate data you want
    ###########################################################
    def _write_dot(self):
        self._of.write("## Jagadeesh Vasudevamurthy ####\n")
        self._of.write("digraph g {\n")
        t = self._g.get_graph_type()
        if t == GraphType.UNDIRECTED or t == GraphType.WEIGHTED_UNDIRECTED:
            self._of.write("\t edge [dir=none, color=red]")
        else:
            self._of.write("edge [color=red]")
        self._of.write("\n")
        nodelist = self._g.list_of_nodes()
        # Time complexity: THETA(V + E)
        for n in nodelist:
            p1 = n.get_num()
            rp1 = self._g.get_real_name(p1)
            fanouts_of_n_edges = n.all_fanout_edges_of_a_node()
            for nf in fanouts_of_n_edges:
                p2 = nf.get_num()
                rp2 = self._g.get_real_name(p2)
                w = nf.get_weight()
                s = ""
                if (
                    t == GraphType.WEIGHTED_UNDIRECTED
                    or t == GraphType.WEIGHTED_DIRECTED
                ):
                    if t == GraphType.WEIGHTED_DIRECTED or (p1 < p2):
                        s = s + "   " + rp1 + " -> " + rp2 + " [label = " + str(w) + "]"
                elif t == GraphType.DIRECTED or (p1 < p2):
                    s = s + "   " + rp1 + " -> " + rp2
                if s != "":
                    self._of.write("\t")
                    self._of.write(s)
                    self._of.write("\n")
        self._of.write("}")


class GraphType(enum.Enum): 
    NONE = 0
    UNDIRECTED = 1
    DIRECTED = 2
    WEIGHTED_UNDIRECTED = 3
    WEIGHTED_DIRECTED  = 4



###########################################################
# GraphInterface.py
# Author: Jagadeesh Vasudevamurthy
# Copyright: Jagadeesh Vasudevamurthy 2024
###########################################################

############################################################
# You can have any Data. 
# You must writethe routines below 
#   __init__
#   -get_key
#   __str__
#   get_real_name -- name for printing
#   __hash__
#   __lt__
###########################################################
class Data:
    def __init__(self, n: "string"):
        self._name = n  ### _name is used as key for this project
        self.age = 100  ## To show you can have anything,

    def _get_key(self) -> "string":
        return self._name

    def __str__(self) -> "string":
        return self._name

    def get_real_name(self) -> "string":
        return self._name

    #'''
    def __hash__(self)->'int':
        k = self._get_key()
        t = hash(k)
        return t
    #'''
    def __lt__(self, other: "Data") -> "bool":
      if not isinstance(other, type(self)):
            assert False
      n1 = self._get_key()
      n2 = other._get_key()
      return (n1 < n2)

    ############################################################
    # Do not change anything below
    ###########################################################
    
    #############################
    # Overload ==
    # (a == b) == !(a < b) && !(b < a)
    #############################
    def __eq__(self, b: "Data") -> "bool":
        return not (self < b) and not (b < self)
    
    #############################
    # Overload >
    # (a > b) = (b < a)
    #############################
    def __gt__(self, b: "Data") -> "bool":
        return b < self

    #############################
    # Overload <=
    # (a <= b) = !(b < a)
    #############################
    def __le__(self, b: "Data") -> "bool":
        return not (b < self)

    #############################
    # Overload >=
    # (a >= b) = !(a < b)
    #############################
    def __ge__(self, b: "Data") -> "bool":
        return not (self < b)

    #############################
    # Overload !=
    # (a != b) == !(a == b)
    #############################
    def __ne__(self, b: "Data") -> "bool":
        return not (self == b)
  
 ############################################################
# GraphInterface
###########################################################
class GraphInterface: 
  def __init__(self):
    self._index = 0
    self._dict = {} # Key is item UDT: Value is index (0 to n-1)
    self._list = [] # Given number between 0 to n-1 get Data in O(1) time

  def __len__(self)->'int':
    l =len(self._dict)
    assert(l == self._index)
    return l

  ############################################################
  # If Data d is already there get a unique number
  # If Data d is not there, return -1
  ###########################################################
  def find(self, d:'Data')->'int':
    ##calls DATA  def __hash__(self)->'int':
    ##if you don't write hash
    ## TypeError: unhashable type: 'Data'
    if (d in self._dict):
      n = self._dict.get(d) #Key is int  Value is the 'DATA'  THETA(1)
      assert(n >= 0 and n < self._index)
      return n
    return -1

  ############################################################
  # If Data d is already there get a unique number
  # If Data d is not there, return -1
  ###########################################################
  def find_by_name(self, s:'string')->'int':
    d = Data(s)
    if (d in self._dict):
      n = self._dict.get(d) #Key is int  Value is the 'data'  THETA(1)
      assert(n >= 0 and n < self._index)
      return n
    return -1

  ############################################################
  # If Data d is already there gives a unique number
  # If Data d is not there, stores the data in a dict and returns unique int
  ###########################################################
  def insert(self, d:'Data')->'int':
    n = self.find(d)
    if (n == -1):
      #Not in the dict. Add to dict and to list. Note everything is pointer 
      self._dict[d] = self._index #Key is int  Value is the d  THETA(1)
      self._list.append(d)
      n = self._index
      self._index = self._index + 1
    return n

  
  ############################################################
  # Given an unique int gives user data in THETA(1) time
  ###########################################################
  def __getitem__(self, n:'int')->'string':
    assert(n >= 0 and n < self._index)
    return self._list[n].get_real_name()
 
############################################################
# start up
###########################################################
if __name__ == "__main__":
   g = GraphInterface()



############################################################
# Graph.py
# Author: Jagadeesh Vasudevamurthy
# Copyright: Jagadeesh Vasudevamurthy 2024
###########################################################

############################################################
# NOTHING CAN BE CHANGED IN THIS FILE
###########################################################

############################################################
# All imports
###########################################################
import collections
import math  # for infinity


############################################################
# Edge
# Name less data structure
# node number is guaranteed to be int from 0 to n-1
###########################################################
class Edge:
    def __init__(self, n: "Node", weight: "float"):
        self._other_node = n  # _other node
        self._weight = weight  # _weight is float

    ############################################################
    # All Public routines. YOU SHOULD ONLY CALL THESE ROUTINES
    ###########################################################
    def get_other_node(self) ->'Node':
        return self._other_node

    def get_num(self) -> "int":
        return self.get_other_node().get_num()

    def get_weight(self) -> "float":
        return self._weight

    def change_weight(self, w: "float") -> "None":
        self._weight = w

############################################################
# Node
# Name less data structure
# node num is guaranteed to be int from 0 to n-1
###########################################################
class Node:
    def __init__(self, n: "int"):
        self._num = n 
        self._fanins = {}  # dict of fanins of Node. Key is edge other node num int, Value is Edge
        self._fanouts = {} # dict of fanouts of Node. Key is edge other node num int, Value is Edge

    #we must write hash function as we are inserting all nodes in a dictonary of graph
    # self._dict = {}  #all nodes are in a dictionary
    # n = Node(100)
    # self._add_node(n)

    def _get_key(self)->'int':
        return self._num

    def __hash__(self)->'int':
        k = self._get_key()
        t = hash(k)
        return t

    ############################################################
    # All Public routines. YOU SHOULD ONLY CALL THESE ROUTINES
    ###########################################################
    def get_num(self) -> "int":
        return self._num

    def add_fan_out(self, e: "Edge") -> "None":
        key = e.get_num()
        self._fanouts[key] = e  #key is int. Value is edge

    def add_fan_in(self, e: "Edge") -> "None":
        key = e.get_num()
        self._fanins[key] = e #key is int. Value is edge

    def num_fan_outs(self) -> "int":
        return len(self._fanouts)

    def num_fan_ins(self) -> "int":
        return len(self._fanins)

    def all_fanout_edges_of_a_node(self) -> "list of fanout edges":
        # l will have edge {othernode, weight}
        l = list(self._fanouts.values())
        return l

    def all_fanin_edges_of_a_node(self) -> "list of fanin edges":
        # l will have edge {othernode, weight}
        l = list(self._fanins.values())
        return l
 
    def node_has_fanout_edge(self, e: "Edge") -> "Edge or None":
        aedge = self._fanouts.get(e.get_num())  # key is int
        if aedge:
            return aedge
        else:
            return None

    def node_has_fanin_edge(self, e: "Edge") -> "Edge or None":
        aedge = self._fanins.get(e.get_num())  # key is int
        if aedge:
            return aedge
        else:
            return None

    #get from_node to_node weight
    #self is from_node
    def get_from_node_2_to_node_weight(self, tonode:"Node", must_be_there:'bool') ->'float':
      e = Edge(tonode,0) #create a dummy edge of {tonode,0}
      se = self.node_has_fanout_edge(e) #THETA(1)
      if (must_be_there):
        assert(se) #Stored edge must be there
        return se.get_weight()
      else:
        return math.inf

class Graph:
    def __init__(self,graphtype: "GraphType"):
        self._numE = 0  # Number of edges
        self._type = graphtype  # Graph type
        self._dict = {}  #all nodes are in a dictionary
        # node num is int from 0 to n-1. 
        # Value is the Node. 
        # calls the __hash__ of node
        self._data_interface = GraphInterface()
        
    ############################################################
    # All Public routines. YOU SHOULD ONLY CALL THESE ROUTINES
    ###########################################################
    def get_numV(self) -> "int":
        n = len(self._dict)
        return n

    def get_numE(self) -> "int":
        return self._numE

    def is_directed_graph(self) -> "bool":
        if self._type == GraphType.DIRECTED:
            return True
        if self._type == GraphType.WEIGHTED_DIRECTED:
            return True
        return False

    def is_undirected_graph(self) -> "bool":
        return not (self.is_directed_graph())

    def is_weighted_graph(self) -> "bool":
        if self._type == GraphType.WEIGHTED_UNDIRECTED:
            return True
        if self._type == GraphType.WEIGHTED_DIRECTED:
            return True
        return False

    def get_graph_type(self) -> "GraphType":
        return self._type

    def get_graph_type_as_string(self) -> "string":
        t = self.get_graph_type()
        if t == GraphType.UNDIRECTED:
            return "UNDIRECTED GRAPH"
        if t == GraphType.DIRECTED:
            return "DIRECTED GRAPH"
        if t == GraphType.WEIGHTED_UNDIRECTED:
            return "WEIGHTED_UNDIRECTED GRAPH"
        if t == GraphType.WEIGHTED_DIRECTED:
            return "WEIGHTED_DIRECTED GRAPH"
        return "NONE"

    def list_of_nodes(self) -> "list of nodes":
        # Key is int from 0 to n-1. 
        # Value is the Node. 
        l = list(self._dict.values()) # we get list of all nodes
        return l

    def build_node(self, num:'int') -> "Node":
        n = Node(num)
        return n
    
    def build_node_and_to_graph(self, num:'int') -> "Node":
        n = Node(num)
        #calls __hash__ of node
        self._add_node(n)

    def has_node(self,nodenum:'int') -> "bool":
        if nodenum in self._dict: #key is int
          return True
        return False

    def get_node(self,node:'Node')->'Node':
      if (self.has_node(node.get_num())):
        n = self._dict[node.get_num()]
        assert(n)
        return n
      return None

    def add_edge(self,f:'int', t:'int', w:'float'):
        f = Node(f)
        t = Node(t)
        self._add_edge(f,t,w)

    def get_real_name(self,i:'int')->'string':
        s = self._data_interface[i]
        return s

    def dump_as_list(self):
      n = self.get_numV()
      a = []
      for i in range(n):
        a.append([])
      all_nodes = self.list_of_nodes()
      for node in all_nodes:
        #print(a)
        n = node.get_num()
        f = node.num_fan_outs()
        if (f):
          fanouts_of_n_edges = node.all_fanout_edges_of_a_node()
          for nf in fanouts_of_n_edges:
            d = nf.get_num()
            w = nf.get_weight()
            l = [d,w]
            a[n].append(l)

      print("\tg = [")
      for alist in a:
            print("\t\t",alist,",")
      print("\t]")

    def dump(self, name):
        print("------------", name, "------------ ")
        print(self.get_graph_type())
        print("Num Vertices =", self.get_numV())
        print("Num Edges    =", self._numE)
        numedge = 0
        all_nodes = self.list_of_nodes()
        for node in all_nodes:
            #node._num = int 0 to n-1
            #node._fanouts = {}
            n = node.get_num()
            rn = self.get_real_name(n)
            print(rn, "Fanouts: ", end="")
            f = node.num_fan_outs()
            if f == 0:
                print("NONE")
            else:
                fanouts_of_n_edges = node.all_fanout_edges_of_a_node()
                j = 0
                for nf in fanouts_of_n_edges:
                    numedge = numedge + 1
                    fnum = nf.get_num()
                    rd = self.get_real_name(fnum)
                    if j < f - 1:
                        print(rd, ",", sep="", end="")
                    else:
                        print(rd)
                    j = j + 1
            print(rn, "Fanins : ", end="")
            f = node.num_fan_ins()
            if f == 0:
                print("NONE")
            else:
                fanins_of_n_edges = node.all_fanin_edges_of_a_node()
                j = 0
                for nf in fanins_of_n_edges:
                    numedge = numedge + 1
                    fnum = nf.get_num()
                    rd = self.get_real_name(fnum)
                    if j < f - 1:
                        print(rd, ",", sep="", end="")
                    else:
                        print(rd)
                    j = j + 1
        assert numedge/2 == self._numE

    ##########################################################
    # Nothing can be changed
    # TIME: THETA(V + E)
    # SPACE: THETA(V)
    ##########################################################
    def assert_dfs_passed(self, has_loop: "bool", dfs_order: "list of nodes"):
        t = self.get_graph_type()
        if (t == GraphType.UNDIRECTED) or (t == GraphType.WEIGHTED_UNDIRECTED):
            return
        if has_loop == False:
            set_of_visited_nodes = set()
            for n in dfs_order:
                ## Go on fanins of node
                fanins_of_n_edges = n.all_fanin_edges_of_a_node()
                for nfanin in fanins_of_n_edges:
                    nf = nfanin.get_other_node()
                    must_be_there = nf in set_of_visited_nodes  # find in THETA(1)
                    assert must_be_there
                set_of_visited_nodes.add(n)  # add in THETA(1)
            # All nodes must be visited
            assert len(set_of_visited_nodes) == self.get_numV()
            print("DFS ASSERT PASSED")

    ############################################################
    # All Private routines. YOU SHOULD NOT CALL THESE ROUTINES
    ###########################################################
    def _add_node(self, n:'Node')->"Node":
        storedn = self.get_node(n)
        if (storedn):
          return storedn
        key = n.get_num()
        n = Node(key) #build a node. This is NOT in graph
        self._dict[key] = n # Key is unique number int (0 to n-1) 
        return n

    def _add_an_edge(self,f:'Node', t:'Node', fanout:'bool', w:'float'):
        f = self._add_node(f)
        t = self._add_node(t)
        if (fanout):
          e = f.node_has_fanout_edge(t)
          if (e):
            ew = e.get_weight()
            if (w < ew):
              e.change_weight(w)
          else:
            #first time
            e = Edge(t, w)
            self._numE = self._numE + 1
            f.add_fan_out(e)
        else:
          e = f.node_has_fanin_edge(t)
          if (e):
            ew = e.get_weight()
            if (w < ew):
              e.change_weight(w)
          else:
            #first time
            e = Edge(t, w)
            f.add_fan_in(e)

    def _add_edge(self,f:'Node', t:'Node', w:'float'):
        self._add_an_edge(f,t,True,w) #fanout
        self._add_an_edge(t,f,False,w) #fanin
        if (self._type == GraphType.UNDIRECTED) or (self._type == GraphType.WEIGHTED_UNDIRECTED):
          self._add_an_edge(t,f,True,w) #fanout
          self._add_an_edge(f,t,False,w) #fanin

    ############################################################
    ## All the routines written by students
    ##########################################################
    def write_dot(self, f):
        b = GraphDot(self, f)
