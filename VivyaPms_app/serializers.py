from django.contrib.auth import authenticate
from rest_framework import serializers
from VivyaPms_app import models
from VivyaPms_app.models import Users, RoomType, Room, DocumentType, VisaTypes


class VivyaPms_serializer( serializers.ModelSerializer ):
    class Meta:
        model = models.Users
        fields = ['email']


class VivyaPms_serializer1( serializers.ModelSerializer ):
    class Meta:
        model = models.Users
        fields = ['user_id', 'first_name', 'email', 'phone', 'is_active', 'valid_option', 'end_date', 'user_limit']


class UserCreateSerializer( serializers.ModelSerializer ):
    class Meta:
        model = models.Users
        fields = ['user_type', 'user_id', 'first_name', 'email', 'phone', 'is_active', 'valid_option', 'end_date',
                  'user_limit',
                  'last_name', 'password', 'email_verified', 'admin_id', 'status', 'created_at']


class updateRoomTypeSerializer( serializers.ModelSerializer ):
    class Meta:
        model = models.RoomType
        fields = ['name', 'is_active', 'room_type_id']


class deleteRoomTypeSerializer( serializers.ModelSerializer ):
    class Meta:
        model = models.RoomType
        fields = '__all__'


class GetRoomSerializer( serializers.ModelSerializer ):
    class Meta:
        model = models.Room
        fields = "__all__"


class GetDocumentTypeSerializer( serializers.ModelSerializer ):
    class Meta:
        model = models.DocumentType
        fields = "__all__"


class GetVisaTypeSerializer( serializers.ModelSerializer ):
    class Meta:
        model = models.VisaTypes
        fields = "__all__"


# =========================================login super admin ===================================================


class LoginSerializer( serializers.Serializer ):
    email = serializers.EmailField()
    password = serializers.CharField( write_only=True )


# ============================================excel===================================================================


class RoomUploadSerializer( serializers.Serializer ):
    excel_file = serializers.FileField()
    admin_id = serializers.IntegerField()


# ===============================================update room==============================================================
class UpdateRoomSerializer( serializers.Serializer ):
    property_id = serializers.IntegerField()
    room_id = serializers.IntegerField()
    room_type_id = serializers.IntegerField()
    admin_id = serializers.IntegerField()
    name = serializers.CharField()
    is_active = serializers.CharField()


# ===============================================update room type=====================================================

class UpdateRoomTypeSerializer( serializers.Serializer ):
    is_active = serializers.CharField( max_length=1 )
    room_type_id = serializers.IntegerField()
    name = serializers.CharField( max_length=150 )
    admin_id = serializers.IntegerField()


# ==============================================update property=============================

class UpdatePropertySerializer( serializers.Serializer ):
    property_id = serializers.IntegerField()
    admin_id = serializers.IntegerField()
    property_type_id = serializers.IntegerField()
    name = serializers.CharField()
    contact_number = serializers.CharField( max_length=50 )
    website = serializers.CharField( max_length=255 )
    mobile_number = serializers.CharField( max_length=255 )
    manager_name = serializers.CharField( max_length=255 )
    registration_id = serializers.CharField( max_length=255 )
    po_box = serializers.CharField( max_length=255 )
    email = serializers.CharField( max_length=255 )
    address = serializers.CharField( max_length=255 )
    city = serializers.CharField( max_length=255 )
    state = serializers.CharField( max_length=255 )
    pin = serializers.CharField( max_length=10 )
    logo = serializers.CharField()
    is_active = serializers.CharField()
    created_at = serializers.CharField()
    created_by = serializers.IntegerField()
    status = serializers.CharField()


class PropertySerializer( serializers.ModelSerializer ):
    class Meta:
        model = models.Property
        fields = '__all__'
