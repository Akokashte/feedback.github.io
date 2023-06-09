from datetime import datetime
from django.contrib import messages
# used for authentication to get user info i.e for authentication purpose
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User # used for signup
from django.shortcuts import render,redirect,HttpResponse
from home.models import Feedback,Contact,AcademicForm, TheoryFeedback, PracticalFeedback,Practical, ParentsFeedback, AlumniFeedback
import pandas as pd
import datetime

# Create your views here.
# def forgotpass(request):
#     if request.method == 'POST':
#         global otp, email
#         username = request.POST['username']
#         fname = request.POST['fname']
#         lname = request.POST['lname']
#         pass1 = request.POST['pass1']
#         pass2 = request.POST['pass2']
#         try:

#             entered_otp = request.POST['otp']
#             print('trying', entered_otp)
#             print(otp)
#             if int(entered_otp) == int(otp):
#                 return render(request, 'newpass.html')
#             else:
#                 return render(request, 'forgotpass.html', {'msg':"OTP didn't matched", 'otp':''})
#         except:
#             otp = randint(100000, 999999)
#             body = f'The OTP for password reset is {otp}'
            
#             with connection.cursor() as cursor:
#                 try:
#                     email = request.POST["email"]
#                     cursor.execute("select name from userinfo where email = %s", [email])
#                     row = cursor.fetchone()
#                 except Exception as e:
#                     return render(request, 'forgotpass.html',{'msg':"Error while connecting to database", 'otp':''})

#             if row != None:
#                 try:
#                     send_mail(
#                     'OTP',
#                     body,
#                     email,
#                     [f'{request.POST["email"]}'],
#                     fail_silently=False,
#                     )
#                     return(render(request, "forgotpass.html",{'otp':otp}))
#                 except Exception as e:
#                     print(e)
#             else:
#                 return render(request, 'forgotpass.html',{'msg':"Email not found in database. You don't have accound", 'otp':''})
#     return(render(request, "forgotpass.html", {'otp':''} ))
    


# Authentication API's
def handleSignup(request):
    if request.method == 'POST':
        # Get the post parameters
        username = request.POST['username']
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']

        request.session['username']=username
        # Check for errorneous inputs
        # username should be under 10 characters
        if len(username)>50:
            messages.error(request, "Username must be under 50 characters")
            return redirect('home')

        # username should be alphanumeric
        # if not username.isalnum():
        #     messages.error(request, "Username should only contain letters and numbers")
        #     return redirect('home')

        # password and confirm password must be same
        if pass1 != pass2:
            messages.error(request,"Passwords do not match")
            return redirect('home')

        # Create the user using inbuild django functionalities
        myuser = User.objects.create_user(username,email,pass1)
        myuser.first_name = fname
        myuser.last_name = lname
        myuser.save()
        messages.success(request, "Your feedback account has been created successfully")
        return redirect('home')
    else:
        return HttpResponse('404 - Not Found')

def handleLogin(request):
    if request.method == "POST":
        loginusername = request.POST['loginusername']
        loginpassword = request.POST['loginpassword']
        user = authenticate(username=loginusername,password=loginpassword)
        print(user)
        if user is not None:
            request.session['username']=loginusername
            login(request,user)
            messages.success(request,"Successfully Logged In")
            return redirect('home')
        else:
            messages.error(request,"Invalid Credentials, Please try again")
            return redirect('home')

    else:
        return HttpResponse('404 - Not Found')
    
def handleLogout(request):
        if request.session['username']:
            del request.session['username']
        logout(request)
        messages.success(request, "Successfully Logged Out")
        return redirect("home")

def home(request):
    return render(request,'index.html')

