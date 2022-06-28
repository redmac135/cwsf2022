import os
import re
import uuid
from pathlib import Path
from .ai import predict

def parse_file(f):
    if not os.path.exists('media'):
        os.makedirs('media')

    filename = f"{uuid.uuid4()}.txt"
    path = Path(os.path.join('media', filename))
    path.touch(exist_ok=True)
    with open(path, 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)
        destination.seek(0)
        data = destination.read().decode()
        lines = re.split(r'[\s,]+', data)
    return predict(lines)