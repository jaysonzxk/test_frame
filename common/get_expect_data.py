"""
author： mask
filename: get_expect_data.py
datetime： 2021/3/20 11:33 
ide： PyCharm
"""


from test_data.read_data import get_test_data
import json


def get_expect(*args, expect_name='expect'):
    """
    动态获取期望值，
    :param args: 元组：测试文件路径，sheet名称，数字n
    :param expect_name: 表格头部key
    :return:
    """
    expect = json.loads(get_test_data(*args).get(expect_name))
    expect_list = [expect['code'], expect['message']]
    return expect_list


# if __name__ == '__main__':
#     res = get_expect('app_test_data.xlsx', 'personalcenter', 2)
#     print('{}'.format(res))