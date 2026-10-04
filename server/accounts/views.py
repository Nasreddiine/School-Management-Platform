from django.conf import settings
from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.exceptions import InvalidToken
from rest_framework_simplejwt.serializers import TokenRefreshSerializer
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from rest_framework.permissions import IsAuthenticated


from .serializers import LoginSerializer


class LoginView(TokenObtainPairView):
    serializer_class = LoginSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        try:
            serializer.is_valid(raise_exception=True)
        except Exception as e:
            return Response({"detail": str(e)}, status=status.HTTP_401_UNAUTHORIZED)

        user = serializer.user
        access = serializer.validated_data["access"]
        refresh = serializer.validated_data["refresh"]

        response = Response(
            {"role": user.role, "username": user.username},
            status=status.HTTP_200_OK,
        )

        response.set_cookie(
            key=settings.SIMPLE_JWT["AUTH_COOKIE"],
            value=access,
            max_age=int(settings.SIMPLE_JWT["ACCESS_TOKEN_LIFETIME"].total_seconds()),
            httponly=True,
            secure=settings.SIMPLE_JWT["AUTH_COOKIE_SECURE"],
            samesite=settings.SIMPLE_JWT["AUTH_COOKIE_SAMESITE"],
            path="/",
        )

        response.set_cookie(
            key=settings.SIMPLE_JWT["AUTH_COOKIE_REFRESH"],
            value=refresh,
            max_age=int(settings.SIMPLE_JWT["REFRESH_TOKEN_LIFETIME"].total_seconds()),
            httponly=True,
            secure=settings.SIMPLE_JWT["AUTH_COOKIE_SECURE"],
            samesite=settings.SIMPLE_JWT["AUTH_COOKIE_SAMESITE"],
            path="/api/auth/refresh/",
        )

        return response


class CookieTokenRefreshSerializer(TokenRefreshSerializer):
    refresh = None

    def validate(self, attrs):
        attrs["refresh"] = self.context["request"].COOKIES.get(
            settings.SIMPLE_JWT["AUTH_COOKIE_REFRESH"]
        )
        if not attrs["refresh"]:
            raise InvalidToken("No refresh token found in cookie")
        return super().validate(attrs)


class CookieTokenRefreshView(TokenRefreshView):
    serializer_class = CookieTokenRefreshSerializer

    def finalize_response(self, request, response, *args, **kwargs):
        if response.data.get("access"):
            response.set_cookie(
                key=settings.SIMPLE_JWT["AUTH_COOKIE"],
                value=response.data["access"],
                max_age=int(settings.SIMPLE_JWT["ACCESS_TOKEN_LIFETIME"].total_seconds()),
                httponly=True,
                secure=settings.SIMPLE_JWT["AUTH_COOKIE_SECURE"],
                samesite=settings.SIMPLE_JWT["AUTH_COOKIE_SAMESITE"],
                path="/",
            )
            del response.data["access"]
        return super().finalize_response(request, response, *args, **kwargs)


class LogoutView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        response = Response({"detail": "Logged out"}, status=200)
        response.delete_cookie(settings.SIMPLE_JWT["AUTH_COOKIE"], path="/")
        response.delete_cookie(
            settings.SIMPLE_JWT["AUTH_COOKIE_REFRESH"],
            path="/api/auth/refresh/",
        )
        return response

from rest_framework.permissions import IsAuthenticated


class WhoAmIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        return Response({
            "username": request.user.username,
            "role": request.user.role,
        })