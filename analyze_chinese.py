from wordcloud import WordCloud
import matplotlib.pyplot as plt
import pandas as pd
from collections import Counter
import jieba


with open("Chinese_story.txt", encoding="utf-8") as f:
    text = f.read()

words = jieba.cut(text)

cleaned_words = [word.strip() for word in words if word.strip() and len(word.strip()) > 1]

word_counts = Counter(cleaned_words)

word_frequencies = pd.DataFrame(word_counts.items(), columns=['word', 'frequency'])

word_frequencies.to_csv("word_frequencies.csv", index=False)

wordcloud = WordCloud(
    font_path="NotoSansSC-VariableFont_wght.ttf",  
    width=800,
    height=400,
    background_color="white",
    collocations=False,  
    max_words=200,  
    max_font_size=100  
).generate_from_frequencies(word_counts)

wordcloud.to_file("wordcloud.png")

top_20_words = word_frequencies.nlargest(20, 'frequency')
plt.figure(figsize=(10,6))
plt.bar(top_20_words['word'], top_20_words['frequency'])
plt.xticks(rotation=90)
plt.title('Top 20 Most Frequent Words')
plt.tight_layout()
plt.savefig("top20_words.png")

print("word_frequencies.csv, wordcloud.png, and top20_words.png")
