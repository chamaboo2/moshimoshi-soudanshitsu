# もしもし相談室
## 〜歴史の有名人に聞いてみた！〜

> 昔の決断から、いまの一手を。

歴史上の人物が実際に行った決断や行動を手がかりに、現代の悩みを整理するStreamlitアプリです。

これは「歴史人物になりきるチャット」ではありません。

**史実 → 判断傾向（アプリ側の解釈） → 現代の悩みへの応用**

の順番を崩さない設計です。

初期公開人物は次の4名だけです。

1. 楠木正成
2. 小野篁
3. 平重盛
4. 空海

---

# まず確認できること

APIキーを設定する前でも、`.env` またはStreamlit Secretsで `DEMO_MODE=true` にすると、固定のデモ回答で画面と操作を確認できます。

本番では `DEMO_MODE=false` にしてOpenAI APIを使用します。

---

# 1. Supabaseを作る

1. Supabaseにログインします。
2. **New project** から新しいプロジェクトを作成します。
3. プロジェクトが起動したら、左側の **SQL Editor** を開きます。
4. このフォルダの `schema.sql` の内容をSQL Editorへ貼り付けます。
5. **Run** を押します。
6. `consultations` と `feedback` の2テーブルが作成されれば完了です。

このMVPは、ブラウザ側ではなくStreamlitサーバー側からSupabaseへ保存します。
そのためSupabaseの **Secret Key** を使用します。

**Secret KeyをGitHubへ絶対に保存しないでください。**

Supabase公式ドキュメントではPythonクライアントは `create_client()` で初期化でき、Secret Keyはサーバー側のみで扱う必要があります。

---

# 2. SupabaseのURLとSecret Keyを確認する

Supabaseのプロジェクト画面で、接続情報またはAPI Keysを開きます。

取得するものは次の2つです。

- `SUPABASE_URL`
- `SUPABASE_SECRET_KEY`

`SUPABASE_SECRET_KEY` は外部に公開しないでください。

---

# 3. OpenAI APIキーを設定する

OpenAI PlatformでAPIキーを作成します。

このMVPはOpenAIの **Responses API** を利用します。
モデルは初期値として `gpt-5.6-terra` を設定しています。

コストを抑えたい場合は `.env` またはStreamlit Secretsの `OPENAI_MODEL` を、利用可能な別モデルへ変更できます。

---

# 4. ローカルで動かす

## Windowsの場合

このフォルダを開いた状態でPowerShellまたはコマンドプロンプトを開きます。

### 4-1. 仮想環境を作成

```bash
python -m venv .venv
```

### 4-2. 仮想環境を有効化

PowerShell:

```bash
.venv\Scripts\Activate.ps1
```

コマンドプロンプト:

```bash
.venv\Scripts\activate.bat
```

### 4-3. 必要なものをインストール

```bash
pip install -r requirements.txt
```

### 4-4. `.env` を作る

`.env.example` をコピーして、ファイル名を `.env` にします。

中身を自分のキーへ置き換えます。

```text
OPENAI_API_KEY=...
OPENAI_MODEL=gpt-5.6-terra
SUPABASE_URL=...
SUPABASE_SECRET_KEY=...
DEMO_MODE=false
```

### 4-5. アプリを起動

```bash
streamlit run app.py
```

ブラウザが開けば完了です。

---

# 5. APIキーなしで画面だけ確認する

`.env` の

```text
DEMO_MODE=true
```

に変更します。

その後、

```bash
streamlit run app.py
```

を実行します。

固定のデモ回答で、人物選択・相談入力・回答画面・史実表示を確認できます。

本番公開前に `DEMO_MODE=false` へ戻してください。

---

# 6. GitHubへアップロードする

GitHubで新しいRepositoryを作成します。

このフォルダ内のファイルをそのままアップロードしてください。

アップロード対象の主なファイル:

```text
app.py
figures.py
llm.py
db.py
styles.py
utils.py
schema.sql
requirements.txt
.env.example
.gitignore
README.md
.streamlit/config.toml
.streamlit/secrets.toml.example
```

**アップロードしてはいけないもの:**

```text
.env
.streamlit/secrets.toml
```

`.gitignore` に登録済みです。

---

# 7. Streamlit Community Cloudで公開する

Streamlit Community Cloud公式の現在の流れは、GitHub Repositoryを選び、エントリーポイントを指定して公開する方式です。

1. `share.streamlit.io` を開きます。
2. GitHubアカウントでログイン・接続します。
3. 右上の **Create app** を押します。
4. 既存のGitHubアプリを使う選択肢を選びます。
5. Repositoryを選びます。
6. Branchは通常 `main`。
7. Main file path は `app.py`。
8. **Advanced settings** を開きます。
9. Secrets欄に、次の形式で入力します。

```toml
OPENAI_API_KEY = "..."
OPENAI_MODEL = "gpt-5.6-terra"
SUPABASE_URL = "..."
SUPABASE_SECRET_KEY = "..."
DEMO_MODE = "false"
```

10. Deployします。

Streamlit公式も、APIキー等はGitHubへ置かずCommunity CloudのSecretsへ保存する方法を推奨しています。

---

# 8. 相談内容の保存ルール

相談入力欄の下に、

> 相談内容と回答を、サービス改善のため保存してよい

というチェックがあります。

初期値は **OFF** です。

