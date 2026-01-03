from django import template
from django.template.defaultfilters import stringfilter
import markdown as md
import re

register = template.Library()

@register.filter()
@stringfilter
def markdown(value):
    """Convert Markdown to HTML, stripping quiz sections."""
    if value is None:
        return ''
    # Strip out quiz sections wrapped in HTML comments
    value = re.sub(r'<!-- QUIZ_START -->.*?<!-- QUIZ_END -->', '', value, flags=re.DOTALL)
    return md.markdown(value, extensions=['markdown.extensions.fenced_code', 'markdown.extensions.tables', 'markdown.extensions.toc'])

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
