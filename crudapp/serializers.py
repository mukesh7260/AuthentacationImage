from rest_framework import serializers
from crudapp.models import College , Principle
class PrincipleSerializer(serializers.ModelSerializer):
   
    class Meta:
        model = Principle 
        fields = "__all__" 
        



class CollegeSerializer(serializers.ModelSerializer):
    principle = PrincipleSerializer(many=True)
    
    class Meta:
        model = College 
        fields = ['cname','clocation','cid','cstate','principle']
        

class CollegeSerializer(serializers.ModelSerializer):
    principle =serializers.SerializerMethodField()
    def get_first_name(self,obj):
        return obj.principle 
    principle = PrincipleSerializer(many=True) 
    class Meta:
        model = College 
        fields = ['cname','clocation','cid','cstate','ccountry','principle']
    