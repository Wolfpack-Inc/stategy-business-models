from peewee import *

database = MySQLDatabase('video-games', **{'charset': 'utf8', 'use_unicode': True, 'host': '165.22.199.122', 'user': 'remote', 'password': 'EtrPCEc0jt'})

class UnknownField(object):
    def __init__(self, *_, **__): pass

class BaseModel(Model):
    class Meta:
        database = database

class Games(BaseModel):
    console = CharField(null=True)
    controllers = CharField(null=True)
    esrb = CharField(null=True)
    game = CharField(primary_key=True)
    game_name = CharField(null=True)
    is_online = IntegerField(null=True)
    max_player = IntegerField(null=True)
    min_player = IntegerField(null=True)
    rating = CharField(null=True)
    release_date = DateTimeField(null=True)
    site = CharField(null=True)
    summary = TextField(null=True)

    class Meta:
        table_name = 'games'

class CriticReviews(BaseModel):
    date = DateTimeField(null=True)
    game = ForeignKeyField(column_name='game', field='game', model=Games)
    grade = IntegerField(null=True)
    lang = CharField(null=True)
    review = TextField(null=True)
    source = CharField()

    class Meta:
        table_name = 'critic_reviews'
        indexes = (
            (('game', 'source'), True),
        )
        primary_key = CompositeKey('game', 'source')

class GameDevelopers(BaseModel):
    developer = CharField()
    game = ForeignKeyField(column_name='game', field='game', model=Games)

    class Meta:
        table_name = 'game_developers'
        indexes = (
            (('developer', 'game'), True),
        )
        primary_key = CompositeKey('developer', 'game')

class GameGenres(BaseModel):
    game = ForeignKeyField(column_name='game', field='game', model=Games)
    genre = CharField()

    class Meta:
        table_name = 'game_genres'
        indexes = (
            (('game', 'genre'), True),
        )
        primary_key = CompositeKey('game', 'genre')

class Sales(BaseModel):
    critic_score = IntegerField(null=True)
    game = ForeignKeyField(column_name='game', field='game', model=Games)
    japan_sales = IntegerField(null=True)
    na_sales = IntegerField(null=True)
    other_sales = IntegerField(null=True)
    pal_sales = IntegerField(null=True)
    position = IntegerField(null=True)
    total_sales = IntegerField(null=True)
    total_shipped = IntegerField(null=True)
    user_score = IntegerField(null=True)
    vgchartz_score = IntegerField(null=True)
    week = IntegerField()

    class Meta:
        table_name = 'sales'
        indexes = (
            (('game', 'week'), True),
        )
        primary_key = CompositeKey('game', 'week')

class UserReviews(BaseModel):
    date = DateTimeField(null=True)
    game = ForeignKeyField(column_name='game', field='game', model=Games)
    grade = IntegerField(null=True)
    helpful_nb = IntegerField(null=True)
    helpful_nb_total = IntegerField(null=True)
    lang = CharField(null=True)
    review = TextField(null=True)
    username = CharField()

    class Meta:
        table_name = 'user_reviews'
        indexes = (
            (('game', 'username'), True),
        )
        primary_key = CompositeKey('game', 'username')

class WeeklyPrices(BaseModel):
    complete = FloatField(null=True)
    game = ForeignKeyField(column_name='game', field='game', model=Games)
    graded = FloatField(null=True)
    loose = FloatField(null=True)
    new = FloatField(null=True)
    only_box = FloatField(null=True)
    only_manual = FloatField(null=True)
    week = IntegerField()

    class Meta:
        table_name = 'weekly_prices'
        indexes = (
            (('game', 'week'), True),
        )
        primary_key = CompositeKey('game', 'week')

class WeeklyScores(BaseModel):
    critic_nb = IntegerField(null=True)
    critic_score = IntegerField(null=True)
    game = ForeignKeyField(column_name='game', field='game', model=Games)
    user_nb = IntegerField(null=True)
    user_score = IntegerField(null=True)
    week = IntegerField()

    class Meta:
        table_name = 'weekly_scores'
        indexes = (
            (('game', 'week'), True),
        )
        primary_key = CompositeKey('game', 'week')

