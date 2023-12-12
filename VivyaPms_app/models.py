from django.db import models


#
class VivyapmsAppAuthtoken(models.Model):
    digest = models.CharField(primary_key=True, max_length=128)
    token_key = models.CharField(max_length=8)
    created = models.DateTimeField()
    expiry = models.DateTimeField(blank=True, null=True)
    user_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'VivyaPms_app_authtoken'


class VivyapmsAppUsersupdate(models.Model):
    user_id = models.AutoField(primary_key=True)
    user_type = models.CharField(max_length=15, blank=True, null=True)
    first_name = models.CharField(max_length=255, blank=True, null=True)
    last_name = models.CharField(max_length=255, blank=True, null=True)
    email = models.CharField(max_length=255, blank=True, null=True)
    phone = models.CharField(max_length=15, blank=True, null=True)
    password = models.CharField(max_length=255, blank=True, null=True)
    is_active = models.CharField(max_length=1, blank=True, null=True)
    activated_date = models.DateTimeField(blank=True, null=True)
    last_login_date = models.DateTimeField(blank=True, null=True)
    last_logout_date = models.DateTimeField(blank=True, null=True)
    email_verified = models.CharField(max_length=1, blank=True, null=True)
    user_limit = models.IntegerField(blank=True, null=True)
    valid_option = models.CharField(max_length=15, blank=True, null=True)
    end_date = models.DateField(blank=True, null=True)
    property_id = models.IntegerField(blank=True, null=True)
    admin_id = models.IntegerField(blank=True, null=True)
    status = models.CharField(max_length=1, blank=True, null=True)
    created_by = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    modified_by = models.IntegerField(blank=True, null=True)
    modified_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'VivyaPms_app_usersupdate'


class Attachments(models.Model):
    document_id = models.IntegerField()
    file_path = models.CharField(max_length=255)
    file_name = models.CharField(max_length=255)
    thumbnail = models.CharField(max_length=255)
    file_size = models.CharField(max_length=10)
    file_ext = models.CharField(max_length=5)
    document_type = models.CharField(max_length=50, blank=True, null=True)
    attachment_type = models.CharField(max_length=50, blank=True, null=True)
    ocr_data = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'attachments'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class Country(models.Model):
    admin_id = models.IntegerField()
    short_name = models.CharField(max_length=5)
    short_name_two = models.CharField(max_length=2)
    name = models.CharField(max_length=150)
    country_id = models.IntegerField()
    is_active = models.CharField(max_length=1, db_comment='comment truncated A Active, D Deactive')
    status = models.CharField(max_length=1, db_comment='L Live, D Deleted')
    created_by = models.IntegerField()
    created_at = models.DateTimeField()
    modified_by = models.IntegerField(blank=True, null=True)
    modified_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'country'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class DocumentDetails(models.Model):
    document_details_id = models.AutoField(primary_key=True)
    property_id = models.IntegerField()
    admin_id = models.IntegerField()
    duration_of_stay = models.IntegerField()
    duration_stay_india = models.IntegerField()
    date_of_arrival_in_india = models.DateTimeField(blank=True, null=True)
    arriving_from = models.IntegerField(blank=True, null=True)
    next_destination = models.IntegerField(blank=True, null=True)
    native_country_address = models.CharField(max_length=255, blank=True, null=True)
    arrived_from_port = models.IntegerField(blank=True, null=True)
    arrived_at_port = models.CharField(max_length=255, blank=True, null=True)
    address_in_india = models.CharField(max_length=255, blank=True, null=True)
    register_no = models.CharField(max_length=255, blank=True, null=True)
    rfid_room_key = models.CharField(max_length=255, blank=True, null=True)
    c_form_no = models.CharField(max_length=50, blank=True, null=True)
    adult = models.IntegerField(blank=True, null=True)
    child = models.IntegerField(blank=True, null=True)
    check_in_date_time = models.DateTimeField(blank=True, null=True)
    given_name = models.CharField(max_length=255, blank=True, null=True)
    family_name = models.CharField(max_length=150, blank=True, null=True)
    gender = models.CharField(max_length=10, blank=True, null=True)
    nationality = models.IntegerField(blank=True, null=True)
    dob = models.DateField(blank=True, null=True)
    visit_purpose = models.IntegerField(blank=True, null=True)
    nationality_by_birth = models.IntegerField(blank=True, null=True)
    parentage = models.IntegerField(blank=True, null=True)
    document_type = models.IntegerField(blank=True, null=True)
    email = models.CharField(max_length=150, blank=True, null=True)
    phone = models.CharField(max_length=150, blank=True, null=True)
    passport_number = models.CharField(max_length=150, blank=True, null=True)
    passport_date_of_issue = models.DateField(blank=True, null=True)
    passport_valid_till = models.DateField(blank=True, null=True)
    passport_place_of_issue = models.CharField(max_length=250, blank=True, null=True)
    passport_place_of_issue_country = models.IntegerField(blank=True, null=True)
    visa_number = models.CharField(max_length=150, blank=True, null=True)
    visa_date_of_issue = models.DateField(blank=True, null=True)
    visa_valid_till = models.DateField(blank=True, null=True)
    visa_place_of_issue_city = models.CharField(max_length=150, blank=True, null=True)
    visa_place_of_issue_country = models.IntegerField(blank=True, null=True)
    type_of_visa = models.CharField(max_length=150, blank=True, null=True)
    visa_no_of_entry = models.CharField(max_length=150, blank=True, null=True)
    photo = models.CharField(max_length=150, blank=True, null=True)
    is_submitted = models.CharField(max_length=1, blank=True, null=True, db_comment='Y submitted, N not submitted')
    restore_data = models.CharField(max_length=1, db_comment='N No, Y Yes')
    status = models.CharField(max_length=1, blank=True, null=True, db_comment='L Live, D Deleted')
    created_at = models.DateTimeField()
    created_by = models.IntegerField()
    modified_at = models.DateTimeField(blank=True, null=True)
    modified_by = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'document_details'


