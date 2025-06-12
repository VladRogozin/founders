from django.shortcuts import render, redirect
from .models import AvatarItem, ComputerItem
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

    computers = ComputerItem.objects.all()
    owned_computers = profile.owned_computeritems.all()

    # Формируем URL для активного аватара
    if profile.active_skin:
        avatar_url = profile.active_skin.image.url
    else:
        # Fallback на дефолтный аватар
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
        'all_skins': items,
        'owned_skins': owned,
        'all_computers': computers,
        'owned_computers': owned_computers,
    })

from django.shortcuts import get_object_or_404
from django.contrib import messages
from django.apps import apps

@login_required
def buy_item(request, model_name, item_id):
    profile = request.user.profile

    # Ограничим доступ к только разрешённым моделям
    allowed_models = {
        'avataritem': 'shops.AvatarItem',
        'computeritem': 'shops.ComputerItem',
    }

    model_path = allowed_models.get(model_name.lower())
    if not model_path:
        messages.error(request, "Неверный тип товара.")
        return redirect('shop')

    ModelClass = apps.get_model(*model_path.split('.'))
    item = get_object_or_404(ModelClass, id=item_id)

    owned_field_name = f"owned_{model_name.lower()}s"
    if hasattr(profile, owned_field_name):
        owned_items = getattr(profile, owned_field_name).all()
        if item in owned_items:
            messages.info(request, "Уже куплено.")
        elif profile.coins >= item.price:
            profile.coins -= item.price
            getattr(profile, owned_field_name).add(item)
            profile.save()
            messages.success(request, "Покупка успешна.")
        else:
            messages.error(request, "Недостаточно монет.")
    else:
        messages.error(request, "Покупка невозможна.")

    return redirect('shop')


from django.apps import apps

@login_required
def use_item(request, model_name, item_id):
    profile = request.user.profile

    allowed_models = {
        'avataritem': AvatarItem,
        'computeritem': ComputerItem,
    }

    owned_fields = {
        'avataritem': 'owned_skins',
        'computeritem': 'owned_computeritems',
    }

    ModelClass = allowed_models.get(model_name.lower())
    if not ModelClass:
        messages.error(request, "Неверный тип предмета.")
        return redirect('shop')

    item = get_object_or_404(ModelClass, id=item_id)

    owned_field_name = owned_fields.get(model_name.lower())
    if not owned_field_name:
        messages.error(request, "Неверный тип предмета.")
        return redirect('shop')

    owned_items = getattr(profile, owned_field_name).all()

    if item not in owned_items:
        messages.error(request, "Сначала купите этот предмет.")
        return redirect('shop')

    if model_name.lower() == 'avataritem':
        profile.active_skin = item
    elif model_name.lower() == 'computeritem':
        profile.active_computer = item

    profile.save()
    messages.success(request, "Предмет применён.")
    return redirect('shop')
