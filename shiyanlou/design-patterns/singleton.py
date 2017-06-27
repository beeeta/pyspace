"""
singleton
重点注意装饰器对类的重定义方法

"""

class Singleton(object):
    def __init__(self,cls):
        self._cls = cls
        
    def Instance(self):
        try:
            return self._instance
        except AttributeError:
            self._instance = self._cls()
            return self._instance
        
    def __call__(self):
        raise TypeError('singleton can not be call')
    
@Singleton
class Target(object):
    def targetMethod(self):
        print(id(self))
        
if __name__=='__main__':
    Target.Instance().targetMethod()
    Target.Instance().targetMethod()
    