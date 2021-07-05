
'''Wordsfilter - A powerfull word filter tool for Python 3 (open source).
'''

__version__ = 0.1


def wordsfilter(list, post):
    '''This is wordlist filter for django projects. It takes a list of word for filtering and post string.
    '''
    char = [
        '.', ',', ';', ':', '"', '\'', '/', '[', ']', '{', '}', '(', ')', '~', '`', '!', '@', '#', '$', '%', '^', '&', '*', '-', '_', '=', '+', '?'
    ]
    number, words = 0, []
    post = post.lower()
    for j in char:
        post = post.replace(j, ' ')
    post = post.split(' ')
    for word in post:
        if word in list:
            number += 1
            words.append(word)
    return (number, words)