def report(request):
    from wsgiref.util import FileWrapper
    from django.conf import settings
    import mimetypes

    admin_user = str(request.user)
    if  admin_user == 'admin@gmail.com':
        
        if request.method == "POST":
                        myclass = str(request.POST.get('classselect'))
                        sem = str(request.POST.get('semselect'))
                        feedbacktype = str(request.POST.get('feedbacktype'))
                        plots = str(request.POST.get('plots'))
                        reporttype = str(request.POST.get('reporttype'))
                        
                        # code for reding and labelling particular csv file data
                        if myclass == 'se' and sem=='even':
                            xsl=f'static/computer_semiv_{feedbacktype}_summary.csv'
                            if feedbacktype == 'theory':
                                label = ['EM-IV','AOA','DBMS','OS','MP']
                            else:
                                label = ['AOA Lab','DBMS Lab','OS Lab','MP Lab','Python Programming Lab']

                        elif myclass=='se' and sem=='odd':
                            xsl=f'static/computer_semiii_{feedbacktype}_summary.csv'
                            if feedbacktype == 'theory':
                                label = ['EM-III','DSGT','DSA','DLCA','CG']
                            else:
                                label = ['EM-III Tutorials','DSA Lab','DLCA','CG Lab','OOPJ Lab']

                        elif myclass == 'te' and sem=='even':
                            xsl=f'static/computer_semvi_{feedbacktype}_summary.csv'
                            if feedbacktype == 'theory':
                                label = ['SPCC','CSS','MC','AI','IOT']
                            else:
                                label = ['SPCC Lab','CSS Lab','MC Lab','AI Lab','CCL Lab']

                        elif myclass=='te' and sem=='odd':
                            xsl=f'static/computer_semv_{feedbacktype}_summary.csv'
                            if feedbacktype == 'theory':
                                label = ['TCS','SE','CN','DWM','IP']
                            else:
                                label = ['SE Lab','CN Lab','DWM Lab','BCE - II']

                        elif myclass == 'be' and sem=='even':
                            xsl=f'static/computer_semviii_{feedbacktype}_summary.csv'
                            if feedbacktype == 'theory':
                                label = ['DNL','VMN','SDL','MAK','SST']
                            else:
                                label = ['DNL Lab','CSS Lab','SDL lab','MAK Lab','ST Lab']

                        elif myclass=='be' and sem=='odd':
                            xsl=f'static/computer_semvii_{feedbacktype}_summary.csv' 
                            if feedbacktype == 'theory':
                                label = ['ML ','Big Data Analysis','NLP','Information Retrieval','CSL']
                            else:
                                label = ['ML Lab','Big Data Analysis Lab','NLP Lab','Information Retrieval Lab']
                            
                        computer_semvi_theory_summary = pd.read_csv(xsl)

                        subject_1_rating = int(eval(computer_semvi_theory_summary.iloc[8][-1]))
                        subject_2_rating = int(eval(computer_semvi_theory_summary.iloc[17][-1]))
                        subject_3_rating = int(eval(computer_semvi_theory_summary.iloc[26][-1]))
                        subject_4_rating = int(eval(computer_semvi_theory_summary.iloc[35][-1]))
                        subject_5_rating = int(eval(computer_semvi_theory_summary.iloc[44][-1]))

                        # The required list named as rating_list
                        rating_list = subject_1_rating, subject_2_rating, subject_3_rating, subject_4_rating, subject_5_rating

                        if myclass == 'be' and sem=='odd' and feedbacktype=='practical':
                            rating_list = list(rating_list)
                            rating_list.pop()
                            print(rating_list[0], rating_list[1], rating_list[2], rating_list[3])
                        if myclass == 'te' and sem=='odd' and feedbacktype=='practical':
                            rating_list = list(rating_list)
                            rating_list.pop()
                            print(rating_list[0], rating_list[1], rating_list[2], rating_list[3])
                        # print(rating_list[0], rating_list[1], rating_list[2], rating_list[3], rating_list[4])
                                
                        values = rating_list
                        if reporttype == 'download':
                            filename     = xsl # Select your file here.
                            download_name =filename
                            wrapper      = FileWrapper(open(filename))
                            content_type = mimetypes.guess_type(filename)[0]
                            response     = HttpResponse(wrapper,content_type=content_type)
                            # response['Content-Length']      = os.path.getsize(filename)    
                            response['Content-Disposition'] = "attachment; filename=%s"%download_name
                            return response

                        context = {
                            'plots': plots,
                            'label': label,
                            'values': values,
                            'rating_type': 'Overall Rating',
                        }
                        return render(request,'report.html',context)
        return render(request,'report.html')
    else:
        messages.error(request,'Admin Login is required !')
        return redirect('home')


