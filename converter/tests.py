from django.test import TestCase

a = {'x': 1, 'y': 2, 'z': 3}
if 'x' and 'y' and 'z' in a.keys():
    print(666)
