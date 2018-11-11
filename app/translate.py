# -*- coding: utf-8 -*-
import json, requests
from flask_babel import _
from app import app

def translate(text, source_language, dest_language):
    if 'MS_TRANSLATOR_KEY' not in app.config or not app.config['MS_TRANSLATOR_KEY']:
        return _('Error: the translation service is not configured.')
    auth = {'Ocp-Apim-Subscription-Key': app.config['MS_TRANSLATOR_KEY'],
            'Content-Type': 'application/json'
            }
    r = requests.post('https://api.cognitive.microsofttranslator.com/translate?api-version=3.0&from={}&to={}'.format(source_language, dest_language),
        headers=auth, json=[{'text':text}])
    if r.status_code != 200:
        return _('Error %(code)s: the translation service failed.', code=r.status_code)
    return (json.loads(r.content))[0]['translations'][0]['text']
