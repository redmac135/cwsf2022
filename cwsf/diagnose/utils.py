import os
import re
import uuid
from django.core.files import File
from .models import DiagnoseModel

def parse_file(f):
    id = str(uuid.uuid4())
    filename = id + '.txt'
    path = os.path.join('media', filename)
    with open(path, 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)
        data = destination.read().decode()
        lines = re.split(r'[\s,]+', data)
        for line in lines:
            print(line)
        DiagnoseModel.objects.create(
            unique = id,
            upload = File(destination)
        )