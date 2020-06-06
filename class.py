class hun:
    too = 0   # class-in objectuud dundaa heregledeg
    def __init__(self, ner:str, nas:int):   # ehnii parametr urgelj 'self', __init__ - utga uguh
       self.ner = ner   # gishuun ugugduld utga onooh
       self.nas = nas   # gishuun ugugduld utga onooh
       hun.too = hun.too + 1
    def hi(self):
        print('snu', self.ner, self.nas)

hun1 = hun("John", 36)
hun2 = hun("Donald", 32)
print(hun1.too)
print(hun2.ner, hun1.nas)
hun1.hi()
hun2.hi()