"""Generate Markov text from text files."""

from random import choice


def open_and_read_file(file_path):
    """Take file path as string; return text as string.

    Takes a string that is a file path, opens the file, and turns
    the file's contents as one string of text.
    """

    # your code goes here
    long_text=''
    with open(file_path) as f:
        for line in f:
            line=line.replace("\n"," ")
            long_text+=line

    return long_text

def make_chains(text_string):
    """Take input text as string; return dictionary of Markov chains.

    A chain will be a key that consists of a tuple of (word1, word2)
    and the value would be a list of the word(s) that follow those two
    words in the input text.

    For example:

        >>> chains = make_chains('hi there mary hi there juanita')

    Each bigram (except the last) will be a key in chains:

        >>> sorted(chains.keys())
        [('hi', 'there'), ('mary', 'hi'), ('there', 'mary')]

    Each item in chains is a list of all possible following words:

        >>> chains[('hi', 'there')]
        ['mary', 'juanita']

        >>> chains[('there','juanita')]
        [None]
    """

    chains = {}

    # your code goes here
    words=text_string.strip().strip("\n").split(" ")
    for i in range(0,len(words)-2):
        key_phrase=(words[i],words[i+1])
        next_word=words[i+2]
        chains[key_phrase]=chains.get(key_phrase,[])+[next_word]


    return chains


def make_text(chains):
    """Return text from chains."""
        

    words = []

    # your code goes here
    pair = list(chains.keys())[0]
    words+=[pair[0],pair[1]]
    
    while chains.get(pair,False):
        next_word=choice(chains[pair])
        words.append(next_word)
        chains[pair].remove(next_word)
        pair=(pair[1],next_word)

    print(words)
    return ' '.join(words)


input_path = 'gettysburg.txt'

# Open the file and turn it into one long string
input_text = open_and_read_file(input_path)

# Get a Markov chain
chains = make_chains(input_text)
for chain in chains:
    print(chain,chains[chain])

# Produce random text
random_text = make_text(chains)

# print(random_text)
