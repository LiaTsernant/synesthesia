# File for adding custom methods for the template
from django import template
register = template.Library() 

# Custom method for adding a NUMBER variable to the template
# Where is this used? 
# -on the Note's page, where I add note's number to a string, for being able to display different audio for different note
@register.filter(name='addstr')
def addstr(arg1, arg2):
    """concatenate arg1 & arg2"""
    return str(arg1) + str(arg2)