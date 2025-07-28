import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from wordcloud import WordCloud
import nltk
import string
from nltk.corpus import stopwords

nltk.download("stopwords")

df = pd.read_csv("datasets/fake reviews dataset.csv", encoding='ISO-8859-1')
df = df.head(200)


grouped = df.groupby("rating").size()
print(grouped)


def clean_text(text):
    
    text = text.lower()
    text = text.translate(str.maketrans('', '', string.punctuation))  # Remove punctuation
    tokens = text.split()
    tokens = [word for word in tokens if word not in stopwords.words('english')]  # Remove stopwords
    return " ".join(tokens)


df['CleanText'] = df['text_'].apply(clean_text)
print(df['CleanText'])

five_star = " ".join(df[df["rating"] == 5]["CleanText"])
four_star = " ".join(df[df["rating"] == 4]["CleanText"])
three_star = " ".join(df[df["rating"] == 3]["CleanText"])
two_star = " ".join(df[df["rating"] == 2]["CleanText"])
one_star = " ".join(df[df["rating"] == 1]["CleanText"])


fivewc = WordCloud(width=800, height=400, background_color="white", colormap="Blues").generate(five_star)
fourwc = WordCloud(width=800, height=400, background_color="white", colormap="RdYlBu_r").generate(four_star)
threewc = WordCloud(width=800, height=400, background_color="white", colormap="Purples_r").generate(three_star)
twowc = WordCloud(width=800, height=400, background_color="white", colormap="Oranges").generate(two_star)
onewc = WordCloud(width=800, height=400, background_color="white", colormap="Greens").generate(one_star)


fig, axs = plt.subplots(3, 2, figsize=(8, 5))

axs[0, 0].imshow(fivewc)
axs[0, 0].set_title("5 Stars")

axs[0, 1].imshow(fourwc)
axs[0, 1].set_title("4 Stars")

axs[1, 0].imshow(threewc)
axs[1, 0].set_title("3 Stars")

axs[1, 1].imshow(twowc)
axs[1, 1].set_title("2 Stars")

axs[2, 0].imshow(onewc)
axs[2, 0].set_title("1 Star")
axs[2, 1].axis('off')

plt.tight_layout()
plt.show()
