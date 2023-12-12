import logging
from datetime import date

from dateutil.relativedelta import relativedelta
from django.contrib.auth.hashers import check_password
from django.contrib.auth.hashers import make_password
from django.http import HttpResponse, JsonResponse
from django.utils.crypto import get_random_string
from django.views.generic.base import logger
from . import models, serializers
from .models import Users
from .serializers import VivyaPms_serializer, VivyaPms_serializer1, UserCreateSerializer
from rest_framework.generics import GenericAPIView, UpdateAPIView


# ===============================================admin get method===============================================
class UserProfileInfo( GenericAPIView ):
    serializer_class = VivyaPms_serializer

    def post(self, request, **kwargs):
        try:
            query = Users.objects.filter( email=request.data['email'] )
            serializer_class = VivyaPms_serializer1( query, many=True )
            logger.info( "User data has been fetched Successfully." )
            data = {
                'response_code': 200,
                'message': 'User details fetched successfully',
                'statusFlag': True,
                'status': 'SUCCESS',
                'errorDetails': None,
                'data': serializer_class.data
            }
            return Response( data )
        except Exception as e:
            data = {
                'response_code': 500,
                'message': 'User details fetching failed',
                'statusFlag': False,
                'status': 'FAILED',
                'errorDetails': str( e ),
                'data': []
            }
            logger.error( "User details Fetching process is failed." )
            return Response( data )


class UserProfileInfo1( GenericAPIView ):
    serializer_class = VivyaPms_serializer

    def get(self, request, **kwargs):
        try:
            query = Users.objects.filter( email=kwargs['email'] )
            serializer_class = VivyaPms_serializer1( query, many=True )
            logger.info( "User data has been fetched Successfully." )
            data = {
                'response_code': 200,
                'message': 'User details fetched successfully',
                'statusFlag': True,
                'status': 'SUCCESS',
                'errorDetails': None,
                'data': serializer_class.data
            }
            return Response( data )
        except Exception as e:
            data = {
                'response_code': 500,
                'message': 'User details fetching failed',
                'statusFlag': False,
                'status': 'FAILED',
                'errorDetails': str( e ),
                'data': []
            }
            logger.error( "User details Fetching process is failed." )
            return Response( data )


# ==============================admin create=============================================================
class UserDetailsCreate( GenericAPIView ):
    serializer_class = UserCreateSerializer

    def post(self, request, **kwargs):
        try:
            serializer_class = UserCreateSerializer( data=request.data )
            if serializer_class.is_valid():
                hashed_password = make_password( serializer_class.validated_data['password'] )
                serializer_class.validated_data['password'] = hashed_password
                if serializer_class.validated_data['valid_option'].lower() == 'yearly':
                    serializer_class.validated_data['end_date'] = date.today() + relativedelta( years=1 )
                elif serializer_class.validated_data['valid_option'].lower() == 'half yearly':
                    serializer_class.validated_data['end_date'] = date.today() + relativedelta( months=6 )
                elif serializer_class.validated_data['valid_option'].lower() == 'quarterly':
                    serializer_class.validated_data['end_date'] = date.today() + relativedelta( months=3 )
                serializer_class.save()
            logging.info( "User data has been posted Successfully." )
            data = {
                'response_code': 200,
                'message': 'User details posted successfully',
                'statusFlag': True,
                'status': 'SUCCESS',
                'errorDetails': None,
                'data': serializer_class.data
            }
            return Response( data )
        except Exception as e:
            data = {
                'response_code': 500,
                'message': 'User details posting failed',
                'statusFlag': False,
                'status': 'FAILED',
                'errorDetails': str( e ),
                'data': []
            }
            logging.error( "User details posting process is failed." )
            return Response( data )

# ============================delete for room type===================================================
class Delete_product( GenericAPIView ):
    queryset = models.RoomType.objects.all()

    def delete(self, request, room_type_id, *args, **kwargs):
        try:
            query = models.RoomType.objects.get( room_type_id=room_type_id )
            serializer_instance = serializers.deleteRoomTypeSerializer( query )
            serialized_data = serializer_instance.data
            query.delete()
            logging.info( "User data has been deleted successfully." )

            data = {
                'response_code': 200,
                'message': 'User details deleted successfully',
                'statusFlag': True,
                'status': 'SUCCESS',
                'errorDetails': None,
                'data': serialized_data  # Include the serialized data, not the instance
            }
            return Response( data )
        except models.RoomType.DoesNotExist:
            data = {
                'response_code': 404,
                'message': 'User details not found',
                'statusFlag': False,
                'status': 'FAILED',
                'errorDetails': 'RoomType not found',
                'data': []
            }
            logging.error( "User details not found for deletion." )
            return Response( data )
        except Exception as e:
            data = {
                'response_code': 500,
                'message': 'User details deletion failed',
                'statusFlag': False,
                'status': 'FAILED',
                'errorDetails': str( e ),
                'data': []
            }
            logging.error( "User details deletion process is failed." )
            return Response( data )


# ================================get all  method for room===================================================================

