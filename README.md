# Putting it All Together

## Lab-34
<br>

### Feature Tasks and Requirements

#### Choice 1: Use your own Template/s
- If you’ve built a template repository for your Django sites, or APIs, or both - now’s the time to put them to work.
- See what it would take to combine the two approaches into one starter kit to rule them all.

<br>

#### Choice 2: Use API Quick Start Template
##### The API Quick Start is a built out skeleton project with lots of the tools we’ve been using in class. Check it out. If you like it, use it. But better yet, use it as an inspiration to build your own that’s a perfect fit.

- WARNING: 
  ##### There is no guarantee that the API Quick Start is a perfect fit for your needs, is bug free, etc. It’s a great jumping off point though. And if you spot any bugs or have ideas for improvements make a PR!

<br>

- Modify your application paying close attention to the instructions in README.md found in root of repository.
  - Install from requirements.txt.
  - Export (aka freeze) requirements.
  - Change things app folder to be cookie_stands
  - Go through code base looking for Thing,thing and things change to cookie-stand related names.
  - E.g. Thing model becomes CookieStand
  - E.g. ThingList becomes CookieStandList

<br>

- Pro Tip: Do a global text search looking for thing
  - Search should be case insensitive.
  - WARNING: Do NOT just cut and paste. Think through each change carefully.

<br>

- Create/rename .env using .env.sample as starting point.
  - Here’s a handy way to generate a secret key
    - python -c “import secrets; print(secrets.token_urlsafe())”

<br>

### CookieStand Model Details
- The CookieStand model must contain
```
    location = models.CharField(max_length=256)
    owner = models.ForeignKey(
        get_user_model(), on_delete=models.CASCADE, null=True, blank=True
    )
    description = models.TextField(blank=True)
    hourly_sales = models.JSONField(default=list, null=True)
    minimum_customers_per_hour = models.IntegerField(default=0)
    maximum_customers_per_hour = models.IntegerField(default=0)
    average_cookies_per_sale = models.FloatField(default=0)

    def __str__(self):
        return self.location
```

- Notice the use of JSONField.
- Once changes are complete make migrations, migrate, and test locally.

<br>

#### Database Deployment Requirements
- Host your Database at ElephantSQL

<br>

#### Site Deployment Requirements
- We’ll handle deployment a little later. For now run your site locally, but the Database should be remote.

<br>

---

<br>