class DocumentType(models.Model):
    name = models.CharField(max_length=150)
    admin_id = models.IntegerField()
    is_active = models.CharField(max_length=1, db_comment='comment truncated A Active, D Deactive')
    status = models.CharField(max_length=1, db_comment='L Live, D Deleted')
    created_by = models.IntegerField()
    created_at = models.DateTimeField()
    modified_by = models.IntegerField(blank=True, null=True)
    modified_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'document_type'


class MapRoomDocument(models.Model):
    room_id = models.IntegerField()
    document_id = models.IntegerField()
    primary_document_id = models.IntegerField(blank=True, null=True)
    secondary_document_id = models.CharField(max_length=250, blank=True, null=True)
    check_in_status = models.CharField(max_length=1, db_comment='A active, D deactive')
    check_in_date = models.DateTimeField(blank=True, null=True)
    check_out_date = models.DateTimeField(blank=True, null=True)
    from_room_id = models.IntegerField()
    is_room_changed = models.CharField(max_length=1)
    room_check_in_type = models.CharField(max_length=50, blank=True, null=True)
    room_check_out_type = models.CharField(max_length=50, blank=True, null=True)
    adult = models.IntegerField(blank=True, null=True)
    child = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField()
    created_by = models.IntegerField()
    modified_at = models.DateTimeField(blank=True, null=True)
    modified_by = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'map_room_document'


class Property(models.Model):
    property_id = models.AutoField(primary_key=True)
    admin_id = models.IntegerField()
    property_type_id = models.IntegerField()
    name = models.CharField(max_length=255)
    contact_number = models.CharField(max_length=50)
    website = models.CharField(max_length=255)
    mobile_number = models.CharField(max_length=255)
    manager_name = models.CharField(max_length=255)
    registration_id = models.CharField(max_length=255)
    po_box = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=255)
    pin = models.CharField(max_length=10)
    logo = models.CharField(max_length=225, blank=True, null=True)
    is_active = models.CharField(max_length=1, db_comment='comment truncated A Active, D Deactive')
    status = models.CharField(max_length=1, db_comment='L Live, D Deleted')
    created_by = models.IntegerField()
    created_at = models.DateTimeField()
    modified_by = models.IntegerField(blank=True, null=True)
    modified_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'property'


class PropertyType(models.Model):
    property_type_id = models.AutoField(primary_key=True)
    admin_id = models.IntegerField()
    name = models.CharField(max_length=255)
    is_active = models.CharField(max_length=1, db_comment='comment truncated A Active, D Deactive')
    status = models.CharField(max_length=1, db_comment='L Live, D Delete')
    created_by = models.IntegerField()
    created_at = models.DateTimeField()
    modified_by = models.IntegerField(blank=True, null=True)
    modified_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'property_type'


