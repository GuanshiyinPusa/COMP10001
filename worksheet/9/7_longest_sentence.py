def longest_sentence_length(text):
    sentences = text.split('.')
    return max(len(sentence.split()) for sentence in sentences)

        