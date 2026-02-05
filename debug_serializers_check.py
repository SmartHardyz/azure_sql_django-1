import sys, os, traceback
sys.path.insert(0, r'E:\Downloads\VisualCode\azure_sql_django')
print('PYTHONPATH:', sys.path[0])
try:
    with open('api/serializers.py', 'rb') as f:
        data = f.read()
    print('\nFILE BYTES REPR (first 2000 bytes):')
    print(repr(data[:2000]))
    try:
        text = data.decode('utf-8')
    except Exception:
        text = data.decode('latin-1')
    print('\nFILE TEXT (first 2000 chars):')
    print(text[:2000])
except Exception:
    traceback.print_exc()

os.environ.setdefault('DJANGO_SETTINGS_MODULE','azure_project.settings')
import django
try:
    django.setup()
except Exception:
    print('django.setup() failed:')
    traceback.print_exc()

print('\nNow attempting import api.serializers')
try:
    import importlib
    importlib.invalidate_caches()
    s = importlib.import_module('api.serializers')
    print('MODULE FILE:', getattr(s, '__file__', None))
    print('DEFINED SERIALIZERS:', [n for n in dir(s) if n.endswith('Serializer')])
except Exception:
    traceback.print_exc()
