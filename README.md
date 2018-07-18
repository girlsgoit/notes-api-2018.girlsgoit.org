# Welcome to notes-api.girlsgoit.org

### Steps to run the project:
1. Download or clone the repo.
2. Open a terminal window in the downloaded/cloned folder.
3. Run `pip install -r requirements.txt` if you don't have Django installed. Skip this step otherwise.
4. Run `python manage.py migrate` to apply database migrations.
5. Run `python manage.py createsuperuser` to create a super user :-D.
6. Run `python manege.py runserver`. If everything is ok you should see in your terminal window something written like:

```
System check identified no issues (0 silenced).
Django version 2.0.7, using settings 'notes_api.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CONTROL-C.
```

If you see this you're golden and you can start working.
