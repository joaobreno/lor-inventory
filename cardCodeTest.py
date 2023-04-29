from lor_deckcodes import LoRDeck, CardCodeAndCount



# Decoding
deck = LoRDeck.from_deckcode('CEBQCAYCBEBAEAQDAYCAIB2PQAAYEAMKAEBQEAICBQYQGAQCAUEQUAYEA4RUEXIDAEAQEAQBAIBAQAIEAIKA')

list(deck)

for i in deck.cards:
    print(i)