def contact(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        content = request.POST['content']

        if len(name)<2 or len(email)<3 or len(phone)<10 or len(content)<4:
                messages.error(request,'Please fill the form correctly')
        else:
            contact = Contact(name=name,email= email,phone=phone,content=content)
            contact.save()
            messages.success(request,'Form Submitted Successfully !')

    return render(request,'contact.html')

def about(request):
    return render(request,'about.html')

data = {}
userlist = []
def feedback(request):
    # getting all form data
    Myformdata = dict(request.POST)
    Myformdata.pop('csrfmiddlewaretoken')
    print(Myformdata)
    email = request.session['username']

    # accessing academic model data which is latest one
    filteredData  = AcademicForm.objects.filter(email=email).order_by('-id').values()[0]
    print(filteredData['email'],filteredData['sem'],filteredData['myclass'],filteredData['branch'])

    if not request.user.is_authenticated:
        messages.error(request,"Please login")
        return redirect('home')
    # print(userlist)
    for i in userlist:
        if(i == request.user):
            messages.error(request, 'You have already responded !')
            return render(request,'index.html')
    
    if request.method == "POST":         
                feedback = Feedback(email=filteredData['email'],myclass=filteredData['myclass'],sem=filteredData['sem'],branch=filteredData['branch'],q1=Myformdata['q1'],q2=Myformdata['q2'],q3=Myformdata['q3'],q4=Myformdata['q4'],q5=Myformdata['q5'],q6=Myformdata['q6'],q7=Myformdata['q7'],suggestion=Myformdata['suggestion'],date=datetime.today())
                feedback.save()
                messages.success(request, 'Your response has been submitted successfully !')
                inputList.append(request.user)
                return render(request,'index.html')
    return render(request,'feedback.html')

def parentsfeedback(request):
    if request.method == 'GET':
        return render(request, 'ParentsFeedback.html')
    elif request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        comments = request.POST.get('comments')
        parent_feedback = ParentsFeedback(name=name, email=email, comments=comments)
        parent_feedback.save()
        messages.success(request,'Form Submitted Successfully !')
        return redirect('home')
    else:
        messages.success(request,'Some error occured , please try again later!')
        return redirect('home')

def alumnifeedback(request):
    if request.method == 'GET':
        return render(request, 'AlumniFeedback.html')
    elif request.method == 'POST':

        name = request.POST.get('name')
        passout_year = request.POST.get('passout_year')
        department = request.POST.get('department')
        email = request.POST.get('email')
        comments = request.POST.get('comments')

        alumni_feedback = AlumniFeedback(name=name, passout_year=passout_year, department=department, email=email, comments=comments)
        alumni_feedback.save()

        messages.success(request,'Form Submitted Successfully !')
        return redirect('home')
    else:
        messages.success(request,'Some error occured , please try again later!')
        return redirect('home')

def form_select(request):
     return render(request, 'form_select.html')

inputList = []
def form(request):
        arr = AcademicForm.objects.values_list()
        myclass = ''
        sem = ''
        # print(arr)
        # checking fetched data from database
        for data in arr:
            data = list(data)
            inputList.append(data[1:6])
        # print(inputList,type(inputList))  #all data related to aleready visited users

        if request.method == 'POST':
            email =  request.session['username']
            branch = request.POST.get('branch')
            myclass = request.POST.get('class')
            sem = request.POST.get('sem')
            feedbacktype = request.POST.get('feedbacktype')
            form = AcademicForm(email=email,branch=branch,myclass=myclass,sem=sem,feedbacktype=feedbacktype,date=datetime.today())
            form.save()
            tempList = [email,branch,myclass,sem,feedbacktype]
            # print(tempList)
            if tempList in inputList:
                messages.error(request,'You have already responded...')
                return redirect('form')
            # messages.success(request, 'Your response has been submitted successfully !')
            if feedbacktype == 'theory':
               if myclass == 'te' and sem=='odd':
                return render(request,'CompSem5Theory.html')
               elif myclass == 'te' and sem=='even':
                return render(request,'CompSem6Theory.html')
               elif myclass == 'se' and sem=='odd':
                return render(request,'CompSem3Theory.html')
               elif myclass == 'se' and sem=='even':
                return render(request,'CompSem4Theory.html')
               elif myclass == 'be' and sem=='odd':
                return render(request,'CompSem7Theory.html')
               elif myclass == 'be' and sem=='even':
                return render(request,'CompSem8Theory.html')
            if feedbacktype == 'practical':
               if myclass == 'te' and sem=='odd':
                return render(request,'CompSem5Practical.html')
               elif myclass == 'te' and sem=='even':
                return render(request,'CompSem6Practical.html')
               elif myclass == 'se' and sem=='odd':
                return render(request,'CompSem3Practical.html')
               elif myclass == 'se' and sem=='even':
                return render(request,'CompSem4Practical.html')
               elif myclass == 'be' and sem=='odd':
                return render(request,'CompSem7Practical.html')
               elif myclass == 'be' and sem=='even':
                return render(request,'CompSem8Practical.html')

        if not request.user.is_authenticated:
                messages.error(request,"Please login")
                return redirect('home')
        else:
            return render(request,'form.html',{'email':request.session['username']})
    


# Saving Feedback Responses
def save_responses(request):
        # Theory Responses
        if (request.method == 'POST' and request.POST.get('form_type')=='theory'):
            academic_year = request.POST.get('academic_year')
            semester = request.POST.get('semester')
            branch = request.POST.get('branch')
            year = request.POST.get('year')

            s1_subject_name=request.POST.get('s1_subject_name')
            s1_teacher_name=request.POST.get('s1_teacher_name')

            s2_subject_name=request.POST.get('s2_subject_name')
            s2_teacher_name=request.POST.get('s2_teacher_name')

            s3_subject_name=request.POST.get('s3_subject_name')
            s3_teacher_name=request.POST.get('s3_teacher_name')

            s4_subject_name=request.POST.get('s4_subject_name')
            s4_teacher_name=request.POST.get('s4_teacher_name')

            s5_subject_name=request.POST.get('s5_subject_name')
            s5_teacher_name=request.POST.get('s5_teacher_name')
            
            feedback_data = TheoryFeedback(academic_year=academic_year, semester=semester, branch=branch, year=year, 
            s1_subject_name=s1_subject_name, s1_teacher_name=s1_teacher_name, s1_q1=request.POST.get('s1_q1'), s1_q2=request.POST.get('s1_q2'), s1_q3=request.POST.get('s1_q3'), s1_q4=request.POST.get('s1_q4'), s1_q5=request.POST.get('s1_q5'), s1_q6=request.POST.get('s1_q6'), s1_q7=request.POST.get('s1_q7'), s1_suggestion=request.POST.get('s1_suggestion'),
            s2_subject_name=s2_subject_name, s2_teacher_name=s2_teacher_name, s2_q1=request.POST.get('s2_q1'), s2_q2=request.POST.get('s2_q2'), s2_q3=request.POST.get('s2_q3'), s2_q4=request.POST.get('s2_q4'), s2_q5=request.POST.get('s2_q5'), s2_q6=request.POST.get('s2_q6'), s2_q7=request.POST.get('s2_q7'), s2_suggestion=request.POST.get('s2_suggestion'),
            s3_subject_name=s3_subject_name, s3_teacher_name=s3_teacher_name, s3_q1=request.POST.get('s3_q1'), s3_q2=request.POST.get('s3_q2'), s3_q3=request.POST.get('s3_q3'), s3_q4=request.POST.get('s3_q4'), s3_q5=request.POST.get('s3_q5'), s3_q6=request.POST.get('s3_q6'), s3_q7=request.POST.get('s3_q7'), s3_suggestion=request.POST.get('s3_suggestion'),
            s4_subject_name=s4_subject_name, s4_teacher_name=s4_teacher_name, s4_q1=request.POST.get('s4_q1'), s4_q2=request.POST.get('s4_q2'), s4_q3=request.POST.get('s4_q3'), s4_q4=request.POST.get('s4_q4'), s4_q5=request.POST.get('s4_q5'), s4_q6=request.POST.get('s4_q6'), s4_q7=request.POST.get('s4_q7'), s4_suggestion=request.POST.get('s4_suggestion'),
            s5_subject_name=s5_subject_name, s5_teacher_name=s5_teacher_name, s5_q1=request.POST.get('s5_q1'), s5_q2=request.POST.get('s5_q2'), s5_q3=request.POST.get('s5_q3'), s5_q4=request.POST.get('s5_q4'), s5_q5=request.POST.get('s5_q5'), s5_q6=request.POST.get('s5_q6'), s5_q7=request.POST.get('s5_q7'), s5_suggestion=request.POST.get('s5_suggestion'))

            feedback_data.save()

            column_names = ['id', 'academic_year', 'semester', 'branch', 'year',
                's1_subject_name', 's1_teacher_name', 's1_q1','s1_q2','s1_q3','s1_q4','s1_q5','s1_q6','s1_q7', 's1_suggestion',
                's2_subject_name', 's2_teacher_name', 's2_q1','s2_q2','s2_q3','s2_q4','s2_q5','s2_q6','s2_q7', 's2_suggestion',
                's3_subject_name', 's3_teacher_name', 's3_q1','s3_q2','s3_q3','s3_q4','s3_q5','s3_q6','s3_q7', 's3_suggestion',
                's4_subject_name', 's4_teacher_name', 's4_q1','s4_q2','s4_q3','s4_q4','s4_q5','s4_q6','s4_q7', 's4_suggestion',
                's5_subject_name', 's5_teacher_name', 's5_q1','s5_q2','s5_q3','s5_q4','s5_q5','s5_q6','s5_q7', 's5_suggestion',]
            
            data_object = TheoryFeedback.objects.values_list()
            data_frame = pd.DataFrame(data_object, columns=column_names)
            data_frame.to_csv('static/theory_responses.csv')

            data = pd.read_csv('static/theory_responses.csv', index_col=0)

            question_nos = ['s1_q1','s1_q2','s1_q3','s1_q4','s1_q5','s1_q6','s1_q7',
                's2_q1','s2_q2','s2_q3','s2_q4','s2_q5','s2_q6','s2_q7',
                's3_q1','s3_q2','s3_q3','s3_q4','s3_q5','s3_q6','s3_q7',
                's4_q1','s4_q2','s4_q3','s4_q4','s4_q5','s4_q6','s4_q7',
                's5_q1','s5_q2','s5_q3','s5_q4','s5_q5','s5_q6','s5_q7']
            
            s1 = data.loc[data['s1_subject_name'] == s1_subject_name, question_nos[0:7]].copy(deep=True)
            s2 = data.loc[data['s2_subject_name'] == s2_subject_name, question_nos[7:14]].copy(deep=True)
            s3 = data.loc[data['s3_subject_name'] == s3_subject_name, question_nos[14:21]].copy(deep=True)
            s4 = data.loc[data['s4_subject_name'] == s4_subject_name, question_nos[21:28]].copy(deep=True)
            s5 = data.loc[data['s5_subject_name'] == s5_subject_name, question_nos[28:35]].copy(deep=True)

            rating_s1 = {'s1_q1':[0,0,0,0,0], 's1_q2':[0,0,0,0,0], 's1_q3':[0,0,0,0,0], 's1_q4':[0,0,0,0,0],'s1_q5':[0,0,0,0,0], 's1_q6':[0,0,0,0,0], 's1_q7':[0,0,0,0,0]}
            rating_s2 = {'s2_q1':[0,0,0,0,0], 's2_q2':[0,0,0,0,0], 's2_q3':[0,0,0,0,0], 's2_q4':[0,0,0,0,0],'s2_q5':[0,0,0,0,0], 's2_q6':[0,0,0,0,0], 's2_q7':[0,0,0,0,0]}
            rating_s3 = {'s3_q1':[0,0,0,0,0], 's3_q2':[0,0,0,0,0], 's3_q3':[0,0,0,0,0], 's3_q4':[0,0,0,0,0],'s3_q5':[0,0,0,0,0], 's3_q6':[0,0,0,0,0], 's3_q7':[0,0,0,0,0]}
            rating_s4 = {'s4_q1':[0,0,0,0,0], 's4_q2':[0,0,0,0,0], 's4_q3':[0,0,0,0,0], 's4_q4':[0,0,0,0,0],'s4_q5':[0,0,0,0,0], 's4_q6':[0,0,0,0,0], 's4_q7':[0,0,0,0,0]}
            rating_s5 = {'s5_q1':[0,0,0,0,0], 's5_q2':[0,0,0,0,0], 's5_q3':[0,0,0,0,0], 's5_q4':[0,0,0,0,0],'s5_q5':[0,0,0,0,0], 's5_q6':[0,0,0,0,0], 's5_q7':[0,0,0,0,0]}

            for a in range(len(question_nos)):
                if (a<7):
                    for b in s1[question_nos[a]]:
                        rating_s1[question_nos[a]][b-1] = rating_s1[question_nos[a]][b-1] + 1
                if (6<a and a<14):
                    for b in s2[question_nos[a]]:
                        rating_s2[question_nos[a]][b-1] = rating_s2[question_nos[a]][b-1] + 1
                if (13<a and a<21):
                    for b in s3[question_nos[a]]:
                        rating_s3[question_nos[a]][b-1] = rating_s3[question_nos[a]][b-1] + 1
                if (20<a and a<28):
                    for b in s4[question_nos[a]]:
                        rating_s4[question_nos[a]][b-1] = rating_s4[question_nos[a]][b-1] + 1
                if (27<a and a<35):
                    for b in s5[question_nos[a]]:
                        rating_s5[question_nos[a]][b-1] = rating_s5[question_nos[a]][b-1] + 1
                else:
                    pass

            rating_s1 = pd.DataFrame(rating_s1).T
            rating_s2 = pd.DataFrame(rating_s2).T
            rating_s3 = pd.DataFrame(rating_s3).T
            rating_s4 = pd.DataFrame(rating_s4).T
            rating_s5 = pd.DataFrame(rating_s5).T

            rating_cols_dictionary = {0:'Not Satisfactory', 1:'Satisfactory', 2:'Good', 3:'Very Good', 4:'Excellent'}

            questions_list = ['Whether teaching is relevant to syllabus?', 'Whether doubts are cleared properly?',
                            'Whether Notes are provided properly?',      'Whether voice is clear?',
                            'Whether language is simple?',               'Whether elearning resources are used properly?',
                            'Overall impression of teacher']

            rating_s1.rename(columns = rating_cols_dictionary, index={question_nos[0]:questions_list[0],  question_nos[1]:questions_list[1],  question_nos[2]:questions_list[2],  question_nos[3]:questions_list[3],  question_nos[4]:questions_list[4],  question_nos[5]:questions_list[5],  question_nos[6]:questions_list[6]},  inplace = True)
            rating_s2.rename(columns = rating_cols_dictionary, index={question_nos[7]:questions_list[0],  question_nos[8]:questions_list[1],  question_nos[9]:questions_list[2],  question_nos[10]:questions_list[3], question_nos[11]:questions_list[4], question_nos[12]:questions_list[5], question_nos[13]:questions_list[6]}, inplace = True)
            rating_s3.rename(columns = rating_cols_dictionary, index={question_nos[14]:questions_list[0], question_nos[15]:questions_list[1], question_nos[16]:questions_list[2], question_nos[17]:questions_list[3], question_nos[18]:questions_list[4], question_nos[19]:questions_list[5], question_nos[20]:questions_list[6]}, inplace = True)
            rating_s4.rename(columns = rating_cols_dictionary, index={question_nos[21]:questions_list[0], question_nos[22]:questions_list[1], question_nos[23]:questions_list[2], question_nos[24]:questions_list[3], question_nos[25]:questions_list[4], question_nos[26]:questions_list[5], question_nos[27]:questions_list[6]}, inplace = True)
            rating_s5.rename(columns = rating_cols_dictionary, index={question_nos[28]:questions_list[0], question_nos[29]:questions_list[1], question_nos[30]:questions_list[2], question_nos[31]:questions_list[3], question_nos[32]:questions_list[4], question_nos[33]:questions_list[5], question_nos[34]:questions_list[6]}, inplace = True)
            
            no_of_responses = rating_s1['Not Satisfactory'] + rating_s1['Satisfactory'] + rating_s1['Good'] + rating_s1['Very Good'] + rating_s1['Excellent']

            rating_s1['Total Marks'] = rating_s1['Not Satisfactory']*1 + rating_s1['Satisfactory']*2 + rating_s1['Good']*3 + rating_s1['Very Good']*4 + rating_s1['Excellent']*5
            rating_s1['Out of'] = no_of_responses*5
            rating_s1.loc['Total'] = rating_s1.sum()
            rating_s1['Percentage'] = rating_s1['Total Marks']*100/rating_s1['Out of']

            rating_s2['Total Marks'] = rating_s2['Not Satisfactory']*1 + rating_s2['Satisfactory']*2 + rating_s2['Good']*3 + rating_s2['Very Good']*4 + rating_s2['Excellent']*5
            rating_s2['Out of'] = no_of_responses*5
            rating_s2.loc['Total'] = rating_s2.sum()
            rating_s2['Percentage'] = rating_s2['Total Marks']*100/rating_s2['Out of']

            rating_s3['Total Marks'] = rating_s3['Not Satisfactory']*1 + rating_s3['Satisfactory']*2 + rating_s3['Good']*3 + rating_s3['Very Good']*4 + rating_s3['Excellent']*5
            rating_s3['Out of'] = no_of_responses*5
            rating_s3.loc['Total'] = rating_s3.sum()
            rating_s3['Percentage'] = rating_s3['Total Marks']*100/rating_s3['Out of']

            rating_s4['Total Marks'] = rating_s4['Not Satisfactory']*1 + rating_s4['Satisfactory']*2 + rating_s4['Good']*3 + rating_s4['Very Good']*4 + rating_s4['Excellent']*5
            rating_s4['Out of'] = no_of_responses*5
            rating_s4.loc['Total'] = rating_s4.sum()
            rating_s4['Percentage'] = rating_s4['Total Marks']*100/rating_s4['Out of']

            rating_s5['Total Marks'] = rating_s5['Not Satisfactory']*1 + rating_s5['Satisfactory']*2 + rating_s5['Good']*3 + rating_s5['Very Good']*4 + rating_s5['Excellent']*5
            rating_s5['Out of'] = no_of_responses*5
            rating_s5.loc['Total'] = rating_s5.sum()
            rating_s5['Percentage'] = rating_s5['Total Marks']*100/rating_s5['Out of']

            theory_ratings_list = [rating_s1, rating_s2, rating_s3, rating_s4, rating_s5]

            theory_summary = pd.DataFrame()
            theory_summary.to_csv(str('static/'+branch+'_sem'+semester+'_'+'theory_summary.csv'))
            print(str('static/'+branch+'_sem'+semester+'_'+'theory_summary.csv'), "\n\n")
            
            subject_name_list = [s1_subject_name, s2_subject_name, s3_subject_name, s4_subject_name, s5_subject_name]
            subject_teacher_list = [s1_teacher_name, s2_teacher_name, s3_teacher_name, s4_teacher_name, s5_teacher_name]

            with open(str('static/'+branch+'_sem'+semester+'_'+'theory_summary.csv'), 'a') as f:
                for i in range(len(theory_ratings_list)):
                    f.write(str(subject_name_list[i] + " " + subject_teacher_list[i] + " " + academic_year))
                    theory_ratings_list[i].to_csv(f)
                    f.write("\n\n")
            f.close()
            print(theory_ratings_list)

            return redirect('home')
        
        # Practical and Project Responses
        if (request.method == 'POST' and request.POST.get('form_type')=='practical'):
            academic_year = request.POST.get('academic_year')
            semester = request.POST.get('semester')
            branch = request.POST.get('branch')
            year = request.POST.get('year')

            p1_subject_name=request.POST.get('p1_subject_name')
            p1_teacher_name=request.POST.get('p1_teacher_name')

            p2_subject_name=request.POST.get('p2_subject_name')
            p2_teacher_name=request.POST.get('p2_teacher_name')

            p3_subject_name=request.POST.get('p3_subject_name')
            p3_teacher_name=request.POST.get('p3_teacher_name')

            p4_subject_name=request.POST.get('p4_subject_name')
            p4_teacher_name=request.POST.get('p4_teacher_name')

            p5_subject_name=request.POST.get('p5_subject_name')
            p5_teacher_name=request.POST.get('p5_teacher_name')

            project_name=request.POST.get('project_name')
            project_teacher_name=request.POST.get('project_teacher_name')
            
            feedback_data = PracticalFeedback(academic_year=academic_year, semester=semester, branch=branch, year=year, 
            p1_subject_name=p1_subject_name, p1_teacher_name=p1_teacher_name, p1_q1=request.POST.get('p1_q1'), p1_q2=request.POST.get('p1_q2'), p1_q3=request.POST.get('p1_q3'), p1_q4=request.POST.get('p1_q4'), p1_q5=request.POST.get('p1_q5'), p1_q6=request.POST.get('p1_q6'), p1_q7=request.POST.get('p1_q7'), p1_suggestion=request.POST.get('p1_suggestion'),
            p2_subject_name=p2_subject_name, p2_teacher_name=p2_teacher_name, p2_q1=request.POST.get('p2_q1'), p2_q2=request.POST.get('p2_q2'), p2_q3=request.POST.get('p2_q3'), p2_q4=request.POST.get('p2_q4'), p2_q5=request.POST.get('p2_q5'), p2_q6=request.POST.get('p2_q6'), p2_q7=request.POST.get('p2_q7'), p2_suggestion=request.POST.get('p2_suggestion'),
            p3_subject_name=p3_subject_name, p3_teacher_name=p3_teacher_name, p3_q1=request.POST.get('p3_q1'), p3_q2=request.POST.get('p3_q2'), p3_q3=request.POST.get('p3_q3'), p3_q4=request.POST.get('p3_q4'), p3_q5=request.POST.get('p3_q5'), p3_q6=request.POST.get('p3_q6'), p3_q7=request.POST.get('p3_q7'), p3_suggestion=request.POST.get('p3_suggestion'),
            p4_subject_name=p4_subject_name, p4_teacher_name=p4_teacher_name, p4_q1=request.POST.get('p4_q1'), p4_q2=request.POST.get('p4_q2'), p4_q3=request.POST.get('p4_q3'), p4_q4=request.POST.get('p4_q4'), p4_q5=request.POST.get('p4_q5'), p4_q6=request.POST.get('p4_q6'), p4_q7=request.POST.get('p4_q7'), p4_suggestion=request.POST.get('p4_suggestion'),
            p5_subject_name=p5_subject_name, p5_teacher_name=p5_teacher_name, p5_q1=request.POST.get('p5_q1'), p5_q2=request.POST.get('p5_q2'), p5_q3=request.POST.get('p5_q3'), p5_q4=request.POST.get('p5_q4'), p5_q5=request.POST.get('p5_q5'), p5_q6=request.POST.get('p5_q6'), p5_q7=request.POST.get('p5_q7'), p5_suggestion=request.POST.get('p5_suggestion'),
            project_name=project_name, project_teacher_name=project_teacher_name, project_q1=request.POST.get('project_q1'), project_q2=request.POST.get('project_q2'), project_q3=request.POST.get('project_q3'), project_q4=request.POST.get('project_q4'), project_q5=request.POST.get('project_q5'), project_q6=request.POST.get('project_q6'), project_q7=request.POST.get('project_q7'), project_suggestion=request.POST.get('project_suggestion'))

            feedback_data.save()

            column_names = ['id', 'academic_year', 'semester', 'branch', 'year',
                'p1_subject_name', 'p1_teacher_name', 'p1_q1','p1_q2','p1_q3','p1_q4','p1_q5','p1_q6','p1_q7', 'p1_suggestion',
                'p2_subject_name', 'p2_teacher_name', 'p2_q1','p2_q2','p2_q3','p2_q4','p2_q5','p2_q6','p2_q7', 'p2_suggestion',
                'p3_subject_name', 'p3_teacher_name', 'p3_q1','p3_q2','p3_q3','p3_q4','p3_q5','p3_q6','p3_q7', 'p3_suggestion',
                'p4_subject_name', 'p4_teacher_name', 'p4_q1','p4_q2','p4_q3','p4_q4','p4_q5','p4_q6','p4_q7', 'p4_suggestion',
                'p5_subject_name', 'p5_teacher_name', 'p5_q1','p5_q2','p5_q3','p5_q4','p5_q5','p5_q6','p5_q7', 'p5_suggestion',
                'project_name', 'project_teacher_name','project_q1','project_q2','project_q3','project_q4','project_q5','project_q6','project_q7','project_suggestion']
            
            data_object = PracticalFeedback.objects.values_list()
            data_frame = pd.DataFrame(data_object, columns=column_names)
            data_frame.to_csv('static/practical_responses.csv')

            data = pd.read_csv('static/practical_responses.csv', index_col=0)

            question_nos = ['p1_q1','p1_q2','p1_q3','p1_q4','p1_q5','p1_q6','p1_q7',
                'p2_q1','p2_q2','p2_q3','p2_q4','p2_q5','p2_q6','p2_q7',
                'p3_q1','p3_q2','p3_q3','p3_q4','p3_q5','p3_q6','p3_q7',
                'p4_q1','p4_q2','p4_q3','p4_q4','p4_q5','p4_q6','p4_q7',
                'p5_q1','p5_q2','p5_q3','p5_q4','p5_q5','p5_q6','p5_q7',
                'project_q1','project_q2','project_q3','project_q4','project_q5','project_q6','project_q7']
            
            p1 = data.loc[data['p1_subject_name']==p1_subject_name, question_nos[0:7]].copy(deep=True)
            p2 = data.loc[data['p2_subject_name']==p2_subject_name, question_nos[7:14]].copy(deep=True)
            p3 = data.loc[data['p3_subject_name']==p3_subject_name, question_nos[14:21]].copy(deep=True)
            p4 = data.loc[data['p4_subject_name']==p4_subject_name, question_nos[21:28]].copy(deep=True)
            p5 = data.loc[data['p5_subject_name']==p5_subject_name, question_nos[28:35]].copy(deep=True)
            project = data.loc[data['project_name']==project_name, question_nos[35:42]].copy(deep=True)

            # p1 = data[question_nos[0:7]].copy(deep=True)
            # p2 = data[question_nos[7:14]].copy(deep=True)
            # p3 = data[question_nos[14:21]].copy(deep=True)
            # p4 = data[question_nos[21:28]].copy(deep=True)
            # p5 = data[question_nos[28:35]].copy(deep=True)
            # project = data[question_nos[35:42]].copy(deep=True)

            rating_p1 = {'p1_q1':[0,0,0,0,0], 'p1_q2':[0,0,0,0,0], 'p1_q3':[0,0,0,0,0], 'p1_q4':[0,0,0,0,0],'p1_q5':[0,0,0,0,0], 'p1_q6':[0,0,0,0,0], 'p1_q7':[0,0,0,0,0]}
            rating_p2 = {'p2_q1':[0,0,0,0,0], 'p2_q2':[0,0,0,0,0], 'p2_q3':[0,0,0,0,0], 'p2_q4':[0,0,0,0,0],'p2_q5':[0,0,0,0,0], 'p2_q6':[0,0,0,0,0], 'p2_q7':[0,0,0,0,0]}
            rating_p3 = {'p3_q1':[0,0,0,0,0], 'p3_q2':[0,0,0,0,0], 'p3_q3':[0,0,0,0,0], 'p3_q4':[0,0,0,0,0],'p3_q5':[0,0,0,0,0], 'p3_q6':[0,0,0,0,0], 'p3_q7':[0,0,0,0,0]}
            rating_p4 = {'p4_q1':[0,0,0,0,0], 'p4_q2':[0,0,0,0,0], 'p4_q3':[0,0,0,0,0], 'p4_q4':[0,0,0,0,0],'p4_q5':[0,0,0,0,0], 'p4_q6':[0,0,0,0,0], 'p4_q7':[0,0,0,0,0]}
            rating_p5 = {'p5_q1':[0,0,0,0,0], 'p5_q2':[0,0,0,0,0], 'p5_q3':[0,0,0,0,0], 'p5_q4':[0,0,0,0,0],'p5_q5':[0,0,0,0,0], 'p5_q6':[0,0,0,0,0], 'p5_q7':[0,0,0,0,0]}
            rating_project = {'project_q1':[0,0,0,0,0], 'project_q2':[0,0,0,0,0], 'project_q3':[0,0,0,0,0], 'project_q4':[0,0,0,0,0],'project_q5':[0,0,0,0,0], 'project_q6':[0,0,0,0,0], 'project_q7':[0,0,0,0,0]}

            for a in range(len(question_nos)):
                if (a<7):
                    for b in p1[question_nos[a]]:
                        rating_p1[question_nos[a]][b-1] = rating_p1[question_nos[a]][b-1] + 1
                if (6<a and a<14):
                    for b in p2[question_nos[a]]:
                        rating_p2[question_nos[a]][b-1] = rating_p2[question_nos[a]][b-1] + 1
                if (13<a and a<21):
                    for b in p3[question_nos[a]]:
                        rating_p3[question_nos[a]][b-1] = rating_p3[question_nos[a]][b-1] + 1
                if (20<a and a<28):
                    for b in p4[question_nos[a]]:
                        rating_p4[question_nos[a]][b-1] = rating_p4[question_nos[a]][b-1] + 1
                if (27<a and a<35):
                    for b in p5[question_nos[a]]:
                        rating_p5[question_nos[a]][b-1] = rating_p5[question_nos[a]][b-1] + 1
                if (34<a and a<42):
                    for b in project[question_nos[a]]:
                        rating_project[question_nos[a]][b-1] = rating_project[question_nos[a]][b-1] + 1
                else:
                    pass

            rating_p1 = pd.DataFrame(rating_p1).T
            rating_p2 = pd.DataFrame(rating_p2).T
            rating_p3 = pd.DataFrame(rating_p3).T
            rating_p4 = pd.DataFrame(rating_p4).T
            rating_p5 = pd.DataFrame(rating_p5).T
            rating_project = pd.DataFrame(rating_project).T

            rating_cols_dictionary = {0:'Not Satisfactory', 1:'Satisfactory', 2:'Good', 3:'Very Good', 4:'Excellent'}

            questions_list = ['Whether teaching is relevant to syllabus?', 'Whether doubts are cleared properly?',
                            'Whether Notes are provided properly?',      'Whether voice is clear?',
                            'Whether language is simple?',               'Whether elearning resources are used properly?',
                            'Overall impression of teacher']

            rating_p1.rename(columns = rating_cols_dictionary,      index={question_nos[0]:questions_list[0],  question_nos[1]:questions_list[1],  question_nos[2]:questions_list[2],  question_nos[3]:questions_list[3],  question_nos[4]:questions_list[4],  question_nos[5]:questions_list[5],  question_nos[6]:questions_list[6]},  inplace = True)
            rating_p2.rename(columns = rating_cols_dictionary,      index={question_nos[7]:questions_list[0],  question_nos[8]:questions_list[1],  question_nos[9]:questions_list[2],  question_nos[10]:questions_list[3], question_nos[11]:questions_list[4], question_nos[12]:questions_list[5], question_nos[13]:questions_list[6]}, inplace = True)
            rating_p3.rename(columns = rating_cols_dictionary,      index={question_nos[14]:questions_list[0], question_nos[15]:questions_list[1], question_nos[16]:questions_list[2], question_nos[17]:questions_list[3], question_nos[18]:questions_list[4], question_nos[19]:questions_list[5], question_nos[20]:questions_list[6]}, inplace = True)
            rating_p4.rename(columns = rating_cols_dictionary,      index={question_nos[21]:questions_list[0], question_nos[22]:questions_list[1], question_nos[23]:questions_list[2], question_nos[24]:questions_list[3], question_nos[25]:questions_list[4], question_nos[26]:questions_list[5], question_nos[27]:questions_list[6]}, inplace = True)
            rating_p5.rename(columns = rating_cols_dictionary,      index={question_nos[28]:questions_list[0], question_nos[29]:questions_list[1], question_nos[30]:questions_list[2], question_nos[31]:questions_list[3], question_nos[32]:questions_list[4], question_nos[33]:questions_list[5], question_nos[34]:questions_list[6]}, inplace = True)
            rating_project.rename(columns = rating_cols_dictionary, index={question_nos[35]:questions_list[0], question_nos[36]:questions_list[1], question_nos[37]:questions_list[2], question_nos[38]:questions_list[3], question_nos[39]:questions_list[4], question_nos[40]:questions_list[5], question_nos[41]:questions_list[6]}, inplace = True)
            
            no_of_responses = rating_p1['Not Satisfactory'] + rating_p1['Satisfactory'] + rating_p1['Good'] + rating_p1['Very Good'] + rating_p1['Excellent']

            rating_p1['Total Marks'] = rating_p1['Not Satisfactory']*1 + rating_p1['Satisfactory']*2 + rating_p1['Good']*3 + rating_p1['Very Good']*4 + rating_p1['Excellent']*5
            rating_p1['Out of'] = no_of_responses*5
            rating_p1.loc['Total'] = rating_p1.sum()
            rating_p1['Percentage'] = rating_p1['Total Marks']*100/rating_p1['Out of']

            rating_p2['Total Marks'] = rating_p2['Not Satisfactory']*1 + rating_p2['Satisfactory']*2 + rating_p2['Good']*3 + rating_p2['Very Good']*4 + rating_p2['Excellent']*5
            rating_p2['Out of'] = no_of_responses*5
            rating_p2.loc['Total'] = rating_p2.sum()
            rating_p2['Percentage'] = rating_p2['Total Marks']*100/rating_p2['Out of']

            rating_p3['Total Marks'] = rating_p3['Not Satisfactory']*1 + rating_p3['Satisfactory']*2 + rating_p3['Good']*3 + rating_p3['Very Good']*4 + rating_p3['Excellent']*5
            rating_p3['Out of'] = no_of_responses*5
            rating_p3.loc['Total'] = rating_p3.sum()
            rating_p3['Percentage'] = rating_p3['Total Marks']*100/rating_p3['Out of']

            rating_p4['Total Marks'] = rating_p4['Not Satisfactory']*1 + rating_p4['Satisfactory']*2 + rating_p4['Good']*3 + rating_p4['Very Good']*4 + rating_p4['Excellent']*5
            rating_p4['Out of'] = no_of_responses*5
            rating_p4.loc['Total'] = rating_p4.sum()
            rating_p4['Percentage'] = rating_p4['Total Marks']*100/rating_p4['Out of']

            rating_p5['Total Marks'] = rating_p5['Not Satisfactory']*1 + rating_p5['Satisfactory']*2 + rating_p5['Good']*3 + rating_p5['Very Good']*4 + rating_p5['Excellent']*5
            rating_p5['Out of'] = no_of_responses*5
            rating_p5.loc['Total'] = rating_p5.sum()
            rating_p5['Percentage'] = rating_p5['Total Marks']*100/rating_p5['Out of']

            rating_project['Total Marks'] = rating_project['Not Satisfactory']*1 + rating_project['Satisfactory']*2 + rating_project['Good']*3 + rating_project['Very Good']*4 + rating_project['Excellent']*5
            rating_project['Out of'] = no_of_responses*5
            rating_project.loc['Total'] = rating_project.sum()
            rating_project['Percentage'] = rating_project['Total Marks']*100/rating_project['Out of']

            practical_ratings_list = [rating_p1, rating_p2, rating_p3, rating_p4, rating_p5]

            practical_summary = pd.DataFrame()
            practical_summary.to_csv(str('static/'+branch+'_sem'+semester+'_'+'practical_summary.csv'))

            practical_name_list = [p1_subject_name, p2_subject_name, p3_subject_name, p4_subject_name, p5_subject_name, project_name]
            practical_teacher_list = [p1_teacher_name, p2_teacher_name, p3_teacher_name, p4_teacher_name, p5_teacher_name, project_teacher_name]

            with open(str('static/'+branch+'_sem'+semester+'_'+'practical_summary.csv'), 'a') as f:
                for i in range(len(practical_ratings_list)):
                    f.write(str("\n\n"+ practical_name_list[i] + " " + practical_teacher_list[i] + " " + academic_year + " " + year + " " + branch + " " + semester))
                    practical_ratings_list[i].to_csv(f)
                    f.write("\n\n")
            
            return redirect('home')
        
def practical(request):
    # getting all form data
    Myformdata = dict(request.POST)
    Myformdata.pop('csrfmiddlewaretoken')
    print(Myformdata)
    email = request.session['username']

    # accessing academic model data which is latest one
    filteredData  = AcademicForm.objects.filter(email=email).order_by('-id').values()[0]
    print(filteredData['email'],filteredData['sem'],filteredData['myclass'],filteredData['branch'])

    if not request.user.is_authenticated:
        messages.error(request,"Please login")
        return redirect('home')
    # print(userlist)
    for i in userlist:
        if(i == request.user):
            messages.error(request, 'You have already responded !')
            return render(request,'index.html')
    
    if request.method == "POST":         
                practical = Practical(email=filteredData['email'],myclass=filteredData['myclass'],sem=filteredData['sem'],branch=filteredData['branch'],q1=Myformdata['q1'],q2=Myformdata['q2'],q3=Myformdata['q3'],q4=Myformdata['q4'],q5=Myformdata['q5'],q6=Myformdata['q6'],q7=Myformdata['q7'],suggestion=Myformdata['suggestion'],date=datetime.today())
                practical.save()
                messages.success(request, 'Your response has been submitted successfully !')
                inputList.append(request.user)
                return render(request,'index.html')
    return render(request,'feedback.html')

