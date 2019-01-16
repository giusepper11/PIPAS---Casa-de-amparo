from allauth.account.adapter import DefaultAccountAdapter


class UserAccountAdapter(DefaultAccountAdapter):

    def save_user(self, request, user, form, commit=True):
        """
        This is called when saving user via allauth registration.
        We override this to set additional data on user object.
        """
        # Do not persist the user yet so we pass commit=False
        # (last argument)
        user = super(UserAccountAdapter, self).save_user(request, user, form, commit=False)
        if form.cleaned_data.get('is_pf',None):
            user.is_pf = True
        elif form.cleaned_data.get('is_pj',None):
            user.is_pj = True
        user.save()