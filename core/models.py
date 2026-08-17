from django.db import models

class Banner(models.Model):
    title = models.CharField(max_length=200, verbose_name="หัวข้อแบนเนอร์")
    subtitle = models.CharField(max_length=300, blank=True, null=True, verbose_name="ข้อความย่อย")
    image = models.ImageField(upload_to="banners/", verbose_name="รูปภาพแบนเนอร์")
    button_text = models.CharField(max_length=100, blank=True, null=True, verbose_name="ข้อความบนปุ่ม")
    button_url = models.CharField(max_length=200, blank=True, null=True, verbose_name="ลิงก์ปุ่ม")
    order = models.IntegerField(default=0, verbose_name="ลำดับการแสดงผล")
    is_active = models.BooleanField(default=True, verbose_name="เปิดใช้งาน")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="วันที่สร้าง")

    class Meta:
        verbose_name = "สไลด์หน้าแรก (Banner)"
        verbose_name_plural = "สไลด์หน้าแรก (Banners)"
        ordering = ['order', '-created_at']

    def __str__(self):
        return self.title


class News(models.Model):
    CATEGORY_CHOICES = [
        ('ข่าวประชาสัมพันธ์', 'ข่าวประชาสัมพันธ์'),
        ('กิจกรรมสาขา', 'กิจกรรมสาขา'),
        ('ผลงานนักศึกษา', 'ผลงานนักศึกษา'),
        ('อบรมและสัมมนา', 'อบรมและสัมมนา'),
    ]

    title = models.CharField(max_length=200, verbose_name="หัวข้อข่าวสาร")
    category = models.CharField(max_length=100, choices=CATEGORY_CHOICES, default='ข่าวประชาสัมพันธ์', verbose_name="หมวดหมู่")
    content = models.TextField(verbose_name="เนื้อหาข่าวสาร")
    image = models.ImageField(upload_to="news/", blank=True, null=True, verbose_name="รูปภาพประกอบ")
    is_featured = models.BooleanField(default=False, verbose_name="ข่าวเด่น/ปักหมุด")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="วันที่ประกาศ")

    class Meta:
        verbose_name = "ข่าวสารและกิจกรรม"
        verbose_name_plural = "ข่าวสารและกิจกรรม"
        ordering = ['-is_featured', '-created_at']

    def __str__(self):
        return f"[{self.category}] {self.title}"


class Course(models.Model):
    LEVEL_CHOICES = [
        ('ปริญญาตรี', 'ปริญญาตรี'),
        ('ปริญญาโท', 'ปริญญาโท'),
        ('ปริญญาเอก', 'ปริญญาเอก'),
        ('หลักสูตรระยะสั้น', 'หลักสูตรระยะสั้น'),
    ]

    name = models.CharField(max_length=200, verbose_name="ชื่อหลักสูตร")
    level = models.CharField(max_length=100, choices=LEVEL_CHOICES, default='ปริญญาตรี', verbose_name="ระดับการศึกษา")
    degree_title = models.CharField(max_length=200, blank=True, null=True, verbose_name="ชื่อปริญญา (ย่อ/เต็ม)")
    description = models.TextField(verbose_name="รายละเอียดหลักสูตร")
    career_opportunities = models.TextField(verbose_name="โอกาสในการประกอบอาชีพ")
    duration = models.CharField(max_length=100, default="4 ปี", verbose_name="ระยะเวลาศึกษา")
    credits = models.CharField(max_length=100, default="120+ หน่วยกิต", verbose_name="จำนวนหน่วยกิต")
    icon = models.CharField(max_length=50, default="fa-laptop-code", verbose_name="ไอคอน FontAwesome (เช่น fa-laptop-code)")
    image = models.ImageField(upload_to="courses/", blank=True, null=True, verbose_name="รูปภาพหลักสูตร")
    order = models.IntegerField(default=0, verbose_name="ลำดับการแสดงผล")

    class Meta:
        verbose_name = "หลักสูตรการศึกษา"
        verbose_name_plural = "หลักสูตรการศึกษา"
        ordering = ['order', 'id']

    def __str__(self):
        return f"{self.name} ({self.level})"


class Faculty(models.Model):
    name = models.CharField(max_length=200, verbose_name="ชื่อ-นามสกุล")
    academic_rank = models.CharField(max_length=100, verbose_name="ตำแหน่งทางวิชาการ (เช่น ผศ.ดร., ดร., อ.)")
    position = models.CharField(max_length=200, verbose_name="ตำแหน่งงาน/หน้าที่รับผิดชอบ")
    education = models.CharField(max_length=300, blank=True, null=True, verbose_name="วุฒิการศึกษา")
    expertise = models.CharField(max_length=200, blank=True, null=True, verbose_name="ความเชี่ยวชาญ (เช่น วิทยาการคอมพิวเตอร์)")
    email = models.EmailField(blank=True, null=True, verbose_name="อีเมล")
    phone = models.CharField(max_length=50, blank=True, null=True, verbose_name="เบอร์โทรศัพท์")
    image = models.ImageField(upload_to="faculty/", blank=True, null=True, verbose_name="รูปถ่าย")
    order = models.IntegerField(default=0, verbose_name="ลำดับการแสดงผล")

    class Meta:
        verbose_name = "คณาจารย์และบุคลากร"
        verbose_name_plural = "คณาจารย์และบุคลากร"
        ordering = ['order', 'id']

    def __str__(self):
        return f"{self.academic_rank} {self.name}"
