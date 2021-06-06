from profiles.models import UserProfile


def get_active_character(request):
    profile = UserProfile.objects.get(user=request.user)
    character = profile.active_character
    return character
