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

### URLs

Now I want to be able to reach an actual "links" page (I'll deal with the fact that I want this to all be one page later). I used `include` to put in the pattern-matcher and send users to links.url, but that doesn't exist yet so I'll create it.

Then:

- add the URL pattern `path('', views.links, name="links")` to polls.urls.py
- create `/template/links` folder in `links/`
- create `links.html` file and plop it in that folder
- then in `views.py` (which is really where we define what I would think of as endpoints rather than "views", but whatever), just simply return that `links.html` file when that function/endpoint is reached.

Now, going to `mysite/links` takes me to that HTML page which renders properly in the browser!

### admin panel

Now for the admin panel. I just need to add a couple lines to `links/admin.py` to tell Django that the Links should be available from the admin panel. 

I also need to create admin credentials. To do this, I use the terminal and just enter `python manage.py createsuperuser`. That's really it. Now I can just add Links directly through that admin terminal. Awesome!

### rendering some links

Now to get those links to render on my page. I think I'll need to adjust my `views` (to make the Link data accessible to the page) and then for now I'll just do a super-simple loop and show them all as list items.

Here are the steps:

- in `views.py` of the "links" app, I imported a shortcut function called `get_list_or_404` which I (apparently correctly) guessed would return the full list of my links
- use that function to assign all my links to a variable (line 7)
- provide that list as context to the template by adding it as a dictionary as the final argument to `render()`
- then, I can just access that list from within the template, looping over it to create the links i need.

### thoughts on getting started

So, I feel like I'm in a good place for a first session. I got my project and app created, set up my model, and I can now add Links using the admin panel and view them in a simple, unformatted list of links by visiting `localhost:8000/links`. Next obvious step is to add some more formatting and sort the links into lists based on their category (which will also require a db update/migration).

Another big thing I hadn't properly thought through was building and deployment. Deployment is going to be trickier than it was with a Node.js app, and just using the default settings results in an error (I also had to set an environment variable on Netlify called `PYTHON_VERSION` to get it to not use Python 2.7).  It sounds like Heroku might offer a more Django-friendly deployment option but it's not authorizing me into my GH account at the moment, so that will be something to try next time.

### deployment attempt

Let's give [this](https://www.askpython.com/django/deploy-django-app-on-heroku) a whirl!
