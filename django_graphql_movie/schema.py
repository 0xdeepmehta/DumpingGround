import graphene
import movies.schema

class Query(movies.schema.query, graphene.ObjectType):
	pass

class Mutation(movies.schema.Mutation, graphene.ObjectType):
	pass


# Let's create the final schema
schema = graphene.Schema(query=Query, mutation=Mutation)
