class Student(object):     ###����һ�����ࣻҲ��ֱ�Ӷ��庯��
	pass
	
def set_age(self, age):    ###����һ��������Ϊʵ������
	self.age = age
from types import MethodType
s.set_age = MethodType(set_age, s, Student)   		### ��ʵ���󶨷���
Student.set_age = MethodType(set_age, s, Student) 	### ����󶨷���

class Student(object):             
	__slots__ = ("name", "age")     ###������ֻ��ָ�������ԣ�ֻ�Ե�ǰ������Ч���Լ̳�����������

class Student(object):

    @property 					### @propertyװ�������Ǹ����һ������������Ե��á�����ʹ��s.score=70���ú����Լ���ȡ����ֵ
    def score(self):
        return self._score