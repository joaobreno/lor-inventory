import psycopg2
import json

con = psycopg2.connect(
    host='localhost',
    database='lor_inventory',
    user='postgres',
    password='jbpo95',
)
cur = con.cursor()

base_sql = '''
  CREATE TABLE Set1 (
    Id int,
    associatedCards text[] DEFAULT NULL,
    associatedCardRefs text[] DEFAULT NULL,
    gameAbsolutePath text DEFAULT NULL,
    fullAbsolutePath text DEFAULT NULL,
    regions text[] DEFAULT NULL,
    regionRefs text[] DEFAULT NULL,
    attack int DEFAULT NULL,
    cost int DEFAULT NULL,
    health int DEFAULT NULL,
    description text,
    descriptionRaw text,
    levelupDescription text,
    levelupDescriptionRaw text,
    flavorText text,
    artistName text,
    name text,
    cardCode text,
    keywords text[] DEFAULT NULL,
    keywordRefs text[] DEFAULT NULL,
    spellSpeed text,
    spellSpeedRef text,
    rarity text,
    rarityRef text,
    subtypes text[] DEFAULT NULL,
    supertype text,
    type text,
    collectible text,
    set text,
    PRIMARY KEY (Id)
  )
'''

cur.execute(base_sql)


con.commit()
con.close()
