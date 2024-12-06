class Author:
    def __init__(self,name,next=None):
        self.name=name
        self.next=next

    def __str__(self):
        return str(self.name)