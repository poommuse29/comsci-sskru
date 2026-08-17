from django.contrib import admin
from .models import Banner, News, Course, Faculty

@admin.register(Banner)
class BannerAdmin(admin.ModelAdmin):
    list_display = ('title', 'order', 'is_active', 'created_at')
    list_filter = ('is_active',)
    search_fields = ('title', 'subtitle')
    list_editable = ('order', 'is_active')


@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'is_featured', 'created_at')
    list_filter = ('category', 'is_featured', 'created_at')
    search_fields = ('title', 'content')
    list_editable = ('is_featured',)


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('name', 'level', 'degree_title', 'duration', 'order')
    list_filter = ('level',)
    search_fields = ('name', 'description', 'career_opportunities')
    list_editable = ('order',)


@admin.register(Faculty)
class FacultyAdmin(admin.ModelAdmin):
    list_display = ('name', 'academic_rank', 'position', 'email', 'phone', 'order')
    list_filter = ('academic_rank',)
    search_fields = ('name', 'position', 'education', 'email')
    list_editable = ('order',)

# Admin Header Customization
admin.site.site_header = "ระบบจัดการข้อมูล สาขาวิชาวิทยาการคอมพิวเตอร์ (CS@SSKRU)"
admin.site.site_title = "CS@SSKRU Admin"
admin.site.index_title = "ยินดีต้อนรับสู่ระบบจัดการข้อมูลเว็บไซต์ CS@SSKRU"
