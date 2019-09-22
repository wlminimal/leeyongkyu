from django import template
from home.models import Genesis, Exodus
import sys

register = template.Library()

# genesis snippet
@register.inclusion_tag('home/tags/snippets.html', takes_context=True)
def snippet_tags(context):
    
    # Get request.path ex) /address/path_that_I_want/
    # And get 3rd item from list
    slug = context['request'].path.split('/')[2]
    print("---------------------------------")
    print(slug)
    print(sys.modules[__name__])
    # Change string to class object
    snippet = getattr(sys.modules[__name__], slug.capitalize()) 
    print(snippet)
    return {
        'snippets': snippet.objects.all().order_by('id'),
        'request': context['request']
    }