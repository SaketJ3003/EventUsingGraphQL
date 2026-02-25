import graphene
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from graphene_django import DjangoObjectType

class UserType(DjangoObjectType):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'first_name', 'last_name')

class SignupMutation(graphene.Mutation):

    class Arguments:
        username   = graphene.String(required=True)
        email      = graphene.String(required=True)
        password   = graphene.String(required=True)
        first_name = graphene.String()
        last_name  = graphene.String()

    success = graphene.Boolean()
    message = graphene.String()
    user    = graphene.Field(UserType)

    def mutate(self, info, username, email, password, first_name='', last_name=''):
        if User.objects.filter(username=username).exists():
            return SignupMutation(success=False, message='Username already taken.', user=None)

        if User.objects.filter(email=email).exists():
            return SignupMutation(success=False, message='Email already registered.', user=None)

        user = User.objects.create_user(username=username, email=email, password=password, first_name=first_name, last_name=last_name)

        return SignupMutation(success=True, message='User created successfully.', user=user)


class LoginMutation(graphene.Mutation):

    class Arguments:
        email = graphene.String(required=True)
        password = graphene.String(required=True)

    success = graphene.Boolean()
    message = graphene.String()
    user    = graphene.Field(UserType)

    def mutate(self, info, email, password):

        try:
            user_obj = User.objects.get(email=email)
        except User.DoesNotExist:
            return LoginMutation(success=False, message='Invalid credentials.', user=None)

        user = authenticate(request=info.context, username=user_obj.username, password=password)
        if user is None:
            return LoginMutation(success=False, message='Invalid credentials.', user=None)

        return LoginMutation(success=True, message='Login successful.', user=user)

class Mutation(graphene.ObjectType):
    signup = SignupMutation.Field()
    login  = LoginMutation.Field()



class Query(graphene.ObjectType):
    all_users = graphene.List(UserType)

    def resolve_all_users(self, info):
        
        return User.objects.all()
        

schema = graphene.Schema(query=Query, mutation=Mutation)

