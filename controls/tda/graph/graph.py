import os.path
import os
class Graph():   #clase padre
    @property
    def num_vertex(self):
        raise NotImplementedError("Subclass must implement abstract method")
    
    @property
    def num_edges(self):
        raise NotImplementedError("Subclass must implement abstract method")
    
    def exist_edges(self, v1, v2):
        raise NotImplementedError("Subclass must implement abstract method")
    
    def weight_edges(self, v1, v2):
        raise NotImplementedError("Subclass must implement abstract method")
    
    def insert_edges(self, v1, v2):
        raise NotImplementedError("Subclass must implement abstract method")
    
    def insert_edges_weight(self, v1, v2, weight):
        raise NotImplementedError("Subclass must implement abstract method")
    
    def adjacent(self, v1):
        raise NotImplementedError("Subclass must implement abstract method")
    
    def __str__(self) -> str:
        out = ""
        for i in range(0, self.num_vertex):
            out += 'V'+ str(i+1) +'\n'
            adjs = self.adjacent(i)
            if not adjs.isEmpty:
                for j in range(0, adjs._length):
                    adj = adjs.get(j)
                    out += 'adj '+"V" + str(adj._destination+1) +' weight '+ str(adj._weight) +'\n'
        return out
    
    def paint_graph(self):
        url = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))+"/static/d3/grafoDato.js" #cambiar grafoDato a grafo.js
        js = 'var nodes = new vis.DataSet(['
        #vertices
        for i in range(0, self.num_vertex):
            letter = chr(65+i)
            js += '{id: '+str(i+1)+', label: "'+str(i+1)+'"},'+'\n'   #cambiar leter por str(i+1)
        js += ']);'
        js += '\n'
        
        js += 'var edges = new vis.DataSet([\n'
        #edges
        for i in range(0, self.num_vertex):
            init = str(i+1)
            adjs = self.adjacent(i)
            if not adjs.isEmpty:
                for j in range(0, adjs._length):
                    adj = adjs.get(j)
                    #print(adj._destination)
                    des = str(adj._destination + 1)
                    js += '{from: '+init+', to: '+des+', label: "'+str(adj._weight)+'"},'+'\n'
        js += ']);'
        js += '\n'
        js += 'var container = document.getElementById("mynetwork");\n\t\tvar data = {\n\t\t\tnodes: nodes,\n\t\t\tedges: edges,\n\t\t};\n\t\tvar options = {};\n\t\tvar network = new vis.Network(container, data, options);'
        a = open(url, "w")
        a.write(js)
        a.close()
        print(url)  


