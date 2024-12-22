class Wanted:
    def __init__(self,graph, authors, essays):
        self.authors = authors
        self.essays = essays    
        self.graph = graph

    def wanted_5(self,name):
        """
        Verilen bir yazarın bağlantı sayısını ve bağlantılı yazarları döndürür.
        """
        if name in self.graph.adj_list:
            connection_count = self.graph.node_degrees[name]
            return connection_count
            
        else:
            return {"error": f"{name} isimli yazar bulunamadı."}

        