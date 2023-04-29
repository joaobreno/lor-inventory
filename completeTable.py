import psycopg2
import json

con = psycopg2.connect(
    host='localhost',
    database='lor_inventory',
    user='postgres',
    password='jbpo95',
)
cur = con.cursor()


with open('set1-en_us.json', encoding='utf-8') as dados:
    set1 = json.load(dados)


idCont = 1

for i in set1:

    cur.execute('''
  INSERT INTO Set1
    (Id, associatedCards, associatedCardRefs, gameAbsolutePath, fullAbsolutePath, regions, regionRefs, attack, cost, health, description, descriptionRaw, levelupDescription, levelupDescriptionRaw, flavorText, artistName, name, cardCode, keywords, keywordRefs, spellSpeed, spellSpeedRef, rarity, rarityRef, subtypes, supertype, type, collectible, set)
  VALUES
    (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
  ''', (idCont, i['associatedCards'], i['associatedCardRefs'], i['assets'][0]['gameAbsolutePath'], i['assets'][0]['fullAbsolutePath'], i['regions'], i['regionRefs'], i['attack'], i['cost'], i['health'], i['description'], i['descriptionRaw'], i['levelupDescription'], i['levelupDescriptionRaw'], i['flavorText'], i['artistName'], i['name'], i['cardCode'], i['keywords'], i['keywordRefs'], i['spellSpeed'], i['spellSpeedRef'], i['rarity'], i['rarityRef'], i['subtypes'], i['supertype'], i['type'], i['collectible'], i['set'])
    )

    idCont += 1

con.commit()
con.close()
