# -*- coding: utf-8 -*-
from graphQL.query import Query
from graphQL.mutations import Mutation
from graphQL.subscriptions import Subscription
from graphene import Schema


schema = Schema(query=Query)  # , mutation=Mutation, subscription=Subscription)
