from google_search import *
from word_cloud import *


if __name__ == "__main__":
    search_keyword = "python"
    num_search = 200
    df = google_search(search_keyword, num_search)
    column_name = "タイトル"
    word_cloud(df, column_name)
