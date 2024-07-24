import json
import openai
from bson import ObjectId
from mongo_config import get_database
from openai_config import setup_openai

model_engine = setup_openai()

# Obtener la base de datos
db = get_database()
# Obtener la colección de servicios de restaurantes
restaurant_sv = db.restaurant

def impSlotFillingChatGPT(input, service, intent, userAnswers = None):
    # Busco el servicio por id
    document = restaurant_sv.find_one({"_id": ObjectId(service)})
    document_str = str(document)
    json_wsl = json.dumps(document_str)
    if userAnswers is not None:
        userAnswers_str = json.dumps(userAnswers)
        #prompt = "Forget the information provided in our previous interactions. Provided the prompt: \""+ input +"\", these previous inputs during the conversation: " + userAnswers_str + " and the API specification: "+ json_wsl +", which contains an endpoint called /"+intent+"' with a list of parameters, give me a JSON list with the slots and the values that are given in the prompt directly. If the value is not given, give the value \"Null\" the key of the dictionary is the parameter name and the value, the parameter value"
        prompt = "Forget the information provided in our previous interactions. Provided the prompt: \""+ input +"\", these previous inputs during the conversation: " + userAnswers_str + " and the API specification: "+ json_wsl +", which contains an endpoint called /"+intent+"' with a list of parameters, give me a JSON list with the slots and the values that are given in the prompt directly. If the value is not given, give the value \"Null\" the key of the dictionary is the parameter name and the value, the parameter value"
    else:
        prompt = "Forget the information provided in our previous interactions. Provided the prompt: \""+ input +"\", and the API specification: "+ json_wsl +", which contains an endpoint called /"+intent+"' with a list of parameters, give me a JSON list with the slots and the values that are given in the prompt directly. If the value is not given, give the value \"Null\" the key of the dictionary is the parameter name and the value, the parameter value"

    print(prompt)
    # Generate a response
    completion = openai.Completion.create(
        engine=model_engine,
        prompt=prompt,
        temperature=0,
        max_tokens=1024,
        n=1
    )
    response = completion.choices[0].text
    print("RESPUESTA CHATGPT")
    print(response)
    return response