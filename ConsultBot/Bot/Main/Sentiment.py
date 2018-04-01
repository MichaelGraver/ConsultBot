def sent_match(text, posWords, negWords, negators_bank): 
    Total = 0
    phrase = text.split()
    
    for i in range(1,len(phrase)):
            # If our knowledge base has the word's sentiment
            word = phrase[i]
            if word in posWords:
                Total = +1
            elif word in negWords:
                Total = -1
    
    if Total > 0:
        Sentiment = "Positive"
    elif Total < 0:
        Sentiment = "Negative"
    else:
        Sentiment = "Neutral"

    return Sentiment
