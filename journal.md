# development journal

I will use this journal to record my steps, issues, and solutions as they arise.

## getting started

I am envisioning that I can eventually have a homepage that includes links, weather, maybe an inbox for recent emails and/or chat messages, and calendar reminders. I am not sure if this means I should make separate apps for these functions (they will have separate models and serve separate functions) or just include them all in a single app (the model could contain different classes). I do think that if I make separate apps, I Will need one app to rule them all and import those separate apps into a single view. Anyway, for now I will get started just making links, similar to my existing ReactJS homepage.

### initial steps

1. enter virtual environment for django development
2. django-admin startproject homepyge
3. test:

    ```python manage.py runserver```

4. add .pyc to gitignore and make first commit/sync to GH
5. add the "links" app:

    ```python manage.py startapp links```

### settings.py

I accidentally exposed my `SECRET_KEY` so I erased it and am using an environment variable instead. Note that I had to set `HOMEPYGE_SECRET` in the OS but then also `export` it (I had never grasped that step before) so that it's [an environment variable and not just a shell variable](https://help.ubuntu.com/community/EnvironmentVariables).

I also switched around some settings so that it will honor the environment variable of `HOMEPYGE_DEBUG`, if present, to set `DEBUG.` It defaults to `False` if not set, so that I don't accidentally publish my debug info in production.

### Links app and models

I went ahead and ran `python startapp links` (which I forgot to do earlier) to initialize my "Links" app. I registered it with my project in 'settings' and created a model for Links, which just has a title, description, and URL. I'll probably add other fields later, like at least an image to use for each.

I then ran `python manage.py makemigrations links` followed by `python manage.py migrate` to actually run the SQL to update my tables.
