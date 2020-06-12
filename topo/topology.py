import networkx as nx

class Topology:
    def __init__(self):
        self.__links = None
        self.__switches = None
        self.__G = None

    def set_switches(self,switches):
        self.__switches = switches

    def set_links(self,links):
        self.__links = links        

    def get_switches(self):
        return self.__switches

    def get_links(self):
        return self.__links

    def __generate_graph(self):
        self.__G = nx.Graph()
        if self.__links is None or self.__switches is None:
            raise Exception("Topology has not been discovered yet!")

        self.__G.add_nodes_from(self.__switches) #self.__G.add_nodes_from([1,2,3])
        self.__G.add_edges_from(self.__links)#self.__G.add_edge([(1, 2), (3, 2)])
    
    def calculate_shortest_path(self,src_node,dst_node):
        self.__generate_graph()
        return nx.shortest_path(self.__G,src_node,dst_node)

    
    def get_graph(self):
        return self.__G

        

