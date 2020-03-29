import os
from abc import *




class Formater(metaclass = ABCMeta):
    def __init__(self):
        pass
    def set(self, *args, **kwargs):
        try :
            self.effective()
            self.generate()
        except e:
            print(e)
        pass
    
    def effective(self):



    @abstractmethod
    def generate(self):
        pass

    def to_json(self):
        pass
    

def main():
    
    table = TableFormat()
    table.set()
    table.generate()
    reuslt = table.to_json()

if __name__=="__main__":
    main()