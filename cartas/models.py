from django.db import models


class Set1(models.Model):
    # Field name made lowercase.
    id = models.AutoField(db_column='Id', primary_key=True)
    # Field name made lowercase.
    associatedcards = models.JSONField(
        db_column='associatedCards', blank=True, null=True)
    # Field name made lowercase.
    associatedcardrefs = models.JSONField(
        db_column='associatedCardRefs', blank=True, null=True)
    assets = models.JSONField(blank=True, null=True)
    regions = models.JSONField(blank=True, null=True)
    # Field name made lowercase.
    regionrefs = models.JSONField(
        db_column='regionRefs', blank=True, null=True)
    attack = models.IntegerField(blank=True, null=True)
    cost = models.IntegerField(blank=True, null=True)
    health = models.IntegerField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    # Field name made lowercase.
    descriptionraw = models.TextField(
        db_column='descriptionRaw', blank=True, null=True)
    # Field name made lowercase.
    levelupdescription = models.TextField(
        db_column='levelupDescription', blank=True, null=True)
    # Field name made lowercase.
    levelupdescriptionraw = models.TextField(
        db_column='levelupDescriptionRaw', blank=True, null=True)
    # Field name made lowercase.
    flavortext = models.TextField(
        db_column='flavorText', blank=True, null=True)
    # Field name made lowercase.
    artistname = models.TextField(
        db_column='artistName', blank=True, null=True)
    name = models.TextField(blank=True, null=True)
    # Field name made lowercase.
    cardcode = models.CharField(
        db_column='cardCode', blank=True, null=True, max_length=200)
    keywords = models.JSONField(blank=True, null=True)
    # Field name made lowercase.
    keywordrefs = models.JSONField(
        db_column='keywordRefs', blank=True, null=True)
    # Field name made lowercase.
    spellspeed = models.TextField(
        db_column='spellSpeed', blank=True, null=True)
    # Field name made lowercase.
    spellspeedref = models.TextField(
        db_column='spellSpeedRef', blank=True, null=True)
    rarity = models.TextField(blank=True, null=True)
    # Field name made lowercase.
    rarityref = models.TextField(db_column='rarityRef', blank=True, null=True)
    subtypes = models.JSONField(blank=True, null=True)
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
