from django import template
from django.contrib.auth.models import User
from accounts.models import UserProfile
register = template.Library()

@register.inclusion_tag("accounts/snippets/recommend.html")
def recommended(user):
    if isinstance( user , User ):
        qs = UserProfile.objects.recommended(user)
        return {'recommended':qs}
