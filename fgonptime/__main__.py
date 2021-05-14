from . import fetch_servants
from . import format_servants
from . import to_html

if __name__ == '__main__':
    servants = fetch_servants.main()
    servants = format_servants.main(servants)
    html = to_html.main(servants)
    with open('public/index.html', 'w', encoding='utf-8') as f:
        f.write(html)

