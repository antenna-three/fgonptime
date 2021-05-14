'''
render fetched servants data to html using template
'''

from jinja2 import Environment, FileSystemLoader
import json

from .layout_to_filters import layout_to_filters

def main(servants):
    '''
    Parameters
    ----------
    servants : list(dict)
        result of pandas.DataFrame.to_dict(orient='record')
    '''
    with open('layout.json', 'r', encoding='utf-8') as f:
        layout = json.load(f)

    data = layout
    data['servants'] = servants
    data['filters'] = layout_to_filters(layout['filter_groups'])

    loader = FileSystemLoader('./templates')
    env = Environment(loader=loader, trim_blocks=True, lstrip_blocks=True)
    template = env.get_template('index.html')
    return template.render(data)

def json_to_html():
    with open('data/servants.json', 'r', encoding='utf-8') as f:
        servants = json.load(f)
    html = main(servants)
    with open('public/index.html', 'w', encoding='utf-8') as f:
        f.write(html)

if __name__ == '__main__':
    json_to_html()

