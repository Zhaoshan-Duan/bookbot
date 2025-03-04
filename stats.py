def get_word_count(text):
    return len(text.split())

def character_occurence(text):
    freq = {}
    for c in text.lower():
        freq[c] = freq.get(c, 0) + 1

    return freq
