from priorityQueue import PriorityQueue

class Wanted:
    def __init__(self,graph, authors, essays):
        self.authors = authors
        self.essays = essays    
        self.graph = graph

    def wanted_2(self,name):
        if name not in self.graph.adj_list:
            return f"Author {name} not found in the graph."

        # İşbirliği yapılan yazarlar
        collaborations = self.graph.adj_list[name]

        # Öncelik kuyruğu oluşturuluyor
        priority_queue = PriorityQueue()
        result = []
        result.append("Starting with empty queue.")

        # Kuyruğa ekleme işlemleri
        for collaborator in collaborations:
            weight = self.graph.node_degrees[collaborator]
            priority_queue.heappush((-weight, collaborator))  # Negatif ağırlık ile ekleme
            result.append(f"Added {collaborator} with weight {weight} to the queue.")

        # Kuyruktan çıkarma işlemleri
        result.append("\nRemoving elements from the queue:\n")
        while not priority_queue.is_empty():
            weight, collaborator = priority_queue.heappop()
            result.append(f"Removed {collaborator} with weight {-weight} from the queue.")
            
        return result


    def wanted_5(self,name):
        """
        Verilen bir yazarın bağlantı sayısını ve bağlantılı yazarları döndürür.
        """
        if name in self.graph.adj_list:
            connection_count = self.graph.node_degrees[name]
            return connection_count
            
        else:
            return {"error": f"{name} isimli yazar bulunamadı."}

    def wanted_6(self):
        most_collaborative = max(self.graph.adj_list.items(), key=lambda x: len(x[1]))
        return {"name": most_collaborative[0], "count": len(most_collaborative[1])}
        