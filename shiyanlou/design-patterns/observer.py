"""
observer
还可以使用abc做进一步的抽象和方法共用

注意property,pro.setter
操作的属性名与property装饰的属性名称不能相同，否则会陷入死循环


"""

class LasyBoy(object):
    __metaclass__ = abc.ABCMeta
    @abc.abstractmethod
    def wakeup(self):
        pass


class LazyBoyA(LasyBoy):
    def wakeup(self):
        print("Boy A is getting up")
        
class LazyBoyB(LasyBoy):
    def wakeup(self):
        print("Boy B is getting up")
        
class TiredMom(object):
    def __init__(self):
        self.children = []
        
    def bornChild(self,child):
        self.children.append(child)
        
    def abandChild(self,child):
        self.children.remove(child)
        
    def notify(self,msg):
        for i in self.children:
            i.wakeup()
        
    @property
    def message(self):
        return self._message
    
    @message.setter
    def message(self,msg):
        self._message = msg
        self.notify(msg)

if __name__ == '__main__':
    a = LazyBoyA()
    b = LazyBoyB()
    m = TiredMom()
    m.bornChild(a)
    m.bornChild(b)
    m.amessage = 'week up every !!'
    