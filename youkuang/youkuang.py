# -*- coding: utf-8 -*-
"""优矿量化交易"""

# 回归时间段设置
start = '2017-06-12'
end = '2017-06-12'

# 股票策略参照基准(股票)
benchmark = '399006.ZICN'

# 初始资金
capital_base = 10000

# 设置策略执行间隔()
freq = 'm'
refresh_rate = 30

# 选取股票池
# '00000.XSHE'前6位位股票代码，后4位为交易所代码
# universe = ['000001.XSHE', '600000.XSHG']
# StockScreener(Factor.PE.)
universe = set_universe('SH50')


# 初始化回归账户
def initialize(account):
    pass


def handle_data(account):
    """交易策略"""
    pass
