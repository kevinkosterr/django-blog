from graphene_django import DjangoObjectType
import graphene

from ..models import Post

# from core.blog.models import Post


class PostModel(DjangoObjectType):
    class Meta:
        model = Post


class BlogQuery(graphene.ObjectType):
    post = graphene.Field(PostModel, id=graphene.Int())
    posts = graphene.List(PostModel)

    def resolve_post(self, info, **kwargs):
        id = kwargs.get("id")

        if id is not None:
            return Post.objects.get(id=id)

        return None

    def resolve_posts(self, info, **kwargs):
        return Post.objects.all()
