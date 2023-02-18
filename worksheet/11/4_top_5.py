def top5_words(text):
    # Split text into words
    words = text.split()
    
    # Count the frequency of each word
    freqs = {}
    for word in words:
        freqs[word] = freqs.get(word, 0) + 1
    
    # Sort the words by frequency (descending) and alphabetically (ascending)
    sorted_words = sorted(freqs.items(), key=lambda x: (-x[1], x[0]))
    
    # Return the top 5 words
    return [w for w, f in sorted_words[:5]]