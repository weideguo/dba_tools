#coding=utf-8
import socket
with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as s:
	#��������
	s.connect(("www.hao123.com",80))
	#������
	request_line="GET /index.html HTTP/1.1"
	#�����ײ�,���ʹ��"\r\n"�ָ�
	headers="Host:www.hao123.com\r\nContent-Type:text/html"
	#���У���������ײ�����
	blank_line="\r\n"
	#������
	request_body="a=b&c=d"
	#��ϳ�������Ϣ
	message="\r\n".join([request_line,headers,blank_line,request_body])
	#b'GET /index.html HTTP/1.1\r\nHost:www.baidu.com\r\n\r\n'
	s.send(message.encode('utf-8'))
	response=s.recv(10240)
	print(response)

	


#'''
#HTTP����
#	������
#		���󷽷�
#			GET POST PUT
#		����URL
#			/index.html
#		HTTPЭ��汾
#			HTTP/1.1
#	�����ײ�
#	����
#		\r\n
#	������
#
#��������/�����ײ�/����/�����塿֮��ʹ��"\r\n"�ָ�
#
#
#HTTP��Ӧ
#	��Ӧ��(HTTP/1.1 200 OK)
#		HTTPЭ��汾
#		״̬��
#		״̬������
#	��Ӧ�ײ�
#	����
#	��Ӧ��
#'''

















