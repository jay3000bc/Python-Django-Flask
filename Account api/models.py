from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from datetime import date, datetime




class signinInfo(models.Model):
    #id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    client_ip = models.CharField(max_length=50,null=False,default="NULL")
    timestamp = models.DateTimeField(null=False,default=datetime.now)
    # new_timestamp = models.DateTimeField(null=False,default="NULL")

    def __str__(self):
        return '%s' %(self.user.username)
    def save(self, *args, **kwargs):
        self.user = User.objects.get(id = 1)
        super().save(*args, **kwargs)


class Depertment(models.Model):
    DEPT_CHOICES = (
        ('Bachelor of Science','B.Sc.'),
        ('Bachelor of Science in Information Technology','B.Sc.(IT)'),
        ('Master of Science','M.Sc.'),
        ('Bachelor of Engineering','B.E.'),
        ('PhD','PhD'),
    )
    dept_name = models.CharField(max_length=100,null=False, default="NULL", unique=True)
    dept_short = models.CharField(max_length=100,null=False, default="NULL")

    def __str__(self):
        return self.dept_name


class Branch(models.Model):
    branch_name = models.CharField(max_length=100, null=False, default="NULL")
    branch_accronym = models.CharField(max_length=20, null=False, default="NULL")
    depertment = models.ManyToManyField(Depertment)

    def __str__(self):
        return self.branch_name


class Students(models.Model):
    CASTE_CHOICES = (
        ('General','GENERAL'),
        ('OBC','OBC'),
        ('MOBC','MOBC'),
        ('SC','SC'),
        ('ST','ST'),
        ('ST(H)','ST(H)'),
    )
    SEMESTER_CHOICES = (
        ('NULL',''),
        ('First','I'),
        ('Second','II'),
        ('Third','III'),
        ('Fourth','IV'),
        ('Fifth','V'),
        ('Sixth','VI'),
        ('Seventh','VII'),
        ('Eighth','VIII'),
    )
    ENTRY_CHOICES = (
        ('NULL',''),
        ('Regular','Regular'),
        ('Lateral','Lateral'),
    )

    first_name = models.CharField(max_length=100,null=False,default="NULL")
    last_name = models.CharField(max_length=100,null=False,default="NULL")
    date_of_birth = models.DateField(null=False,default=timezone.now)
    # depertment = models.CharField(max_length=100,null=False, choices=DEPT_CHOICES, default="NULL")
    depertment = models.ForeignKey(Depertment, on_delete=models.CASCADE)
    # branch = models.CharField(max_length=100,null=False, choices=BRANCH_CHOICES, default="NULL")
    branch = models.ForeignKey(Branch, on_delete=models.CASCADE)
    caste = models.CharField(max_length=100,null=False, choices=CASTE_CHOICES, default="NULL")
    semester = models.CharField(max_length=100,null=False, choices=SEMESTER_CHOICES, default="NULL")
    admission_year = models.IntegerField(null=False, default=datetime.now().year)
    roll_number = models.CharField(max_length=100, null=False, default="NULL")
    session = models.CharField(max_length=20, null=False, default="NULL")
    father_name = models.CharField(max_length=100, null=False, default="NULL")
    mother_name = models.CharField(max_length=100, null=False, default="NULL")
    address = models.TextField(max_length=500,null=False, default="NULL")
    parents_phone_number = models.CharField(max_length=20, null=False, default="NULL")
    entry_type = models.CharField(max_length=20, null=False, choices=ENTRY_CHOICES, default="Regular")

    def __str__(self):
        return self.first_name + ' ' + self.last_name


