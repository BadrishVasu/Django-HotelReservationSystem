from django.urls import path
from . import views

urlpatterns = [
    path('',views.RoomListView, name='RoomListView'),
    path('room_list/', views.RoomList.as_view(), name='RoomList'),
    path('booking_list/', views.BookingList.as_view(), name='BookingList'),
    path("booking/", views.BookingView.as_view(), name='BookingView'),
    path("room/<category>", views.RoomDetailView.as_view(), name='RoomDetailView'),
    path('booking/cancel/<pk>', views.CancelBookingView.as_view(), name='CancelBooking')
]
