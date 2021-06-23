from graphene_django import DjangoObjectType
import graphene

from ..models import ToDoItem


class ToDoModel(DjangoObjectType):
    class Meta:
        model = ToDoItem


class ToDoQuery(graphene.ObjectType):
    ToDoItem = graphene.Field(
        ToDoModel,
        id=graphene.Int(),
        author=graphene.String(),
        completed=graphene.Boolean(),
    )

    def resolve_todoitem(self, info, **kwargs):
        _id = kwargs.get("id")

        if _id is not None:
            return ToDoItem.objects.get(id=_id)
