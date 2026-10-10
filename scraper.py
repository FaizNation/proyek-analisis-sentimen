from google_play_scraper import Sort, reviews
import pandas as pd
import os

result, continuation_token = reviews(
    'com.bcadigital.blu',
    lang='id', 
    country= 'id',
    sort=Sort.MOST_RELEVANT,
    count=10000,
    filter_score_with= None
)

data = pd.DataFrame(result)

print("Jumlah data:", len(data))

data = data[['content', 'score']]

print(data.head())

data = data.rename(columns={'content': 'ulasan', 'score': 'label'})
print(data.head())

current_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(current_dir, "dataset_ulasan_blubca.csv")
data.to_csv(file_path, index=False, encoding='utf-8')

dataShopee = pd.read_csv(file_path)
print(dataShopee.head())
