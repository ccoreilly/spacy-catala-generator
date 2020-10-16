import json
import re

no_space_before_token = [',', ')', '!', '?', '-']
with_space_before_token = ['(']
no_space_after_token = ['-', '(']

def append_to_str(sentence, token):
    if re.match(r"[a-z0-9]", token, re.IGNORECASE) is not None:
        if sentence[-1:] in no_space_after_token:
            return sentence + token
        else:
            return sentence + ' ' +  token
    elif token in no_space_before_token:
        return sentence + token
    elif token in with_space_before_token:
        return sentence + ' ' + token
    else:
        return sentence


with open('./datasets/ca/wikiann-ca.json') as json_file:
    data = json.load(json_file)

    sentences = []
    
    for element in data:
        sentence = ''
        for token in element['paragraphs'][0]["sentences"][0]["tokens"]:
            sentence = append_to_str(sentence, token['orth'])
        sentences.append(sentence.strip())

    for sentence in sentences:
        print(sentence)