class Author:
    def __init__(self,Id,name,next=None):
        self.name=name
        self.next=next
        self.Id = Id

    def __str__(self):
        return str(self.name)
    
    def getId(self):
        if self.Id is None:
            return 
        return self.Id
    
    def getName(self):
        if self.Id is None:
            return 
        return self.Id