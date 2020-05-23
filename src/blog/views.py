from django.shortcuts import render

posts=[
    {
        'title':'التدوينة الأولى',
        'content':'نص التدوينة الأولى كنص تجريبي',
        'post_date':'15-3-2020',
        'author':'Jamil Houhou'

    },
    {
        'title':'التدوينة الثانية',
        'content':'نص التدوينة الثانية كنص تجريبي',
        'post_date':'10-5-2020',
        'author':'Samir Khamel'

    },
    {
        'title':'التدوينة الثالثة',
        'content':'نص التدوينة الثالثة كنص تجريبي',
        'post_date':'3-5-2020',
        'author':'Rabih Mounir'

    },
    {
        'title':'التدوينة الرابعة',
        'content':'نص التدوينة الرابعة كنص تجريبي',
        'post_date':'20-4-2020',
        'author':'Jamil Houhou'

    },
]

def home(request):
    context={
        'title':'الصفحة الرئيسية',
        'posts':posts
    }
    return render(request,'blog/index.html',context)

def about(request):
    return render(request,'blog/about.html',{'title':'من أنا'})