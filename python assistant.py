import wolframalpha
import wikipedia



input=("Question :")

app_id="AWV4E2-JQ2J9Q9RHA"

client=wolframalpha.Client(app_id)

res=client.query(input)

answer=next(res.results).text

print(answer)



input=("Q :")

print(wikipedia.summary(input))
