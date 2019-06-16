import json


class OpeerateJson:

    def __init__(self):
        self.data = self.read_data()

    def read_data(self):
        """打开json文件"""
        with open('../user.json', mode='r', encoding='utf-8') as fp:
            data = json.load(fp)
        return data

    def get_data(self, id):
        """获取json数据内容"""
        return self.data[id]


if __name__ == '__main__':
    opensui = OpeerateJson()
    a = opensui.get_data('loginout')
    print(a)
