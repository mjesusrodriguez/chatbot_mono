#hace el reconocimiento de intent con ChatGPT
import json
import openai
from openai_config import setup_openai

model_engine = setup_openai()

def intentRecWithChatGPT(input):
    #prompt="for the following input \""+input+"\" give me a JSON with only an intent of the user between those: BookRestaurant, PlayMusic, AddToPlayList, RateBook, SearchScreeningEvent, GetWeather, SearchCreativeWork"
    prompt = "You are a chatbot in the restaurant domain, and your task is to determine the intent behind a user's input or query. Below is a list of intents related to the restaurant domain: BookRestaurant, RestaurantInformation, FindRestaurant, OrderFood. Given the input '"+input+"', determine the intent of the user based on the provided intents, return a JSON with only one. Consider that users often want to make reservations when specifying a type of restaurant."
    completion = openai.Completion.create(
        engine=model_engine,
        prompt=prompt,
        temperature=0.3,
        max_tokens=64,
        top_p=1,
        frequency_penalty=0.5,
        presence_penalty=0)
    response = completion.choices[0].text
    print(response)

    #Proceso JSON
    data = json.loads(response)
    intent = data["intent"]
    return intent