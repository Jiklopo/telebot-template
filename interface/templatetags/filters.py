from django.template import Library

register = Library()


@register.filter(name='test')
def test(value, arg):
    return f'{value}, {arg}, :3'
