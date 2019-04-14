from django.db import models

# Create your models here.

class ActiveIng(models.Model):
    active_ingredient = models.CharField(max_length=60, blank=True, null=True)

    def __str__(self):
        return self.active_ingredient


class ThirdParty(models.Model):
    name = models.CharField(max_length=60, blank=True, null=True)
    tax_card = models.CharField(max_length=60, blank=True, null=True)
    tax_card_file = models.CharField(max_length=60, blank=True, null=True)
    commercial_record = models.CharField(max_length=60, blank=True, null=True)
    commercial_record_file = models.CharField(max_length=60, blank=True, null=True)
    sdea_file = models.CharField(max_length=60, blank=True, null=True)
    address = models.CharField(max_length=60, blank=True, null=True)

    def __str__(self):
        return self.name or ""


class PvSystem(models.Model):
    SYS_TYPES =(
        ('SS', 'PSSF'), ('ML', 'PSMF For Local'), ('MA', 'PSMF For Agent')
    )
     
    MEDRA =(
        ('E', 'Exist'), ('O', 'Exists Outside'), ('N', 'No')
    )

    gm_name = models.CharField(max_length=60, blank=True, null=True)
    gm_email = models.CharField(max_length=60, blank=True, null=True)
    gm_mobile = models.CharField(max_length=60, blank=True, null=True)

    system_type = models.CharField(max_length=60, choices=SYS_TYPES, blank=True, null=True)

    address = models.CharField(max_length=60, blank=True, null=True)

    company_type = models.CharField(max_length=60, blank=True, null=True)

    f_company_id = models.CharField(max_length=60, blank=True, null=True)

    medra_status = models.CharField(max_length=1, choices=MEDRA, blank=True, null=True)
    medra_license_no = models.CharField(max_length=60, blank=True, null=True)
    medra_license_file = models.CharField(max_length=60, blank=True, null=True)

    icsr_status = models.CharField(max_length=1, choices=MEDRA, blank=True, null=True)
    e2b = models.BooleanField(default=True, blank=True, null=True)
    app_type = models.CharField(max_length=60, blank=True, null=True)

    team_members = models.CharField(max_length=60, blank=True, null=True)

    thirdparty = models.ForeignKey(ThirdParty, on_delete=models.CASCADE, blank=True, null=True)
    
    def __str__(self):
        return self.gm_name or ""

class Institution(models.Model):
    INST_TYPE =(
        ('F', 'Factory'), ('T', 'Toll'), ('U', 'Under-Reg'), ('I', 'Importer')
    )

    name = models.CharField(max_length=60, blank=True, null=True)
    # gln = models.PositiveIntegerField(blank=True, null=True)
    # address = models.TextField(max_length=150, blank=True, null=True)
    tax_card = models.CharField(max_length=15, blank=True, null=True)
    commercial_record = models.CharField(max_length=15, blank=True, null=True)
    longitude = models.CharField(max_length=30, blank=True, null=True)
    latitude = models.CharField(max_length=30, blank=True, null=True)
    inst_type = models.CharField(max_length=1, choices=INST_TYPE, blank=True, null=True)
    pvsystem = models.ForeignKey(PvSystem, on_delete=models.CASCADE, blank=True, null=True)
    
    def __str__(self):
        return self.name or ""



class Product(models.Model):
    institution = models.ForeignKey(Institution, on_delete=models.CASCADE, blank=True, null=True)
    name = models.CharField(max_length=60, blank=True, null=True)
    price = models.IntegerField(blank=True, null=True)
    gtin = models.IntegerField(blank=True, null=True)
    quantity = models.CharField(max_length=60, blank=True, null=True)
    active_ing = models.ManyToManyField(ActiveIng)
    
    def __str__(self):
        return self.name
   
