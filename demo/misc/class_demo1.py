###����һ�����ࣻҲ��ֱ�Ӷ��庯��
class Student0(object):     
	pass

###����һ��������Ϊʵ������
def set_age(self, age):    
	self.age = age

from types import MethodType
s.set_age = MethodType(set_age, s, Student)   		### ��ʵ���󶨷���
Student.set_age = MethodType(set_age, s, Student) 	### ����󶨷���

class Student1(object):             
	__slots__ = ("name", "age")     ###������ֻ��ָ�������ԣ�ֻ�Ե�ǰ������Ч���Լ̳�����������


class Student2(object):
    """
    �����һ������������Ե��á�
    s.score ��ȡ����ֵ
    """
    @property 					
    def score(self):
        return "bbb"
    
    """
    �����ʼ���༴��ֱ�ӵ��� Student.read()
    """
    @staticmethod
    def read(self):
        return "aaaa"
        
    """
    ʹ��
    s=Student.my_init()
    s.score
    """
    @classmethod
    def my_init(cls,*args,**kwargs):
        #�൱�ڵ��ù��캯��
        return cls(*args,**kwargs)

