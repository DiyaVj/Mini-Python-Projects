import wolframalpha
import wikipedia
import pyautogui


while True:
    inp = input("How can i help you?: ")

    try:
        app_id = "P4Y3RQ-K2EAVLHTHQ"
        client = wolframalpha.Client(app_id)
        result = client.query(inp)
        answer = next(result.results).text
        print(answer)
    except:
        print(wikipedia.summary(inp))