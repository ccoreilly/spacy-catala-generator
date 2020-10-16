import json
import random

train = []
test = []

with open('./datasets/ca/wikiann-ca.json') as json_file:
    data = json.load(json_file)

    ner_tokens = {}
    
    for element in data:
        for token in element['paragraphs'][0]["sentences"][0]["tokens"]:
            if token['ner'] != "O":
                if token['ner'] in ner_tokens.keys():
                    ner_tokens[token['ner']] += 1
                else:
                    ner_tokens[token['ner']] = 1

    for ner_token in ner_tokens.keys():
        print(f"Token {ner_token} te {ner_tokens[ner_token]} entrades")