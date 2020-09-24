import dialogflow_v2beta1 as dialogflow
import json
import os
from google.protobuf.json_format import MessageToJson


GOOGLE_AUTHENTICATION_FILE_NAME = "service_account.json"
current_directory = os.path.dirname(os.path.realpath(__file__))
path = os.path.join(current_directory, GOOGLE_AUTHENTICATION_FILE_NAME)
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = path
response_string=''
projectid = 'testbot-bvckpr'
language_code = 'en-US'
session_id = 'uuid-12345' #Some session value
inputtext='Hello'

def detect_intent_text(texts,projectid,sessionid,language_code):

    session_id = sessionid
    texts = texts

    session_client = dialogflow.SessionsClient()
    session = session_client.session_path(projectid, session_id)
    text_input = dialogflow.types.TextInput(text=texts, language_code=language_code)
    query_input = dialogflow.types.QueryInput(text=text_input)
    output_audio_config = dialogflow.types.OutputAudioConfig(
            audio_encoding=dialogflow.enums.OutputAudioEncoding
            .OUTPUT_AUDIO_ENCODING_LINEAR_16)

    response = session_client.detect_intent(session=session, query_input=query_input,output_audio_config=output_audio_config)
    
    print(response.output_audio) #Obtaining the audio output binary
    # The response's audio_content is binary.
    with open('output.wav', 'wb') as out:
        out.write(response.output_audio)
        print('Audio content written to file "output.wav"')
    
    
    json_response = MessageToJson(response)
    #json_response is the complete response obtained from DialogFlow as a JSON
    return 200#(json.dumps(json_response))

#Call the detect intent text method
response_string =  detect_intent_text(inputtext,projectid,session_id,language_code)
print(response_string)

