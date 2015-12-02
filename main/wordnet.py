from nltk.corpus import wordnet as wn

def swap_with_ant(token):
    synsets = wn.synsets(token)
    if not synsets:
        return token

    lemmas = synsets[0].lemmas()
    if not lemmas:
        return token

    antonyms = lemmas[0].antonyms()
    if not antonyms:
        return token

    return antonyms[0].name()

if __name__ == '__main__':
    print swap_with_ant('happy')
