from rest_framework import serializers
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password, PBKDF2PasswordHasher
from jist_api.models import *

class depertmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Depertment
        # fields = '__all__'
        fields = (
            'id',
            'dept_name',
            'dept_short',
            # 'url'
        )

class depertmentIdSerializer(serializers.ModelSerializer):
    class Meta:
        model = Depertment
        # fields = '__all__'
        fields = (
            'id',
            # 'url'
        )

class branchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Branch
        # fields = '__all__'
        fields = (
            'id',
            'branch_name',
            'branch_accronym',
            'depertment',
            # 'url'
        )

class getBranchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Branch
        # fields = '__all__'
        fields = (
            'branch_name',
            # 'url'
        )

class studentSerializer(serializers.HyperlinkedModelSerializer):
    depertment_id = serializers.PrimaryKeyRelatedField(
        source = 'depertment',
        queryset = Depertment.objects.all()
    )
    # depertment = depertmentSerializer(read_only=False)
    depertment = serializers.StringRelatedField(many=False)
    # dept = serializers.CharField(write_only=True)
    branch_id = serializers.PrimaryKeyRelatedField(
        source = 'branch',
        queryset = Branch.objects.all()
    )
    branch = serializers.StringRelatedField(many=False)


    class Meta:
        model = Students
        # fields = '__all__'
        fields = (
            'id',
            'roll_number',
            'first_name',
            'last_name',
            'depertment',
            'depertment_id',
            'branch',
            'branch_id',
            'caste',
            'date_of_birth',
            'semester',
            'admission_year',
            'session',
            'father_name',
            'mother_name',
            'address',
            'parents_phone_number',
            'entry_type',
            'url'
        )


class transfer_studentSerializer(serializers.HyperlinkedModelSerializer):
    depertment_id = serializers.PrimaryKeyRelatedField(
        source = 'depertment',
        queryset = Depertment.objects.all()
    )
    # depertment = depertmentSerializer(read_only=False)
    depertment = serializers.StringRelatedField(many=False)
    # dept = serializers.CharField(write_only=True)
    branch_id = serializers.PrimaryKeyRelatedField(
        source = 'branch',
        queryset = Branch.objects.all()
    )
    branch = serializers.StringRelatedField(many=False)


    class Meta:
        model = Transfer_Students
        # fields = '__all__'
        fields = (
            'id',
            'roll_number',
            'first_name',
            'last_name',
            'depertment',
            'depertment_id',
            'branch',
            'branch_id',
            'caste',
            'date_of_birth',
            'semester',
            'admission_year',
            'session',
            'father_name',
            'mother_name',
            'address',
            'parents_phone_number',
            'entry_type',
            'transfered_institute_name',
            'transfer_date',
            'url'
        )


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    # new_password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = (
            'id',
            'username',
            'password',
            # 'new_password',
            'is_superuser',
            'is_staff'
        )
class PasswordChangeSerializer(serializers.Serializer):
    old_password = serializers.CharField(write_only=True)
    new_password = serializers.CharField(write_only=True)



class signinInfoSerializer(serializers.ModelSerializer):
    class Meta:
        # user = UserSerializer()
        model = signinInfo
        # fields = '__all__'
        fields = (
            # 'user',
            'client_ip',
            'timestamp',
            # 'new_timestamp',
            # 'url'
        )

# To store fee details of each depertment except BE depertment.
class OddSemesterFeeSerializer(serializers.ModelSerializer):
    depertment_id = serializers.PrimaryKeyRelatedField(
        source = 'depertment',
        queryset = Depertment.objects.all()
    )
    # depertment = depertmentSerializer(read_only=False)
    depertment = serializers.StringRelatedField(many=False)
    # dept = serializers.CharField(write_only=True)
    # branch_id = serializers.PrimaryKeyRelatedField(
    #     source = 'branch',
    #     queryset = Branch.objects.all()
    # )
    # branch = serializers.StringRelatedField(many=False)
    class Meta:
        model = semester_fees
        # fields = '__all__'
        fields = (
            'id',
            'depertment',
            'depertment_id',
            'branch',
            # 'branch_id',
            'semester',
            'govt_dues',
            'tuition_fee',
            'identity_fee',
            'examination_fee',
            'student_union_fee',
            'game_sports_fee',
            'magazine_fee',
            'laboratory_fee',
            'university_registration_fee',
            'enrolment_fee',
            'electricity_fee',
            'group_insurance_fee',
            'scout_guide_fee',
            'internet_fee',
            'welfare_fee',
            'development_fee',
            'library_caution_fee',
            'transport_fee',
            'training_placement_fee',
            'college_festival_fee',
            'medical_fee',
            'last_admission_date',
            'late_fee',
            # 'last_admission_date',
            # 'url'
        )

