from django import forms
from schools.models import ClassGroup
from accounts.models import Teacher
        
class ClassGroupForm(forms.ModelForm):
    class Meta:
        model = ClassGroup
        fields = "__all__"
    
    def __init__ ( self,  *args, **kwargs ):
        super ( ClassGroupForm, self ).__init__ ( *args, **kwargs )
        instance = getattr ( self, 'instance', None )
        class_group = self.instance
        self.fields['teacher'].queryset = Teacher.objects.filter(school=class_group.grade.school)
#