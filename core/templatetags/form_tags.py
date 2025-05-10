from django import template

register = template.Library()

@register.filter(name='as_field')
def as_field(field):
    return field.as_widget(attrs={
        'class': 'form-control',
        'placeholder': field.label
    })