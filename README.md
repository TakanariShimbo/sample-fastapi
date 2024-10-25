# 仮想環境

```bash
# プロジェクトの仮想環境の作成
conda create -n py310_sample_fastapi python=3.10

# 仮想環境のアクティベート (base → py310_sample_fastapi になったことをチェック)
conda activate py310_sample_fastapi

# 仮想環境にライブラリのインストール
pip install -r requirements.txt
```

# 実行方法

```bash
# サーバーの起動 (http://127.0.0.1:8000/docs)
uvicorn main:app --reload

# テストの実行
python test.py
```
