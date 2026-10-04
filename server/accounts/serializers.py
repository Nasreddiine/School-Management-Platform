from rest_framework_simplejwt.serializers import TokenObtainPairSerializer


class LoginSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        # Add custom claims to the JWT token
        token["role"] = user.role
        token["username"] = user.username

        return token

    def validate(self, attrs):
        data = super().validate(attrs)

        # Also return role in the response body (easier for React)
        data["role"] = self.user.role
        data["username"] = self.user.username

        return data