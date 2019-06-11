from base.runmethod import RunMethod
from data.get_data import GetData


class RunTest:

    def __init__(self):
        self.runm_method = RunMethod()
        self.data = GetData()

    # 程序执行
    def go_on_run(self):
        # 如果拿到的是10行，0 1 3，所以选用将0进行除去
        rows_count = self.data.get_case_lines()
        # for i in range(1, rows_count):