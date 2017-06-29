"""
关于状态保持的几种方法：
闭包；类的属性；生成器局部变量；可变对象作为默认参数
"""

"""
生成器的状态保持
"""
def genLocal():
    local =0
    index = 0
    while index<5:
        print(local)
        yield index
        local += 1
        index += 1
        
        
"""
闭包的状态保持
"""
def closePack():
    local = 0
    def subFunc():
        nonlocal local
        print(local)
        local += 1
    return subFunc
        
"""
默认参数只初始化一次
"""
def defparams(a,temp={}):
    for i in range(5):
        temp['a%d' % i] = a+str(i)
    print(temp)
    
    
    
    