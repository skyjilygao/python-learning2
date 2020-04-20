import smtplib
import sys
from email.mime.text import MIMEText

from email.header import Header
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
mail_host='smtp.qiye.163.com'
mail_user='xx@xx'
mail_pass='!xxx'

def send_mail():
    sender = mail_user
    receivers = ['xx','xxx']

    message = MIMEMultipart()
    message.attach(MIMEText('test...', 'plain', 'utf-8'))

    # message['From'] = Header('Skyjilygao', 'utf-8')
    message['To'] = Header(receivers[0], 'utf-8')
    message['To'] = Header(receivers[1], 'utf-8')

    subject = 'test mail'
    message['Subject'] = Header(subject, 'utf-8')

    # 附件
    # MIMEApplication
    str = 'test/a.txt'
    part = MIMEApplication(open(str,'rb').read())
    part.add_header('Content-Disposition','attachment',filename='a.txt')
    message.attach(part)
    # smtplib.SMTP_SSL()
    smtpObj = smtplib.SMTP_SSL()
    smtpObj.connect(mail_host, 465)
    smtpObj.login(mail_user,mail_pass)
    smtpObj.sendmail(sender, receivers, message.as_string())
    print('mail send ok...')

if __name__ == '__main__':

    count = sys.argv.__len__()
    print("参数大小=",count -1)

    for i in range(1,count):
        print('参数：',sys.argv[i])
    # print("send mail...")
    # send_mail()