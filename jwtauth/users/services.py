from .models import User;
from .serializers import UserSerializer;
import datetime
import jwt
from rest_framework.response import Response;
from rest_framework.exceptions import AuthenticationFailed 


class UsersService:

    def __init__(self):
        print(self);


    def register(self, data):
        name = data['name'];
        email = data['email'];
        password = data['password']

        user = User(
            name = name,
            email = email,
            password = password)

        user.save()
        # user_serializer = UserSerializer(data=data)

        # user_serializer.is_valid(raise_exception=True)
        # user_serializer.save()

        # print('before')
        # print(data)
        # print('after')
        # print(user_serializer.data)


        return user_serializer.data;


    def login(self, data):
        email = data['email']
        password = data['password']

        user = User.objects.filter(email=email).first();

        if user is None:
            return 'User not exists'

        user = User.objects.filter(email=email, password=password).first();

        if user is None:
            return 'Incorrect password';

        payload = {
          "user_id": user.id,
          "exp_time": str(datetime.datetime.utcnow()),
          "int": str(datetime.datetime.utcnow() + datetime.timedelta(minutes=1))
        }

        token = jwt.encode(payload, '4', algorithm='HS256')

        # response_data = {
        #     "message": "success",
        #     "token": token,
        #     }

        # response = Response()
        # response.set_cookie(key="jwt", value=token, httponly=True)
        # response.data = response_data

        # print(token)
        return token

    def get_user(self, request):
        token = request.COOKIES.get('jwt')

        if not token:
            raise AuthenticationFailed('Unauthenticated')

        try:
            payload = jwt.decode(token, '4', algorithms = ['HS256'])
        except:
            raise AuthenticationFailed('Unauthenticated')

        user = User.objects.filter(id=payload['user_id']).first()

        response = {
          "name": user.name,
          "email": user.email        
        }

        return response
        # print(user.name)

        # return user['id']


class AService:
    pass;

class BService:
    pass;