class Get_all( GenericAPIView ):

    def get(self, request, **kwargs):
        try:
            query = models.Room.objects.all()
            serializer_class = serializers.GetRoomSerializer( query, many=True )
            logger.info( "Room data has been fetched Successfully." )
            data = {
                'response_code': 200,
                'message': 'Room details fetched successfully',
                'statusFlag': True,
                'status': 'SUCCESS',
                'errorDetails': None,
                'data': serializer_class.data
            }
            return Response( data )
        except Exception as e:
            data = {
                'response_code': 500,
                'message': 'Room details fetching failed',
                'statusFlag': False,
                'status': 'FAILED',
                'errorDetails': str( e ),
                'data': []
            }
            logger.error( "Room details Fetching process is failed." )
            return Response( data )


# ====================================get by id room================================


class GetByID( GenericAPIView ):
    serializer_class = serializers.GetRoomSerializer

    def get(self, request, room_id, **kwargs):
        try:
            model = models.Room.objects.get( room_id=room_id )
            serializer_class = serializers.GetRoomSerializer( model )
            logger.info( "User data has been fetched Successfully." )
            data = {
                'response_code': 200,
                'message': 'User details fetched successfully',
                'statusFlag': True,
                'status': 'SUCCESS',
                'errorDetails': None,
                'data': serializer_class.data
            }
            return Response( data )

        except Exception as e:
            data = {
                'response_code': 500,
                'message': 'User details fetching failed',
                'statusFlag': False,
                'status': 'FAILED',
                'errorDetails': str( e ),
                'data': []
            }
            logger.error( "User details Fetching process is failed." )
            return Response( data )


# ===================================================login super admin ======================

class LoginAPI( GenericAPIView ):
    serializer_class = serializers.LoginSerializer

    def post(self, request, *args, **kwargs):
        email = request.data.get( 'email' )
        password = request.data.get( 'password' )
        user = models.Users.objects.get( email=email )
        if check_password( password, user.password ):
            user_token = self.get_or_generate_user_token( user )
            account_status = self.get_account_status( user )
            logger.info( "User data has been fetched Successfully." )
            data = {
                'response_code': 200,
                'message': 'User login successfully',
                'statusFlag': True,
                'status': 'SUCCESS',
                'errorDetails': None,
                'token': user_token,
                'data': {'user_id': user.user_id,
                         'first_name': user.first_name,
                         'email': user.email},
                "account_status": account_status
            }
            return JsonResponse( data )

        else:
            data = {
                'response_code': 500,
                'message': 'User login successfully',
                'statusFlag': False,
                'status': 'FAILED',
                'errorDetails': 'User login successfully',
                'data': []
            }
            logger.error( "User details Fetching process is failed." )
            return JsonResponse( data )

    def get_or_generate_user_token(self, user):
        token = models.VivyapmsAppAuthtoken.objects.filter( user_id=user.user_id ).first()

        if not token:
            token = models.VivyapmsAppAuthtoken.objects.create(
                digest=get_random_string( 128 ),
                token_key=get_random_string( 8 ),
                created=timezone.now(),
                user_id=user.user_id
            )

        return token.token_key

    def get_account_status(self, user):
        if user.user_type == "super-admin":
            return "S"
        elif user.user_type == "admin" and date.today() < user.end_date:
            return "A"
        elif user.user_type == "user":
            return "U"
        else:
            return "Unknown"


# =============================================================excel==========================================================
from rest_framework.parsers import MultiPartParser
from rest_framework.decorators import parser_classes
from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import GenericAPIView
import pandas as pd
from django.utils import timezone


@parser_classes( [MultiPartParser] )
class ExcelFileUploadView( GenericAPIView ):
    serializer_class = serializers.RoomUploadSerializer

    def post(self, request, format=None):
        serializer = serializers.RoomUploadSerializer( data=request.data )

        if serializer.is_valid():
            excel_file = request.FILES['excel_file']
            df = pd.read_excel( excel_file )
            for index, row in df.iterrows():
                try:
                    property_name = row['Property name']
                    name = row['Room type']
                    property_objects = models.Property.objects.filter( name=property_name )
                    print( property_objects )
                    for property_obj in property_objects:
                        room_type_objects = models.RoomType.objects.filter( name=name )
                        print( room_type_objects )
                        if room_type_objects.count() == 1:
                            room_type_id = room_type_objects.first().room_type_id
                        elif room_type_objects.count() > 1:
                            print( "Multiple room type objects with the same name. Skipping row." )
                            continue
                        else:
                            print( "No RoomType object with the specified name. Skipping row." )
                            continue
                    print( room_type_id )

                    models.Room.objects.create(
                        admin_id=serializer.validated_data['admin_id'],
                        property_id=property_obj.property_id,
                        name=row['Room number'],
                        room_occupaied_status=row['Availability'],
                        room_type_id=room_type_id,
                        is_active=row['Status'],
                        created_at=timezone.now(),
                    )

                except Exception as e:
                    print( f"Error processing row {index}: {e}" )

            return Response( {'message': 'Data imported successfully'}, status=status.HTTP_201_CREATED )
        else:
            return Response( serializer.errors, status=status.HTTP_400_BAD_REQUEST )