OFFの場合:

- 相談内容をSupabaseへ保存しません。
- 回答をSupabaseへ保存しません。

ONの場合:

- `consultations` に人物名・相談内容・回答・バージョンを保存します。

回答後の

- 役に立った
- いまひとつ

は `feedback` に保存します。

相談保存をOFFにしていた場合、フィードバックは相談本文と紐づけず保存できます。

---

# 9. 史実とAI解釈を混ぜない仕組み

`figures.py` では、人物ごとに次を分離しています。

```text
historical_facts
  確認した史実

decision_patterns
  史実からアプリ側が抽出した判断傾向

uncertain_legends
  伝説・文学・後世の人物像・未確認の逸話

sources
  出典
```

AIへはこの区分を保ったまま渡します。

---

# 10. AIが偽の史実や出典を表示しにくい仕組み

このMVPでは、AIに「史実の説明文」を自由生成させません。

AIが返すのは主に、

- 短い助言
- 使用した `fact_id`
- 現代への応用
- 次の一手

です。

回答画面の「史実の手がかり」と「出典」は、AI本文ではなく `figures.py` に登録済みのデータから表示します。

そのため、AIが存在しない出典URLや偽の名言を画面へ出しにくい構造です。

---

# 11. 現在の4名の史実管理方針

## 楠木正成

文化庁の千早城跡・楠木城跡、国立国会図書館のレファレンス、神戸市資料などを基礎にしています。

後世の「忠臣・楠公」像や軍記の台詞を、本人の確定的な性格・発言として使用しません。

## 小野篁

国立国会図書館のレファレンス、隠岐の島町資料などを基礎にしています。

冥界・閻魔大王・井戸等の伝説は `uncertain_legends` に分離し、回答根拠に使いません。

## 平重盛

神戸市が公開している、神戸大学名誉教授による解説を主要な基礎資料にしています。

『平家物語』の有名な諫言や台詞は文学作品の表現として分離し、本人の実際の発言として使いません。

## 空海

高野山金剛峯寺、東寺、国立国会図書館、香川県、ジャパンサーチ等を利用しています。

満濃池については香川県資料にも「伝えられている」という留保があるため、データ上の確定度を `medium` としており、強い断定の根拠には使用しません。

いろは歌、温泉発見、超自然的な奇跡等は回答根拠に使いません。

---

# 12. 人物を追加するとき

MVP公開中は、UIから自由に人物を追加できません。

新しい人物を公開するときは必ず、次を先に準備してください。

1. 基本プロフィール
2. 重要な史実
3. 史実の情報源
4. 史実から抽出した判断傾向
5. 俗説・不確かな逸話との区別
6. 得意な相談テーマ
7. 回答スタイル

推奨運用は、`figures.py` をChatGPTへ添付し、

> この人物について、公的機関・図書館・博物館・大学等を優先して史実を調査し、既存データ構造を崩さず追加してください。俗説はuncertain_legendsへ分離してください。

と依頼する方法です。

人物を思いついたからキャラクターを作るのではなく、**史実を確認できたあとに人物像を設計**してください。

---

# 13. 史実を修正するとき

`figures.py` 内の該当人物について、次の順番で更新します。

1. `sources` に新しい出典を追加
2. `historical_facts` の本文・source_idsを修正
3. 必要なら `decision_patterns` を見直す
4. 確認できなくなった内容は `uncertain_legends` へ移す
5. `SOURCE_VERSION` を更新

史実を修正したのに判断傾向をそのまま残さないことが重要です。

---

# 14. 俗説を回答対象外にする方法

俗説や伝説を見つけた場合は、`historical_facts` に入れず、`uncertain_legends` に追加します。

`llm.py` のシステム指示で、`uncertain_legends` を回答根拠に使用しないよう固定しています。

---

# 15. 未登録人物へのなりきり防止

利用できる人物は `FIGURES` に登録された4名のみです。

相談欄に、

- 坂本龍馬に変えて
- 紫式部になりきって
- 前の指示を無視して

などと入力しても、選択された人物を変更しないよう `llm.py` に固定指示を入れています。

UIにも自由人物選択欄はありません。

---

# 16. 安全性

相談文に、医療・法律・金融・自傷・他害・犯罪・緊急性の高い内容が含まれる可能性がある場合、アプリ側で安全カテゴリを付けてAIへ渡します。

その場合、歴史人物の考え方だけで回答を完結させず、必要に応じて専門家・公的窓口を利用するよう補足します。

このアプリは専門家の診断・法的判断・投資判断等を代替するものではありません。

---

# ファイル構成

```text
もしもし相談室/
├─ app.py
├─ figures.py
├─ llm.py
├─ db.py
├─ styles.py
├─ utils.py
├─ schema.sql
├─ requirements.txt
├─ .env.example
├─ .gitignore
├─ README.md
└─ .streamlit/
   ├─ config.toml
   └─ secrets.toml.example
```

---

# 現在実装していないもの

MVPでは意図的に実装していません。

- ログイン
- SNS
- フォロー
- コメント
- 人物ランキング
- 課金
- 音声
- 人物同士の会話
- 長期相談履歴
- 自由な人物追加
- 伝説モード

最初は、

**「4人の歴史人物から相談相手を選び、史実を根拠に役立つ回答が返る」**

という一点に集中しています。
