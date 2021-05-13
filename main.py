import fetch_servants
import format_servants
import to_html

if __name__ == '__main__':
    servants = fetch_servants.main()
    servants = format_servants.main(servants)
    html = to_html.main(servants)
    with open('public/index.html', 'w', encoding='utf-8') as f:
        f.write(html)

