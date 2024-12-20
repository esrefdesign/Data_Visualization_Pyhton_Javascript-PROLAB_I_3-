class Wanted:
    def __init__(self, authors, essays):
        self.authors = authors
        self.essays = essays

    def wanted_5(self,name):
        result=0
        for essay in self.authors[name].essay:
            result += len(essay.coauthors)
        return result

        