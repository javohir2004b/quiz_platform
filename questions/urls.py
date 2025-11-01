# from django.urls import path
# from questions import views as questions_views
#
# urlpatterns = [
#     path('register_view/',questions_views.register_view),
#     path('question_create_get/',questions_views.question_create_get),
#     path('option_cr_view/',questions_views.option_cr_view),
#     path('user_detail/<int:pk>/', questions_views.user_detail),
#     path('question_rud/<int:pk>/', questions_views.question_rud),
#     path('option_rud/<int:pk>/', questions_views.option_rud),
#     path('result_rud/<int:pk>/', questions_views.result_rud),
#     path('result_rud/', questions_views.result_rud),
#     path('answer/', questions_views.check_answer, name="check_answer"),
#     path('user_score/<int:pk>/', questions_views.user_score),
# ]



from django.urls import path
from questions import views as questions_views

urlpatterns = [
    path('register_view/', questions_views.register_view),
    path('question_create_get/', questions_views.question_create_get),
    path('option_cr_view/', questions_views.option_cr_view),
    path('user_detail/<int:pk>/', questions_views.user_detail),
    path('question_rud/<int:pk>/', questions_views.question_rud),
    path('option_rud/<int:pk>/', questions_views.option_rud),
    path('result_rud/<int:pk>/', questions_views.result_rud),
    path('result_rud/', questions_views.result_rud),
    path('answer/', questions_views.check_answer, name="check_answer"),
    path('user_score/<int:pk>/', questions_views.user_score),
]