# ================================================UPDATE FOR ROOM========================================================

class UpdateRoom( UpdateAPIView ):
    serializer_class = serializers.UpdateRoomSerializer

    def put(self, request, *args, **kwargs):
        try:
            data = models.Room.objects.get( room_id=request.data['room_id'] )
            serializer_instance = serializers.GetRoomSerializer( instance=data, data=request.data )
            serializer_instance.is_valid( raise_exception=True )
            self.perform_update( serializer_instance )
            logger.info( "Room data has been updated Successfully." )
            data = {
                'response_code': 200,
                'message': 'Room details updated successfully',
                'statusFlag': True,
                'status': 'SUCCESS',
                'errorDetails': None,
                'data': serializer_instance.data
            }
            return Response( data )
        except Exception as e:
            data = {
                'response_code': 500,
                'message': 'Room details updating failed',
                'statusFlag': False,
                'status': 'FAILED',
                'errorDetails': str( e ),
                'data': []
            }
            logger.error( "Room details updating process is failed." )
            return Response( data )


# =======================================================UPDATE FOR ROOM TYPE==============================================
class UpdateRoomType( UpdateAPIView ):
    serializer_class = serializers.UpdateRoomTypeSerializer

    def put(self, request, *args, **kwargs):
        try:
            data = models.RoomType.objects.get( room_type_id=request.data['room_type_id'] )
            serializer_instance = serializers.updateRoomTypeSerializer( instance=data, data=request.data )
            serializer_instance.is_valid( raise_exception=True )
            self.perform_update( serializer_instance )
            logger.info( "Room type data has been updated Successfully." )
            data = {
                'response_code': 200,
                'message': 'Room type details updated successfully',
                'statusFlag': True,
                'status': 'SUCCESS',
                'errorDetails': None,
                'data': serializer_instance.data
            }
            return Response( data )
        except Exception as e:
            data = {
                'response_code': 500,
                'message': 'Room type details updating failed',
                'statusFlag': False,
                'status': 'FAILED',
                'errorDetails': str( e ),
                'data': []
            }
            logger.error( "Room type details updating process is failed." )
            return Response( data )


# =========================================================get all document type==================================================================


class Get_document_type( GenericAPIView ):

    def get(self, request, **kwargs):
        try:
            query = models.DocumentType.objects.all()
            serializer_class = serializers.GetDocumentTypeSerializer( query, many=True )
            logger.info( "Document Type data has been fetched Successfully." )
            data = {
                'response_code': 200,
                'message': 'Document Type details fetched successfully',
                'statusFlag': True,
                'status': 'SUCCESS',
                'errorDetails': None,
                'data': serializer_class.data
            }
            return Response( data )
        except Exception as e:
            data = {
                'response_code': 500,
                'message': 'Document Type fetching failed',
                'statusFlag': False,
                'status': 'FAILED',
                'errorDetails': str( e ),
                'data': []
            }
            logger.error( "Document Type Fetching process is failed." )
            return Response( data )


# ==========================================================Get visa type==================================================


class Get_visa_type( GenericAPIView ):
    # serializer_class = serializers.GetVisaTypeSerializer

    def get(self, request, **kwargs):
        try:
            query = models.VisaTypes.objects.all()
            serializer_class = serializers.GetVisaTypeSerializer( query, many=True )
            logger.info( "Visa Type data has been fetched Successfully." )
            data = {
                'response_code': 200,
                'message': 'Visa Type details fetched successfully',
                'statusFlag': True,
                'status': 'SUCCESS',
                'errorDetails': None,
                'data': serializer_class.data
            }
            return Response( data )
        except Exception as e:
            data = {
                'response_code': 500,
                'message': 'Visa Type fetching failed',
                'statusFlag': False,
                'status': 'FAILED',
                'errorDetails': str( e ),
                'data': []
            }
            logger.error( "Visa Type Fetching process is failed." )
            return Response( data )

# ========================================================update property================================================


class UpdateProperty( UpdateAPIView ):
    serializer_class = serializers.UpdatePropertySerializer

    def put(self, request, *args, **kwargs):
        try:
            data = models.Property.objects.get(property_id=request.data['property_id'])
            serializer_instance = serializers.PropertySerializer(instance=data, data=request.data)
            serializer_instance.is_valid(raise_exception=True)
            self.perform_update( serializer_instance )
            logger.info("Property data has been updated Successfully.")
            data = {
                'response_code': 200,
                'message': 'Property details updated successfully',
                'statusFlag': True,
                'status': 'SUCCESS',
                'errorDetails': None,
                'data': serializer_instance.data
            }
            return Response( data )
        except Exception as e:
            data = {
                'response_code': 500,
                'message': 'Property details updating failed',
                'statusFlag': False,
                'status': 'FAILED',
                'errorDetails': str( e ),
                'data': []
            }
            logger.error( "Property details updating process is failed." )
            return Response( data )
