
def flipset(name=[15, 10, 5]):
    set = {0}
    for i in range(len(name)):
        print(name[i])
        set.add(name[i])
    set.remove(0)
    for i in range(len(set)):
        print(set.pop())
    return set
flipset()

class Fruit: 
    def __init__(self):
        self.type = "kiwi"

    def yell(self):
        print(self.type)
    
x = Fruit()
x.yell()

class Apple(Fruit):
    def __init__(self):
        Fruit.__init__(self)

y = Apple()
y.yell()

