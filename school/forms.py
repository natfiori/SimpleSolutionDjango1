from django import forms

from .models import Career, Subject, Professor, Student, Grade, Absences


class CareerCreationForm(forms.ModelForm):
    class Meta:
        model = Career
        fields = ('name', 'code', 'career_type',)


class CareerEditForm(forms.ModelForm):
    class Meta:
        model = Career
        fields = ('name', 'code', 'career_type',)


class SubjectCreationForm(forms.ModelForm):
    class Meta:
        model = Subject
        fields = ('name', 'code', 'professors', 'students', 'career',)


class SubjectEditForm(forms.ModelForm):
    class Meta:
        model = Subject
        fields = ('name', 'code', 'professors', 'students', 'career',)


class ProfessorCreationForm(forms.ModelForm):
    class Meta:
        model = Professor
        fields = ('code',)


class StudentCreationForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ('code',)


class GradeCreationForm(forms.ModelForm):
    class Meta:
        model = Grade
        fields = ('student', 'date', 'grade')


class GradeEditForm(forms.ModelForm):
    class Meta:
        model = Grade
        fields = ('date', 'grade')


class AbsenceCreationForm(forms.ModelForm):
    class Meta:
        model = Absences
        fields = ('student', 'date', 'absence')


class AbsenceEditForm(forms.ModelForm):
    class Meta:
        model = Absences
        fields = ('date', 'absence')