# To store BE fee details.
class BEFeeSerializer(serializers.ModelSerializer):
    depertment_id = serializers.PrimaryKeyRelatedField(
        source = 'depertment',
        queryset = Depertment.objects.all()
    )
    depertment = serializers.StringRelatedField(many=False)
    class Meta:
        model = be_fee_table
        # fields = '__all__'
        fields = (
            'id',
            'depertment',
            'depertment_id',
            'branch',
            # 'branch_id',
            'semester',
            'govt_dues',
            'identity_fee',
            'examination_fee',
            'student_union_fee',
            'game_sports_fee',
            'magazine_fee',
            'laboratory_fee',
            'university_registration_fee',
            'enrolment_fee',
            'electricity_fee',
            'group_insurance_fee',
            'scout_guide_fee',
            'internet_fee',
            'welfare_fee',
            'development_fee',
            'library_caution_fee',
            'transport_fee',
            'iste_fee',
            'training_placement_fee',
            'college_festival_fee',
            'medical_fee',
            'last_admission_date',
            'late_fee',
            # 'last_admission_date',
            # 'url'
        )

# To store students details who are submitted their admission fees.
class AdmissonSerializer(serializers.ModelSerializer):
    student_id = serializers.PrimaryKeyRelatedField(
        source = 'student',
        queryset = Students.objects.all()
    )
    roll_number = serializers.SlugRelatedField(
        source = 'student',
        # queryset = Students.objects.all(),
        slug_field = 'roll_number',
        # many = True,
        read_only = True,
    )
    student = serializers.StringRelatedField(many=False)

    depertment_id = serializers.PrimaryKeyRelatedField(
        source = 'depertment',
        queryset = Depertment.objects.all()
    )
    depertment = serializers.StringRelatedField(many=False)

    branch_id = serializers.PrimaryKeyRelatedField(
        source = 'branch',
        queryset = Branch.objects.all()
    )
    branch = serializers.StringRelatedField(many=False)
    class Meta:
        model = Admission
        fields = (
            'id',
            'student',
            'semester',
            'student_id',
            'roll_number',
            'depertment',
            'depertment_id',
            'branch',
            'branch_id',
            'admission_date',
            'govt_dues',
            'tuition_fee',
            'identity_fee',
            'examination_fee',
            'student_union_fee',
            'game_sports_fee',
            'magazine_fee',
            'laboratory_fee',
            'university_registration_fee',
            'enrolment_fee',
            'electricity_fee',
            'group_insurance_fee',
            'scout_guide_fee',
            'internet_fee',
            'welfare_fee',
            'development_fee',
            'library_caution_fee',
            'transport_fee',
            'iste_fee',
            'training_placement_fee',
            'college_festival_fee',
            'medical_fee',
            'late_fee',
            'amount',
        )

# To store students details who are submitted their hostel admission fees.
class HostelAdmissonSerializer(serializers.ModelSerializer):
    student_id = serializers.PrimaryKeyRelatedField(
        source = 'student',
        queryset = Students.objects.all()
    )
    roll_number = serializers.SlugRelatedField(
        source = 'student',
        slug_field = 'roll_number',
        read_only = True,
    )
    student = serializers.StringRelatedField(many=False)

    class Meta:
        model = Admission
        fields = (
            'id',
            'student',
            'semester',
            'student_id',
            'roll_number',
            'admission_date',
            'security_money',
            'electricity_fee',
            'mess_security',
            'seat_rent',
            'misc',
            'total'
        )


# To store examination fee details of each depertment.
class ExamFeeSerializer(serializers.ModelSerializer):
    depertment_id = serializers.PrimaryKeyRelatedField(
        source = 'depertment',
        queryset = Depertment.objects.all()
    )
    depertment = serializers.StringRelatedField(many=False)
    class Meta:
        model = Exam_fee_table
        # fields = '__all__'
        fields = (
            'id',
            'depertment',
            'depertment_id',
            'semester',
            'regular_exam_fee',
            'compartmetal_exam_fee_practicle_one',
            'compartmetal_exam_fee_practicle_more',
            'compartmetal_exam_fee_no_practicle_one',
            'compartmetal_exam_fee_no_practicle_more',
            'betterment_exam_fee_one',
            'betterment_exam_fee_more',
            'non_college_fee',
            'late_fee',
            'last_date'
        )


