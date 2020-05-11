from django.db import models
from datetime import date
from multiselectfield import MultiSelectField

# keep outside of Cat class for easy import
PERSONALITY = (
    (1, 'Indoors only'),
    (2, 'Indoors and outdoor'), 
    (3, 'Lap cat'), 
    (4, 'Mellow'), 
    (5, 'Active'), 
    (6, 'Independent'), 
    (7, 'Shy'), 
    (8, 'Playful'), 
    (9, 'Friendly'), 
    (10, 'Curious'), 
    (11, 'Feisty'), 
    (12, 'Affectionate'), 
    (13, 'Loves attention'), 
    (14, 'Aloof'), 
    (15, 'Swats when over stimulated'), 
    (16, 'Needs quiet home'), 
    (17, 'Likes to be held/picked up'), 
    (18, 'Doesn\'t like to be held/picked up'), 
    (19, 'Comfortable with other cats'), 
    (20, 'Not comfortable with other cats'), 
    (21, 'Comfortable with dogs'), 
    (22, 'Not comfortable with dogs'), 
    (23, 'Good with younger kids'),
    (24, 'Good with older kids'),
    (25, 'Needs a home with adults only'),
    (26, 'Needs time to get to know and trust you'),
)

class Cat(models.Model):
    name = models.CharField(max_length=50)

    GENDERS = [
        ('M', 'Male'),
        ('F', 'Female'),
    ]
    gender = models.CharField(max_length=2, choices=GENDERS) 

    age = models.DecimalField(max_digits=4, decimal_places=1) 

    # basic description (color)
    description = models.CharField(max_length=60) 
    breed = models.CharField(max_length=35)

    ITYPES = [('DSH', 'DSH'), ('DMH', 'DMH'), ('DLH', 'DLH')]
    itype = models.CharField(max_length=4, choices = ITYPES)

    STATUSES = [
        ('adopt', 'For adoption'),
        ('temporary', 'Temporary'),
        ('permanent', 'Permanent'),
    ]
    status = models.CharField(max_length=10, choices=STATUSES)
    arrival_date = models.DateField(default=date.today)
    arrival_details = models.TextField()
    medical_history = models.TextField()
    vaccinations = models.TextField()
    is_microchipped = models.BooleanField()
    flea_control_date = models.DateField()
    deworming_date = models.DateField()
    fiv_felv_date = models.DateField()
    special_needs = models.TextField(null=True, blank=True)
    personality = MultiSelectField(choices=PERSONALITY)
    more_personality = models.TextField(null=True, blank=True)
    comments = models.TextField(null=True, blank=True)
    personal_exp = models.TextField(null=True, blank=True)

def upload_path(instance, filename):
    return 'documents/cat_{0}/{1}'.format(instance.cat_id, filename)

class Document(models.Model):
    cat_id = models.IntegerField()  # foreign keys are too difficult with custom path names
    document = models.FileField(upload_to=upload_path)
    name = models.TextField()
    description = models.CharField(max_length=60, blank=True) 
    uploaded_at = models.DateTimeField(auto_now_add=True)
