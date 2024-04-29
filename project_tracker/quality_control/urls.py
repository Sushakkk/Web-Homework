from django.urls import path
from . import views

app_name = 'quality_control'

urlpatterns = [
    # path('', views.Index_1_View.as_view(), name='index_1'),
    path('', views.index_1, name='index_1'),
    path('bugs/', views.bug_list, name='bug_list'),
    path('features/', views.feature_list, name='feature_list'),
    path('bugs/<int:bug_id>/', views.bug_detail, name='bug_detail'),
    # path('bugs/<int:bug_id>/', views.BugReportDetailView.as_view(), name='bug_detail'),
    path('features/<int:feature_id>/', views.feature_detail, name='feature_detail'),
    # path('features/<int:feature_id>/', views.FeatureRequestView.as_view(), name='feature_detail'),
    path('bugs/new_bug/', views.create_BugReport, name='create_BugReport'),
    path('feature/new_feature/', views.create_FeatureRequest, name='create_FeatureRequest'),
    path('bugs/<int:bug_id>/update/', views.update_BugReport, name='update_BugReport'),
    path('/feature/<int:feature_id>/update/', views.update_FeatureRequest, name='update_FeatureRequest'),
    path('bugs/<int:bug_id>/delete/', views.delete_BugReport, name='delete_BugReport'),
    path('/feature/<int:feature_id>/delete/', views.delete_FeatureRequest, name='delete_FeatureRequest'),
]

