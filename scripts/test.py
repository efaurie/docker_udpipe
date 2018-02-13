import requests

test_data = ['This', 'is', 'a', 'test', '.', '', 'This', 'is', 'another', '.']

payload = {
    'data': '\n'.join(test_data),
    'input': 'vertical',
    'model': 'en',
    'tagger': True,
    'parser': True,
    'output': 'conllu'
}

response = requests.get('http://localhost:5000/process', params=payload)
response.raise_for_status()

conll = []
current_sentence = None
for x in response.json()['result'].split('\n'):
    x = x.strip()
    if not x:
        continue

    if x.startswith('# sent_id'):
        conll.append([])
        current_sentence = conll[-1]
    elif x.startswith('#'):
        continue
    else:
        current_sentence.append(x)

for idx, sent in enumerate(conll):
    print(f'**** Sentence {idx+1} ****')
    for x in sent:
        print(x)