class Transfer_Students(models.Model):
    CASTE_CHOICES = (
        ('General','GENERAL'),
        ('OBC','OBC'),
        ('SC','SC'),
        ('ST','ST'),
        ('ST(H)','ST(H)'),
    )
    SEMESTER_CHOICES = (
        ('NULL',''),
        ('First','I'),
        ('Second','II'),
        ('Third','III'),
        ('Fourth','IV'),
        ('Fifth','V'),
        ('Sixth','VI'),
        ('Seventh','VII'),
        ('Eighth','VIII'),
    )
    ENTRY_CHOICES = (
        ('NULL',''),
        ('Regular','Regular'),
        ('Lateral','Lateral'),
    )

    # student = models.ForeignKey(Students, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100,null=False,default="NULL")
    last_name = models.CharField(max_length=100,null=False,default="NULL")
    date_of_birth = models.DateField(null=False,default=timezone.now)
    # depertment = models.CharField(max_length=100,null=False, choices=DEPT_CHOICES, default="NULL")
    depertment = models.ForeignKey(Depertment, on_delete=models.CASCADE)
    # branch = models.CharField(max_length=100,null=False, choices=BRANCH_CHOICES, default="NULL")
    branch = models.ForeignKey(Branch, on_delete=models.CASCADE)
    caste = models.CharField(max_length=100,null=False, choices=CASTE_CHOICES, default="NULL")
    semester = models.CharField(max_length=100,null=False, choices=SEMESTER_CHOICES, default="NULL")
    admission_year = models.IntegerField(null=False, default=datetime.now().year)
    roll_number = models.CharField(max_length=100, null=False, default="NULL")
    session = models.CharField(max_length=20, null=False, default="NULL")
    father_name = models.CharField(max_length=100, null=False, default="NULL")
    mother_name = models.CharField(max_length=100, null=False, default="NULL")
    address = models.TextField(max_length=500,null=False, default="NULL")
    parents_phone_number = models.CharField(max_length=20, null=False, default="NULL")
    entry_type = models.CharField(max_length=20, null=False, choices=ENTRY_CHOICES, default="Regular")
    transfered_institute_name = models.CharField(max_length=100,null=False,default="NULL")
    transfer_date = models.DateField(null=False,default=timezone.now)


    def __str__(self):
        return self.first_name + ' ' + self.last_name


class semester_fees(models.Model):
    SEMESTER_CHOICES = (
        ('Even','EVEN'),
        ('Odd','ODD')
    )

    depertment = models.ForeignKey(Depertment, on_delete=models.CASCADE)
    branch = models.ManyToManyField(Branch)
    semester = models.CharField(max_length=100, null=False, choices=SEMESTER_CHOICES, default="NULL")
    govt_dues = models.DecimalField(max_digits=10, decimal_places=2, null=False, default=0.00)
    tuition_fee = models.DecimalField(max_digits=10, decimal_places=2, null=False, default=0.00)
    identity_fee = models.DecimalField(max_digits=10, decimal_places=2, null=False, default=0.00)
    examination_fee = models.DecimalField(max_digits=10, decimal_places=2, null=False, default=0.00)
    student_union_fee = models.DecimalField(max_digits=10, decimal_places=2, null=False, default=0.00)
    game_sports_fee = models.DecimalField(max_digits=10, decimal_places=2, null=False, default=0.00)
    magazine_fee = models.DecimalField(max_digits=10, decimal_places=2, null=False, default=0.00)
    laboratory_fee = models.DecimalField(max_digits=10, decimal_places=2, null=False, default=0.00)
    university_registration_fee = models.DecimalField(max_digits=10, decimal_places=2, null=False, default=0.00)
    enrolment_fee = models.DecimalField(max_digits=10, decimal_places=2, null=False, default=0.00)
    electricity_fee = models.DecimalField(max_digits=10, decimal_places=2, null=False, default=0.00)
    group_insurance_fee = models.DecimalField(max_digits=10, decimal_places=2, null=False, default=0.00)
    scout_guide_fee = models.DecimalField(max_digits=10, decimal_places=2, null=False, default=0.00)
    internet_fee = models.DecimalField(max_digits=10, decimal_places=2, null=False, default=0.00)
    welfare_fee = models.DecimalField(max_digits=10, decimal_places=2, null=False, default=0.00)
    development_fee = models.DecimalField(max_digits=10, decimal_places=2, null=False, default=0.00)
    library_caution_fee = models.DecimalField(max_digits=10, decimal_places=2, null=False, default=0.00)
    transport_fee = models.DecimalField(max_digits=10, decimal_places=2, null=False, default=0.00)
    training_placement_fee = models.DecimalField(max_digits=10, decimal_places=2, null=False, default=0.00)
    college_festival_fee = models.DecimalField(max_digits=10, decimal_places=2, null=False, default=0.00)
    medical_fee = models.DecimalField(max_digits=10, decimal_places=2, null=False, default=0.00)
    late_fee = models.DecimalField(max_digits=10, decimal_places=2, null=False, default=0.00)
    last_admission_date = models.DateField(null=True)

    def __str__(self):
        return "B.Sc. B.Sc.(IT) M.Sc. Fees"


