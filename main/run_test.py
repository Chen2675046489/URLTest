from base.runmethod import RunMethod
from data.get_data import GetData
from base.commonutil import CommonUtil


class RunTest:

    def __init__(self):
        self.run_method = RunMethod()
        self.data = GetData()
        self.com_util = CommonUtil()

    # 程序执行的主路口
    def go_on_run(self):
        res = None
        rows_count = self.data.get_case_lines()
        print(rows_count)
        for i in range(1, rows_count):
            url = self.data.get_request_url(i)
            method = self.data.get_request_method(i)
            is_run = self.data.get_is_run(i)
            print(is_run)
            data = self.data.get_data_for_json(i)
            expect = self.data.get_expcet_data(i)
            header = self.data.is_header(i)
            if is_run:
                # method, url, data, header
                res = self.run_method.run_main(method, url, data, header)
                print(res)
                if self.com_util.is_contain(expect, res):
                    self.data.write_result(i, "测试通过")
                else:
                    self.data.write_result(i, "测试失败")


if __name__ == '__main__':
    run = RunTest()
    run.go_on_run()
