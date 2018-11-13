import wolframalpha

input = raw_input("What's Your Question:  ")
app_id = "RJEUEA-U2HHRPRXGL"
client = wolframalpha.Client(app_id)
res = client.query(input)
ans = next(res.results).text

print (ans)
