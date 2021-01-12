from django.urls import path, include
from rest_framework import routers

from jist_api.views import *

router = routers.DefaultRouter()
router.register('student', StudentViewSet)
router.register('depertment', DepertmentViewSet)
router.register('branch', BranchViewSet)
router.register('user', UserCreateViewSet)
router.register('password', PasswordChangeViewset)
router.register('oddsemesterfee', OddSemesterFeeViewSet)
router.register('befee', BEFeeViewSet)
router.register('admission', AdmissionViewSet)
router.register('examfee', ExamFeeViewSet)
router.register('spotfee', SpotAdmissionFeeViewSet)
router.register('examination', ExaminationViewSet)
router.register('compartmental', CompartmentalViewSet)
router.register('betterment', BettermentViewSet)
router.register('transfer', Transfer_StudentViewSet)
router.register('prospectus', FormAndProspectusViewSet)
router.register('get_branch', GetBranchViewSet, basename='branch')
router.register('get_department_id', getDepertmentIdViewSet, basename='depertment')
router.register('get_students', getStudentsFromQuery, basename='students')


urlpatterns = [
    path('', include(router.urls)),
    path('signinInfo/', signinInfoView),
    path('token/', token),
    path('refresh_token/', refresh_token),
    path('revoke_token/', revoke_token),
]
