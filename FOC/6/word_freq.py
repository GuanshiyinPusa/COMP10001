def word_freq(text):
    freq = {}
    for word in text.split():
        word = word.strip() # remove the leading whitespaces 

        if word not in freq:
            freq[word] = 1
        else:
            freq[word] += 1
    return freq

print(word_freq("Hello world! Have a nice day!"))
