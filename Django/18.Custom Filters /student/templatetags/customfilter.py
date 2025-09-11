from django import template
register = template.Library()



# Without decoratpt
"""def myreplace(value , arg):

    return value.replace(arg, 'We are')


register.filter('iamToweare' , myreplace)"""





@register.filter(name='iamToweare')
def myreplace(value , arg):

    return value.replace(arg, 'We are')


