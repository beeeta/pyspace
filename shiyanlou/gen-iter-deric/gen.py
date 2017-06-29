"""
关于创建可重复进入的迭代器

for a in A //调用类的__iter__()方法,而这个对象的结果本身又是一个生成器，就成为了一个可重复进入的生成器
"""

"""
不可重复进入的生成器
"""
class UnRepIter(object):
    def __init__(self,start,stop):
        self.start = start
        self.stop = stop
        
    def __iter__(self):
        return self
            
    def __next__(self):
        if self.stop > self.start:
            res = self.start
            self.start += 1
            return res
        else:
            raise StopIteration       


"""
可重复进入的生成器
"""
class RepIter(object):
    def __init__(self,start,stop):
        self.start = start
        self.stop = stop
        
    def __iter__(self):
        start = self.start
        while self.stop>start:
            yield start
            start += 1 
        
        
"""
可变值作为函数默认参数
"""
def defParam(a,temp=[]):
    temp.append(a)
    for i in range(5):
        temp.append(i)
    print(temp)
        

        
if __name__ == '__main__':
    unRepIter = UnRepIter(1,5)
    for i in unRepIter:
        print(i,end=' ')
    for i in unRepIter:
        print(i,end=' ')        
        
    print('\n===========================\n')
    
    repIter = RepIter(1,5)
    for i in repIter:
        print(i,end=' ')
    for i in repIter:
        print(i,end=' ')    
        
    print('\n===========================\n')
        
    defParam('yak')