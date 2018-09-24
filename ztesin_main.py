import unittest
from selenium import webdriver
import HTMLTestRunner
import time
import smtplib
from email.mime.multipart import MIMEMultipart
from  email.mime.text import MIMEText
from email.mime.application import MIMEApplication
# 用例路径
testcase_path = r'D:\PycharmProjects\ztestin\test_case'
# 收集测试用例
test_suit = unittest.TestSuite()
discover = unittest.defaultTestLoader.discover(testcase_path,pattern='test*.py',top_level_dir=None)
# 添加测试用例到集合
test_suit.addTests(discover)
now = time.strftime('%Y-%m-%d %H-%M-%S')
# print(nowtime)
# 执行测试用例
report_file = "D:\\PycharmProjects\\ztestin\\report\\{}_report.html".format(now)
title = u'云测测试报告'
with open(report_file,'ab+') as fp:
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp,title=title,description=u"云测测试报告详情")
    runner.run(discover)

# 设置邮件基本信息
server_add = 'smtp.qq.com'
port = 465
user = '2291506058@qq.com'
psw ='kprhddcltliyebcg'
reciver = '2291506058@qq.com'

msg = MIMEMultipart()
msg["from"] =reciver
msg['Subject']=title
msg["to"]=reciver

# 邮件内容
b = report_file
with open(b,'rb') as fd:
    mail_body = fd.read()
body = MIMEText(mail_body,'html','utf-8')
msg.attach(body)

# att =MIMEText(mail_body,'base64','utf-8')
# att['Content-Type']='application/octet-stream'
# att['Content-Dispostion']='attachment;file={} report.html'.format(now)
# msg.attach(att)

# 发送附件
att = MIMEApplication(open(report_file, 'rb').read())
# att = MIMEText(sendfile, 'base64', 'utf-8')
att['Content-Type'] = 'application/octet-stream'
att.add_header('Content-Disposition', 'attachment', filename=('utf-8', '', now + "_report.html"))
msg.attach(att)

smtp = smtplib.SMTP_SSL(server_add,port)
smtp.login(user,psw)
smtp.sendmail(user,reciver,msg.as_string())
smtp.quit()






