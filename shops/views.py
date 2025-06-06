from django.shortcuts import render, redirect
from .models import AvatarItem
from accounts.models import Profile
from django.contrib.auth.decorators import login_required
import os
from django.conf import settings
# shops/views.py
from django.shortcuts import render, redirect, get_object_or_404
from .models import AvatarItem
from django.contrib.auth.decorators import login_required

@login_required
def shop_view(request):
    profile = request.user.profile
    items = AvatarItem.objects.all()
    owned = profile.owned_skins.all()
    available = items.exclude(id__in=owned)

    avatar_path = os.path.join(
        settings.BASE_DIR, 'static', 'base_img_profile', profile.avatar
    )
    if os.path.exists(avatar_path):
        avatar_url = settings.STATIC_URL + 'base_img_profile/' + profile.avatar
    else:
        avatar_url = settings.MEDIA_URL + profile.avatar

    return render(request, 'shops/shop.html', {
        'profile': profile,
        'avatar_url': avatar_url,
        'available_items': available,
        'owned_items': owned,
        'all_skins': items,
        'owned_skins': owned,
    })


from django.shortcuts import get_object_or_404
from django.contrib import messages

@login_required
def buy_skin(request, skin_id):
    profile = request.user.profile
    skin = get_object_or_404(AvatarItem, id=skin_id)

    if skin in profile.owned_skins.all():
        messages.info(request, "Скин уже куплен.")
    elif profile.coins >= skin.price:
        profile.coins -= skin.price
        profile.owned_skins.add(skin)
        profile.save()
        messages.success(request, "Скин куплен!")
    else:
        messages.error(request, "Недостаточно монет.")

    return redirect('shop')


@login_required
def use_skin(request, skin_id):
    profile = request.user.profile
    skin = get_object_or_404(AvatarItem, id=skin_id)

    if skin in profile.owned_skins.all():
        profile.avatar = skin.image.name  # сохраняем путь относительно media/
        profile.save()
        messages.success(request, "Скин применён.")
    else:
        messages.error(request, "Скин не куплен.")

    return redirect('shop')