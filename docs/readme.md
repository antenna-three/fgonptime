# fgonptime / FGO 宝具演出時間ランキング

FGOの全サーヴァントの宝具演出時間を@wikiから抽出し、昇順に並べ替え、フィルター機能付きのWebページとして公開しています。

公開されているWebページは[こちら](https://antenna-three.github.io/fgonptime/)です。

## 動作環境

Python 3.9およびpipenvが必要です。

## インストール

```shell
$ git clone https://github.com/antenna-three/fgonptime.git
$ cd fgonptime
$ pipenv install
```

## 使用方法

以下のコマンドでスクレイピングからページ生成までが行われます。

```shell
$ pipenv run python -m fgonptime
```

新クラス実装時の対応

layout.jsonを編集

to_css.pyのexport_cssを実行



## 構成

- .github/workflows/gh-pages.yml
    - GitHub Actionsに登録されるアクションです。スクリプトを定期実行し、GitHub Pagesにpublicの内容をデプロイします。デプロイされたページはgh-pagesブランチにあります。
- docs/readme.md
    - このreadmeです。
- fgonptime/
    - スクレイピングからHTMLの出力までを行うPythonパッケージです。
    - \__main__.py
        - 外部から呼び出されるメインモジュールです。fetch_servants, format_servants, to_htmlを順に呼び出します。
    - fetch_servants.py
        - 以下のサイトからサーヴァント一覧と宝具演出時間を抽出し、マージします。
            - [サーヴァント/一覧/番号順 Fate/Grand Order @wiki【FGO】](https://w.atwiki.jp/f_go/pages/713.html)
            - [サーヴァント/隠しステータス Fate/Grand Order @wiki【FGO】](https://w.atwiki.jp/f_go/pages/304.html)
    - format_servants.py
        - fetch_servantsで抽出した表を宝具演出時間でソートし、名前が被っているサーヴァントにクラスの注釈を追加します。
    - to_html.py
        - format_servantsで作られた表をtemplates/index.htmlのテンプレートに流し込んでpublic/index.htmlを生成します。
- public/
    - GitHub Pagesにデプロイされる元となるディレクトリです。
    - index.html
        - Pythonパッケージによって生成された本体ページです。
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
- columns.json
    - fetch_servants.pyが出力する列の設定です。
- layout.json
    - フィルターに使うパラメータと表の列に使うパラメータの設定です。

## 作成者

[@antenna_games](https://twitter.com/antenna_games)

## ライセンス

MIT License. See `LICENSE` for more information.