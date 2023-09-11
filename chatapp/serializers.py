from django.contrib.auth.models import User
from rest_framework import serializers
from .models import UserProfile


class UserRegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True, style={'input_type': 'password'})
    email = serializers.EmailField(required=True)
    is_online = serializers.BooleanField(default=True)

    class Meta:
        model = User
        fields = ['username', 'password', 'email', 'first_name', 'last_name', 'is_online']

    def create(self, validated_data):
        # Create a new User object with the validated data
        user = User.objects.create_user(**validated_data)
        user.is_online = True
        user.save()
        return user


class UserLoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(style={'input_type': 'password'})

    def validate(self, data):
        username = data.get('username')
        password = data.get('password')

        if username and password:
            user = User.objects.filter(username=username).first()

            if user is None:
                raise serializers.ValidationError("User not found.")
            
            if not user.check_password(password):
                raise serializers.ValidationError("Incorrect password.")

            data['user'] = user
        else:
            raise serializers.ValidationError("Must include 'username' and 'password' fields.")

        return data


class UserProfileSerializer(serializers.ModelSerializer):
    is_online = serializers.BooleanField(default=True)

    class Meta:
        model = UserProfile
        fields = '__all__'  # Include all fields from the UserProfile model
