import wikipedia


article_name = input("Podaj nazwę artykułu na Wikipedii: ")
article_page = wikipedia.page(article_name)
print("\n" + article_page.url)
print("\n" + article_page.summary)
