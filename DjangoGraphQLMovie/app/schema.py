import graphene
from graphene_django.types import DjangoObjectType, ObjectType
from .models import Actor,Movie

# Create a GraphQL type for the actor model
class ActorType(DjangoObjectType):
	class Meta: # In Meta Section We've specify which Django model properties, we want in the API.
		model = Actor 

# create GraphQl Type for the movies model

class MovieType(DjangoObjectType):
	class Meta: # In Meta Section we've specify Which Django Model properties, We Want in API
		model = Movie



# Let's Create the Query 

class query(ObjectType):
	actor = graphene.Field(ActorType, id=graphene.Int()) # fetch particular actor by specifiy the Id
	movie = graphene.Field(MovieType, id=graphene.Int()) # fetch particular Movie By Specifiy thr Id
	actors = graphene.Field(ActorType)
	movies = graphene.Field(MovieType)

	# Let's Create Resolver 
	def resovle_actor(self, info, **kwargs):
		id = kwargs.get('id')

		if id is not None:
			return Actor.objects.get(pk=id)

		return None

	def resolve_movie(self, info, **kwargs):
		id = kwargs.get('id')

		if id is not None:
			return Movie.objects.get(pk=id)

		return None

	def resolve_actors(self, info, **kwargs):
		return Actor.objects.all()

	def resolve_movies(self, info, **kwargs):
		return Movie.objects.all()



# class Input object types
class ActorInput(graphene.InputObjectType):
	id = graphene.ID()
	name = graphene.String()

class MovieInput(graphene.InputObjectType):
	id = graphene.ID()
	title = graphene.String()
	actors = graphene.List(ActorInput)
	year = graphene.Int()



#Create Mutations for actor
class CreateActor(graphene.Mutation):
	class Arguments:
		input = ActorInput(required=True)

	# response
	ok = graphene.Boolean()
	actor = graphene.Field(ActorType)

	# user input opreation
	@staticmethod
	def mutate(root, info, input=None):
		ok = True
		actor_instance = Actor(name=input.name)
		actor_instance.save()
		return CreateActor(ok=ok, actor=actor_instance)

class UpdateActor(graphene.Mutation):
	class Arguments:
		id = graphene.Int(required=True)
		input = ActorInput(required=True)

	ok = graphene.Boolean()
	actor = graphene.Field(ActorType)

	@staticmethod
	def mutate(root, info, id, input=None):
		ok = False
		actor_instance = Actor.objects.get(pk=id)
		if actor_instance:
			ok = True
			actor_instance.name = input.name
			actor_instance.save()
			return UpdateActor(ok=ok, actor=actor_instance)
		return UpdateActor(ok=ok, actor=None)


# Let's create the mutation for movie 

class CreateMovie(graphene.Mutation):
	class Arguments:
		input = MovieInput(required=True)

	ok = graphene.Boolean()
	movie = graphene.Field(MovieType)

	@staticmethod
	def mutate(root, info, input=None):
		ok = True
		actors = []
		for actors_input in input.actors:
			actor = Actor.objects.get(pk=actors_input.id)
			if actor is None:
				return CreateMovie(ok=False, movie=None)
			actors.append(actor)

		movie_instance = Movie(title=input.title, year=input.year)
		movie_instance.save()
		movie_instance.actors.set(actors)
		return CreateMovie(ok=ok, movie=movie_instance)

class UpdateMovie(graphene.Mutation):
	class Arguments:
		id = graphene.Int(required=True)
		input = MovieInput(required=True)
	#create Payload	
	ok = graphene.Boolean()
	movie = graphene.Field(MovieType)

	# Handle the input
	@staticmethod
	def mutate(root, info, id, input=None):
		ok = False
		movie_instance = Movie.objects.get(pk=id)
		if movie_instance:
			ok = True
			actors = []
			for actor_input in input.actors:
				actor = Actor.objects.get(pk=actor_input.id)
				if actor is None:
					return UpdateActor(ok=False, movie=None)
				actors.append(actor)

			movie_instance.title = input.title
			movie_instance.year = input.year
			movie_instance.save()
			movie_instance.actors.set(actors)
			return UpdateActor(ok=ok, movie=movie_instance)
		return UpdateActor(ok=ok, movie=None)



class Mutation(graphene.ObjectType):
	create_actor = CreateActor.Field()
	Update_actor = UpdateActor.Field()
	create_movie = CreateMovie.Field()
	Update_movie = UpdateMovie.Field()








