
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
        n: "num vertices",
        g: "graph",
        graph_name: "string",
        a: "python list of tuples (from, to, weight)",
        min_sum: 'list of size 1',  # Must compute always
        min_prod: 'list of size 1',  # Compute only if all weights > 0 and n <= LIMIT
        ws: 'List of all path weights used for computing min MST sum',
        wp: 'List of all path weights used for computing min MST product',
        show: 'bool'  # Must show SUM graph if show == True
    ):
        ## NOTHING CAN BE CHANGED BELOW
        self._n = n
        self._g = g
        self._graph_name = graph_name
        self._a = a  # Python list of tuples (from, to, weight)
        self._min_sum = min_sum
        self._min_prod = min_prod
        self._ws = ws  # Path used for MST sum weights
        self._wp = wp  # Path used for MST product weights
        self._show = show
        # DO NOT BUILD GRAPH or COMPUTE PRODUCT if self._n > self._MAX
        self._MAX = 100

        if (self._n <= self._MAX):
            self._build_graph(a)
        else:
            self._show = False

        if (self._show):
            input_graph_file = outputFileBase + self._graph_name + ".dot"
            self._g.write_dot(input_graph_file)  # You already have this routine
            print("graph is at:", input_graph_file)

        output_graph_file = outputFileBase + self._graph_name + "out.dot"
        if (self._n <= self._MAX):
            # You have the graph. Get all edges from the graph.
            edges = self._build_edge_data_struture_from_graph()
        else:
            # You never built the graph.
            edges = self._a

        # Compute min_sum always.
        # Compute min_product only if n <= LIMIT and all weights > 0.
        # Must output graph as a dot file if show == True.
        self._compute_min_sum_min_prod(edges, output_graph_file)

    def _build_graph(self, a:"python list of tuples (from, to, weight)"):
        nodes = set()
        for (f, t, w) in a:
            nodes.add(f)
            nodes.add(t)
        for i in nodes:
            if self._g._data_interface.find_by_name(str(i)) == -1:
                self._g._data_interface.insert(Data(str(i)))
        for (f, t, w) in a:
            self._g.add_edge(f, t, w)

    def _compute_min_sum_min_prod(self, edges: "python list of tuples (from, to, weight)", out_file: 'string'):
        # Helper functions for the Union-Find (Disjoint Set) structure.
        def find(parent, x):
            if parent[x] != x:
                parent[x] = find(parent, parent[x])
            return parent[x]

        def union(parent, rank, x, y):
            rx = find(parent, x)
            ry = find(parent, y)
            if rx != ry:
                if rank[rx] < rank[ry]:
                    parent[rx] = ry
                elif rank[rx] > rank[ry]:
                    parent[ry] = rx
                else:
                    parent[ry] = rx
                    rank[rx] += 1
                return True
            return False

        # Function to build MST using Kruskal's algorithm; returns the MST edges.
        def build_mst_sum(n, edgelist):
            edgelist_sorted = sorted(edgelist, key=lambda x: x[2])
            parent = [i for i in range(n)]
            rank = [0] * n
            mst_edges = []
            count = 0
            for (f, t, w) in edgelist_sorted:
                if union(parent, rank, f, t):
                    mst_edges.append((f, t, w))
                    count += 1
                    if count == n - 1:
                        break
            return mst_edges

        # 1) Compute the MST sum.
        mst_sum_edges = build_mst_sum(self._n, edges)
        self._ws.clear()  # Clear the list that stores MST weights.
        sum_val = 0
        for (f, t, w) in mst_sum_edges:
            sum_val += w
            self._ws.append(w)
        self._min_sum[0] = sum_val

        # 2) Compute the MST product only if all weights are positive and n <= _MAX.
        can_compute_product = True
        if self._n > self._MAX:
            can_compute_product = False
        else:
            for (f, t, w) in edges:
                if w <= 0:
                    can_compute_product = False
                    break

        if can_compute_product:
            mst_prod_edges = build_mst_sum(self._n, edges)
            self._wp.clear()
            prod_val = 1
            for (f, t, w) in mst_prod_edges:
                prod_val *= w
                self._wp.append(w)
            self._min_prod[0] = prod_val
        else:
            self._min_prod[0] = -1

        # 3) If self._show is True, output the MST (sum) graph to out_file.
        if self._show:
            # Retain only the MST edges in the graph.
            is_undirected = self._g.is_undirected_graph()
            mst_set = set()
            for (f, t, w) in mst_sum_edges:
                if is_undirected:
                    if f < t:
                        mst_set.add((f, t))
                    else:
                        mst_set.add((t, f))
                else:
                    mst_set.add((f, t))

            # Clean up the graph: remove edges not used in the MST from fanouts and fanins.
            all_nodes = self._g.list_of_nodes()
            for node in all_nodes:
                n = node.get_num()
                # Process fanout edges.
                fanout_edges = list(node.all_fanout_edges_of_a_node())
                for edge_obj in fanout_edges:
                    tnode = edge_obj.get_num()
                    if is_undirected:
                        pair = (n, tnode) if n < tnode else (tnode, n)
                        if pair not in mst_set:
                            node._fanouts.pop(tnode, None)
                    else:
                        if (n, tnode) not in mst_set:
                            node._fanouts.pop(tnode, None)
                # Process fanin edges.
                fanin_edges = list(node.all_fanin_edges_of_a_node())
                for edge_obj in fanin_edges:
                    tnode = edge_obj.get_num()
                    if is_undirected:
                        pair = (tnode, n) if tnode < n else (n, tnode)
                        if pair not in mst_set:
                            node._fanins.pop(tnode, None)
                    else:
                        if (tnode, n) not in mst_set:
                            node._fanins.pop(tnode, None)

            # Update the graph's edge count. For undirected graphs, _numE should equal the number of MST edges.
            self._g._numE = len(mst_sum_edges)
            self._g.write_dot(out_file)
            print("Output MST sum graph is at:", out_file)

    def _build_edge_data_struture_from_graph(self) -> "python list (from, to, weight)":
        # Build and return a list of edges from the graph's nodes.
        edges_list = []
        is_undirected = self._g.is_undirected_graph()
        visited = set()
        all_nodes = self._g.list_of_nodes()
        for node in all_nodes:
            n = node.get_num()
            fanouts = node.all_fanout_edges_of_a_node()
            for edge_obj in fanouts:
                t = edge_obj.get_num()
                w = edge_obj.get_weight()
                if is_undirected:
                    pair = (n, t) if n < t else (t, n)
                    if pair not in visited:
                        visited.add(pair)
                        edges_list.append((n, t, w))
                else:
                    edges_list.append((n, t, w))
        return edges_list


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
