import wikipedia
import wolframalpha
while True:
    input = raw_input("Your Ques plz:  ")
    try:
        #wolframalpha
        app_id = "RJEUEA-U2HHRPRXGL"
        client = wolframalpha.Client(app_id)
        res = client.query(input)
        ans = next(res.results).text
        print (ans)

    except:
        #wikipedia
        print wikipedia.summary(input, sentences=5)
