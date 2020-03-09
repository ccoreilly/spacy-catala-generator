import json
import random

train = []
test = []

with open('../datasets/ca/wikiann-ca.json') as json_file:
    data = json.load(json_file)
    total_len = len(data)
    test_len = 0.2 * total_len

    for sentence in data:
        if random.random() > 0.5 and len(test) < test_len:
            test.append(sentence)
        else:
            train.append(sentence)

with open('../datasets/ca/train.json', 'w') as outfile:
    json.dump(train, outfile)

with open('../datasets/ca/test.json', 'w') as outfile:
    json.dump(test, outfile)

