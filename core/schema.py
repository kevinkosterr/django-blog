from blog.graphql.query import BlogQuery
import graphene


class Query(BlogQuery):
    pass


schema = graphene.Schema(query=Query)
