import smtplib
from email.mime.text import MIMEText


class SendEmail:
    global email_host
    global send_user
    global password
    email_host = "smtp.163.com"
    send_user = "17620016080@163.com"
    password = "Che123456n"

    def send_emai(self, user_list, sub, content):
        user = send_user
        message = MIMEText(content, _subtype='plain', _charset='UTF-8')
        message['Subject'] = sub
        message['From'] = user
        message['TO'] = ";".join(user_list)
        print('开始准备发送邮件')
        try:
            server = smtplib.SMTP()
            server.connect(email_host)
            server.login(send_user, password)
            server.sendmail(user, user_list, message.as_string())
        except:
            print('发送失败')
        else:
            print("邮件发送成功！")
        finally:
            server.close()

    def send_main(self, pass_list, fail_list):
        pass_num = float(len(pass_list))
        fail_num = float(len(fail_list))
        cont_num = pass_num + fail_num
        # 进行百分比
        pass_result = "%.2f%%" % (pass_num / cont_num * 100)
        fail_result = "%.2f%%" % (fail_num / cont_num * 100)

        user_list = ['17620016080@163.com']
        sub = "接口自动化测试报告"
        content = "此次一共运行接口个数为%s个，通过个数为%s，失败个数为%s，通过率为%s，失败率为%s" % (
                                                    cont_num, pass_num, fail_num,
                                                    pass_result, fail_result)
        self.send_emai(user_list, sub, content)


if __name__ == '__main__':
    sen = SendEmail()
    sen.send_main([1, 2, 3, 4, 5], [8, 9])
