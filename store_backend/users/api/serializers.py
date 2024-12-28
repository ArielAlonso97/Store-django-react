from rest_framework import serializers
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id','username','email','password']
        
    def validate_password(self,value):
        if(len(value)<8):
            raise serializers.ValidationError("paswword should be longer 8 characters or more")
        return value
    
    def validate_email(self,value):
        for user in User.objects.all():
            if(value ==user.email):
                 raise serializers.ValidationError("Email already in use")
        return value
    
    def create(self, validated_data):
        user = User(
            username=validated_data['username'],
            email=""" validated_data['email'] """,
        )
        user.set_password(validated_data['password'])
        user.save()
        return user