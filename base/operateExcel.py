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

    # 根据对应的case_id找到对应行的内容
    def get_rows_data(self, case_id):
        """根据对应的case_id找到对应行的内容"""
        row_num = self.get_row_num(case_id)
        rows_data = self.get_row_values(row_num)
        return rows_data

    # 根据对应的case_id找到对应的行号
    def get_row_num(self, case_id):
        """根据对应的case_id找到对应的行号"""
        num = 0
        clols_data = self.get_cols_data()
        for col_data in clols_data:
            if case_id in col_data:
                return num
            num = num+1

    # 根据行号，找到该行的内容
    def get_row_values(self, row):
        """根据行号，找到该行的内容"""
        tables = self.data
        row_data = tables.row_values(row)
        return row_data

    # 获取某一列的内容
    def get_cols_data(self, col_id=None):
        """获取某一列的内容"""
        if col_id != None:
            cols = self.data.col_values(col_id)
        else:
            cols = self.data.col_values(0)
        return cols


if __name__ == '__main__':
    opear_excel = OperateExcel()
    a = opear_excel.get_rows_data('Imooc-11')
    print(a)

