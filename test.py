import json
'''data = []
with open('bekkur.json', 'r', encoding='utf-8') as bekkur:
    data = json.loads(bekkur.read())
teljari = 0
for x in data['nemendur']:
    teljari += 1
kennitolur = []
nofn = []
brautir = []
for x in range(teljari):
    kennitolur.append(data['nemendur'][x]['kt'])
    nofn.append(data['nemendur'][x]['nafn'])
    brautir.append(data['nemendur'][x]['braut'])

print(kennitolur)
print(nofn)
print(brautir)'''

with open('bekkur.json', 'r', encoding='utf-8') as f:
    bekkur = json.load(f)
print(bekkur)

print(bekkur['nemendur'][0])
'''
for x in bekkur['nemendur'][0]['kt']:
    if x in kt:
        print("test")
'''
kt = '1206734249'
nofn = ''
brautir = ''
teljari = 0
for x in bekkur['nemendur']:
    teljari += 1
for x in range(teljari):
    if bekkur['nemendur'][x]['kt'] in kt:
        nofn = bekkur['nemendur'][x]['nafn']
        brautir = bekkur['nemendur'][x]['braut']
print(nofn, brautir)

for x in bekkur['nemendur']:
    if x['kt'] == kt:
        nofn = x['nafn']
        brautir = x['braut']