class be_fee_table(models.Model):
    SEMESTER_CHOICES = (
        ('Even','EVEN'),
        ('Odd','ODD')
    )

    depertment = models.ForeignKey(Depertment, on_delete=models.CASCADE)
    branch = models.ManyToManyField(Branch)
    semester = models.CharField(max_length=100, null=False, choices=SEMESTER_CHOICES, default="NULL")
    govt_dues = models.DecimalField(max_digits=10, decimal_places=2, null=False, default=0.00)
    identity_fee = models.DecimalField(max_digits=10, decimal_places=2, null=False, default=0.00)
    examination_fee = models.DecimalField(max_digits=10, decimal_places=2, null=False, default=0.00)
    student_union_fee = models.DecimalField(max_digits=10, decimal_places=2, null=False, default=0.00)
    game_sports_fee = models.DecimalField(max_digits=10, decimal_places=2, null=False, default=0.00)
    magazine_fee = models.DecimalField(max_digits=10, decimal_places=2, null=False, default=0.00)
    laboratory_fee = models.DecimalField(max_digits=10, decimal_places=2, null=False, default=0.00)
    university_registration_fee = models.DecimalField(max_digits=10, decimal_places=2, null=False, default=0.00)
    enrolment_fee = models.DecimalField(max_digits=10, decimal_places=2, null=False, default=0.00)
    electricity_fee = models.DecimalField(max_digits=10, decimal_places=2, null=False, default=0.00)
    group_insurance_fee = models.DecimalField(max_digits=10, decimal_places=2, null=False, default=0.00)
    scout_guide_fee = models.DecimalField(max_digits=10, decimal_places=2, null=False, default=0.00)
    internet_fee = models.DecimalField(max_digits=10, decimal_places=2, null=False, default=0.00)
    welfare_fee = models.DecimalField(max_digits=10, decimal_places=2, null=False, default=0.00)
    development_fee = models.DecimalField(max_digits=10, decimal_places=2, null=False, default=0.00)
    library_caution_fee = models.DecimalField(max_digits=10, decimal_places=2, null=False, default=0.00)
    transport_fee = models.DecimalField(max_digits=10, decimal_places=2, null=False, default=0.00)
    iste_fee = models.DecimalField(max_digits=10, decimal_places=2, null=False, default=0.00)
    training_placement_fee = models.DecimalField(max_digits=10, decimal_places=2, null=False, default=0.00)
    college_festival_fee = models.DecimalField(max_digits=10, decimal_places=2, null=False, default=0.00)
    medical_fee = models.DecimalField(max_digits=10, decimal_places=2, null=False, default=0.00)
    late_fee = models.DecimalField(max_digits=10, decimal_places=2, null=False, default=0.00)
    last_admission_date = models.DateField(null=True)


class hostel_fee_table(models.Model):
    SEMESTER_CHOICES = (
        ('Even','EVEN'),
        ('Odd','ODD')
    )

    semester = models.CharField(max_length=100, null=False, choices=SEMESTER_CHOICES, default="NULL")
    security_money = models.DecimalField(max_digits=10, decimal_places=2, null=False, default=0.00)
    electricity_fee = models.DecimalField(max_digits=10, decimal_places=2, null=False, default=0.00)
    mess_security = models.DecimalField(max_digits=10, decimal_places=2, null=False, default=0.00)
    seat_rent = models.DecimalField(max_digits=10, decimal_places=2, null=False, default=0.00)
    misc = models.DecimalField(max_digits=10, decimal_places=2, null=False, default=0.00)
    total = models.DecimalField(max_digits=10, decimal_places=2, null=False, default=0.00)
    late_fee = models.DecimalField(max_digits=10, decimal_places=2, null=False, default=0.00)
    last_admission_date = models.DateField(null=True)

    def __str__(self):
        return self.semester


