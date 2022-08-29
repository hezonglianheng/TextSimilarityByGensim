from spacy.lang.en import English
import csv
from collections import defaultdict
import re


def get_docs():
    csv.field_size_limit(500 * 1024 * 1024)
    with open(r'fake.csv', mode='r+',
              encoding='utf8', newline='') as file:
        reader = csv.reader(file)
        dictionary = defaultdict(int)
        all_titles = []
        all_files = []
        url_str = r'http.+'
        for row in reader:
            if row[6] == 'english' and row[4] != '':
                all_titles.append(row[4])
                news_text = row[5].lower()
                url_match = re.match(url_str, news_text)
                if url_match:
                    news_text = news_text[:url_match.start()] + news_text[url_match.end():]
                nlp = English()
                doc = nlp(news_text)
                text = []
                for token in doc:
                    if (not token.is_stop) and (not token.is_space) \
                            and (not token.is_punct):
                        dictionary[str(token)] += 1
                        text.append(str(token))
                all_files.append(text)
        for text in all_files:
            for word in text:
                if dictionary[word] == 1:
                    text.remove(word)
        return all_files, all_titles


if __name__ == "__main__":
    print(get_docs())