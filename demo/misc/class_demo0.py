
'''
zabbix_api
������ workdir
��   ������ get_zabbbix_value.py
��	������ __init__.py
��   ������ yyy.py					# import  get_zabbbix_value
������  xxx.py        				# impoer workdir.get_zabbbix_value
'''


#�̳�
class Mammal(Object):
	pass

class Dog(Mammal):				 #���̳�
    pass
	
class Dog(Mammal, Runnable):     #���ؼ̳�
    pass


#������

class Student(object):
	def __init__(self, name):		 #����Դ��������г�ʼ��	
		self.name = name
	def __str__(self):				 #����ʹ��print(Student("name"))
		return 'Student object (name: %s)' % self.name	
	__repr__ = __str__               
	
#ֱ����ʾ�������õĲ���__str__()������__repr__()	
#__str__()   ###�����û��������ַ�����
#__repr__()  ###���س��򿪷��߿������ַ���
#__name__()  ###��ȡ������
#_main_

#��������ڽű����ж��Ƿ��ڡ�ִ��pythonģ�顿���ߡ�����pythonģ�顿
#if __name__='__main__'			
#�������ģ��(python�ļ�)����__name__��Ϊ__main__;���ִ�У���Ϊ__main__��



class Fib(object):
    def __init__(self):
        self.a, self.b = 0, 1 	# ��ʼ��

    def __iter__(self):
        return self 			# �����Լ���  ���� for n in Fib():

    def __getitem__(self, n):   #���������������һ��ʹ�ã���Fib()[0]
        a, b = 1, 1
        for x in range(n):
            a, b = b, a + b
        return a
		
	def next(self):
        self.a, self.b = self.b, self.a + self.b 	# ������һ��ֵ
        if self.a > 100000: 						# �˳�ѭ��������
            raise StopIteration();
        return self.a 								# ������һ��ֵ