#ǳ����(slice cpoy)		��ԭ�����޸�Ӱ������				
#Ԫ��ֻ������
person=['name',['savings',100]]

#��savings ����100�޸Ķ�Ӱ�� person hubby wify
hubby=person[:]							#��Ƭ����  [1:5]��ȡ�±�1����5-1��Ԫ��;��ָ����Ϊȫ;  [::3] Ԫ�ؼ��Ϊ3
wify=list(person)
hubby=person

#####################################
#���(deep copy) ��ԭ�����޸Ĳ�Ӱ������

import copy
wify=copy.deepcopy(person)