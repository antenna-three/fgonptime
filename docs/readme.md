# fgonptime / FGO 宝具演出時間ランキング

FGOの全サーヴァントの宝具演出時間を@wikiから抽出し、昇順に並べ替え、フィルター機能付きのWebページとして公開しています。

## 動作環境

Python 3.9にて動作を確認しています。実行には下記コマンドによってライブラリをインストールする必要があります。

```shell
$ pip install -r requirements.txt
```

## 構成

- fetch_servants.py
    - 以下のサイトからサーヴァント一覧と宝具演出時間を抽出し、マージします。
        - [サーヴァント/一覧/番号順 Fate/Grand Order @wiki【FGO】](https://w.atwiki.jp/f_go/pages/713.html)
        - [サーヴァント/隠しステータス Fate/Grand Order @wiki【FGO】](https://w.atwiki.jp/f_go/pages/304.html)
- format_servants.py
    - fetch_servantsで抽出した表を宝具演出時間でソートし、名前が被っているサーヴァントにクラスの注釈を追加します。
- to_html.py
    - format_servantsで作られた表をtemplates/index.htmlのテンプレートに流し込んでpublic/index.htmlを生成します。
- main.py
    - fetch_servants, format_servants, to_htmlを順に呼び出します。
- .github/workflows/gh-pages.yml
    - GitHub Actionsに登録されるアクションです。main.pyを定期実行し、GitHub Pagesにpublicの内容をデプロイします。
- public/
    - GitHub Pagesにデプロイされるディレクトリです。
    - index.html
        - 生成された本体ページです。
    - about.html
        - サイトの使い方や免責についてのページです。
    - css/filter.css
        - フィルター機能を実装しているCSSです。
    - css/style.css
        - index.htmlのスタイルシートです。
    - js/script.js
        - チェックボックスの内容を属性にしてfilter.cssに反映させるスクリプトです。
- templates/index.html
    - public/index.htmlのテンプレートです。
- layout.json
    - フィルターに使うパラメータと表の列に使うパラメータの設定です。

## 使用方法

`main.py`を実行するとスクレイピングからhtmlの生成までが行われます。`fetch_servants.py`, `format_servants.py`, `to_html.py`を個別に実行すると中間生成物がdata/に作られます。

## 作成者

[@antenna_games](https://twitter.com/antenna_games)