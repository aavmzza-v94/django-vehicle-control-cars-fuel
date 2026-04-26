from django.contrib.auth import get_user_model # para usuarios... formularios..
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

class CustomUserCreationForm(UserCreationForm):
    class Meta: # se usa para almacenar datos e ir acumulando adicionalmente...
        model = get_user_model() # llama al que tengamos definido en el settings.py usuarios..
        fields = [
            "email",
            "username", # no olvidar la coma, se crea una tupla...
        ]

class CustomUserChangeForm(UserChangeForm): # asi se tiene formularios para modificar los usuarios desde el admin..
    class Meta: # se usa para almacenar datos e ir acumulando adicionalmente...
        model = get_user_model() # llama al que tengamos definido en el settings.py usuarios..
        fields = [
            "email",
            "username", # no olvidar la coma, se crea una tupla...
        ]