import conf
from email import encoders
from email.header import Header
from email.mime.text import MIMEText
from email.utils import parseaddr, formataddr

import smtplib

def _format_addr(s):
        name, addr = parseaddr(s)
        return formataddr((Header(name, 'utf-8').encode(), addr))

from_addr = conf.email['user']
password = conf.email['password']
to_addr = 'ahuigo@smtp.ahuigo.com'
smtp_server = 'smtp.partner.outlook.cn'
port=587

msg = MIMEText('hello, send by Python...', 'plain', 'utf-8')
msg['From'] = _format_addr('From <%s>' % from_addr)
msg['To'] = _format_addr('To <%s>' % to_addr)
msg['Subject'] = Header('subject……', 'utf-8').encode()
print('msg:',msg)
print('====')

server = smtplib.SMTP(smtp_server, port)
server.starttls()
server.set_debuglevel(1)
server.login(from_addr, password)
server.sendmail(from_addr, [to_addr], msg.as_string())
server.quit()
