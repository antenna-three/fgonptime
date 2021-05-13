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
    dfs = pandas.read_html(url, match='宝具長さ', header=(0, 1), index_col=0)
    if dfs:
        servants = dfs[0]
    else:
        raise IOError('Hidden status table not found')
    servants.drop(index='No', inplace=True)
    servants.drop(index='083', inplace=True) #drop solomon
    servants.rename(columns=str.lower, inplace=True)
    servants.columns = ('_'.join(dict.fromkeys(c)) for c in servants.columns)
    servants.rename(columns={'クラス': 'class', '宝具長さ_倍速': 'strtime'}, inplace=True)
    servants.columns.name = 'number'
    servants = servants[~servants.index.duplicated(keep='first')]
    np_times = servants['strtime'].str.extractall(r'(?P<time>\d{1,2}\.\d)(?:[@＠](?P<cond>.{1,2}))?')
    min_times = np_times.astype({'time': 'float'}).sort_values('time').groupby(level=0).head(1).sort_index(0)
    min_times.reset_index(level=1, inplace=True)
    servants = pandas.concat([servants, min_times], axis=1)
    return servants

def main():
    '''
    merge servant list and hidden status
    '''
    with open('cols_to_use.json', 'r', encoding='utf-8') as f:
        cols_to_use = json.load(f)

    servants = fetch_ordered_servants()
    hidden_status = fetch_hidden_status()
    merged = servants.merge(
                hidden_status,
                left_index=True,
                right_index=True,
                suffixes=(None, '_hidden')
                )
    return merged[cols_to_use]

def dump_json():
    servants = main()
    servants.to_json('data/servants_fetched.json', orient='records', force_ascii=False, indent=4)

def dump_csv():
    servants = main()
    servants.to_csv('data/servants.csv')

if __name__ == '__main__':
    dump_csv()

