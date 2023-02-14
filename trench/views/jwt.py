from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken

from trench.views import MFAFirstStepMixin, MFASecondStepMixin, MFAStepMixin, User
from datetime import datetime, timedelta


class MFAJWTView(MFAStepMixin):
    
    def _successful_authentication_response(self, user: User) -> Response:
        token = RefreshToken.for_user(user=user)
        remember = self.request.data.get('remember', 1)
        token['exp'] = datetime.utcnow() + timedelta(days=int(remember))
        return Response(data={"refresh": str(token), "access": str(token.access_token)})

    def _remembered_authentication_response(self, user: User) -> Response:
        token = RefreshToken.for_user(user=user)
        remember = self.request.data.get('remember', 1)
        token['exp'] = datetime.utcnow() + timedelta(days=int(remember))
        return Response(data={"refresh": str(token), "access": str(token.access_token), 'method': 'remembered'})


class MFAFirstStepJWTView(MFAJWTView, MFAFirstStepMixin):
    pass


class MFASecondStepJWTView(MFAJWTView, MFASecondStepMixin):
    pass
