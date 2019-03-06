from django.db import models
from django.core.validators import FileExtensionValidator
from django.core.validators import ValidationError
# Create your models here.
def max_size_allowed(value): # add this to some file where you can import it from
    limit = 2*1024*1024
    if value.size>limit:
        raise ValidationError('File too large. Size should not exceed 2 MB.')
COURSE_CHOICES = (
    ('btech','B-Tech'),
    ('bcom', 'B-Com'),
    ('mba','MBA'),
    )

class amcat_login_with_face_tracker(models.Model):
    first_name = models.CharField(max_length=50)
    middle_name=models.CharField(max_length=50,null=True)
    last_name = models.CharField(max_length=50)
    model_pic = models.ImageField(upload_to ='pic_folder/')
    course = models.CharField(max_length=10, choices=COURSE_CHOICES, default='btech')
    


