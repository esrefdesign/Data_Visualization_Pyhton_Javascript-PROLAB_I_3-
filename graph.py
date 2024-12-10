class Graph:
    def __init__(self):
        self.adj_list = {}

    def add_node(self, author):
        if author not in self.adj_list:
            self.adj_list[author] = []

    def add_edge(self, author1, author2):
        if author2 not in self.adj_list[author1]:
            self.adj_list[author1].append(author2)
        if author1 not in self.adj_list[author2]:
            self.adj_list[author2].append(author1)