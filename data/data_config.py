

class global_var:
    # case_id
    id = '0'
    url = '1'
    run = '2'
    request_way = '3'
    header = '4'
    case_depend = '5'
    data_depend = '6'
    field_depend = '7'
    data = '8'
    expect = '9'
    result = '10'


def get_id():
    """返回id"""
    return int(global_var.id)


def get_url():
    """返回url"""
    return int(global_var.url)


def get_run():
    """返回是否运行"""
    return int(global_var.run)


def get_request_way():
    """返回请求方式"""
    return int(global_var.request_way)


def get_header():
    """返回请求头"""
    return int(global_var.header)


def get_case_depend():
    """返回依赖ID"""
    return int(global_var.case_depend)


def get_data_depend():
    """返回依赖数据"""
    return int(global_var.data_depend)


def get_field_depend():
    """返回依赖所属字段"""
    return int(global_var.field_depend)


def get_data():
    """返回请求数据"""
    return int(global_var.data)


def get_expect():
    """返回预期判断"""
    return int(global_var.expect)


def get_result():
    """返回实际结果"""
    return int(global_var.result)


def get_header_var():
    header = {
        'header': '123456',
        'coolie': 'chenwj'
    }