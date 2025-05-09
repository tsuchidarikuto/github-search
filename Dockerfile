FROM python:3.12-slim-bookworm

WORKDIR /app

# 必要なパッケージをインストール
COPY config/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt


# 出力ディレクトリの作成
RUN mkdir -p /app/output

# 環境変数の設定
ENV PYTHONUNBUFFERED=1



# 実行コマンド
CMD ["python", "src/simple_github_search.py"] 