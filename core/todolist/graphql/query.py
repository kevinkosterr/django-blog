from graphene_django import DjangoObjectType
import graphene

from ..models import ToDoItem


class ToDoModel(DjangoObjectType):
    class Meta:
        model = ToDoItem


class ToDoQuery(graphene.ObjectType):
    ToDoItem = graphene.Field(ToDoModel, id=graphene.Int())
    ToDoItems = graphene.List(ToDoModel)

    def resolve_ToDoItem(self, info, **kwargs):
        _id = kwargs.get("id")

        if _id is not None:
            return ToDoItem.objects.get(id=_id)

        return None

    def resolve_ToDoItems(self, info, **kwargs):
        limit = kwargs.get("limit")
        if not limit:
            return ToDoItem.objects.all()
        return ToDoItem.objects.all()[:limit]
