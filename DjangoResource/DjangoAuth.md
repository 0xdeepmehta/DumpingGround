## For creating  User:
``` python
from django.contrib.auth.models import User
user = User.objects.create_user('deep', 'deepmehta@dreamer.com', '!be@dreamer$man!')
user.first_name = "Deep" 
user.last_name = "Mehta"
user.save()
```


## Change Password (You can't see the password of user cuz, Django don't store in plain text. But you can change them)
``` python
from django.contrib.auth.models import User
user = User.objects.get(username="deep")
user.set_password('hereismynewpassword~now_u_don`t_fuck_me')
user.save()
```

## Authneticate User
``` python 
from django.contrib.auth import authenticate
'''
:param username:<str> User name of the request.username
:param password:<str> Password of the request.password
:return: <userObject> if user exist else None 
'''
user = authenticate(username="deep", password="hereismynewpassword~now_u_don`t_fuck_me")
```


## Permissions and Authorization
``` python

```
