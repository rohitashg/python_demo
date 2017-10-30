from django.forms import ModelChoiceField
class GetNameModelChoiceField(ModelChoiceField):
    def label_from_instance(self, obj):
         return obj.name
class GetStateNameModelChoiceField(ModelChoiceField):
    def label_from_instance(self, obj):
         return obj.state_name

class GetUnitModelChoiceField(ModelChoiceField):
    def label_from_instance(self, obj):
        return obj.name
