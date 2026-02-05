import sys, os, traceback
sys.path.insert(0, r'E:\Downloads\VisualCode\azure_sql_django')
os.environ.setdefault('DJANGO_SETTINGS_MODULE','azure_project.settings')
import django
django.setup()
try:
    import api.serializers as s
    print('FILE:', getattr(s, '__file__', None))
    print('SERIALIZERS:', [n for n in dir(s) if n.endswith('Serializer')])
    # Print source of module to inspect
    import inspect
    print('\nSOURCE:\n')
    print('\n'.join(inspect.getsource(s).splitlines()[-40:]))
except Exception:
    traceback.print_exc()
