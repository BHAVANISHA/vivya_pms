from VivyaPms import swagger_service
from django.urls import path, include
from .views import UserProfileInfo, UserDetailsCreate,Delete_product
from VivyaPms_app import views
urlpatterns = [

    path( 'docs/', swagger_service.schema_view.with_ui( 'swagger', cache_timeout=0 ),
          name='schema-swagger-ui' ),
    path( 'using_get/<str:email>', views.UserProfileInfo1.as_view() ),
    path( 'using_post/', UserProfileInfo.as_view() ),
    path( 'admin_create/', UserDetailsCreate.as_view() ),
    path( 'login/', views.LoginAPI.as_view(), name='knox_login' ),
    path( 'delete/room_type/<int:room_type_id>', Delete_product.as_view() ),
    path('get_all/room/',views.Get_all.as_view()),
    path('get_by_id/room/<int:room_id>/',views.GetByID.as_view()),
    path( 'import-excel/',views.ExcelFileUploadView.as_view(), name='import-room' ),
    path('update room/',views.UpdateRoom.as_view()),
    path('update room type/',views.UpdateRoomType.as_view()),
    path('get_document_type/',views.Get_document_type.as_view()),
    path( 'get_visa_type/', views.Get_visa_type.as_view() ),
    path('update_property/',views.UpdateProperty.as_view())

]