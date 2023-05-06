作成途中であり, 研究内容を活かしたアプリを制作予定です.
関連した内容を学会で発表 (6月) 予定であり, 発表後にコードを公開したいと考えており,
現在は <code>REAME.md</code>ぐらいしかありません.

研究のアブストラクト (公開済み)

```txt
近年, 株価や為替レートといった時系列データを対象にその変動を人工知能により予測する研究が盛んになされている.
時系列データの 1 つにトレーディングカードゲーム (Trading Card Game: TCG) に用いられるカードの価格がある.
TCG とは攻撃値や能力を表す文章が記述された専用のカードを用いて対戦するゲームであり,
ゲームの魅力のみならず価格の変動性も注目を集めている.
こうした背景から, TCG のカードの価格変動を機械学習手法により予測する研究がいくつかなされているが,
深層学習を用いたものはほとんど存在しない. また, TCG のカードにおいて価格が上昇するものは少数であり,
モデルの学習においてはデータの不均衡さが課題となる. カードの価格変動においてはカードの能力を表す数値やテキストのデータに加えて,
レアリティや発売時期, 過去の価格などの多様なデータが要因となっている.
そこで, 本研究ではマルチモーダルデータと深層学習を用いてカードの価格上昇の有無を予測するモデルを提案し, その有効性を示す.
```

## 目次
- [目次](#目次)
- [環境構築](#環境構築)
- [streamlit とは？](#streamlit-とは)
## 環境構築

```
pip install streamlit
streamlit hello
```
<a id="env"></a>
## streamlit とは？

<a href="https://streamlit.io/">streamlit</a>とは Web アプリケーションを開発するためのフレームワークの 1 つである。UI の構築を HTML や CSS を用いることなく実装することができ、機械学習などのデータサイエンスを用いたアプリの開発向けになっている。

ウィジェットを容易に実装することができ、

```Python
st.title('Hello Streamlit')
st.sidebar.title("設定")
uploaded_file = st.sidebar.file_uploader("ファイル選択", type="csv")
```

と記述すると図1のようになります。
<div align="center">
<figure style="text-align:center;">
<img src="./img/ex_streamlit_widget.png" style="height:200pt; display:block">
<figcaption style="display:block">
図1 streamlit を用いたウィジェットの実装例
</figcaption>
</figure>
</div>
