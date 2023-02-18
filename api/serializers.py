from rest_framework import serializers
from .models import Accounts
from .managers import AccountManager
from django.contrib.auth import get_user_model, authenticate

# User Serializer
class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        User = get_user_model()
        model = User
        fields = ('iid', 'userid', 'user_type', 'name')

# Register Serializer
class RegisterAccountSerializer(serializers.ModelSerializer):
    class Meta:
        User = get_user_model()
        model = User
        fields = ('iid', 'userid', 'name', 'password', 'user_type')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        account = Accounts(userid=validated_data['userid'], password=validated_data['password'], name=validated_data['name'], iid=validated_data['iid'], user_type=validated_data['user_type'])
        account.groups = [validated_data['userid']]
        account.save()

        return account

class LoginSerializer(serializers.Serializer):
    userid = serializers.IntegerField()
    password = serializers.CharField()

    def validate(self,data):
        userid = data['userid']
        password = data['password']
        user = Accounts.objects.filter(userid=userid, password=password)
        if user.exists():
            user = user[0]
            
        if user and user.is_active:
            return user
        raise serializers.ValidationError("Pass")