class PurposeToVisit(models.Model):
    admin_id = models.IntegerField()
    visit_id = models.IntegerField()
    name = models.CharField(max_length=150)
    is_active = models.CharField(max_length=1, db_comment='comment truncated A Active, D Deactive')
    status = models.CharField(max_length=1, db_comment='L Live, D Deleted')
    created_by = models.IntegerField()
    created_at = models.DateTimeField()
    modified_by = models.IntegerField(blank=True, null=True)
    modified_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'purpose_to_visit'


class RoomType(models.Model):
    room_type_id = models.AutoField(primary_key=True)
    admin_id = models.IntegerField()
    name = models.CharField(max_length=255)
    is_active = models.CharField(max_length=1)
    status = models.CharField(max_length=1, blank=True, null=True)
    created_by = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    modified_by = models.IntegerField(blank=True, null=True)
    modified_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'room_type'
class Room(models.Model):
    room_id = models.AutoField(primary_key=True)
    admin_id = models.IntegerField()
    property_id = models.IntegerField()
    name = models.CharField(max_length=150)
    room_occupaied_status = models.CharField(max_length=1,null=True)
    room_type_id = models.IntegerField()
    room_status = models.CharField(max_length=1,null=True)
    is_active = models.CharField(max_length=1)
    status = models.CharField(max_length=1,null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    created_by = models.IntegerField(blank=True, null=True)
    modified_at = models.DateTimeField(blank=True, null=True)
    modified_by = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'room'


class Setting(models.Model):
    meta_key = models.CharField(max_length=50)
    meta_value = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'setting'


class SpecialCategory(models.Model):
    admin_id = models.IntegerField()
    sp_cat_id = models.IntegerField()
    name = models.CharField(max_length=150)
    status = models.CharField(max_length=1, db_comment='L Live, D Deleted')
    created_by = models.IntegerField()
    created_at = models.DateTimeField()
    modified_by = models.IntegerField(blank=True, null=True)
    modified_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'special_category'


class UserPermission(models.Model):
    user = models.AutoField(primary_key=True)
    user_id = models.IntegerField()
    page_name = models.CharField(max_length=50)
    view = models.CharField(max_length=1)
    create = models.CharField(max_length=1)
    edit = models.CharField(max_length=1)
    delete = models.CharField(max_length=1)
    other_permission = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'user_permission'


class Users(models.Model):
    user_id = models.AutoField(primary_key=True)
    user_type = models.CharField(max_length=15)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(unique=True, max_length=255)
    phone = models.CharField(max_length=15)
    password = models.CharField(max_length=255, blank=True, null=True)
    is_active = models.CharField(max_length=1, db_comment='N No, Y Yes')
    activated_date = models.DateTimeField(blank=True, null=True)
    last_login_date = models.DateTimeField(blank=True, null=True)
    last_logout_date = models.DateTimeField(blank=True, null=True)
    email_verified = models.CharField(max_length=1)
    user_limit = models.IntegerField()
    valid_option = models.CharField(max_length=15, blank=True, null=True)
    end_date = models.DateField(blank=True, null=True)
    property_id = models.IntegerField(blank=True, null=True)
    admin_id = models.IntegerField(blank=True, null=True)
    status = models.CharField(max_length=1, db_comment='L Live, D Deleted')
    created_by = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    modified_by = models.IntegerField(blank=True, null=True)
    modified_at = models.DateTimeField(blank=True, null=True)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField(blank=True, null=True)
    is_staff = models.IntegerField(blank=True, null=True)
    date_joined = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'users'


class UsersGroups(models.Model):
    users_id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'users_groups'


class UsersUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    users_id = models.IntegerField()
    permission_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'users_user_permissions'


class VisaTypes(models.Model):
    admin_id = models.IntegerField()
    short_name = models.CharField(max_length=5)
    name = models.CharField(max_length=150)
    is_active = models.CharField(max_length=1, db_comment='comment truncated A Active, D Deactive')
    status = models.CharField(max_length=1, db_comment='L Live, D Deleted')
    created_by = models.IntegerField()
    created_at = models.DateTimeField()
    modified_by = models.IntegerField(blank=True, null=True)
    modified_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'visa_types'
