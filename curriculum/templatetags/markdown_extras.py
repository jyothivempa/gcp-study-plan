from django import template
from django.template.defaultfilters import stringfilter
import markdown as md

register = template.Library()

@register.filter()
@stringfilter
def markdown(value):
    return md.markdown(value, extensions=['markdown.extensions.fenced_code', 'markdown.extensions.tables'])

@register.filter()
@stringfilter
def extract_flashcards(value):
    import re
    import json
    # Match <!-- FLASHCARDS ... -->
    match = re.search(r'<!--\s*FLASHCARDS\s*(\[.*?\])\s*-->', value, re.DOTALL)
    if match:
        try:
            return match.group(1)
        except:
            return "[]"
@register.filter()
def jsonify(value):
    import json
    if not value:
        return "[]"
    return json.dumps(value)
