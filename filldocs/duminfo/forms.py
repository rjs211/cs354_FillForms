from django.forms import ModelForm
from .models import DumUser
from filldocs.ceti_dict import necdict
from filldocs.ceti_dict import getFormWidget




class DumUserForm1(ModelForm):
    # template_name = 'duminfo/dum_forms.html'

    class Meta:
        model = DumUser
        fields = necdict[1]
        widgets = getFormWidget(1)

class DumUserForm2(ModelForm):
    # template_name = 'duminfo/dum_forms.html'

    class Meta:
        model = DumUser
        fields = necdict[2]
        widgets = getFormWidget(2)


class DumUserForm3(ModelForm):
    # template_name = 'duminfo/dum_forms.html'

    class Meta:
        model = DumUser
        fields = necdict[3]
        widgets = getFormWidget(3)

class DumUserForm4(ModelForm):
    # template_name = 'duminfo/dum_forms.html'

    class Meta:
        model = DumUser
        fields = necdict[4]
        widgets = getFormWidget(4)

class DumUserForm5(ModelForm):
    # template_name = 'duminfo/dum_forms.html'

    class Meta:
        model = DumUser
        fields = necdict[5]
        widgets = getFormWidget(5)

class DumUserForm6(ModelForm):
    # template_name = 'duminfo/dum_forms.html'

    class Meta:
        model = DumUser
        fields = necdict[6]
        widgets = getFormWidget(6)

class DumUserForm7(ModelForm):
    # template_name = 'duminfo/dum_forms.html'

    class Meta:
        model = DumUser
        fields = necdict[7]
        widgets = getFormWidget(7)

class DumUserForm8(ModelForm):
    # template_name = 'duminfo/dum_forms.html'

    class Meta:
        model = DumUser
        fields = necdict[8]
        widgets = getFormWidget(8)




formDict = {
    1:DumUserForm1,
    2:DumUserForm2,
    3:DumUserForm3,
    4:DumUserForm4,
    5:DumUserForm5,
    6:DumUserForm6,
    7:DumUserForm7,
    8:DumUserForm8,
}

formName = {
    1:'MyForm',
    2:'Form2 yay',
    3: 'Joining Report',
    4: 'Request / Requisition Form',
    5: 'Statement of Assets and Liabilites',
    6: 'Attestation Form',
    7: 'IITP club Membership Form',
    8: 'ID Card Details',
}