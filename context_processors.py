# from patient.models import PatientProfile
# from doctor.models import DoctorProfile
#
# def user_type(request):
# 
#     if request.user.is_authenticated:
#         if PatientProfile.objects.filter(patient = request.user):
#             isuser = PatientProfile.objects.filter(patient = request.user)
#         elif DoctorProfile.objects.filter(doctor=request.user):
#             isuser = DoctorProfile.objects.filter(doctor=request.user)
#         usertype = [int(each.usertype) for each in isuser][0]
#
#         return {
#             'usertype' : usertype
#         }
#     else:
#         x=3
#         return {
#             'x' : x
#         }
