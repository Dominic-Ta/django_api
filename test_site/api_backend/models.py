# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = "auth_group"


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey("AuthPermission", models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = "auth_group_permissions"
        unique_together = (("group", "permission"),)


class AuthPermission(models.Model):
    content_type = models.ForeignKey("DjangoContentType", models.DO_NOTHING)
    codename = models.CharField(max_length=100)
    name = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = "auth_permission"
        unique_together = (("content_type", "codename"),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=30)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()
    last_name = models.CharField(max_length=150)

    class Meta:
        managed = False
        db_table = "auth_user"


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = "auth_user_groups"
        unique_together = (("user", "group"),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = "auth_user_user_permissions"
        unique_together = (("user", "permission"),)


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    change_message = models.TextField()
    content_type = models.ForeignKey(
        "DjangoContentType", models.DO_NOTHING, blank=True, null=True
    )
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    action_flag = models.PositiveSmallIntegerField()

    class Meta:
        managed = False
        db_table = "django_admin_log"


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = "django_content_type"
        unique_together = (("app_label", "model"),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = "django_migrations"


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = "django_session"


class StudentPerformance(models.Model):
    gender = models.TextField(primary_key=True)
    # Note that it's important to have at least one model here to contain the
    # value of primary_key = True.

    """
        Automatic primary key fields

        By default, Django gives each model the following field:

        id = models.AutoField(primary_key=True)

        This is an auto-incrementing primary key.

        If you???d like to specify a custom primary key, j
        ust specify primary_key=True on one of your fields. 
        If Django sees you???ve explicitly set Field.primary_key, 
        it won???t add the automatic id column.

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
