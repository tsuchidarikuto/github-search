# GitHub User Search Application

GitHubユーザーを検索し、結果をCSVファイルとして保存するPythonアプリケーションです。

## 機能

- GitHubのGraphQL APIを使用したユーザー検索
- 高度な検索構文のサポート（AND、OR、NOT、完全一致など）
- 検索結果のCSVファイルへの保存
- Dockerサポート

## 必要条件

- Python 3.8以上
- Docker（オプション）
- GitHub Personal Access Token

## セットアップ

1. リポジトリをクローン：
```bash
git clone https://github.com/yourusername/github-user-search.git
cd github-user-search
```

2. GitHub Personal Access Tokenの取得：
   - GitHubの設定から「Developer settings」→「Personal access tokens」→「Tokens (classic)」を選択
   - 「Generate new token」をクリック
   - 必要な権限（`read:user`）を付与
   - トークンを生成し、安全な場所に保存

3. 環境変数の設定：
   - `.env`ファイルを作成し、以下の内容を追加：
   ```
   GITHUB_TOKEN=your_github_token_here
   ```

## 使用方法

### Pythonで直接実行

1. 必要なパッケージをインストール：
```bash
pip install -r requirements.txt
```

2. アプリケーションを実行：
```bash
python src/simple_github_search.py
```

### Dockerで実行

1. イメージをビルド：
```bash
docker compose build
```

2. アプリケーションを実行：
```bash
docker compose up
```

## 検索クエリの構文

- 基本演算子：
  * OR: いずれかの条件に一致（例：`"python OR javascript"`）
  * AND: 両方の条件に一致（例：`"python AND developer"`）
  * NOT: 一致を除外（例：`"python NOT java"`）
- 完全一致：
  * `"python developer"`: 完全一致
  * `python developer`: 部分一致
- 修飾子：
  * `in:bio`: ユーザーのbioで検索
  * `in:name`: ユーザー名で検索
  * `followers:>1000`: 1000人以上のフォロワー
  * `location:japan`: 日本のユーザー

## 出力

検索結果は`output`ディレクトリにCSVファイルとして保存されます。ファイル名にはタイムスタンプが含まれます。

## ライセンス

MIT License

## 貢献

1. このリポジトリをフォーク
2. 新しいブランチを作成（`git checkout -b feature/amazing-feature`）
3. 変更をコミット（`git commit -m 'Add some amazing feature'`）
4. ブランチにプッシュ（`git push origin feature/amazing-feature`）
5. プルリクエストを作成

## code
This is the code used in our research. Please execute the code according to the numbers. Please note that some codes require you to enter your GitHub or ChatGPT token key.

## ethical_document
There are two PDF documents below. The author and affiliation information has been removed.

- Consent Form
- Participant Information Sheet