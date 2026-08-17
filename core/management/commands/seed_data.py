from django.core.management.base import BaseCommand
from core.models import Banner, News, Course, Faculty

class Command(BaseCommand):
    help = 'Populate database with official seed data for CS@SSKRU'

    def handle(self, *args, **options):
        self.stdout.write(self.style.NOTICE('Starting seed data insertion with official assets...'))

        # 1. Banners
        Banner.objects.all().delete()
        Banner.objects.create(
            title="สาขาวิชาวิทยาการคอมพิวเตอร์ มรภ.ศรีสะเกษ",
            subtitle="\"ก้าวสู่อนาคตทางเทคโนโลยี สร้างสรรค์ซอฟต์แวร์แห่งนวัตกรรม\" หลักสูตรที่มุ่งผลิตนักวิทยาศาสตร์คอมพิวเตอร์ โปรแกรมเมอร์ และนักวิเคราะห์ข้อมูล เพื่อเข้าสู่ตลาดงานยุคดิจิทัลระดับโลก",
            button_text="สมัครเข้าศึกษาต่อ",
            button_url="https://www.oass.sskru.ac.th/std.sskru/s1.html",
            order=1,
            is_active=True
        )
        Banner.objects.create(
            title="เชี่ยวชาญด้านวิทยาการคอมพิวเตอร์ มีคุณธรรม นำนวัตกรรมเพื่อพัฒนาท้องถิ่น",
            subtitle="หลักสูตรปรับปรุง พ.ศ. 2568 เน้นเรียนรู้จากการทำงานจริง โครงงานนวัตกรรม และสหกิจศึกษาร่วมกับบริษัทเทคโนโลยีระดับแถวหน้า",
            button_text="ข้อมูลวิชาหลักสูตร",
            button_url="#courses",
            order=2,
            is_active=True
        )
        Banner.objects.create(
            title="100% โอกาสมีงานทำ พร้อมเครือข่ายศิษย์เก่ากว่า 500+ คน",
            subtitle="รองรับตำแหน่งงานอนาคต: Full-Stack Developer, AI & Data Engineer, Cloud Administrator & DevOps, Cybersecurity Analyst",
            button_text="แผนการเรียน 4 ปี",
            button_url="#schedule",
            order=3,
            is_active=True
        )
        self.stdout.write(self.style.SUCCESS('Successfully seeded 3 Banners.'))

        # 2. Courses
        Course.objects.all().delete()
        Course.objects.create(
            name="วิทยาศาสตรบัณฑิต สาขาวิชาวิทยาการคอมพิวเตอร์",
            level="ปริญญาตรี",
            degree_title="วท.บ. (วิทยาการคอมพิวเตอร์)",
            duration="4 ปี",
            credits="133 หน่วยกิตขั้นต่ำ",
            icon="fa-laptop-code",
            description="มุ่งเน้นการปูพื้นฐานทฤษฎีทางคอมพิวเตอร์ โครงสร้างระบบ การเขียนโปรแกรม ปัญญาประดิษฐ์ และความมั่นคงปลอดภัยไซเบอร์ เน้นการเรียนรู้จากการทำงานจริง โครงงานนวัตกรรม และสหกิจศึกษา",
            career_opportunities="• Software Developer / Full-Stack Web Developer\n• AI & Data Engineer / Data Scientist\n• Mobile Application Developer (iOS/Android)\n• Cloud Administrator & DevOps Engineer\n• Computer Forensics & Cybersecurity Analyst",
            order=1
        )
        Course.objects.create(
            name="วิทยาการคอมพิวเตอร์และเทคโนโลยีปัญญาประดิษฐ์",
            level="ปริญญาโท",
            degree_title="วท.ม. (วิทยาการคอมพิวเตอร์)",
            duration="2 ปี",
            credits="36 หน่วยกิต",
            icon="fa-brain",
            description="เจาะลึกงานวิจัยประยุกต์ด้าน AI, Deep Learning, Big Data Analytics และการพัฒนานวัตกรรมดิจิทัลสำหรับยกระดับอุตสาหกรรมและชุมชนภาคตะวันออกเฉียงเหนือ",
            career_opportunities="• Senior AI & Machine Learning Researcher\n• Chief Technology Officer (CTO) / Tech Lead\n• Data Science & Analytics Specialist\n• อาจารย์และนักวิชาการคอมพิวเตอร์ในสถาบันอุดมศึกษา",
            order=2
        )
        self.stdout.write(self.style.SUCCESS('Successfully seeded 2 Courses.'))

        # 3. News
        News.objects.all().delete()
        News.objects.create(
            title="เปิดรับสมัครนักศึกษาใหม่ สาขาวิชาวิทยาการคอมพิวเตอร์ (TCAS69)",
            category="ข่าวประชาสัมพันธ์",
            content="สาขาวิชาวิทยาการคอมพิวเตอร์ คณะศิลปศาสตร์และวิทยาศาสตร์ มหาวิทยาลัยราชภัฏศรีสะเกษ เปิดรับสมัครนักเรียน ม.6 หรือเทียบเท่า เข้าศึกษาต่อระดับปริญญาตรี ประจำปีการศึกษา 2569 หลักสูตรปรับปรุง พ.ศ. 2568 สมัครออนไลน์ได้แล้ววันนี้",
            is_featured=True
        )
        News.objects.create(
            title="การประเมินคุณภาพการศึกษาระดับหลักสูตร ตามมาตรฐาน AUN-QA",
            category="ข่าวประชาสัมพันธ์",
            content="สาขาวิชาวิทยาการคอมพิวเตอร์ ได้รับการประเมินคุณภาพระดับหลักสูตรตามมาตรฐาน AUN-QA ด้วยผลการประเมินระดับคะแนนความพึงพอใจดีเยี่ยม ณ คณะศิลปศาสตร์และวิทยาศาสตร์ มรภ.ศรีสะเกษ",
            is_featured=True
        )
        News.objects.create(
            title="การแข่งขันหุ่นยนต์ศรีสะเกษโรโบติกส์ (Sisaket Robotics 2026)",
            category="กิจกรรมสาขา",
            content="จัดแข่งขันหุ่นยนต์เยาวชนชิงถ้วยเกียรติยศสูงสุด รวมทั้งสิ้น 33 รายการ สำหรับระดับการศึกษาขั้นพื้นฐาน อาชีวศึกษา และอุดมศึกษาทั่วประเทศ ณ มหาวิทยาลัยราชภัฏศรีสะเกษ",
            is_featured=False
        )
        News.objects.create(
            title="อบรมเชิงปฏิบัติการ 'AI & Modern Web Development Bootcamp'",
            category="อบรมและสัมมนา",
            content="เสริมสร้างทักษะการพัฒนายูสเซอร์อินเทอร์เฟซ การเขียนโปรแกรม Python/Java และการเชื่อมต่อ AI APIs ให้แก่นักศึกษาสาขาวิทยาการคอมพิวเตอร์ชั้นปีที่ 1-4 โดยอาจารย์ประจำสาขาและวิทยากรผู้เชี่ยวชาญ",
            is_featured=False
        )
        self.stdout.write(self.style.SUCCESS('Successfully seeded 4 News items.'))

        # 4. Official Faculty Members with downloaded photo paths
        Faculty.objects.all().delete()
        Faculty.objects.create(
            name="เจษฎา โพนแก้ว (Jessada Phonkaew)",
            academic_rank="ผศ.ดร.",
            position="อาจารย์ผู้รับผิดชอบหลักสูตร (ความเชี่ยวชาญ: วิทยาการคอมพิวเตอร์)",
            education="ปร.ด. (วิทยาการคอมพิวเตอร์)",
            email="jessada.p@sskru.ac.th",
            phone="043-009700 ต่อ 50528",
            image="faculty/jessada_p.jpg",
            order=1
        )
        Faculty.objects.create(
            name="เจษฎา ชาตรี (Jessada Chatree)",
            academic_rank="ดร.",
            position="อาจารย์ผู้รับผิดชอบหลักสูตร (ความเชี่ยวชาญ: Computer Science and Engineering)",
            education="ปร.ด. (Computer Science and Engineering)",
            email="jessada.c@sskru.ac.th",
            phone="043-009700 ต่อ 50528",
            image="faculty/jessada_c.jpg",
            order=2
        )
        Faculty.objects.create(
            name="กริชบดินทร์ ผิวหอม (Krichbodin Phewhom)",
            academic_rank="ดร.",
            position="อาจารย์ผู้รับผิดชอบหลักสูตร (ความเชี่ยวชาญ: วิศวกรรมคอมพิวเตอร์)",
            education="ปร.ด. (วิศวกรรมคอมพิวเตอร์)",
            email="krichbodin.p@sskru.ac.th",
            phone="043-009700 ต่อ 50528",
            image="faculty/krichbodin.jpg",
            order=3
        )
        Faculty.objects.create(
            name="พิศาล สุขขี (Phisan Sukkee)",
            academic_rank="ผศ.",
            position="อาจารย์ผู้รับผิดชอบหลักสูตร (ความเชี่ยวชาญ: วิทยาการคอมพิวเตอร์)",
            education="วท.ม. (วิทยาการคอมพิวเตอร์)",
            email="phisan.s@sskru.ac.th",
            phone="084-298-2456",
            image="faculty/phisan.jpg",
            order=4
        )
        Faculty.objects.create(
            name="กนิษฐา อินธิชิต (Kanittha Inthichit)",
            academic_rank="ผศ.ดร.",
            position="หัวหน้าสาขาวิชาฯ / อาจารย์ผู้รับผิดชอบหลักสูตร (ความเชี่ยวชาญ: เทคโนโลยีสารสนเทศ)",
            education="ปร.ด. (เทคโนโลยีสารสนเทศ)",
            email="kanittha.i@sskru.ac.th",
            phone="043-009700 ต่อ 50528",
            image="faculty/kanittha.jpg",
            order=5
        )
        self.stdout.write(self.style.SUCCESS('Successfully seeded 5 Official Faculty members.'))
        self.stdout.write(self.style.SUCCESS('All official seed data updated successfully!'))
