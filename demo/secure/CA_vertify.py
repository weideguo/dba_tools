##CA证书的验证
'''
申请者通过非对称加密算法（RSA） 生成一对公钥和密钥，然后把需要的申请信息（国家，域名等）连同公钥发送给 证书认证机构（CA）
CA构确认无误后通过消息摘要算法（MD5，SHA) 生成整个申请信息的摘要签名M， 然后 把 签名M和使用的摘要算法 用 CA自己的私钥 进行加密

客户端得到服务端返回的证书，通过读取得到 服务端证书的发布机构（Issuer）
客户端去操作系统查找这个发布机构的的证书，如果是不是根证书就继续递归下去 直到拿到根证书。
用 根证书的公钥 去 解密验证 上一层证书的合法性，再拿下一层证书的公钥去验证更下层证书的合法性；递归回溯。
最后验证服务器端的证书是 可信任 的。
'''


'''
#证书包含
公钥
证书拥有者身份信息
数字证书认证机构（发行者）信息
发行者对这份文件的数字签名及使用的算法
有效期


证书的格式和验证方法普遍遵循X.509 国际标准。                 不需要公钥可以读取部分信息
证书是可以通过 CA的公钥 去解密得到证书的签名摘要的
'''

##离线验证
import OpenSSL
f=open('./ca.crt','r')
x=OpenSSL.crypto.load_certificate(OpenSSL.crypto.FILETYPE_PEM,f.read())
x.get_subject()
x.get_issuer()




#在线验证
import ssl, socket

hostname = 'www.google.com'
ctx = ssl.create_default_context()
s = ctx.wrap_socket(socket.socket(), server_hostname=hostname)
s.connect((hostname, 443))
cert = s.getpeercert()

subject = dict(x[0] for x in cert['subject'])
issued_to = subject['commonName']
issuer = dict(x[0] for x in cert['issuer'])
issued_by = issuer['commonName']
