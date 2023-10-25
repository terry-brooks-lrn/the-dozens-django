# -*- coding: utf-8 -*-
from graphene import Mutation, Enum, Argument
from API.models import Insult


class Mutation(Mutation):
    def mutate(root, info, **kwargs):
        pass

    # class JokeCategory(Enum):
    #     class Meta:
    #         enum = Insult.CATEGORY
    #         description = "Enumerated Catagory for Jokes"
    # class Arguments:
    #     category = Argument(Mutation.JokeCategory,required=True)
