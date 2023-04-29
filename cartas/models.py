from django.db import models

class Set1(models.Model):
    id = models.IntegerField(primary_key=True)
    associatedcards = models.TextField(blank=True, null=True)  # This field type is a guess.
    associatedcardrefs = models.TextField(blank=True, null=True)  # This field type is a guess.
    gameabsolutepath = models.TextField(blank=True, null=True)
    fullabsolutepath = models.TextField(blank=True, null=True)
    regions = models.TextField(blank=True, null=True)  # This field type is a guess.
    regionrefs = models.TextField(blank=True, null=True)  # This field type is a guess.
    attack = models.IntegerField(blank=True, null=True)
    cost = models.IntegerField(blank=True, null=True)
    health = models.IntegerField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    descriptionraw = models.TextField(blank=True, null=True)
    levelupdescription = models.TextField(blank=True, null=True)
    levelupdescriptionraw = models.TextField(blank=True, null=True)
    flavortext = models.TextField(blank=True, null=True)
    artistname = models.TextField(blank=True, null=True)
    name = models.TextField(blank=True, null=True)
    cardcode = models.TextField(blank=True, null=True)
    keywords = models.TextField(blank=True, null=True)  # This field type is a guess.
    keywordrefs = models.TextField(blank=True, null=True)  # This field type is a guess.
    spellspeed = models.TextField(blank=True, null=True)
    spellspeedref = models.TextField(blank=True, null=True)
    rarity = models.TextField(blank=True, null=True)
    rarityref = models.TextField(blank=True, null=True)
    subtypes = models.TextField(blank=True, null=True)  # This field type is a guess.
    supertype = models.TextField(blank=True, null=True)
    type = models.TextField(blank=True, null=True)
    collectible = models.TextField(blank=True, null=True)
    set = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'set1'

    def __str__(self):
        return self.name

    def getAssets(self):
        return self.assets

    def imgPath(self):
        imgPath = '/static/img/cards/set1/' + self.cardcode + '.png'
        return imgPath

    def getRegion(self):
        return self.regions

    def getKeywords(self):
        return self.keywords

    def getTribe(self):
        return self.subtypes

    def getAssociatedCards(self):
        return self.associatedcardrefs
