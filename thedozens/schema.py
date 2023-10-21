# -*- coding: utf-8 -*-
import graphene
from API.filters import InsultFilter
from API.models import Insult
from graphene import relay
from graphene_django import DjangoObjectType
from graphene_django.filter import DjangoFilterConnectionField


class InsultType(DjangoObjectType):
    class Meta:
        model = Insult
        field = (
            "content",
            "category",
            "explicit",
            "added_on",
            "added_by",
            "last_modified",
            "status",
        )
        filterset_class = InsultFilter
        interfaces = (relay.Node,)


class Query(graphene.ObjectType):
    insults = graphene.List(InsultType)
    insult_by_category = graphene.Field(InsultType, category=graphene.String())
    insults_by_status = graphene.Field(InsultType, status=graphene.String())
    insults_by_classification = graphene.Field(InsultType, explicit=graphene.Boolean())
    insult_by_id = graphene.Field(InsultType, id=graphene.ID())

    def resolve_insults(root, info, **kwargs):
        return Insult.objects.fiter(status="A")

    def resolve_insult_by_category(root, info, category):
        return Insult.objects.fiter(status="A").filter(category=category)

    def resolve_insults_by_status(root, info, status):
        return Insult.objects.filter(status=status)

    def resolve_insults_by_classification(root, info, explicit):
        return Insult.objects.filter(explicit=explicit)

    def resolve_insult_by_id(root, info, ID):
        return Insult.objects.get(id=ID)


class Mutation(graphene.ObjectType):
    pass


class Subscription(graphene.ObjectType):
    pass


schema = graphene.Schema(query=Query, mutation=Mutation, subscription=Subscription)
