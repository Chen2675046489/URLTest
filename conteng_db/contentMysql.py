import pymysql.cursors
import json

class OperationMysql:

    def __init__(self):
        """使用构造函数对数据库进行全局连接"""
        try:
            conn = pymysql.connect(
                host='127.0.0.1',
                port=3306,
                user='root',
                password='Che895183729n',
                charset='utf8',
                db='django_restful',
                cursorclass=pymysql.cursors.DictCursor)
            self.cursor = conn.cursor()
            print('------连接成功------')
        except pymysql.err:
            print('------链接出错------')

    def search_one(self, sql):
        """查询数据"""
        self.cursor.execute(sql)
        result = self.cursor.fetchone()
        result = json.dumps(result)
        return result


if __name__ == '__main__':
    op_mysql = OperationMysql()
    sql = "select * from api_user where username='chen'"
    a = op_mysql.search_one(sql)
    print(type(a))

