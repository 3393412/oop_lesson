import csv, os

class TableDB() :
    def __init__(self):
        self.table_database = []
        self.table = []
    def insert(self,table):
        __location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
        with open(os.path.join(__location__, table)) as f:
            rows = csv.DictReader(f)
            for r in rows:
                self.table_database.append(dict(r))
    def search(self, table_name):
        for city in self.table_database:
            if city['country'] == table_name:
                self.table.append(city['city'])
class Table() :
    def __init__(self, table_name, table):
        p = TableDB()
        p.insert(table)
        p.search(table_name)
        self.table = []
        self.all = p.table_database
        self.crr = None
    def filter(self, condition):
        self.table = []
        for item in self.all:
            if condition(item):
                self.table.append(item)
    def aggregate(self, aggregation_key, aggregation_function):
        aggregated_list = [float(i[aggregation_key]) for i in self.table]
        self.crr = (aggregation_function(aggregated_list))
    def __str__(self):
        return self.crr
a =Table('Italy',"Cities.csv")
a.filter(lambda i: i['country'] == 'Italy')
a.aggregate('temperature', lambda i: sum(i)/len(i))
print(a.__str__())
