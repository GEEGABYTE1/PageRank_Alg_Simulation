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
        
        first_web_link = lst_vertex[0]
        second_web_link = lst_vertex[1]
        third_web_link = lst_vertex[-1]

        for i in lst_vertex:
            test.add_vertex(i)


        values = [first_web_link, second_web_link, third_web_link]
        test.add_edge(first_web_link, second_web_link)
        test.add_edge(first_web_link, third_web_link)
        test.add_edge(second_web_link, third_web_link)
        test.add_edge(third_web_link, first_web_link)
        percentages = [Fraction(1, 3), Fraction(1, 3), Fraction(1, 3)]
        values_dict = {key: value for key, value in zip(values, percentages)}
        base_percentages = percentages
        j_changer = 0
        for i in range(10):

            if j_changer % 3 == 0:
                j_changer = 0
            
            if j_changer == 0:
                values_dict[values[0]] = values_dict[values[-1]]
                base_percentages[0] = base_percentages[-1]
            elif j_changer == 1:
                y = Fraction(1, 2) * base_percentages[-2]
                values_dict[values[-2]] = y 
                base_percentages[-2] = y
            else:
                #first_half = base_percentages[0] / 2
                second_half = base_percentages[-2]
                values_dict[values[-1]] = second_half * 2
                base_percentages[-1] = values_dict[values[-1]]

    
            j_changer += 1

        
        for i, j in values_dict.items():
            j_numerator = j.numerator 
            j_denominator = j.denominator
            ratio = j_numerator / j_denominator
            percentage = ratio * 100 
            percentage = int(percentage)
            values_dict[i] = percentage 

        for i, j in values_dict.items():
            print("Site {vertex} has a percent share of: {percentage}%".format(vertex=i.value, percentage=j))




            
                


        









prompt1 = Alg()

prompt1.PageRank(['X', 'Y', 'Z'])