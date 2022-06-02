from django.db import models
from multiselectfield import MultiSelectField


event_duration_choice = (
    ('Minute', 'minute'),
    ('Day', 'day'),
    ('Hour', 'hour'),
)

day_choices = (
    ('Monday', 'Mon'),
    ('Tuesday', 'Tue'),
    ('Wednesday', 'Wed'),
    ('Thursday', 'Thur'),
    ('Friday', 'Fri'),
    ('Saturday', 'Sat'),
    ('Sunday', 'Sun'),
)
keyword = (
    ('Window','Window'),
    ('Sunrise','Sunrise'),
    ('Sunset','Sunset'),
    ('Low Tide','Low Tide'),
    ('Temperature','Temperature'),
    )

class Filter(models.Model):
    filter_detail = models.CharField('Filter Detail', max_length=300, null=True)
    keyword = models.CharField(max_length=30, choices=keyword)
    X1 = models.CharField('value to set(X1)', max_length=200, null=True, blank=True, help_text = "if Window is selected Please use 12-hour clock and X2 should be greater than X1")
    X2 = models.CharField('value to set(X2)', max_length=200, null=True, blank=True)


    def __str__(self):
        return str(self.filter_detail)[:100]

    class Meta:
        verbose_name_plural = "FIlters"

class EventDetails(models.Model):
    title = models.CharField(max_length=200, help_text = "Event Title")
    days_to_look = models.IntegerField(null=True, help_text = "Number of days to look")
    days = MultiSelectField(choices=day_choices, null=True, help_text = "Days to look at")
    free_event = models.BooleanField('include free events?', default=True)
    event_duration_type = models.CharField(max_length=100, choices=event_duration_choice, help_text = "Days / Hours / Minutes")
    event_duration = models.IntegerField()
    apply_snooze = models.BooleanField(default=True, help_text = "Apply snooze") 
    snooze_type = models.CharField(max_length=100, choices=event_duration_choice, help_text = "Days / Hours / Minutes")
    snooze_duration = models.IntegerField(help_text = "Duration for the snooze")
    snooze_days = MultiSelectField(choices=day_choices, null=True, blank=True, help_text = "Snooze days (Optional)")
    filter = models.ManyToManyField(Filter, help_text = "Choose Filter(s)")
    calenders = models.ManyToManyField('Calenders', help_text = "Pick calendars to look into")


    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "Event Details"

class Calenders(models.Model):
    name = models.CharField(null=True, blank=True, max_length=200)
    ide = models.CharField(max_length=400, null=True, blank=True)
    token_url = models.CharField(max_length=200, null=True, blank=True)
    title = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return str(self.name + ': ' + self.title)

    class Meta:
        verbose_name_plural = "Calenders"

class Token(models.Model):
    name = models.CharField(max_length=500, null=True)
    email = models.EmailField(null=True)
    token_file = models.FileField(null=True, blank=True, upload_to='json_files')
    status = models.BooleanField(default=True)


    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Tokens"
