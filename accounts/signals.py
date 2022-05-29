from django.db.models.signals import post_save

from .models import User, UserDocument


def create_document(sender, **kwargs):
    if kwargs["created"]:
        if kwargs["instance"]:
            p1 = UserDocument(user=kwargs["instance"])
            p1.save()


post_save.connect(sender=User, receiver=create_document)
