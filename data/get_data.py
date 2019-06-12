from base.operateExcel import OperateExcel
from base.operateJson import OpeerateJson
from data import data_config


class GetData:

    def __init__(self):
        self.opera_excel = OperateExcel()

    def get_case_lines(self):
        """获取excel行数，就是我们的case的行数"""
        return self.opera_excel.get_lines()

    def get_is_run(self, row):
        """判断是否运行"""
        flag = None
        col = data_config.get_run()
        row_model = self.opera_excel.get_cell_value(row, col)
        if row_model == 'yes':
            flag = True
        else:
            flag = False
        return flag

    def is_header(self, row):
        """获取请求头"""
        col = data_config.get_header()
        header = self.opera_excel.get_cell_value(row, col)
        if header == 'yes':
            return 'header'
        else:
            return None

    def get_request_method(self, row):
        """获取请求方式"""
        col = data_config.get_request_way()
        request_method = self.opera_excel.get_cell_value(row, col)
        return request_method

    def get_request_url(self, row):
        """获取url地址"""
        col = data_config.get_url()
        url = self.opera_excel.get_cell_value(row, col)
        return url

    def get_request_data(self, row):
        """获取请求数据"""
        col = data_config.get_data()
        data = self.opera_excel.get_cell_value(row, col)
        if data == '':
            return None
        else:
            return data

    def get_data_for_json(self, row):
        # json可以放到实例化方法中
        """获取请求数据中的json数据"""
        opera_json = OpeerateJson()
        request_data = opera_json.get_data(self.get_request_data(row))
        return request_data

    def get_expcet_data(self, row):
        """获取预期结果"""
        col = data_config.get_expect()
        expect = self.opera_excel.get_cell_value(row, col)
        if expect == '':
            return None
        else:
            expect


if __name__ == '__main__':
    get_data = GetData()
    a = get_data.get_data_for_json(2)
    print(a)