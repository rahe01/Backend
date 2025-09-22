from django.contrib.auth.models import Permission
from django.contrib.contenttypes.models import ContentType
from core.permission_config import PERMISSION_CONFIG




def assign_permissions(user, role):
    """
    Assign permissions to a user based on their role.
    """
    if role not in PERMISSION_CONFIG:
        return  # No permissions to assign for this role

    permissions_to_assign = PERMISSION_CONFIG[role]

    for model, perms in permissions_to_assign.items():
        content_type = ContentType.objects.get_for_model(model)
        for perm in perms:
            try:
                permission = Permission.objects.get(codename=f"{perm}_{model._meta.model_name}", content_type=content_type)
                user.user_permissions.add(permission)
            except Permission.DoesNotExist:
                continue  # Skip if the permission does not exist

    user.save()