import numpy as np
import pandas as pd
from os import path
from PIL import Image
import cv2
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator
import csv
import matplotlib.pyplot as plt
import random

# View word frequency
# df = pd.read_csv(r"words.csv", sep=',', names=['freq'], index_col=0)
# print(df.head())
# df_sort = df.sort_values('freq', ascending=False)
# df_sort.plot.bar()
# plt.xticks(rotation=50)
# plt.xlabel("Words")
# plt.ylabel("Freq.")
# plt.show()

# Generate text
with open(r"words.csv") as file:
    text = csv.reader(file)
    text = list(text)
    text[0][0] = 'Polymer'

words = []
for row in text:
    for _ in range(round(100*float(row[1]))):
        words.append(row[0])

random.shuffle(words)
words = ' '.join([str(elem) for elem in words])


# Create and generate a word cloud image:
mask = cv2.imread(r"C:\Users\nicep\Desktop\Reseach_Post\Documents\Poly_Dat\cript-docs\Figure_Gen_Codes\cloud.png")
wordcloud = WordCloud(background_color=None, mode='RGBA', max_font_size=180, min_font_size=30, mask=mask, color_func=lambda *args, **kwargs: (255,255,255), collocation_threshold=2)  # min_font_size=4, max_font_size=20, background_color="white"
wordcloud.generate(words)

# Display the generated image:
pic = cv2.imread(r"C:\Users\nicep\Desktop\Reseach_Post\Documents\Poly_Dat\cript-docs\Figure_Gen_Codes\cloud_red.png")
pic = cv2.cvtColor(pic,  cv2.COLOR_BGR2RGB)
plt.imshow(pic)
plt.imshow(wordcloud)
plt.axis("off")
plt.savefig('word_cloud.png', format='png', dpi=1200)
plt.show()





