import akshare as ak

def get_cbond_data():
    df = ak.bond_zh_hs_cov_spot()

    df = df[[
        '代码',
        '名称',
        '最新价',
        '涨跌幅',
        '转股价值',
        '转股溢价率'
    ]]

    return df
