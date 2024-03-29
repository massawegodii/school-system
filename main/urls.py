from django.urls import path
from .import views
from .views import course_form, display_course,add_student2,display_module


urlpatterns = [
    
    path('course-form/', course_form, name='course_form'),
    path('display-course/', display_course, name='display_course'),
     path('display_module/', display_module, name='display_module'),
    path('add_student2/', add_student2, name='add_student2'),
    path ("register/",views.registerPage, name = 'register'),
    path("login/",views.loginPage, name= "login"),
    path("logout/",views.logoutPage, name = "logout"),
    path("",views.home, name= "home"),
    path("student_home/",views.studentHome, name ="student_home"),
    path("add_student/",views.add_student, name ='add_student'),
    path("add_admin/",views.add_admin, name ='add_admin'),
    path("add_subject/",views.add_subject, name ='add_subject'),
    path("get_att/",views.get_att, name ='get_att'),
    path("add_j/", views.add_j, name ='add_j'),
    path("get_subtype/",views.get_subtype, name ='get_subtype'),
    path("full_attendance/",views.full_attendance, name ='full_attendance'),
    path("full_marksheet/",views.full_marksheet, name ='full_marksheet'),
    path("full_skillset/",views.full_skillset, name ='full_skillset'),
    path("result/<course_code>/<dept>", views.search_result, name = 'search_result'),
    path("result1/", views.search_result1, name = 'search_result1'),
    path("result/update/<result_id>/<course_code>", views.update_result, name ='update_result'),
    path("add_result/<dept>/<course_id>", views.add_result, name='add_result'),
    path("search_student_registered/", views.search_student_registered, name = 'search_student_registered'),
    path("get_subtype_networking_marks", views.get_subtype_networking_marks, name = 'get_subtype_networking_marks'),
    path("get_subtype_ai_marks", views.get_subtype_ai_marks, name = 'get_subtype_ai_marks'),
    path("get_subtype_sys_n_media_marks", views.get_subtype_sys_n_media_marks, name = 'get_subtype_sys_n_media_marks'),
    path("get_subtype_dbms_marks", views.get_subtype_dbms_marks, name = 'get_subtype_dbms_marks'),
    path("get_subtype_project_marks", views.get_subtype_project_marks, name = 'get_subtype_project_marks'),
    path("get_subtype_programming_marks", views.get_subtype_programming_marks, name = 'get_subtype_programming_marks'),
    path("get_all_the_marks", views.get_all_the_marks, name = 'get_all_the_marks'),
    path('pdf/', views.GeneratePdf.as_view(),name ="generate_pdf"),
    path('pdf2/<course_id>/<dept_id>', views.GeneratePdf2.as_view(),name ="generate_pdf2"),
    path('ranksheet/', views.subject_ranksheet,name ="ranksheet"),
    path('add_teacher/', views.registerPageTeacher,name ="add_teacher"),
    path('add_dept/', views.addDept,name ="add_dept"),
    path('teacher_home/', views.teacher_home,name ="teacher_home"),
    path('assign_teacher_dept_search/', views.assign_teacher_dept_search,name ="assign_teacher_dept_search"),
    # path('add_module/', views.add_module,name ="add_module"),
    path('assign_teacher/<dept_id>', views.assign_teacher,name ="assign_teacher"),
    # path('student_sub_register/', views.student_sub_register,name ="student_sub_register"),
    path('see_registration_status/', views.see_registration_status,name ="see_registration_status"),
    path('teacher_approve_search/', views.teacher_approve_search,name ="teacher_approve_search"),
    path('teacher_approval/<course_code>/<student_dept>', views.teacher_approval,name ="teacher_approval"),
    path('course_wise_participation/', views.courseWiseParticipation,name ="course_wise_participation"),
    path('course_wise_performance/', views.course_wise_performance,name ="course_wise_performance"),
    path('session_wise_courses/', views.session_wise_courses,name ="session_wise_courses"),
    path('student_rating/', views.student_rating,name ="student_rating"),
    path('get_ratings_teacher/', views.get_ratings_teacher,name ="get_ratings_teacher"),
    path('get_ratings_admin/', views.get_ratings_admin,name ="get_ratings_admin"),
    path('dept_performance/', views.dept_performance,name ="dept_performance"),
    path('subject_ranksheet_teacher/', views.subject_ranksheet_teacher,name ="subject_ranksheet_teacher"),
    path('delete_result/', views.delete_result,name ="delete_result"),
    path('delete_result2/<dept>/<course_id>', views.delete_result2,name ="delete_result2"),
    path('teacher_subject_list/', views.teacher_subject_list,name ="teacher_subject_list"),
    path('delete_student/', views.delete_student,name ="delete_student"),
    path('remove_teacher/', views.remove_teacher,name ="remove_teacher"),





]