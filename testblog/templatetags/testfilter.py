from django import template

register = template.Library()


@register.filter
def myFilterSensitiveWords(value, arg1):
    mystr1 = str(value)
    if mystr1.find("包子大帝") >= 0:
        return mystr1.replace("包子大帝",arg1)
    else:
        return value