class FCompany(models.Model):
    REL =(
        ('A', 'Agent'), ('B', 'Branch')
    )

    pv_system_id = models.ForeignKey(PvSystem, on_delete=models.CASCADE, blank=True, null=True)

    name = models.CharField(max_length=60, blank=True, null=True)
    relations = models.CharField(max_length=1, choices=REL, blank=True, null=True)
    sdea_file = models.CharField(max_length=60, blank=True, null=True)
    contract_file = models.CharField(max_length=60, blank=True, null=True)
    address = models.CharField(max_length=60, blank=True, null=True)
    reg_no = models.CharField(max_length=60, blank=True, null=True)

    qppv_name = models.CharField(max_length=60, blank=True, null=True)
    qppv_email = models.CharField(max_length=60, blank=True, null=True)
    qppv_mobile = models.CharField(max_length=60, blank=True, null=True)

    def __str__(self):
        return self.name


class Qppv(models.Model):
    first_name = models.CharField(max_length=60, blank=True, null=True)
    middle_name = models.CharField(max_length=60, blank=True, null=True)
    last_name = models.CharField(max_length=60, blank=True, null=True)

    nationalid = models.CharField(max_length=60, blank=True, null=True)
    nationalid_file = models.CharField(max_length=60, blank=True, null=True)

    educations_id = models.CharField(max_length=60, blank=True, null=True)
    educations_file = models.CharField(max_length=60, blank=True, null=True)
    job_number = models.CharField(max_length=60, blank=True, null=True)

    email_formal = models.CharField(max_length=60, blank=True, null=True)
    email_personal = models.CharField(max_length=60, blank=True, null=True)
    mobile_formal = models.CharField(max_length=60, blank=True, null=True)
    mobile_personal = models.CharField(max_length=60, blank=True, null=True)
    address = models.CharField(max_length=60, blank=True, null=True)

    company_name = models.CharField(max_length=60, blank=True, null=True)
    company_email = models.CharField(max_length=60, blank=True, null=True)
    contract_date = models.CharField(max_length=60, blank=True, null=True)
    contract_file = models.CharField(max_length=60, blank=True, null=True)
    tafweed = models.CharField(max_length=60, blank=True, null=True)

    social_insurance_no = models.CharField(max_length=60, blank=True, null=True)
    social_insurance_file = models.CharField(max_length=60, blank=True, null=True)

    certificates_id = models.CharField(max_length=60, blank=True, null=True)
    certificates_file = models.CharField(max_length=60, blank=True, null=True)

    def __str__(self):
        return self.last_name

class QppvDeputy(models.Model):
    first_name = models.CharField(max_length=60, blank=True, null=True)
    middle_name = models.CharField(max_length=60, blank=True, null=True)
    last_name = models.CharField(max_length=60, blank=True, null=True)
    
    nationalid = models.CharField(max_length=60, blank=True, null=True)
    nationalid_file = models.CharField(max_length=60, blank=True, null=True)
    
    educations_id = models.CharField(max_length=60, blank=True, null=True)
    educations_file = models.CharField(max_length=60, blank=True, null=True)
    job_number = models.CharField(max_length=60, blank=True, null=True)
    
    email_formal = models.CharField(max_length=60, blank=True, null=True)
    email_personal = models.CharField(max_length=60, blank=True, null=True)
    mobile_formal = models.CharField(max_length=60, blank=True, null=True)
    mobile_personal = models.CharField(max_length=60, blank=True, null=True)
    address = models.CharField(max_length=60, blank=True, null=True)
    
    company_name = models.CharField(max_length=60, blank=True, null=True)
    company_email = models.CharField(max_length=60, blank=True, null=True)
    contract_date = models.CharField(max_length=60, blank=True, null=True)
    contract_file = models.CharField(max_length=60, blank=True, null=True)
    tafweed = models.CharField(max_length=60, blank=True, null=True)
    
    social_insurance_no = models.CharField(max_length=60, blank=True, null=True)
    social_insurance_file = models.CharField(max_length=60, blank=True, null=True)
    
    certificates_id = models.CharField(max_length=60, blank=True, null=True)
    certificates_file = models.CharField(max_length=60, blank=True, null=True)

    def __str__(self):
        return self.last_name
