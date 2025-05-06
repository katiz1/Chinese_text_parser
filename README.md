# Chinese Text Analysis with Jieba and Python

About the Project

This project analyzes the Chinese text "紅樓夢" (Dream of the Red Chamber) by Xueqin Cao, one of China's most famous works of literature. The goal is to apply natural language processing (NLP) techniques to break down the text, count how often each word appears, and identify common word pairs (bigrams).
Using Python and the Jieba library, the project segments the Chinese text into individual words. The frequency of each word is calculated using pandas and Counter, showing how often each word appears. This analysis helps uncover language patterns in Chinese texts and lays the groundwork for further exploration in computational linguistics and NLP.

## Tools Used

    Python
    Jieba – for Chinese word segmentation
    pandas 
    Counter  
    matplotlib / seaborn 
    wordcloud 
    Noto Sans SC  – for showing Chinese characters correctly in the word cloud

    1. Create a Virtual Environment
    
    2. Install Required Libraries: 
    pip install jieba pandas matplotlib seaborn wordcloud
    
    3.Add a Chinese Font
    Download a Chinese font Noto Sans SC from Google Fonts. Place the .ttf file in the same folder as the script.
    
    4. Download a Chinese story (I used 《紅樓夢》 from Project Gutenberg) and save it as a .txt file in the same folder.
    
    5.Open the text and tokenize it with Jieba
    
    6. Use Counter from the collections module to count the frequency of each word
    
    7. Create a Pandas DataFrame
    
    8. Save the DataFrame to a CSV File

## When you run the script:

    - It reads and segments the Chinese text.
    - Saves a CSV file (word_frequencies.csv) with the word frequencies.
    - Generates a word cloud image (wordcloud.png) to show the most common words.
    - Creates a bar chart (top20_words.png) for the top 20 most frequent words.
    - Prints the top bigrams (frequent word pairs) in the terminal.

## Special thanks

    Project Gutenberg - for the open-access Chinese texts.

    Jieba - for making Chinese word segmentation easy to use.
