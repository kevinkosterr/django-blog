from todolist.graphql.query import ToDoQuery
import graphene


class Query(ToDoQuery):
    pass


schema = graphene.Schema(query=Query)
