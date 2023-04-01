from quote import quote
import random

def getQuote():
    res = quote('family', limit=20)
    quote_index = random.randint(0,20)
    obtained_quote = res[quote_index]["quote"]
    author = res[0]["author"]
    feed = f'Here is a quote by {author}. {obtained_quote}'
    return feed