class Admission(models.Model):
    SEMESTER_CHOICES = (
        ('NULL',''),
        ('First','I'),
        ('Second','II'),
        ('Third','III'),
        ('Fourth','IV'),
        ('Fifth','V'),
        ('Sixth','VI'),
        ('Seventh','VII'),
        ('Eighth','VIII'),
    )
    student = models.ForeignKey(Students, on_delete=models.CASCADE)
    semester = models.CharField(max_length=100,null=False, choices=SEMESTER_CHOICES, default="NULL")
    depertment = models.ForeignKey(Depertment, on_delete=models.CASCADE)
    branch = models.ForeignKey(Branch, on_delete=models.CASCADE)
    admission_date = models.DateField(null=False,default=timezone.now)
    govt_dues = models.DecimalField(max_digits=10, decimal_places=2, null=False, default=0.00)
    tuition_fee = models.DecimalField(max_digits=10, decimal_places=2, null=False, default=0.00)
    identity_fee = models.DecimalField(max_digits=10, decimal_places=2, null=False, default=0.00)
    examination_fee = models.DecimalField(max_digits=10, decimal_places=2, null=False, default=0.00)
    student_union_fee = models.DecimalField(max_digits=10, decimal_places=2, null=False, default=0.00)
    game_sports_fee = models.DecimalField(max_digits=10, decimal_places=2, null=False, default=0.00)
    magazine_fee = models.DecimalField(max_digits=10, decimal_places=2, null=False, default=0.00)
    laboratory_fee = models.DecimalField(max_digits=10, decimal_places=2, null=False, default=0.00)
    university_registration_fee = models.DecimalField(max_digits=10, decimal_places=2, null=False, default=0.00)
    enrolment_fee = models.DecimalField(max_digits=10, decimal_places=2, null=False, default=0.00)
    electricity_fee = models.DecimalField(max_digits=10, decimal_places=2, null=False, default=0.00)
    group_insurance_fee = models.DecimalField(max_digits=10, decimal_places=2, null=False, default=0.00)
    scout_guide_fee = models.DecimalField(max_digits=10, decimal_places=2, null=False, default=0.00)
    internet_fee = models.DecimalField(max_digits=10, decimal_places=2, null=False, default=0.00)
    welfare_fee = models.DecimalField(max_digits=10, decimal_places=2, null=False, default=0.00)
    development_fee = models.DecimalField(max_digits=10, decimal_places=2, null=False, default=0.00)
    library_caution_fee = models.DecimalField(max_digits=10, decimal_places=2, null=False, default=0.00)
    transport_fee = models.DecimalField(max_digits=10, decimal_places=2, null=False, default=0.00)
    iste_fee = models.DecimalField(max_digits=10, decimal_places=2, null=False, default=0.00)
    training_placement_fee = models.DecimalField(max_digits=10, decimal_places=2, null=False, default=0.00)
    college_festival_fee = models.DecimalField(max_digits=10, decimal_places=2, null=False, default=0.00)
    medical_fee = models.DecimalField(max_digits=10, decimal_places=2, null=False, default=0.00)
    late_fee = models.DecimalField(max_digits=10, decimal_places=2, null=False, default=0.00)
    amount = models.DecimalField(max_digits=10, decimal_places=2, null=False, default=0.00)

    def __str__(self):
        return self.student


class HostelAdmission(models.Model):
    SEMESTER_CHOICES = (
        ('NULL',''),
        ('First','I'),
        ('Second','II'),
        ('Third','III'),
        ('Fourth','IV'),
        ('Fifth','V'),
        ('Sixth','VI'),
        ('Seventh','VII'),
        ('Eighth','VIII'),
    )
    student = models.ForeignKey(Students, on_delete=models.CASCADE)
    semester = models.CharField(max_length=100, null=False, choices=SEMESTER_CHOICES, default="NULL")
    admission_date = models.DateField(null=False, default=timezone.now)
    security_money = models.DecimalField(max_digits=10, decimal_places=2, null=False, default=0.00)
    electricity_fee = models.DecimalField(max_digits=10, decimal_places=2, null=False, default=0.00)
    mess_security = models.DecimalField(max_digits=10, decimal_places=2, null=False, default=0.00)
    seat_rent = models.DecimalField(max_digits=10, decimal_places=2, null=False, default=0.00)
    misc = models.DecimalField(max_digits=10, decimal_places=2, null=False, default=0.00)
    total = models.DecimalField(max_digits=10, decimal_places=2, null=False, default=0.00)

    def __str__(self):
        return self.student


