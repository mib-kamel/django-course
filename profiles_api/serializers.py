from rest_framework import serializers
from profiles_api import models

class HelloSerializer(serializers.Serializer):
    """Serializes a name field for testing our APIView."""
    
    name = serializers.CharField(max_length=10)
    

class UserProfileSerializer(serializers.ModelSerializer):
    """Serializes a user profile object."""
    
    class Meta:
        model = models.UserProfile
        fields = ('id', 'email', 'name', 'password')
        # Extra keyword arguments for the password field.
        # Make sure that the password is write only.
        extra_kwargs = {
            'password': {
                'write_only': True,
                'style': {
                    'input_type': 'password'
                }
            }
        }
        
    def create(self, validated_data):
        """Create and return a new user."""
        
        user = models.UserProfile.objects.create_user(
            email=validated_data['email'],
            name=validated_data['name'],
            password=validated_data['password'],
        )
        
        return user
    
    def update(self, instance, validated_data):
        """Handle updating user account."""
        
        # If the user didn't provide a password, then just return the instance.
        if 'password' in validated_data:
            password = validated_data.pop('password')
            instance.set_password(password)
        
        # The super method will call the ModelSerializer's update method.
        return super().update(instance, validated_data)
    
    
class ProfileFeedItemSerializer(serializers.ModelSerializer):
    """Serializes profile feed items."""
    
    class Meta:
        model = models.ProfileFeedItem
        fields = ('id', 'user_profile', 'status_text', 'created_on')
        # Make sure that the user_profile field is read only.
        extra_kwargs = {
            'user_profile': {
                'read_only': True
            }
        }