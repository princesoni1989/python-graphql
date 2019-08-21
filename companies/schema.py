import graphene;
from graphene_django.types import DjangoObjectType, ObjectType
from .models import Company


class CompanyType(DjangoObjectType):
    class Meta:
        model = Company


class Query(ObjectType):
    companies = graphene.List(CompanyType)

    def resolve_companies(self, info):
        return Company.objects.all()


schema = graphene.Schema(query=Query)
