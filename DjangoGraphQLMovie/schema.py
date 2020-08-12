import graphene
import app.schema

class Query(app.schema.query, graphene.ObjectType):
	pass

class Mutation(app.schema.Mutation, graphene.ObjectType):
	pass


# Let's create the final schema
schema = graphene.Schema(query=Query, mutation=Mutation)
