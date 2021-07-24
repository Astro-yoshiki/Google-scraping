import requests
import bs4
import pandas as pd


def google_search(search_keyword, num_search):
    print("【検索した単語】{}".format(search_keyword))

    # 検索順位取得処理
    # Google検索の実施
    search_url = f"https://www.google.co.jp/search?hl=ja&num={num_search}&q=" + search_keyword
    res_google = requests.get(search_url)
    # Responseオブジェクトが持つステータスコードが200番台(成功)以外だったら、エラーメッセージを吐き出してスクリプトを停止します。
    res_google.raise_for_status()
    print("Google検索結果を取得")

    # res_google.textは、検索結果のページのHTML
    bs4_google = bs4.BeautifulSoup(res_google.text, "html.parser")
    google_search_page = bs4_google.select("div.kCrYT>a")

    # rank:検索順位
    rank = 1
    site_rank = []
    site_title = []
    site_url = []

    for site in google_search_page:
        try:
            site_title.append(site.select("h3.zBAuLc")[0].text)
            site_url.append(site.get("href").split("&sa=U&")[0].replace("/url?q=", ""))
            site_rank.append(rank)
            rank += 1
        except IndexError:
            continue

    print("以上")

    df = pd.DataFrame({"順位": site_rank, "タイトル": site_title, "URL": site_url})
    df.to_csv("keyword.csv", index=False)

    return df