class Examination_fee_table(models.Model):
    SEMESTER_CHOICES = (
        ('NULL',''),
        ('First','I'),
        ('Second','II'),
        ('Third','III'),
        ('Fourth','IV'),
        ('Fifth','V'),
        ('Sixth','VI'),
        ('Seventh','VII'),
        ('Eighth','VIII'),
    )
    student = models.ForeignKey(Students, on_delete=models.CASCADE)
    semester = models.CharField(max_length=100,null=False, choices=SEMESTER_CHOICES, default="NULL")
    depertment = models.ForeignKey(Depertment, on_delete=models.CASCADE)
    branch = models.ForeignKey(Branch, on_delete=models.CASCADE)
    fees_submit_date = models.DateField(null=False,default=timezone.now)
    amount = models.DecimalField(max_digits=10, decimal_places=2, null=False, default=0.00)
    late_fee = models.DecimalField(max_digits=10, decimal_places=2, null=False, default=0.00)

    def __str__(self):
        return self.student


class Compartmental_fee_table(models.Model):
    SEMESTER_CHOICES = (
        ('NULL',''),
        ('First','I'),
        ('Second','II'),
        ('Third','III'),
        ('Fourth','IV'),
        ('Fifth','V'),
        ('Sixth','VI'),
        ('Seventh','VII'),
        ('Eighth','VIII'),
    )
    student = models.ForeignKey(Students, on_delete=models.CASCADE)
    semester = models.CharField(max_length=100,null=False, choices=SEMESTER_CHOICES, default="NULL")
    depertment = models.ForeignKey(Depertment, on_delete=models.CASCADE)
    branch = models.ForeignKey(Branch, on_delete=models.CASCADE)
    fees_submit_date = models.DateField(null=False,default=timezone.now)
    amount = models.DecimalField(max_digits=10, decimal_places=2, null=False, default=0.00)
    late_fee = models.DecimalField(max_digits=10, decimal_places=2, null=False, default=0.00)

    def __str__(self):
        return self.student


class Betterment_fee_table(models.Model):
    SEMESTER_CHOICES = (
        ('NULL',''),
        ('First','I'),
        ('Second','II'),
        ('Third','III'),
        ('Fourth','IV'),
        ('Fifth','V'),
        ('Sixth','VI'),
        ('Seventh','VII'),
        ('Eighth','VIII'),
    )
    student = models.ForeignKey(Students, on_delete=models.CASCADE)
    semester = models.CharField(max_length=100,null=False, choices=SEMESTER_CHOICES, default="NULL")
    depertment = models.ForeignKey(Depertment, on_delete=models.CASCADE)
    branch = models.ForeignKey(Branch, on_delete=models.CASCADE)
    fees_submit_date = models.DateField(null=False,default=timezone.now)
    amount = models.DecimalField(max_digits=10, decimal_places=2, null=False, default=0.00)
    late_fee = models.DecimalField(max_digits=10, decimal_places=2, null=False, default=0.00)

    def __str__(self):
        return self.student


