# 使用するベースイメージ
FROM python:3.8-slim

# ワーキングディレクトリを設定
WORKDIR /app

# ホストのrequirements.txtをコンテナ内にコピー
COPY backend/app/requirements.txt /app/requirements.txt

# 依存関係をインストール
RUN pip install --no-cache-dir -r /app/requirements.txt

# ホストのアプリケーションコードをコンテナにコピー
COPY backend/app /app

# FastAPIを起動するためのコマンド
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]
