from base.operateExcel import OperateExcel
from base.runmethod import RunMethod
from data.get_data import GetData
import json
from jsonpath_rw import jsonpath, parse


class DependentData:
    """处理数据依赖的问题"""
    def __init__(self, case_id):
        self.case_id = case_id
        self.opera_excle = OperateExcel()
        self.data = GetData()

    # 通过case_id去获取该case_id的整行数据
    def get_case_line_data(self):
        """根据case_id去获取该case_id的整行数据"""
        rows_data = self.opera_excle.get_rows_data(self.case_id)
        return rows_data

    # 执行依赖测试，获取结果
    def run_dependent(self):
        """执行依赖测试，获取结果"""
        run_method = RunMethod()
        row_num = self.opera_excle.get_row_num(self.case_id)
        request_data = self.data.get_data_for_json(row_num)
        header = self.data.is_header(row_num)
        method = self.data.get_request_method(row_num)
        url = self.data.get_request_url(row_num)
        res = run_method.run_main(method, url, request_data, header)
        # 需要将数据更改为json格式
        return json.loads(res)

    # 根据依赖的key去获取执行依赖测试case的响应，然后返回
    def get_data_for_key(self, row):
        """根据依赖的key去获取执行依赖测试case的响应，然后返回"""
        depent_data = self.data.get_denpent_key(row)
        response_data = self.run_dependent()
        json_exe = parse(depent_data)
        madle = json_exe.find(response_data)
        return [math.value for math in madle][0]


if __name__ == '__main__':
    denpet = DependentData('Imooc-11')
    A = denpet.get_data_for_key(11)
    print(A)


    # order = {
    #       "data": [],
    #       "errorCode": 10001,
    #       "errorDesc": "请先登录",
    #       "status": 0,
    #       "timestamp": 1560583627578
    #     }
    # res = 'timestamp'
    # json_exe = parse(res)
    # madle = json_exe.find(order)
    # print([math.value for math in madle][0])
