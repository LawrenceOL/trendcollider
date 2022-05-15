from rest_framework import serializers
from .models import MyUser, Weigh_In


class MyUser_Serializer(serializers.HyperlinkedModelSerializer):
    weigh_ins = serializers.HyperlinkedRelatedField(
        view_name='weigh_in',
        many=True,
        read_only=True
    )

    class Meta:
        model = MyUser
        fields = ('email', 'date_of_birth', 'is_active', 'is_admin')


class Weigh_In_Serializer(serializers.HyperlinkedModelSerializer):
    myuser = serializers.HyperlinkedRelatedField(
        view_name='myuser_detail',
        read_only=True
    )

    class Meta:
        model = Weigh_In
        fields = ('weigh_in_user', 'date', 'weight')
