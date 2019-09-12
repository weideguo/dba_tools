#coding=utf-8

import socket
import re

HOST = ''
PORT = 8000
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind((HOST, PORT))
#���óɼ���ģʽ
sock.listen(100)

while True:
	conn, addr = sock.accept()
	request = conn.recv(1024).decode('utf-8')
	method = request.split(' ')[0]
	src  = request.split(' ')[1]
	
	print('Connect by: ', addr)
	print('Request is: \n', request)
	
	if method == 'GET':
		if src == '/index.html':
			content = "this is index"
		elif re.match('^/\?.*$', src):
			entry = src.split('?')[1]      
			content = 'HTTP/1.x 200 ok\r\nContent-Type: text/html\r\n\r\n'
			content += entry
		else:
			content='request'	
	elif method == 'POST':
		form = request.split('\r\n')
		entry = form[-1]      # ������Ϣ�����һ������������
		content = 'HTTP/1.x 200 ok\r\nContent-Type: text/html\r\n\r\n'
		content += entry
	conn.sendall(content.encode('utf-8'))
	conn.close()