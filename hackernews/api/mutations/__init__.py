import graphene
from hackernews.api.mutations.news import CreateNews, EmptyDB


class Mutations(graphene.ObjectType):
    """
    All created mutations
    """

    add_news = CreateNews.Field(description="News for tech enthusiast hackers")
    delete_everything = EmptyDB.Field()
