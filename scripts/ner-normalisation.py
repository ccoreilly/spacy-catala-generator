import json
import random

train = []
test = []

with open('./datasets/ca/wikiann-ca.json') as json_file:
    data = json.load(json_file)

    ner_tokens = {}

    for element in data:
        sentence = ""
        for token in element['paragraphs'][0]["sentences"][0]["tokens"]:
            sentence = sentence + " " + token['orth']
            if token['ner'] != "O":
                if token['ner'] in ner_tokens.keys():
                    ner_tokens[token['ner']]['count'] += 1
                    ner_tokens[token['ner']]['samples'].append(sentence)
                else:
                    ner_tokens[token['ner']] = {
                        'count': 1,
                        'samples': [sentence]
                    }

    for ner_token in ner_tokens.keys():
        print(
            f"Token {ner_token} te {ner_tokens[ner_token]['count']} entrades")
        i = 0
        for sample in ner_tokens[ner_token]['samples']:
            print(f"Sample: {sample}")
            i += 1
            if i > 3:
                break
