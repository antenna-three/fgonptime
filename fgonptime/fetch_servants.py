'''
fetch servant list and noble phantasm time from fgo atwiki
'''

import pandas
import json

def fetch_ordered_servants():
    '''
    fetch servant list
    '''
    url = 'https://w.atwiki.jp/f_go/pages/713.html'
    dfs = pandas.read_html(url, match='マシュ・キリエライト', header=0, index_col=0)
    if dfs:
        servants = dfs[0]
    else:
        raise IOError('Servants table not found')
    servants.drop(index='No.', inplace=True)
    servants.rename(columns=str.lower, inplace=True)
    servants.columns.name = 'number'
    np_split = servants['宝具'].str.extract('(?P<range>.*)(?P<color>[ＡＢＱABQ])')
    servants = pandas.concat([servants, np_split], axis=1)
    servants.replace({'color': {'Ａ': 'A', 'Ｂ': 'B', 'Ｑ': 'Q'}}, inplace=True)
    return servants

def fetch_hidden_status():
    '''
    fetch hidden status including noble phantasm time
    '''
    url = 'https://w.atwiki.jp/f_go/pages/304.html'
    dfs = pandas.read_html(url, match='倍速/秒', header=0, index_col=0)
    if dfs:
        servants = dfs[0]
    else:
        raise IOError('Hidden status table not found')
    servants.rename(columns=str.lower, inplace=True)
    servants.rename(columns={'クラス': 'class', '倍速/秒': 'strtime'}, inplace=True)
    servants.dropna(axis='index', subset=['strtime'], inplace=True)
    servants = servants.query('strtime not in ["不明", "省略"]')
    servants.columns.name = 'number'
    np_times = servants['strtime'].str.extractall(r'(?P<time>\d{1,2}\.\d)(?:[@＠](?P<cond>.{1,2}))?')
    min_times = np_times.astype({'time': 'float'}).sort_values('time').groupby(level=0).head(1).sort_index(0)
    min_times.reset_index(level=1, inplace=True)
    servants = pandas.concat([servants, min_times], axis=1)

    np_split = servants['宝具'].str.extract('(?P<range>.*)(?P<color>[ＡＢＱABQ])')
    servants = pandas.concat([servants, np_split], axis=1)
    servants.replace({'color': {'Ａ': 'A', 'Ｂ': 'B', 'Ｑ': 'Q'}}, inplace=True)
    return servants

def main():
    '''
    extract required columns
    '''
    with open('columns.json', 'r', encoding='utf-8') as f:
        columns = json.load(f)

    #servants = fetch_ordered_servants()
    servants = fetch_hidden_status()
    return servants[columns]

def dump_json():
    servants = main()
    servants.to_json('data/servants_fetched.json', orient='records', force_ascii=False, indent=4)

def dump_csv():
    servants = main()
    servants.to_csv('data/servants.csv')

if __name__ == '__main__':
    dump_csv()

