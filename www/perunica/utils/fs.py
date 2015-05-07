import uuid
import os

def path_and_rename(path):
    def wrapper(instance, filename):
        ext = filename.split('.')[-1]
        if instance.pk:
            filename = '{}.{}'.format(instance.pk, ext)
        else:
            filename = '{}.{}'.format(str(uuid.uuid1()), ext)
        return os.path.join(path, filename)
    return wrapper

