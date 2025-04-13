import jieba
import pandas as pd
from collections import Counter


with open("chinese_story.txt", "r", encoding="utf-8") as f:
    text = f.read()


words = jieba.cut(text) 


word_freq = Counter(words)


df = pd.DataFrame(word_freq.items(), columns=["word", "frequency"])


df.to_csv("chinese_word_frequencies.csv", index=False, encoding="utf-8-sig")

print(df)
