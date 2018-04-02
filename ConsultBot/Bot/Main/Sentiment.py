def sent_match(text, posWords, negWords, negators_bank): 
    Total = 0
    phrase = text.split()
    Negate = False
    Sentiment = ""
    for i in range(1,len(phrase)):
            # If our knowledge base has the word's sentiment
            word = phrase[i]
            if word in posWords:
                Total = +1
            elif word in negWords:
                Total = -1
            elif word in negators_bank:
                Negate = True
    
    if Negate == True and Total > 0:
        Sentiment = "Negative"
    elif Negate == False and Total > 0:
        Sentiment = "Positive"
    elif Negate == True and Total < 0:
        Sentiment = "Positive"
    elif Negate == False and Total < 0:
        Sentiment = "Negative"
    else:
        Sentiment = "Neutral"

    return Sentiment
