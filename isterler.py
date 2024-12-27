from priorityQueue import PriorityQueue
from bstNode import BST
import os
class Wanted:
    def __init__(self,graph, authors, essays):
        self.authors = authors
        self.essays = essays    
        self.graph = graph

    def wanted_1(self, author_A, author_B):
        if author_A not in self.graph.adj_list or author_B not in self.graph.adj_list:
            return f"Author {author_A} or {author_B} not found in the graph."

        # Initialize the search
        visited = set()  # Set to track visited nodes
        queue = PriorityQueue()  # Priority queue to explore the shortest path
        distance_table = {author_A: 0}  # Distance to author_A is 0
        previous_node = {author_A: None}  # Keep track of the previous node to reconstruct the path
        queue.heappush((0, author_A))  # Start the search from author_A

        result = []
        result.append(f"Starting with author {author_A}.")

        while not queue.is_empty():
            current_distance, current_author = queue.heappop()

            # If the node is already visited, skip it
            if current_author in visited:
                continue

            # Mark the node as visited
            visited.add(current_author)

            # If we reached the destination author B, reconstruct the path
            if current_author == author_B:
                path = []
                while current_author is not None:
                    path.insert(0, current_author)
                    current_author = previous_node[current_author]
                return path

            # Explore the neighbors of the current author
            for neighbor in self.graph.adj_list.get(current_author, []):
                edge_weight = self.graph.get_edge_weight(current_author, neighbor)
                new_distance = current_distance + edge_weight

                # Update the distance table and enqueue the neighbor if necessary
                if neighbor not in visited and (neighbor not in distance_table or new_distance < distance_table[neighbor]):
                    distance_table[neighbor] = new_distance
                    previous_node[neighbor] = current_author
                    queue.heappush((new_distance, neighbor))  # Add the neighbor with the new distance to the queue


        return f"No path found between {author_A} and {author_B}."


    
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
   
    def get_bst(bst):
        # Örnek bir BST oluştur

        bst_dict = bst.to_dict()
        return 
    
    def wanted_3(self, author_name):
        if author_name not in self.graph.adj_list:
            return {"error": f"Author {author_name} not found in the graph."}

        # Initialize the priority queue and BST
        queue = PriorityQueue()
        bst = BST()

        # Add authors to the priority queue and BST
        for collaborator in self.graph.adj_list[author_name]:
            weight = self.graph.node_degrees[collaborator]
            queue.heappush((-weight, collaborator))  # Push with negative weight to prioritize higher weights
            bst.insert(collaborator)  # Insert collaborator into BST

        # Extract priority queue contents
        priority_queue_content = []
        while not queue.is_empty():
            _, collaborator = queue.heappop()
            priority_queue_content.append(collaborator)

        # Visualize the BST
        

        # Return the result as a dictionary
        result = {
            priority_queue_content: priority_queue_content,
        }

        return result
    def wanted_4(self, author_name):
        if author_name not in self.graph.adj_list:
            return f"Author {author_name} not found in the graph."

        # A yazarı ve işbirlikçi yazarlar
        visited = {author_name}
        queue = PriorityQueue()
        distance_table = {author_name: 0}  # A yazarına olan mesafe 0
        result = []
        result.append(f"Starting with author: {author_name}")

        # Kuyruğa A yazarını ekleyelim (heappush ile)
        queue.heappush((0, author_name))

        while not queue.is_empty():  # Kuyruk boşsa döngüyü sonlandır
            current_distance, current_author = queue.heappop()  # heappop kullanarak en öncelikli elemanı al

            # Yazarın işbirlikçilerini inceleyelim
            for neighbor in self.graph.adj_list.get(current_author, []):
                if neighbor not in visited:
                    visited.add(neighbor)
                    edge_weight = self.graph.get_edge_weight(current_author, neighbor)  # Get edge weight
                    new_distance = current_distance + edge_weight  # Add the edge weight
                    distance_table[neighbor] = new_distance
                    queue.heappush((new_distance, neighbor))  # Kuyruğa yeni mesafeyi ekleyelim
                    result.append(f"Distance to {neighbor} is {new_distance}")

            # Adım adım mesafeleri tabloya ekleyelim

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
        
    def wanted_7(self, author_name):
        if author_name not in self.graph.adj_list:
            return f"Author {author_name} not found in the graph."

        # Initialize the search
        visited = {author_name}  # Set to keep track of visited nodes
        queue = PriorityQueue()  # Priority queue to explore the longest path
        longest_path = [author_name]  # List to store the longest path
        max_length = 0  # Variable to store the maximum path length
        
        # Start the search from the given author
        queue.heappush((0, author_name, [author_name]))  # (distance, current_author, path)
        
        while not queue.is_empty():
            current_distance, current_author, current_path = queue.heappop()

            # Check if this path is the longest so far
            if len(current_path) > max_length:
                max_length = len(current_path)
                longest_path = current_path

            # Explore the neighbors of the current author
            for neighbor in self.graph.adj_list.get(current_author, []):
                if neighbor not in visited:
                    visited.add(neighbor)
                    edge_weight = self.graph.get_edge_weight(current_author, neighbor)
                    new_distance = current_distance + edge_weight  # Add the edge weight
                    new_path = current_path + [neighbor]
                    queue.heappush((new_distance, neighbor, new_path))  # Add new path to the queue

        return {
            "longest_path": longest_path,
        }