class Exam_fee_table(models.Model):
    SEMESTER_CHOICES = (
        ('Even','EVEN'),
        ('Odd','ODD')
    )

    depertment = models.ForeignKey(Depertment, on_delete=models.CASCADE)
    semester = models.CharField(max_length=100, null=False, choices=SEMESTER_CHOICES, default="NULL")
    regular_exam_fee = models.DecimalField(max_digits=10, decimal_places=2, null=False, default=0.00)
    compartmetal_exam_fee_practicle_one = models.DecimalField(max_digits=10, decimal_places=2, null=False, default=0.00)
    compartmetal_exam_fee_practicle_more = models.DecimalField(max_digits=10, decimal_places=2, null=False, default=0.00)
    compartmetal_exam_fee_no_practicle_one = models.DecimalField(max_digits=10, decimal_places=2, null=False, default=0.00)
    compartmetal_exam_fee_no_practicle_more = models.DecimalField(max_digits=10, decimal_places=2, null=False, default=0.00)
    betterment_exam_fee_one = models.DecimalField(max_digits=10, decimal_places=2, null=False, default=0.00)
    betterment_exam_fee_more = models.DecimalField(max_digits=10, decimal_places=2, null=False, default=0.00)
    non_college_fee = models.DecimalField(max_digits=10, decimal_places=2, null=False, default=0.00)
    late_fee = models.DecimalField(max_digits=10, decimal_places=2, null=False, default=0.00)
    last_date = models.DateField(null=True)


class Spot_Admission_Fee(models.Model):
    govt_dues = models.DecimalField(max_digits=10, decimal_places=2, null=False, default=0.00)
    identity_fee = models.DecimalField(max_digits=10, decimal_places=2, null=False, default=0.00)
    examination_fee = models.DecimalField(max_digits=10, decimal_places=2, null=False, default=0.00)
    student_union_fee = models.DecimalField(max_digits=10, decimal_places=2, null=False, default=0.00)
    game_sports_fee = models.DecimalField(max_digits=10, decimal_places=2, null=False, default=0.00)
    magazine_fee = models.DecimalField(max_digits=10, decimal_places=2, null=False, default=0.00)
    laboratory_fee = models.DecimalField(max_digits=10, decimal_places=2, null=False, default=0.00)
    university_registration_fee = models.DecimalField(max_digits=10, decimal_places=2, null=False, default=0.00)
    enrolment_fee = models.DecimalField(max_digits=10, decimal_places=2, null=False, default=0.00)
    electricity_fee = models.DecimalField(max_digits=10, decimal_places=2, null=False, default=0.00)
    group_insurance_fee = models.DecimalField(max_digits=10, decimal_places=2, null=False, default=0.00)
    scout_guide_fee = models.DecimalField(max_digits=10, decimal_places=2, null=False, default=0.00)
    internet_fee = models.DecimalField(max_digits=10, decimal_places=2, null=False, default=0.00)
    welfare_fee = models.DecimalField(max_digits=10, decimal_places=2, null=False, default=0.00)
    development_fee = models.DecimalField(max_digits=10, decimal_places=2, null=False, default=0.00)
    library_caution_fee = models.DecimalField(max_digits=10, decimal_places=2, null=False, default=0.00)
    transport_fee = models.DecimalField(max_digits=10, decimal_places=2, null=False, default=0.00)
    iste_fee = models.DecimalField(max_digits=10, decimal_places=2, null=False, default=0.00)
    training_placement_fee = models.DecimalField(max_digits=10, decimal_places=2, null=False, default=0.00)
    college_festival_fee = models.DecimalField(max_digits=10, decimal_places=2, null=False, default=0.00)
    medical_fee = models.DecimalField(max_digits=10, decimal_places=2, null=False, default=0.00)
    form_and_prospectus_fee = models.DecimalField(max_digits=10, decimal_places=2, null=False, default=0.00)
    counselling_fee = models.DecimalField(max_digits=10, decimal_places=2, null=False, default=0.00)
    hostel_admission_fee = models.DecimalField(max_digits=10, decimal_places=2, null=False, default=0.00)
    spot_admission_fine = models.DecimalField(max_digits=10, decimal_places=2, null=False, default=0.00)

# Model for prospectus sell data.
class form_and_prospectus_table(models.Model):
    student_name = models.CharField(max_length=100, null=False, default="NULL")
    depertment = models.CharField(max_length=100, null=False, default="NULL")
    branch = models.CharField(max_length=100, null=False, default="NULL")
    prospectus_fee = models.DecimalField(max_digits=10, decimal_places=2, null=False, default=0.00)
    purchase_date = models.DateField(null=True,default=timezone.now)
