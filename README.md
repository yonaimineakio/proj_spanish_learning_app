# このレポジトリーは？
このレポジトリーはAIスペイン語学習アプリを共同開発用レポジトリです。

# ブランチ戦略
ブランチ戦略とは、*ブランチの切り方のルール*です。
ブランチの切り方のルールを定める理由はシンプルで、意図しないmainブラントへのpushを避けることです。
間違えて直Pushした時の元に戻している時間ほど無駄なことはありまあせん。TickTokスクロールしてた方が有益です。
以下リモートブランチにpushするまでの手順です。

①mainブランチ上でリモートブランチトと同期します。

```git pull```

②`feature/<なんとなく推測できる変更内容の英字>`でブランチをチェックアウトします。
例: readmeを追加した場合。

```git checkout -b feature/add-reaedme```

③変更ファイルを確認。

```git status```

④変更内容をステージングする。※不要なファイル追加を防ぐため基本的に`git add .`でなく直接ファイルパスを指定しましょう。

```git add <ファイルパス>```

⑤変更内容をコミット。

```git commit -m <なんとなく変更内容がわかる一文>```

⑥リモートブランチにpush
※最初のpush時は上流ブランチをセットしてください的なエラーと推奨コマンドが出ると思うのでそれを実行しましょう。

```git push```

ここまで完了したら次にPR(Pull Request)を出しましょう。

### PRの出し方

1 Compare & Pull Requestをクリック。
<img width="970" alt="スクリーンショット 2024-11-02 15 23 04" src="https://github.com/user-attachments/assets/c02b0812-6bfa-4995-9650-978afdc4039e">

2 適当な文章を入れる。
<img width="1290" alt="スクリーンショット 2024-11-02 15 23 21" src="https://github.com/user-attachments/assets/2b0c1d53-0f92-456a-853d-94477c2d4de7">

3 マージても大丈夫そうならマージをクリック。

<img width="978" alt="スクリーンショット 2024-11-02 15 23 33" src="https://github.com/user-attachments/assets/9241dd22-e84b-46e5-8b65-4180ceeebe7c">

4 マージできたら完了。
<img width="1325" alt="スクリーンショット 2024-11-02 15 23 44" src="https://github.com/user-attachments/assets/23d46c83-83bb-4d22-b554-763a08197656">


### PRのレビューについて
基本はお互いにレビューを求めず、PRを作成したらそのままmainブランチにマージしましょう。

これはお互いのレビュー待ちに起因するフラストレーションと開発効率を上げるためです。(まぁーそもそも二人だけだし、、)

将来的にはpushしたら自動でコードを整形してくれるlintやLLMにコードレビューしてもらう的な機能も入れたいですがそれはおいおいで。

## タスク管理について
基本タスクは全てissueベースで管理しましょう。

これはお互いが今何をどれぐらい進められているかを把握するためです。

何かアプリに追加や修正を加える場合はissueを作成しましょう。

とは言ってもめちゃくちゃ小さい修正,タイポの修正やコメント修正などのためにいちいちissueを作成するのは面倒なのでその場合はスキップしましょう。

### issue作成の仕方。
1
<img width="1393" alt="スクリーンショット 2024-11-02 14 44 20" src="https://github.com/user-attachments/assets/b27c186c-6d39-4776-99ec-69d4eddcc9cc">

2 適当なタイトルと説明を追加しましょう。
<img width="1336" alt="スクリーンショット 2024-11-02 14 45 28" src="https://github.com/user-attachments/assets/a5222294-20ec-485d-a48e-7a203684a27d">

3 完了したらcloseしましょう。
<img width="1002" alt="スクリーンショット 2024-11-02 14 46 45" src="https://github.com/user-attachments/assets/51e9e198-8e3a-45b1-973b-363414af22b4">


