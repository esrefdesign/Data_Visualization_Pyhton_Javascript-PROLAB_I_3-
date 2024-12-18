
class Author:
    def __init__(self,orcid,name):
        self.name=name
        self.orcid = orcid
        self.essay=set()
    
        self.collaborations = {}  # İşbirlikçi yazarlar ve ağırlıklar

    def add_collaboration(self, coauthor, weight=1):
        """İşbirlikçi yazar ve ağırlığı ekle."""
        if coauthor in self.collaborations:
            self.collaborations[coauthor] += weight
        else:
            self.collaborations[coauthor] = weight
    