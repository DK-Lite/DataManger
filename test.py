import json
from abc import *
from os import path

class FormatManager(metaclass = ABCMeta):
    data = None

    def __init__(self):
        pass
    # def __call__(self, *input, **kwargs):
    #     try:
    #         return self.recognize(*input, **kwargs)
    #     except:
    #         pass

    def load(self, path):
        with open(path) as json_file:
            self.data = json.load(json_file)
    
    def set_data(self, key="", value=""):
        self.data[key] = value

    def generate(self):
        success = True
        for key, value in self.data.items():
            try:
                self.validation(key, value)
            except ValueError:
                print("The value of the %s is not defined" % (key))
                success = False

        if success: pass

        print("Try again")
        
        
    def to_json(self):
        pass

    @abstractmethod
    def validation(self, key, value):
        pass

class TradeTable(FormatManager):
    
    func = dict()
    def __init__(self):
        super().__init__()

        self.func['ymd'] = lambda x: x == "" 
        self.func['value'] = lambda x: x == "" 
        self.func['area'] = lambda x: x == "" 

    def __default(self, x):
        return x == ""

    def validation(self, key, value):
        if self.func[key](value): raise ValueError
        pass
        #print("Incorrect data format, should be YYYY-MM-DD")

def main():
    abspath = path.dirname(path.abspath(__file__))
    dirpath = path.join(abspath, 'format')
    filepath = path.join(dirpath, 'trade_table.json')

    uformat = TradeTable()
    uformat.load(filepath)

    inputs = {
        'key':'ymd', 
        'value':'2019-01-01'
    }

    uformat.set_data(**inputs)

    uformat.generate()
    uformat.to_json()

if __name__=="__main__":
    main()
