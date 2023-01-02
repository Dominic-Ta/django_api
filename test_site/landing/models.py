from django.db import models

# Create your models here.
class StudentPerformance(models.Model):
    gender = models.TextField(primary_key=True)
    # Note that it's important to have at least one model here to contain the
    # value of primary_key = True.

    """
        Automatic primary key fields

        By default, Django gives each model the following field:

        id = models.AutoField(primary_key=True)

        This is an auto-incrementing primary key.

        If you’d like to specify a custom primary key, j
        ust specify primary_key=True on one of your fields. 
        If Django sees you’ve explicitly set Field.primary_key, 
        it won’t add the automatic id column.

        Each model requires exactly one field to have 
        primary_key=True (either explicitly declared or automatically added).

    """
    race_ethnicity = models.TextField(
        db_column="race/ethnicity", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.
    parental_level_of_education = models.TextField(
        db_column="parental level of education", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.
    lunch = models.TextField(blank=True, null=True)
    test_preparation_course = models.TextField(
        db_column="test preparation course", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.
    math_score = models.TextField(
        db_column="math score", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.
    reading_score = models.TextField(
        db_column="reading score", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.
    writing_score = models.TextField(
        db_column="writing score", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = "student_performance"