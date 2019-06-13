import xlrd
from xlutils.copy import copy


class OperateExcel:
    """对Excel进行数据操作"""
    def __init__(self, file_name=None, sheet_id=None):
        # 加入file_name存在则进行下列的代码
        """初始化，每次调用OperateExcle都会被调用一次"""
        if file_name:
            self.file_name = file_name
            self.sheet_id = sheet_id
            self.data = self.get_data()
        else:
            self.file_name = r'../接口用例.xls'
            self.sheet_id = 0
        self.data = self.get_data()

    # 获取sheet的内容
    def get_data(self):
        """获取sheet的内容 ，并返回"""
        data = xlrd.open_workbook(self.file_name)
        tables = data.sheet_by_index(self.sheet_id)
        return tables

    # 获取单元格的行数
    def get_lines(self):
        """获取单元格的行数"""
        tables = self.data
        return tables.nrows

    # 获取单元格的内容
    def get_cell_value(self, row, col):
        """获取单元格的内容"""
        return self.data.cell_value(row, col)

    # 写入数据
    def write_value(self, row, col, value):
        """
        写入测试结果数据
        row, col, value
        """
        read_data = xlrd.open_workbook(self.file_name)
        write_data = copy(read_data)
        sheet_data = write_data.get_sheet(0)
        sheet_data.write(row, col, value)
        write_data.save(self.file_name)


if __name__ == '__main__':
    opear_excel = OperateExcel()
    a = opear_excel.get_cell_value(1, 8)
    print(a)

