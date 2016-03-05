# -*- coding: utf-8 -*-
from django import forms
from django.utils.translation import ugettext_lazy as _

class ContactsForm(forms.Form):
    name = forms.CharField(
        label=_('name'),
        widget=forms.TextInput(
            attrs={'id': 'name',}
        ),
        max_length=100,
        error_messages={
            "required": _('Enter Name.'),
        },
    )
    phone = forms.CharField(
        label=_("phone"),
        widget=forms.TextInput(
            attrs={'id': 'phone',}
        ),
        required=False,
        error_messages={
            "required": _('Enter Phone or E-mail, please.'),
        },
    )
    email = forms.EmailField(
        label=_("email"),
        widget=forms.TextInput(
            attrs={'id': 'email'}
        ),
        required=False,
    )
    message = forms.CharField(
        label=_("message"),
        widget=forms.Textarea(
            attrs={'id': 'message', 'cols': '30', 'rows':'10', 'placeholder': _('Your message')}),
        error_messages={
            "required": _('Enter Message.'),
        },
    )

    def clean(self):
        """
        Validate that the supplied email address or phone is present.
        """
        cleaned_data = super(ContactsForm, self).clean()
        email = cleaned_data.get('email')
        phone = cleaned_data.get('phone')
        if email or phone:
            pass
        else:
            error_list=self.errors.get('phone')
            if error_list is None:
                 error_list=forms.utils.ErrorList()
                 self.errors['phone']=error_list
            error_list.append(self.fields['phone'].error_messages["required"])
        return cleaned_data
