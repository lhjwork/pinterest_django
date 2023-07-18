from django.contrib.auth.forms import UserCreationForm

class AccountUpdateForm(UserCreationForm):
    def __intf__(self, *args, **kwargs):
        super().__init__(*args,**kwargs)

        # id 값에 해당함
        self.fields['username'].disabled = True

