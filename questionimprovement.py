import openai
from openai_config import setup_openai

model_engine = setup_openai()

#Mejora la pregunta realizada, con ChatGPT
def improveQuestionchatGPT(question):
    # manejar el prompt para que devuelva un json con parámetros faltantes.
    prompt = "Give me only one alternative question for this one in the scope of restaurant booking: " + question

    # Generate a response
    completion = openai.Completion.create(
        engine=model_engine,
        prompt=prompt,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.8,
    )
    response = completion.choices[0].text

    if not response:
        response = question

    return response