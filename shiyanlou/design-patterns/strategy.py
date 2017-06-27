"""
strategy
利用继承和多态的理念

"""

import abc


class Student(object):
    __metaclass__ = abc.ABCMeta
    @abc.abstractmethod
    def doPicture(self):
        pass

class XiaoMing(Student):
    def doPicture(self):
        print('xiaoming picture a duck')
        
class XiaoHong(Student):
    def doPicture(self):
        print('xionghong picture a flower')
        
class Teacher(object):
    def __init__(self):
        self._students = []
    
    def addStudents(self,stu):
        self._students.append(stu)
        
    def giveMeHomework(self):
        for s in self._students:
            s.doPicture()
            
if __name__ == '__main__':
    teacher = Teacher()
    teacher.addStudents(XiaoHong())
    teacher.addStudents(XiaoMing())
    teacher.giveMeHomework()