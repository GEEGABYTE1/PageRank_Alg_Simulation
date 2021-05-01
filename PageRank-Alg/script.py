from fractions import Fraction 
from graph import Graph 
from vertex import Vertex

class Alg:
    
    def PageRank(self, lst):
        test = Graph(directed=True)
        lst_vertex = []
        count = 0
        for i in lst:
            temp_vertex = Vertex(i)
            lst_vertex.append(temp_vertex)
        
        for i in lst_vertex:
            test.add_vertex(i)
        
        for idx in range(len(lst_vertex)):
            if idx == 0:
                test.add_edge(lst_vertex[idx], lst_vertex[-1], Fraction(1,len(lst)))
            try:
                test.add_edge(lst_vertex[idx], lst_vertex[idx + 1], Fraction(1, len(lst)))
            except IndexError:
                test.add_edge(lst_vertex[-1], lst_vertex[0], Fraction(1, len(lst)))
        counter = 0
        for i in range(10):
            pass
                    
                









prompt1 = Alg()

prompt1.PageRank(['X', 'Y', 'Z'])