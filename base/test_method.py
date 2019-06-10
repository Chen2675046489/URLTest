import time
import unittest
from base.demo import RunMain
from HTMLTestReportCN import HTMLTestRunner
import mock
from base.demomock import mock_test


class TestMethod(unittest.TestCase):

    def setUp(self):
        """每次方法，之前执行"""
        self.run = RunMain()

    def tearDown(self):
        """每次方法，之后执行"""
        print('test--->tearDown')

    def test_01(self):
        url = 'http://www.imooc.com/m/web/shizhanapi/loadmorepingjia.html?1'
        data = {'cart': '11'}
        # mock_data = mock.Mock(return_value=data)
        # self.run.rum_main = mock_data
        res = mock_test(self.run.rum_main, data, url, 'GET', data)
        # res = self.run.rum_main(url, 'GET', data)
        print(res)
        self.assertEqual(res['cart'], '11', '测试失败')
        # globals()['userid'] = 10009 全局变量，globals()是一个字典

    def test_02(self):
        # print(globals()['userid'])
        url = 'http://www.imooc.com/m/web/shizhanapi/loadmorepingjia.html?1'
        data = {'cart': '21'}
        res = self.run.rum_main(url, 'GET', data)
        self.assertEqual(res['data']['errorCode'], 1006, '测试失败')


if __name__ == '__main__':
    now = time.strftime('%Y-%m-%d %H_%M_%S')
    report_dir = '../report'  # 指定文件目录
    report_name = report_dir + '/' + now + 'test_report.html'
    suite = unittest.TestSuite()
    suite.addTest(TestMethod('test_01'))
    suite.addTest(TestMethod('test_02'))
    with open(report_name, 'wb') as fp:
        runner = HTMLTestRunner(stream=fp, title='自动化测试报告',
                                description='详细测试用例结果',
                                tester='CWJ')  # tester 测试人员姓名
        runner.run(suite)
    # unittest.TextTestRunner().run(suite)
