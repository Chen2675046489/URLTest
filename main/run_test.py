from base.runmethod import RunMethod
from data.get_data import GetData
from base.commonutil import CommonUtil
from data.dependent import DependentData
from sendEmail.sendEmail import SendEmail


class RunTest:

    def __init__(self):
        self.run_method = RunMethod()
        self.data = GetData()
        self.com_util = CommonUtil()
        self.send_email = SendEmail()

    # 程序执行的主路口
    def go_on_run(self):
        res = None
        pass_count = []
        fail_count = []
        rows_count = self.data.get_case_lines()
        for i in range(1, rows_count):
            # 判断是否需要执行
            is_run = self.data.get_is_run(i)
            if is_run:
                url = self.data.get_request_url(i)
                method = self.data.get_request_method(i)
                request_data = self.data.get_data_for_json(i)
                expect = self.data.get_expcet_data_for_mysql(i)
                header = self.data.is_header(i)
                depend_case = self.data.is_denpent(i)
                if depend_case != None:
                    self.depend_data = DependentData(depend_case)
                    # 获取依赖的响应数据
                    depend_response_data = self.depend_data.get_data_for_key(i)
                    # 获取单元格中需要需要修改的名字
                    depend_key = self.data.get_depend_field(i)
                    # 对返回数据进行修改
                    request_data[depend_key] = depend_response_data
                res = self.run_method.run_main(method, url, request_data, header)
                if self.com_util.is_equal(res, expect) == 0:
                    self.data.write_result(i, "pass")
                    pass_count.append(i)
                else:
                    self.data.write_result(i, res)
                    fail_count.append(i)
        self.send_email.send_main(pass_count, fail_count)


if __name__ == '__main__':
    run = RunTest()
    run.go_on_run()
