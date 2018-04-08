from django.contrib.auth.models import User
from rest_framework import serializers

from datetime import datetime

class Comment(object):
    def __init__(self, email, content, created=None):
        self.email = email
        self.content = content
        self.created = datetime.now()

comment = Comment(email='leila@example.com', content='foo bar')

# 验证器
def multiple_of_ten(value):
    if value % 10 != 0:
        raise serializers.ValidationError('Not a multiple of ten')

class CommentSerializer(serializers.Serializer):
    email = serializers.EmailField(validators=[multiple_of_ten,])
    content = serializers.CharField(max_length=200)
    created = serializers.DateTimeField()

    def create(self, validated_data):
        return Comment(**validated_data)

    def update(self, instance, validated_data):
        instance.email = validated_data.get('email',instance.email)
        instance.content = validated_data.get('email',instance.content)
        instance.created = validated_data.get('email',instance.created)
        return instance

    def validate_content(self,value):
        if 'django' not in value:
            raise serializers.ValidationError('这内容不合法')
        return value

    def validate(self, data):
        """
        Check that the start is before the stop.
        """
        if data['start'] > data['finish']:
            raise serializers.ValidationError("finish must occur after start")
        return data


class ProfileSerializer(object):
    pass


class UserSerializer(serializers.Serializer):
    profile = ProfileSerializer()

    class Meta:
        model = User
        fields = ('username','email','profile')

    def create(self, validated_data):
        profile_data = validated_data.pop('profile')
        user = User.objects.create(** validated_data)
        # Profile.objects.create(user=user,**profile_data)

