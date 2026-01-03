import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'gcp_study_plan.settings')
django.setup()

from django import template as django_template

# Test Django's template truthiness
register = django_template.Library()

test_values = [
    '',
    None,
    ' ',
    'test'
]

for val in test_values:
    template_str = '{% if value %}TRUE{% else %}FALSE{% endif %}'
    t = django_template.Template(template_str)
    c = django_template.Context({'value': val})
    result = t.render(c)
    print(f"Value: {repr(val):15} -> Template if: {result}")
