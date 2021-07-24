import MeCab
import matplotlib.pyplot as plt
import pandas as pd
from wordcloud import WordCloud


def word_cloud(df, column_name):
    # MeCab準備
    tagger = MeCab.Tagger()
    tagger.parse("")

    # 全テキストデータを結合
    all_text = ""
    for s in df[column_name]:
        all_text += s

    node = tagger.parseToNode(all_text)

    # 名詞を抽出しリストに
    word_list = []
    while node:
        word_type = node.feature.split(",")[0]
        if word_type == "名詞":
            word_list.append(node.surface)
        node = node.next

    # リストを文字列に変換
    word_chain = " ".join(word_list)

    # ストップワード（除外するワード）の作成
    stopwords = [""]

    # ワードクラウド作成
    W = WordCloud(
        font_path="/System/Library/Fonts/ipaexg.ttf",
        width=500,
        height=500,
        prefer_horizontal=0.8,  # 横書きで配置することを試す確率 (デフォルト0.9)
        background_color="white",
        colormap="tab20",
        stopwords=set(stopwords)
        ).generate(word_chain)

    plt.figure(figsize=(15, 12))
    plt.imshow(W)
    plt.axis("off")
    plt.savefig("wordcloud.png", dpi=100)
    plt.close()