# To store spot admission fee details.
class SpotAdmissionFeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Spot_Admission_Fee
        fields = (
            'id',
            'govt_dues',
            'identity_fee',
            'examination_fee',
            'student_union_fee',
            'game_sports_fee',
            'magazine_fee',
            'laboratory_fee',
            'university_registration_fee',
            'enrolment_fee',
            'electricity_fee',
            'group_insurance_fee',
            'scout_guide_fee',
            'internet_fee',
            'welfare_fee',
            'development_fee',
            'library_caution_fee',
            'transport_fee',
            'iste_fee',
            'training_placement_fee',
            'college_festival_fee',
            'medical_fee',
            'form_and_prospectus_fee',
            'counselling_fee',
            'hostel_admission_fee',
            'spot_admission_fine',
        )


# To store students details who are submitted their examination fees.
class ExaminationSerializer(serializers.ModelSerializer):
    student_id = serializers.PrimaryKeyRelatedField(
        source = 'student',
        queryset = Students.objects.all()
    )
    roll_number = serializers.SlugRelatedField(
        source = 'student',
        queryset = Students.objects.all(),
        slug_field='roll_number',
    )
    student = serializers.StringRelatedField(many=False)

    depertment_id = serializers.PrimaryKeyRelatedField(
        source = 'depertment',
        queryset = Depertment.objects.all()
    )
    depertment = serializers.StringRelatedField(many=False)

    branch_id = serializers.PrimaryKeyRelatedField(
        source = 'branch',
        queryset = Branch.objects.all()
    )
    branch = serializers.StringRelatedField(many=False)
    class Meta:
        model = Examination_fee_table
        fields = (
            'id',
            'student',
            'semester',
            'roll_number',
            'student_id',
            'depertment',
            'depertment_id',
            'branch',
            'branch_id',
            'fees_submit_date',
            'amount',
            'late_fee',
        )

# To store students details who are submitted their compartmental examination fees.
class CompartmentalSerializer(serializers.ModelSerializer):
    student_id = serializers.PrimaryKeyRelatedField(
        source = 'student',
        queryset = Students.objects.all()
    )
    roll_number = serializers.SlugRelatedField(
        source = 'student',
        queryset = Students.objects.all(),
        slug_field='roll_number',
    )
    student = serializers.StringRelatedField(many=False)

    depertment_id = serializers.PrimaryKeyRelatedField(
        source = 'depertment',
        queryset = Depertment.objects.all()
    )
    depertment = serializers.StringRelatedField(many=False)

    branch_id = serializers.PrimaryKeyRelatedField(
        source = 'branch',
        queryset = Branch.objects.all()
    )
    branch = serializers.StringRelatedField(many=False)
    class Meta:
        model = Compartmental_fee_table
        fields = (
            'id',
            'student',
            'semester',
            'student_id',
            'roll_number',
            'depertment',
            'depertment_id',
            'branch',
            'branch_id',
            'fees_submit_date',
            'amount',
            'late_fee',
        )

# To store students details who are submitted their betterment examination fees.
class BettermentSerializer(serializers.ModelSerializer):
    student_id = serializers.PrimaryKeyRelatedField(
        source = 'student',
        queryset = Students.objects.all()
    )
    roll_number = serializers.SlugRelatedField(
        source = 'student',
        queryset = Students.objects.all(),
        slug_field='roll_number',
    )
    student = serializers.StringRelatedField(many=False)

    depertment_id = serializers.PrimaryKeyRelatedField(
        source = 'depertment',
        queryset = Depertment.objects.all()
    )
    depertment = serializers.StringRelatedField(many=False)

    branch_id = serializers.PrimaryKeyRelatedField(
        source = 'branch',
        queryset = Branch.objects.all()
    )
    branch = serializers.StringRelatedField(many=False)
    class Meta:
        model = Betterment_fee_table
        fields = (
            'id',
            'student',
            'semester',
            'student_id',
            'roll_number',
            'depertment',
            'depertment_id',
            'branch',
            'branch_id',
            'fees_submit_date',
            'amount',
            'late_fee',
        )




# To store form and prospectus sell records.
class FormAndProspectusSerializer(serializers.ModelSerializer):
    class Meta:
        model = form_and_prospectus_table
        fields = (
            'id',
            'student_name',
            'depertment',
            'branch',
            'prospectus_fee',
            'purchase_date',
        )
