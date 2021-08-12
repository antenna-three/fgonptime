import pandas
import json

def add_class_to_duplicated_names(servants):
    servants = servants.assign(duplicated=servants.duplicated(subset='name', keep=False))
    name_class = servants.apply(
        lambda r: f'{r["name"]}（{r["class"]}）' if r['duplicated'] else r['name'],
        axis=1
        )
    servants = servants.assign(name=name_class)
    servants.drop(columns='duplicated', inplace=True)
    return servants

def main(servants):
    servants = add_class_to_duplicated_names(servants)
    servants = servants.append({'name': '妖精騎士ランスロット（再臨3）', 'class': '槍', 'range': '全体', 'color': 'B', 'time': 10.8}, ignore_index=True)
    servants = servants.sort_values('time')
    return servants.to_dict(orient='records')

def csv_to_json():
    servants = pandas.read_csv('data/servants.csv', header=0, index_col=0)
    servants = main(servants)
    with open('data/servants.json', 'w', encoding='utf-8') as f:
        json.dump(servants, f, ensure_ascii=False, indent=4)

if __name__ == '__main__':
    csv_to_json()
    
