class Essay:
    def __init__(self,ID,title,next=None):
        self.ID=ID
        self.title=title
        self.next=next

    def __str__(self):
        return str(self.name)
    
    def getId(self):
        if self.ID ==None:
            print("Error Code is 1 :The Id Couldn't Found")
            return
        print(self.ID)
    
    def getTitle(self):
        if self.title ==None:
            print("Error Code is 2 :The Title Couldn't Found")
            return
        return self.title
    
    