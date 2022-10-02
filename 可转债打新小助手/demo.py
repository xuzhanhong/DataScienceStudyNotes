import datetime
import pandas as pd
import akshare as ak


COLUMNS = (
    '债券代码',
    '债券简称',
    '公告日期',
    '发行起始日',
    '发行终止日',
    '计划发行总量',
    '实际发行总量',
    '发行面值',
    '发行价格',
    '发行方式',
    '发行对象',
    '发行范围',
    '承销方式',
    '募资用途说明',
    '初始转股价格',
    '转股开始日期',
    '转股终止日期',
    '网上申购日期',
    '网上申购代码',
    '网上申购简称',
    '网上申购数量上限',
    '网上申购数量下限',
    '网上申购单位',
    '网上申购中签结果公告日及退款日',
    '优先申购日',
    '配售价格',
    '债权登记日',
    '优先申购缴款日',
    '转股代码',
    '交易市场',
    '债券名称',
)


# 获取当天上市可转债信息
def get_bond_cov_issue_cninfo(start_date=None, end_date=None):
    now_date = datetime.datetime.now().date()
    if not start_date:
        start_date = (now_date - datetime.timedelta(days=1)).strftime('%Y%m%d')
    if not end_date:
        end_date = now_date.strftime('%Y%m%d')

    try:
        bond_cov_issue_cninfo_df = ak.bond_cov_issue_cninfo(start_date="20221009", end_date="20221010")
    except Exception as e:
        bond_cov_issue_cninfo_df = pd.DataFrame(columns=COLUMNS)

    return bond_cov_issue_cninfo_df

