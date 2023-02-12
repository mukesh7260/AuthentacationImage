from django.db import models

class College(models.Model):
    cname = models.CharField(max_length=12,null=True,blank=True)
    clocation = models.CharField(max_length=13,null=True,blank=True)
    cid = models.IntegerField(null=True,blank=True)
    cstate = models.CharField(max_length=14,null=True,blank=True)
    ccountry = models.CharField(max_length=15,null=True,blank=True)
    
    def __str__(self):
        return self.cname 
    
# class Principle(models.Model):
#     college = models.OneToOneField(College,on_delete=models.CASCADE,related_name='principle')
#     pname = models.CharField(max_length=12,null=True,blank=True)
#     pcity = models.CharField(max_length=21,null=True,blank=True)
#     pid = models.IntegerField(null=True,blank=True)
    
#     def __str__(self):
#         return self.college.cname 
    

# class Principle(models.Model):
#     college = models.ForeignKey(College,on_delete=models.CASCADE,related_name='principle')
#     pname = models.CharField(max_length=12,null=True,blank=True)
#     pcity = models.CharField(max_length=21,null=True,blank=True)
#     pid = models.IntegerField(null=True,blank=True)
    
#     def __str__(self):
#         return self.college.cname 
    
    
class Principle(models.Model):
    college = models.ManyToManyField(College,related_name='principle')
    pname = models.CharField(max_length=12,null=True,blank=True)
    pcity = models.CharField(max_length=21,null=True,blank=True)
    pid = models.IntegerField(null=True,blank=True)

    