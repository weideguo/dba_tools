#coding=UTF-8 
import os   #Python�ı�׼���е�osģ������ձ�Ĳ���ϵͳ����  
import re   #����������ʽ����  
import urllib   #���ڶ�URL���б����  
from http.server import HTTPServer, BaseHTTPRequestHandler  #����HTTP������ص�ģ��  
#from BaseHTTPServer import HTTPServer, BaseHTTPRequestHandler  
  
#�Զ��崦��������ڴ���HTTP����  
class TestHTTPHandler(BaseHTTPRequestHandler):  
#����GET����  
	def do_GET(self):   
		response_str ='''   
<html>   
<head>   
<title>QR Link Generator</title>   
</head>   
<body>    
<br>   
<br>   
<form action="/qr" name=f method="GET"><input maxLength=1024 size=70   
name=s value="" title="Text to QR Encode"><input type=submit   
value="Show QR" name=qr>   
</form> 
</body>   
</html> 
'''  
		#����Э��汾 
		self.protocal_version = 'HTTP/1.1'
		#������Ӧ״̬�� 
		self.send_response(200)
		#������Ӧͷ
		self.send_header("Welcome", "Contect") 
		self.end_headers() 
		#�����Ӧ����  
		self.wfile.write(response_str.encode('utf-8'))
  
def start_server(port): 
	#HTTPServer�Ĺ��캯��__init__(server_address, RequestHandlerClass, bind_and_activate=True)
    http_server = HTTPServer(('', int(port)), TestHTTPHandler)  
    http_server.serve_forever()  
  
#os.chdir('static')  #�ı乤��Ŀ¼�� static Ŀ¼  
start_server(8000) 