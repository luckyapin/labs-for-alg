import requests
from bs4 import BeautifulSoup
import re
import time
import boyer
import wikipedia


# link = "https://ru.wikipedia.org/wiki/Логика"
# f = requests.get(link).text
# soup = BeautifulSoup(f, features="html.parser")
# p_li_tags = soup.find_all(['p', 'li'])
# p_tags_text = [tag.get_text() for tag in p_li_tags]
# article = ' '.join(p_tags_text)
# words_in_article = re.findall("\w+-{0,1}\w+|[а-яё]+|[a-z]+", article, flags=re.IGNORECASE)

ref = open("Логика.txt", 'r')
words_in_ref = re.findall("\w+-{0,1}\w+|[а-яё]+|[a-z]+", ref.read(), flags=re.IGNORECASE)
wikipedia.set_lang("ru")
wiki_page = wikipedia.page("Логика").content
words_in_article = re.findall("\w+-{0,1}\w+|[а-яё]+|[a-z]+", wiki_page, flags=re.IGNORECASE)


c=0

start_time = time.time()
for i, pat in enumerate(words_in_ref):
    if len(words_in_ref)-2<i:
        break
    c += boyer.boyer(words_in_article, words_in_ref[i:i+3])

print(str(c/len(words_in_article)*100)+"%")
print("--- %s seconds ---" % (time.time() - start_time))
