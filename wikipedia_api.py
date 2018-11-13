import wikipedia

while True:
    input = raw_input("Your Ques plz:  ")
    print wikipedia.summary(input, sentences=1)
