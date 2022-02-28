from flask import Flask, request, jsonify
from flask_cors import CORS
from rutermextract import TermExtractor
from typing import List
from genQoute import genQoute 

app = Flask(__name__)
CORS(app)


def analyz(text: str) -> List[str]:
    term_extractor = TermExtractor()
    definition_list: List[str] = list()
    for term in term_extractor.__call__(text, nested=True):
        definition_list.append(term.normalized)
        #print(str(term.normalized.split(' ')))
    return definition_list

@app.route('/')
def root():  # put application's code here
    return "Генерация цитат по смыслу"

@app.route('/gq', methods=['POST'])
def ke():
    text = request.json
    text = text['text']
    definition_list = analyz(text)
    # print(definition_list) 
    str1=""

    return jsonify(str1), 200, {'Content-Type': 'application/json'}

if __name__ == '__main__':
    app.run(host='0.0.0.0')
app.run(host='0.0.0.0')


