from graphene_django import DjangoObjectType
import graphene
from gql1.models import BankBranches as BankBranchesModel

class BankBranches(DjangoObjectType):
    class Meta:
        model = BankBranchesModel

class Query(graphene.ObjectType):
    # Fields of the query class are the queries that we can query
    bankbranches_search = graphene.List(BankBranches, name=graphene.String(), state=graphene.String())

    # function resolve_fieldname of the class 'Query' will return the output of the query asked
    def resolve_bankbranches_search(self, info, **kwargs):
        name = kwargs.get("name", "")
        state = kwargs.get("state", "")
        return BankBranchesModel.objects.filter(bank_name__icontains=name, state__icontains=state)

schema = graphene.Schema(query=Query)