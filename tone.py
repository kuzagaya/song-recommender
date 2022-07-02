from ibm_watson import ToneAnalyzerV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from config import LAST_FM_API

def tone_analize(txt):
    API_KEY = LAST_FM_API
    url='https://api.eu-gb.tone-analyzer.watson.cloud.ibm.com/instances/06321b09-0687-4fdf-b231-a9becf6e8e88'

    authenticator = IAMAuthenticator(API_KEY)

    tone = ToneAnalyzerV3(
      version = '2021-10-09',
      authenticator = authenticator
    )
    tone.set_service_url(url)

    text = txt

    response = tone.tone(text).get_result()
    return response

def tone_dict(text):
    response = tone_analize(text)
    response = response['document_tone']['tones']
    tones = {'Tone': [],'Score':[]}
    for dict in response:
        tones['Tone'].append(dict['tone_name'])
        tones['Score'].append(dict['score'])
    return tones