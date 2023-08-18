from django import template
from accounts.models import UserProfile
register=template.Library()

@register.inclusion_tag('accounts/on.html')
def img_profile(pk):
    img=UserProfile.objects.get(id=pk)
    return {'img':img}
