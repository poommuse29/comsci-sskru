from django.shortcuts import render
from .models import Banner, News, Course, Faculty

def index(request):
    banners = Banner.objects.filter(is_active=True).order_by('order', '-created_at')
    news_list = News.objects.all().order_by('-is_featured', '-created_at')[:6]
    courses = Course.objects.all().order_by('order', 'id')
    faculty_list = Faculty.objects.all().order_by('order', 'id')

    context = {
        'banners': banners,
        'news_list': news_list,
        'courses': courses,
        'faculty_list': faculty_list,
    }
    return render(request, 'core/index.html', context)
