import helper
import gold

def parse_content(content):
    '''Convert input into a dictionary word: number'''
    content_dict = {word: float(freq) for string in content.splitlines() for word, freq in [string.split()]}
    return content_dict

def make_tree(words):
    '''Creates trie-like nested dictionary'''
    words_trie ={}
    for key, value in words.items():
        for i, char in enumerate(key):
            if char not in words_trie:
                words_trie[char] = set()
            words_trie = words_trie[char]
        words_trie['$' + key] = value
                
    return words_trie

def predict(tree, numbers):
    return {}


if __name__ == '__main__':
    content = helper.read_content(filename='ngrams-10k.txt')

    # When you've finished implementing a part, remove the `gold.` prefix to check your own code.

    # PART 1: Parsing a string into a dictionary.
    words = gold.parse_content(content)

    # PART 2: Building a trie from a collection of words.
    tree = gold.make_tree(words)

    while True:
        # PART 3: Predict words that could follow
        numbers = helper.ask_for_numbers()
        predictions = gold.predict(tree, numbers)

        if not predictions:
            print('No words were found that match those numbers. :(')
        else:
            for prediction, frequency in predictions[:10]:
                print(prediction, frequency)

        response = input('Want to go again? [y/N] ')
        again = response and response[0] in ('y', 'Y')
        if not again:
            break
