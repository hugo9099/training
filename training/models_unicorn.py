# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models


class ApiAbstractproduct(models.Model):
    description = models.TextField()
    months_in_advance = models.SmallIntegerField()
    allowance_field = models.CharField(max_length=30)
    allowance_type = models.SmallIntegerField()
    allowance_value = models.IntegerField()
    carrier = models.ForeignKey('ApiCarrier', models.DO_NOTHING)
    active = models.IntegerField()
    script_properties = models.TextField(blank=True, null=True)
    product_carrier_code = models.CharField(max_length=20, blank=True, null=True)
    enrollment_type = models.ForeignKey('ApiEnrollmenttype', models.DO_NOTHING, blank=True, null=True)
    is_policy_generated = models.IntegerField()
    sales_board_category = models.ForeignKey('ApiSalesboardcategory', models.DO_NOTHING, blank=True, null=True)
    advancing_fee = models.DecimalField(max_digits=10, decimal_places=4)
    hbc_commission_type = models.SmallIntegerField()
    agent_commission_type = models.SmallIntegerField()

    class Meta:
        managed = False
        db_table = 'api_abstractproduct'


class ApiAccount(models.Model):
    first_name = models.CharField(max_length=40)
    last_name = models.CharField(max_length=40)
    middle_name = models.CharField(max_length=40, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    callback_time = models.DateTimeField(blank=True, null=True)
    phone = models.CharField(max_length=20, blank=True, null=True)
    is_smart_phone = models.IntegerField()
    alt_phone = models.CharField(max_length=20, blank=True, null=True)
    email = models.CharField(max_length=254, blank=True, null=True)
    birth_date = models.DateField(blank=True, null=True)
    primary_occupation = models.CharField(max_length=255, blank=True, null=True)
    billing_address = models.CharField(max_length=150, blank=True, null=True)
    mailing_address = models.CharField(max_length=150, blank=True, null=True)
    shipping_address = models.CharField(max_length=150, blank=True, null=True)
    billing_city_state_zip = models.ForeignKey('CoreCitystatezip', models.DO_NOTHING, blank=True, null=True)
    created_by = models.ForeignKey('EntitlementApiuser', models.DO_NOTHING, blank=True, null=True)
    mailing_city_state_zip = models.ForeignKey('CoreCitystatezip', models.DO_NOTHING, blank=True, null=True)
    modified_by = models.ForeignKey('EntitlementApiuser', models.DO_NOTHING, blank=True, null=True)
    shipping_city_state_zip = models.ForeignKey('CoreCitystatezip', models.DO_NOTHING, blank=True, null=True)
    created_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'api_account'


class ApiAddon(models.Model):
    abstractproduct_ptr = models.ForeignKey(ApiAbstractproduct, models.DO_NOTHING, primary_key=True)
    category = models.ForeignKey('ApiAddoncategory', models.DO_NOTHING)
    core_plan_choice = models.ForeignKey('ApiSalesboardcategory', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'api_addon'


class ApiAddoncategory(models.Model):
    code = models.CharField(max_length=5)
    name = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'api_addoncategory'


class ApiAddongrade(models.Model):
    label = models.CharField(max_length=200)
    add_on_id = models.IntegerField()
    linked_addon_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'api_addongrade'


class ApiAddongradeplansizeprice(models.Model):
    plan_size = models.SmallIntegerField()
    hbc_commission = models.DecimalField(max_digits=10, decimal_places=4, blank=True, null=True)
    carrier_monthly_price = models.DecimalField(max_digits=10, decimal_places=4, blank=True, null=True)
    reference_price_value = models.DecimalField(max_digits=10, decimal_places=4, blank=True, null=True)
    min_reserve_fee = models.DecimalField(max_digits=10, decimal_places=4, blank=True, null=True)
    max_reserve_fee = models.DecimalField(max_digits=10, decimal_places=4, blank=True, null=True)
    add_on_grade = models.ForeignKey(ApiAddongrade, models.DO_NOTHING, blank=True, null=True)
    enrollment_fee = models.DecimalField(max_digits=10, decimal_places=4, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'api_addongradeplansizeprice'


class ApiAddonplansizeprice(models.Model):
    plan_size = models.SmallIntegerField()
    hbc_commission = models.DecimalField(max_digits=10, decimal_places=4, blank=True, null=True)
    carrier_monthly_price = models.DecimalField(max_digits=10, decimal_places=4, blank=True, null=True)
    reference_price_value = models.DecimalField(max_digits=10, decimal_places=4, blank=True, null=True)
    min_reserve_fee = models.DecimalField(max_digits=10, decimal_places=4, blank=True, null=True)
    max_reserve_fee = models.DecimalField(max_digits=10, decimal_places=4, blank=True, null=True)
    add_on_id = models.IntegerField(blank=True, null=True)
    enrollment_fee = models.DecimalField(max_digits=10, decimal_places=4, blank=True, null=True)
    hbc_commission_ef = models.DecimalField(max_digits=10, decimal_places=4, blank=True, null=True)
    commissionable_premium = models.DecimalField(max_digits=10, decimal_places=4, blank=True, null=True)
    non_commissionable_fee = models.DecimalField(max_digits=10, decimal_places=4, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'api_addonplansizeprice'


class ApiAddonstateavailability(models.Model):
    state = models.CharField(max_length=2)
    add_on = models.ForeignKey(ApiAddon, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'api_addonstateavailability'


class ApiAgentcarriercode(models.Model):
    carrier_code = models.CharField(max_length=50)
    alt_code = models.CharField(max_length=50, blank=True, null=True)
    agent = models.ForeignKey('CoreAgent', models.DO_NOTHING)
    carrier = models.ForeignKey('ApiCarrier', models.DO_NOTHING)
    carrier_link = models.CharField(max_length=50, blank=True, null=True)
    norvax_link = models.CharField(max_length=50, blank=True, null=True)
    rewrite_code = models.CharField(max_length=50, blank=True, null=True)
    rewrite_link = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'api_agentcarriercode'


class ApiAgentproductcommission(models.Model):
    ef_commission = models.DecimalField(max_digits=10, decimal_places=2)
    mp_commission = models.DecimalField(max_digits=10, decimal_places=2)
    agent = models.ForeignKey('CoreAgent', models.DO_NOTHING)
    product_id = models.IntegerField()
    plan_size = models.SmallIntegerField()

    class Meta:
        managed = False
        db_table = 'api_agentproductcommission'


class ApiAor(models.Model):
    rr_female = models.IntegerField()
    rr_male = models.IntegerField()
    agent = models.ForeignKey('CoreAgent', models.DO_NOTHING)
    product = models.ForeignKey(ApiAbstractproduct, models.DO_NOTHING)
    state = models.CharField(max_length=2)

    class Meta:
        managed = False
        db_table = 'api_aor'
        unique_together = (('product', 'agent', 'state'),)


class ApiAorindex(models.Model):
    index_female = models.SmallIntegerField()
    index_male = models.SmallIntegerField()
    product = models.ForeignKey(ApiAbstractproduct, models.DO_NOTHING)
    state = models.CharField(max_length=2)

    class Meta:
        managed = False
        db_table = 'api_aorindex'


class ApiBranchpaymentschedule(models.Model):
    start_period = models.SmallIntegerField()
    branch = models.ForeignKey('CoreBranch', models.DO_NOTHING)
    end_period_day_delta = models.SmallIntegerField()
    end_period_month_delta = models.SmallIntegerField()
    pay_date_day_delta = models.SmallIntegerField()
    pay_date_month_delta = models.SmallIntegerField()

    class Meta:
        managed = False
        db_table = 'api_branchpaymentschedule'


class ApiCarrier(models.Model):
    name = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'api_carrier'


class ApiCategory(models.Model):
    name = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'api_category'


class ApiCpastatus(models.Model):
    name = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'api_cpastatus'


class ApiCreditcard(models.Model):
    payment_ptr = models.ForeignKey('ApiPayment', models.DO_NOTHING, primary_key=True)
    cc_type = models.SmallIntegerField()
    number = models.CharField(max_length=50)
    expiration_date = models.CharField(max_length=5)
    cvv = models.CharField(max_length=55)
    address = models.CharField(max_length=50)
    address2 = models.CharField(max_length=50, blank=True, null=True)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=2)
    zip_code = models.CharField(max_length=10)

    class Meta:
        managed = False
        db_table = 'api_creditcard'


class ApiCreditcardviewlog(models.Model):
    access_time = models.DateTimeField()
    credit_card = models.ForeignKey(ApiCreditcard, models.DO_NOTHING)
    user = models.ForeignKey('EntitlementApiuser', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'api_creditcardviewlog'


class ApiDisposition(models.Model):
    name = models.CharField(max_length=64)
    code = models.CharField(max_length=64, blank=True, null=True)
    is_sale = models.IntegerField()
    boberdoo_name = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'api_disposition'


class ApiEcheck(models.Model):
    payment_ptr = models.ForeignKey('ApiPayment', models.DO_NOTHING, primary_key=True)
    bank_name = models.CharField(max_length=50)
    bank_location = models.CharField(max_length=50)
    routing_number = models.CharField(max_length=50)
    account_number = models.CharField(max_length=50)
    check_number = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'api_echeck'


class ApiEnrollment(models.Model):
    name = models.CharField(max_length=150)
    sale = models.ForeignKey('ApiSale', models.DO_NOTHING)
    aor = models.ForeignKey('CoreAgent', models.DO_NOTHING, blank=True, null=True)
    core_product = models.ForeignKey(ApiAbstractproduct, models.DO_NOTHING, blank=True, null=True)
    plan_size = models.SmallIntegerField()
    payment = models.ForeignKey('ApiPayment', models.DO_NOTHING, blank=True, null=True)
    package = models.ForeignKey('ApiPackage', models.DO_NOTHING, blank=True, null=True)
    is_verified = models.IntegerField()
    effective_date = models.DateField(blank=True, null=True)
    enrollment_date = models.DateField(blank=True, null=True)
    processed_by = models.ForeignKey('CoreAgent', models.DO_NOTHING, blank=True, null=True)
    processed_date = models.DateTimeField(blank=True, null=True)
    verified_by = models.ForeignKey('CoreAgent', models.DO_NOTHING, blank=True, null=True)
    verified_date = models.DateTimeField(blank=True, null=True)
    sale_product = models.ForeignKey('ApiSaleproduct', models.DO_NOTHING, blank=True, null=True)
    is_processed = models.IntegerField()
    verification_type = models.SmallIntegerField()

    class Meta:
        managed = False
        db_table = 'api_enrollment'


class ApiEnrollmentparticipant(models.Model):
    enrollment = models.ForeignKey(ApiEnrollment, models.DO_NOTHING)
    participant = models.ForeignKey('ApiParticipant', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'api_enrollmentparticipant'


class ApiEnrollmentproduct(models.Model):
    enrollment = models.ForeignKey(ApiEnrollment, models.DO_NOTHING)
    addon_product = models.ForeignKey(ApiAddon, models.DO_NOTHING, blank=True, null=True)
    sale_product = models.ForeignKey('ApiSaleproduct', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'api_enrollmentproduct'


class ApiEnrollmenttype(models.Model):
    name = models.CharField(max_length=100)
    verification_script = models.ForeignKey('ApiVerificationscript', models.DO_NOTHING)
    digital_enrollment_available = models.IntegerField()
    code = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'api_enrollmenttype'


class ApiEnrollmenttypecreditcardallow(models.Model):
    cc_type = models.SmallIntegerField()
    enrollment_type = models.ForeignKey(ApiEnrollmenttype, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'api_enrollmenttypecreditcardallow'


class ApiExcludeddid(models.Model):
    did = models.CharField(max_length=15)

    class Meta:
        managed = False
        db_table = 'api_excludeddid'


class ApiGetmedscrapinglog(models.Model):
    created_date = models.DateTimeField()
    last_modify_date = models.DateTimeField()
    member_id = models.CharField(unique=True, max_length=20)
    group_id = models.CharField(max_length=20)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=100)
    mi = models.CharField(max_length=1)
    date_of_birth = models.DateTimeField(blank=True, null=True)
    start_date = models.DateTimeField(blank=True, null=True)
    telephone1 = models.CharField(max_length=10, blank=True, null=True)
    telephone2 = models.CharField(max_length=10, blank=True, null=True)
    termination_date = models.DateTimeField(blank=True, null=True)
    effective_date = models.DateTimeField(blank=True, null=True)
    gender = models.CharField(max_length=1, blank=True, null=True)
    enrollment_status = models.CharField(max_length=20, blank=True, null=True)
    email = models.CharField(max_length=100, blank=True, null=True)
    ssn = models.CharField(max_length=9, blank=True, null=True)
    coverage_type = models.CharField(max_length=100, blank=True, null=True)
    marital_status = models.CharField(max_length=20, blank=True, null=True)
    address1 = models.CharField(max_length=50, blank=True, null=True)
    address2 = models.CharField(max_length=50, blank=True, null=True)
    city = models.CharField(max_length=40, blank=True, null=True)
    state = models.CharField(max_length=2, blank=True, null=True)
    zip = models.CharField(max_length=5, blank=True, null=True)
    previns = models.CharField(max_length=5, blank=True, null=True)
    external_uniqueid = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'api_getmedscrapinglog'


class ApiHealthcarescrapinglog(models.Model):
    created_date = models.DateTimeField()
    last_modify_date = models.DateTimeField()
    carrier_created_date = models.DateTimeField()
    phone = models.CharField(max_length=10, blank=True, null=True)
    full_name = models.CharField(max_length=100, blank=True, null=True)
    member_id = models.CharField(unique=True, max_length=20)
    termination_date = models.DateTimeField(blank=True, null=True)
    city = models.CharField(max_length=50, blank=True, null=True)
    state = models.CharField(max_length=10, blank=True, null=True)
    monthly_payment = models.CharField(max_length=10, blank=True, null=True)
    first_billing_date = models.CharField(max_length=10, blank=True, null=True)
    one_time = models.CharField(max_length=10, blank=True, null=True)
    policy = models.CharField(max_length=10, blank=True, null=True)
    email = models.CharField(max_length=100, blank=True, null=True)
    active = models.CharField(max_length=50, blank=True, null=True)
    next_billing_date = models.CharField(max_length=20, blank=True, null=True)
    hold = models.CharField(max_length=100, blank=True, null=True)
    product_name = models.CharField(max_length=50, blank=True, null=True)
    amount = models.CharField(max_length=50, blank=True, null=True)
    plan_size = models.CharField(max_length=50, blank=True, null=True)
    agent = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'api_healthcarescrapinglog'


class ApiHiicancellationfilelog(models.Model):
    file_name = models.CharField(max_length=100, blank=True, null=True)
    applicant_id = models.CharField(max_length=100, blank=True, null=True)
    first_name = models.CharField(max_length=100, blank=True, null=True)
    last_name = models.CharField(max_length=100, blank=True, null=True)
    gender = models.CharField(max_length=100, blank=True, null=True)
    dob = models.DateField(blank=True, null=True)
    address = models.CharField(max_length=100, blank=True, null=True)
    city = models.CharField(max_length=100, blank=True, null=True)
    zipcode = models.CharField(max_length=100, blank=True, null=True)
    state = models.CharField(max_length=100, blank=True, null=True)
    phone = models.CharField(max_length=100, blank=True, null=True)
    email = models.CharField(max_length=100, blank=True, null=True)
    member_id = models.CharField(max_length=100, blank=True, null=True)
    product_name = models.CharField(max_length=100, blank=True, null=True)
    application_date = models.DateField(blank=True, null=True)
    enrollment_date = models.DateField(blank=True, null=True)
    effective_date = models.DateField(blank=True, null=True)
    termination_date = models.DateField(blank=True, null=True)
    payment_status = models.CharField(max_length=100, blank=True, null=True)
    payment_status_date = models.CharField(max_length=100, blank=True, null=True)
    agent_first_name = models.CharField(max_length=100, blank=True, null=True)
    agent_last_name = models.CharField(max_length=100, blank=True, null=True)
    agent_code = models.CharField(max_length=100, blank=True, null=True)
    cancellation_code = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'api_hiicancellationfilelog'


class ApiHiienrollmentfilelog(models.Model):
    file_name = models.CharField(max_length=100, blank=True, null=True)
    applicant_id = models.CharField(max_length=100, blank=True, null=True)
    first_name = models.CharField(max_length=100, blank=True, null=True)
    last_name = models.CharField(max_length=100, blank=True, null=True)
    gender = models.CharField(max_length=100, blank=True, null=True)
    dob = models.DateField(blank=True, null=True)
    address = models.CharField(max_length=100, blank=True, null=True)
    city = models.CharField(max_length=100, blank=True, null=True)
    zipcode = models.CharField(max_length=100, blank=True, null=True)
    state = models.CharField(max_length=100, blank=True, null=True)
    phone = models.CharField(max_length=100, blank=True, null=True)
    email = models.CharField(max_length=100, blank=True, null=True)
    member_id = models.CharField(max_length=100, blank=True, null=True)
    product_name = models.CharField(max_length=100, blank=True, null=True)
    application_date = models.DateField(blank=True, null=True)
    enrollment_date = models.DateField(blank=True, null=True)
    effective_date = models.DateField(blank=True, null=True)
    termination_date = models.DateField(blank=True, null=True)
    payment_status = models.CharField(max_length=100, blank=True, null=True)
    payment_status_date = models.CharField(max_length=100, blank=True, null=True)
    agent_first_name = models.CharField(max_length=100, blank=True, null=True)
    agent_last_name = models.CharField(max_length=100, blank=True, null=True)
    agent_code = models.CharField(max_length=100, blank=True, null=True)
    verification_method = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'api_hiienrollmentfilelog'


class ApiHiirefundfilelog(models.Model):
    file_name = models.CharField(max_length=100, blank=True, null=True)
    applicant_id = models.CharField(max_length=100, blank=True, null=True)
    first_name = models.CharField(max_length=100, blank=True, null=True)
    last_name = models.CharField(max_length=100, blank=True, null=True)
    gender = models.CharField(max_length=100, blank=True, null=True)
    dob = models.DateField(blank=True, null=True)
    address = models.CharField(max_length=100, blank=True, null=True)
    city = models.CharField(max_length=100, blank=True, null=True)
    zipcode = models.CharField(max_length=100, blank=True, null=True)
    state = models.CharField(max_length=100, blank=True, null=True)
    phone = models.CharField(max_length=100, blank=True, null=True)
    email = models.CharField(max_length=100, blank=True, null=True)
    member_id = models.CharField(max_length=100, blank=True, null=True)
    product_name = models.CharField(max_length=100, blank=True, null=True)
    application_date = models.DateField(blank=True, null=True)
    enrollment_date = models.DateField(blank=True, null=True)
    effective_date = models.DateField(blank=True, null=True)
    termination_date = models.DateField(blank=True, null=True)
    payment_status = models.CharField(max_length=100, blank=True, null=True)
    payment_status_date = models.CharField(max_length=100, blank=True, null=True)
    agent_first_name = models.CharField(max_length=100, blank=True, null=True)
    agent_last_name = models.CharField(max_length=100, blank=True, null=True)
    agent_code = models.CharField(max_length=100, blank=True, null=True)
    refund_transaction_id = models.CharField(max_length=100, blank=True, null=True)
    corresponding_payment_transaction_id = models.CharField(max_length=100, blank=True, null=True)
    refund_amount = models.CharField(db_column='refund_Amount', max_length=100, blank=True, null=True)  # Field name made lowercase.
    cancellation_code = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'api_hiirefundfilelog'


class ApiHiitransactionfilelog(models.Model):
    file_name = models.CharField(max_length=100, blank=True, null=True)
    applicant_id = models.CharField(max_length=100, blank=True, null=True)
    first_name = models.CharField(max_length=100, blank=True, null=True)
    last_name = models.CharField(max_length=100, blank=True, null=True)
    gender = models.CharField(max_length=100, blank=True, null=True)
    dob = models.DateField(blank=True, null=True)
    address = models.CharField(max_length=100, blank=True, null=True)
    city = models.CharField(max_length=100, blank=True, null=True)
    zipcode = models.CharField(max_length=100, blank=True, null=True)
    state = models.CharField(max_length=100, blank=True, null=True)
    phone = models.CharField(max_length=100, blank=True, null=True)
    email = models.CharField(max_length=100, blank=True, null=True)
    member_id = models.CharField(max_length=100, blank=True, null=True)
    product_name = models.CharField(max_length=100, blank=True, null=True)
    application_date = models.DateField(blank=True, null=True)
    enrollment_date = models.DateField(blank=True, null=True)
    effective_date = models.DateField(blank=True, null=True)
    termination_date = models.DateField(blank=True, null=True)
    payment_status = models.CharField(max_length=100, blank=True, null=True)
    payment_status_date = models.CharField(max_length=100, blank=True, null=True)
    agent_first_name = models.CharField(max_length=100, blank=True, null=True)
    agent_last_name = models.CharField(max_length=100, blank=True, null=True)
    agent_code = models.CharField(max_length=100, blank=True, null=True)
    payment_transaction_id = models.CharField(max_length=100, blank=True, null=True)
    payment_transaction_amount = models.CharField(db_column='payment_transaction_Amount', max_length=100, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'api_hiitransactionfilelog'


class ApiLeadvendor(models.Model):
    company_name = models.CharField(max_length=100)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.CharField(max_length=254, blank=True, null=True)
    phone = models.CharField(max_length=20)
    provider_type = models.CharField(max_length=1)
    default_price_per_lead = models.DecimalField(max_digits=10, decimal_places=2)
    address = models.CharField(max_length=100)
    city_state_zip = models.ForeignKey('CoreCitystatezip', models.DO_NOTHING, blank=True, null=True)
    crm_part1_id = models.IntegerField(blank=True, null=True)
    active = models.IntegerField()
    affiliate_ref = models.CharField(max_length=10, blank=True, null=True)
    budget_profile = models.SmallIntegerField()
    counterpart = models.ForeignKey('self', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'api_leadvendor'


class ApiLeadvendordateprice(models.Model):
    date = models.DateField(blank=True, null=True)
    price_per_lead = models.DecimalField(max_digits=10, decimal_places=2)
    lead_vendor = models.ForeignKey(ApiLeadvendor, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'api_leadvendordateprice'


class ApiLink(models.Model):
    title = models.CharField(max_length=120)
    url = models.CharField(max_length=200)
    category = models.SmallIntegerField()
    index = models.SmallIntegerField()

    class Meta:
        managed = False
        db_table = 'api_link'


class ApiLinkbranch(models.Model):
    branch = models.ForeignKey('CoreBranch', models.DO_NOTHING)
    link = models.ForeignKey(ApiLink, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'api_linkbranch'


class ApiList(models.Model):
    name = models.CharField(max_length=100)
    created_date = models.DateTimeField(blank=True, null=True)
    active = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'api_list'


class ApiListLeadProvider(models.Model):
    list = models.ForeignKey(ApiList, models.DO_NOTHING)
    leadvendor = models.ForeignKey(ApiLeadvendor, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'api_list_lead_provider'
        unique_together = (('list', 'leadvendor'),)


class ApiNotecategory(models.Model):
    category = models.CharField(max_length=255)
    category_type = models.SmallIntegerField()

    class Meta:
        managed = False
        db_table = 'api_notecategory'


class ApiNotification(models.Model):
    created_date = models.DateTimeField(blank=True, null=True)
    phone = models.CharField(max_length=20)
    status = models.SmallIntegerField()
    agent = models.ForeignKey('CoreAgent', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'api_notification'


class ApiOpportunity(models.Model):
    vicidial_lead_id = models.IntegerField(blank=True, null=True)
    vicidial_list_id = models.IntegerField(blank=True, null=True)
    created_date = models.DateTimeField(blank=True, null=True)
    first_name = models.CharField(max_length=100, blank=True, null=True)
    last_name = models.CharField(max_length=100, blank=True, null=True)
    primary_email = models.CharField(max_length=254, blank=True, null=True)
    secondary_email = models.CharField(max_length=254, blank=True, null=True)
    phone = models.CharField(max_length=20, blank=True, null=True)
    mobile = models.CharField(max_length=20, blank=True, null=True)
    address = models.CharField(max_length=200, blank=True, null=True)
    address2 = models.CharField(max_length=200, blank=True, null=True)
    modified_date = models.DateTimeField(blank=True, null=True)
    sales_status = models.ForeignKey('ApiSalestatus', models.DO_NOTHING)
    verification_date = models.DateTimeField(blank=True, null=True)
    src = models.CharField(max_length=50, blank=True, null=True)
    landing_page = models.CharField(max_length=300, blank=True, null=True)
    ip_address = models.CharField(max_length=39, blank=True, null=True)
    external_id = models.CharField(max_length=50, blank=True, null=True)
    currently_insured = models.IntegerField()
    health_conditions = models.IntegerField()
    number_household = models.IntegerField(blank=True, null=True)
    income = models.IntegerField(blank=True, null=True)
    conditions = models.TextField(blank=True, null=True)
    contact_time = models.CharField(max_length=50, blank=True, null=True)
    medications = models.TextField(blank=True, null=True)
    notes = models.TextField(blank=True, null=True)
    city_state_zip = models.ForeignKey('CoreCitystatezip', models.DO_NOTHING, blank=True, null=True)
    lead = models.ForeignKey('MarketingLead', models.DO_NOTHING, blank=True, null=True)
    lead_vendor = models.ForeignKey(ApiLeadvendor, models.DO_NOTHING, blank=True, null=True)
    agent = models.ForeignKey('CoreAgent', models.DO_NOTHING)
    verification_status = models.ForeignKey('ApiVerificationstatus', models.DO_NOTHING)
    budget = models.IntegerField(blank=True, null=True)
    more_than_63days_uninsured = models.IntegerField()
    cost = models.DecimalField(max_digits=10, decimal_places=4, blank=True, null=True)
    disposition = models.ForeignKey(ApiDisposition, models.DO_NOTHING, blank=True, null=True)
    middle_initial = models.CharField(max_length=1, blank=True, null=True)
    eapp_name = models.CharField(max_length=100, blank=True, null=True)
    cpa_status = models.ForeignKey(ApiCpastatus, models.DO_NOTHING)
    current_insurance = models.CharField(max_length=50)
    plan_size = models.SmallIntegerField()
    state = models.CharField(max_length=2, blank=True, null=True)
    created_by = models.SmallIntegerField()
    universal_lead_id = models.CharField(max_length=40, blank=True, null=True)
    sale_date = models.DateTimeField(blank=True, null=True)
    lead_created_date = models.DateTimeField(blank=True, null=True)
    eapp_submitted = models.IntegerField()
    cluster = models.ForeignKey('CoreCluster', models.DO_NOTHING, blank=True, null=True)
    boberdoo_lead_type = models.IntegerField(blank=True, null=True)
    contact_address = models.CharField(max_length=200, blank=True, null=True)
    contact_address2 = models.CharField(max_length=200, blank=True, null=True)
    contact_city_state_zip = models.ForeignKey('CoreCitystatezip', models.DO_NOTHING, blank=True, null=True)
    mailing_address = models.CharField(max_length=200, blank=True, null=True)
    mailing_address2 = models.CharField(max_length=200, blank=True, null=True)
    mailing_city_state_zip_id = models.IntegerField(blank=True, null=True)
    callback_time = models.DateTimeField(blank=True, null=True)
    created_date_only = models.DateField(blank=True, null=True)
    first_call_duration = models.IntegerField(blank=True, null=True)
    first_lead_status = models.ForeignKey('MarketingStatus', models.DO_NOTHING, blank=True, null=True)
    quick_note = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'api_opportunity'
        unique_together = (('phone', 'vicidial_list_id', 'created_date_only'),)


class ApiOpportunityDependants(models.Model):
    opportunity = models.ForeignKey(ApiOpportunity, models.DO_NOTHING)
    opportunitydependant = models.ForeignKey('ApiOpportunitydependant', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'api_opportunity_dependants'
        unique_together = (('opportunity', 'opportunitydependant'),)


class ApiOpportunitydependant(models.Model):
    relation = models.SmallIntegerField()
    opportunity = models.ForeignKey(ApiOpportunity, models.DO_NOTHING)
    participant = models.ForeignKey('ApiParticipant', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'api_opportunitydependant'


class ApiOpportunityvicileadlog(models.Model):
    vicidial_lead_id = models.IntegerField()
    log_date = models.DateTimeField()
    cluster = models.ForeignKey('CoreCluster', models.DO_NOTHING)
    opportunity = models.ForeignKey(ApiOpportunity, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'api_opportunityvicileadlog'


class ApiPackage(models.Model):
    description = models.TextField()
    active = models.IntegerField()
    product = models.ForeignKey('ApiProduct', models.DO_NOTHING, blank=True, null=True)
    sale_name = models.TextField(blank=True, null=True)
    verification_name = models.TextField(blank=True, null=True)
    max_age = models.SmallIntegerField()
    min_age = models.SmallIntegerField()

    class Meta:
        managed = False
        db_table = 'api_package'


class ApiPackageaddon(models.Model):
    required = models.IntegerField()
    default_to_display = models.IntegerField()
    upgradable = models.IntegerField()
    add_on = models.ForeignKey(ApiAddon, models.DO_NOTHING)
    package = models.ForeignKey(ApiPackage, models.DO_NOTHING)
    enrollment_type = models.SmallIntegerField()
    visible = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'api_packageaddon'


class ApiPackagebranchavailability(models.Model):
    branch = models.ForeignKey('CoreBranch', models.DO_NOTHING)
    package = models.ForeignKey(ApiPackage, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'api_packagebranchavailability'


class ApiPackageplansizeavailability(models.Model):
    plan = models.SmallIntegerField()
    package = models.ForeignKey(ApiPackage, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'api_packageplansizeavailability'


class ApiPackagestateavailability(models.Model):
    state = models.CharField(max_length=2)
    package = models.ForeignKey(ApiPackage, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'api_packagestateavailability'


class ApiParticipant(models.Model):
    first_name = models.CharField(max_length=50, blank=True, null=True)
    last_name = models.CharField(max_length=50, blank=True, null=True)
    middle_initial = models.CharField(max_length=1, blank=True, null=True)
    birth_date = models.DateField(blank=True, null=True)
    gender = models.CharField(max_length=1, blank=True, null=True)
    height_feet = models.IntegerField(blank=True, null=True)
    height_inches = models.IntegerField(blank=True, null=True)
    weight = models.IntegerField(blank=True, null=True)
    acc_cer = models.IntegerField()
    al_dr = models.IntegerField()
    als = models.IntegerField()
    alz = models.IntegerField()
    art_d = models.IntegerField()
    asmt = models.IntegerField()
    bip = models.IntegerField()
    bon_d = models.IntegerField()
    brain_syndrome = models.IntegerField()
    cholesterol = models.IntegerField()
    crohn_d = models.IntegerField()
    cu_in = models.TextField(blank=True, null=True)
    cu_inra = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    de_in = models.TextField(blank=True, null=True)
    depression = models.IntegerField()
    dr_vis = models.IntegerField(blank=True, null=True)
    emphysema = models.IntegerField()
    fibromyalgia = models.IntegerField()
    heart_attack = models.IntegerField()
    hepatitis = models.IntegerField()
    hypertension = models.IntegerField()
    in_ch = models.TextField(blank=True, null=True)
    ins_asp = models.TextField(blank=True, null=True)
    insulin_dependent = models.IntegerField()
    internal_cancer = models.IntegerField()
    isc_att = models.IntegerField()
    kidney_disease = models.IntegerField()
    liver_disease = models.IntegerField()
    lupus = models.IntegerField()
    med_ty = models.TextField(blank=True, null=True)
    melanoma_cancer = models.IntegerField()
    multiple_sclerosis = models.IntegerField()
    muscle_disease = models.IntegerField()
    muscle_dysthophy = models.IntegerField()
    myositis = models.IntegerField()
    nu_med = models.IntegerField(blank=True, null=True)
    obs_lung = models.IntegerField()
    obs_pul = models.IntegerField()
    organ_failure = models.IntegerField()
    organ_transplant = models.IntegerField()
    osteoporosis = models.IntegerField()
    oth = models.IntegerField()
    paralysis = models.IntegerField()
    peripheral_vascular_disease = models.IntegerField()
    pregnant = models.IntegerField()
    reas_in = models.TextField(blank=True, null=True)
    rheumatoid_arthritis = models.IntegerField()
    senile_dementia = models.IntegerField()
    sho_ar = models.TextField(blank=True, null=True)
    smoker = models.IntegerField()
    ssno = models.CharField(max_length=11, blank=True, null=True)
    st_dt = models.DateField(blank=True, null=True)
    stroke = models.IntegerField()
    substance_abuse = models.IntegerField()
    thyr = models.IntegerField()
    ulcerative_colitis = models.IntegerField()
    uni_le = models.TextField(blank=True, null=True)
    occupation = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'api_participant'


class ApiPayment(models.Model):
    name = models.CharField(max_length=50)
    sale = models.ForeignKey('ApiSale', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'api_payment'


class ApiPaymentlog(models.Model):
    pay_period = models.CharField(max_length=10)
    report_run_date = models.DateTimeField()
    report_file = models.CharField(max_length=100)
    branch = models.ForeignKey('CoreBranch', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'api_paymentlog'


class ApiPlanchoice(models.Model):
    name = models.CharField(max_length=50)
    plan_type = models.ForeignKey('ApiPlantype', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'api_planchoice'


class ApiPlantype(models.Model):
    name = models.CharField(max_length=50)
    product_type = models.ForeignKey('ApiProducttype', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'api_plantype'


class ApiProduct(models.Model):
    abstractproduct_ptr = models.ForeignKey(ApiAbstractproduct, models.DO_NOTHING, primary_key=True)
    plan_choice = models.ForeignKey(ApiPlanchoice, models.DO_NOTHING)
    term = models.SmallIntegerField()

    class Meta:
        managed = False
        db_table = 'api_product'


class ApiProductplansizeprice(models.Model):
    plan_size = models.SmallIntegerField()
    hbc_commission = models.DecimalField(max_digits=10, decimal_places=4, blank=True, null=True)
    carrier_monthly_price = models.DecimalField(max_digits=10, decimal_places=4, blank=True, null=True)
    reference_price_value = models.DecimalField(max_digits=10, decimal_places=4, blank=True, null=True)
    min_reserve_fee = models.DecimalField(max_digits=10, decimal_places=4, blank=True, null=True)
    max_reserve_fee = models.DecimalField(max_digits=10, decimal_places=4, blank=True, null=True)
    product = models.ForeignKey(ApiProduct, models.DO_NOTHING, blank=True, null=True)
    enrollment_fee = models.DecimalField(max_digits=10, decimal_places=4, blank=True, null=True)
    hbc_commission_ef = models.DecimalField(max_digits=10, decimal_places=4, blank=True, null=True)
    commissionable_premium = models.DecimalField(max_digits=10, decimal_places=4, blank=True, null=True)
    non_commissionable_fee = models.DecimalField(max_digits=10, decimal_places=4, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'api_productplansizeprice'


class ApiProductstateavailability(models.Model):
    state = models.CharField(max_length=2)
    product = models.ForeignKey(ApiProduct, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'api_productstateavailability'


class ApiProducttype(models.Model):
    name = models.CharField(max_length=50)
    code = models.CharField(max_length=2)
    visible_in_calculator = models.IntegerField()
    order_in_calculator = models.SmallIntegerField()

    class Meta:
        managed = False
        db_table = 'api_producttype'


class ApiProfileproductcommission(models.Model):
    ef_commission = models.DecimalField(max_digits=10, decimal_places=2)
    mp_commission = models.DecimalField(max_digits=10, decimal_places=2)
    product = models.ForeignKey(ApiAbstractproduct, models.DO_NOTHING)
    profile = models.ForeignKey('CoreProfile', models.DO_NOTHING)
    plan_size = models.SmallIntegerField()

    class Meta:
        managed = False
        db_table = 'api_profileproductcommission'


class ApiQuickreminder(models.Model):
    note = models.TextField()

    class Meta:
        managed = False
        db_table = 'api_quickreminder'


class ApiRunningtotalcategory(models.Model):
    behavior = models.SmallIntegerField()
    start_date = models.IntegerField()
    end_date = models.CharField(max_length=50)
    delta_date = models.IntegerField()
    category = models.ForeignKey(ApiCategory, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'api_runningtotalcategory'


class ApiSale(models.Model):
    plan_size = models.SmallIntegerField()
    state = models.CharField(max_length=2)
    created_date = models.DateTimeField(blank=True, null=True)
    modified_date = models.DateTimeField(blank=True, null=True)
    sale_date = models.DateTimeField(blank=True, null=True)
    created_by = models.SmallIntegerField()
    first_name = models.CharField(max_length=100, blank=True, null=True)
    last_name = models.CharField(max_length=100, blank=True, null=True)
    middle_initial = models.CharField(max_length=1, blank=True, null=True)
    primary_email = models.CharField(max_length=254, blank=True, null=True)
    secondary_email = models.CharField(max_length=254, blank=True, null=True)
    phone = models.CharField(max_length=20, blank=True, null=True)
    mobile = models.CharField(max_length=20, blank=True, null=True)
    address = models.CharField(max_length=200, blank=True, null=True)
    address2 = models.CharField(max_length=200, blank=True, null=True)
    mailing_address = models.CharField(max_length=200, blank=True, null=True)
    mailing_address2 = models.CharField(max_length=200, blank=True, null=True)
    contact_address = models.CharField(max_length=200, blank=True, null=True)
    contact_address2 = models.CharField(max_length=200, blank=True, null=True)
    verification_date = models.DateTimeField(blank=True, null=True)
    currently_insured = models.IntegerField()
    current_insurance = models.CharField(max_length=50)
    health_conditions = models.IntegerField()
    number_household = models.IntegerField(blank=True, null=True)
    income = models.IntegerField(blank=True, null=True)
    conditions = models.TextField(blank=True, null=True)
    contact_time = models.CharField(max_length=50, blank=True, null=True)
    medications = models.TextField(blank=True, null=True)
    more_than_63days_uninsured = models.IntegerField()
    budget = models.IntegerField(blank=True, null=True)
    notes = models.TextField(blank=True, null=True)
    effective_date = models.DateField(blank=True, null=True)
    enrollment_date = models.DateField(blank=True, null=True)
    quick_remainder = models.TextField(blank=True, null=True)
    agent = models.ForeignKey('CoreAgent', models.DO_NOTHING)
    city_state_zip = models.ForeignKey('CoreCitystatezip', models.DO_NOTHING, blank=True, null=True)
    contact_city_state_zip = models.ForeignKey('CoreCitystatezip', models.DO_NOTHING, blank=True, null=True)
    cpa_status = models.ForeignKey(ApiCpastatus, models.DO_NOTHING)
    disposition = models.ForeignKey(ApiDisposition, models.DO_NOTHING, blank=True, null=True)
    mailing_city_state_zip = models.ForeignKey('CoreCitystatezip', models.DO_NOTHING, blank=True, null=True)
    opportunity = models.ForeignKey(ApiOpportunity, models.DO_NOTHING)
    sales_status = models.ForeignKey('ApiSalestatus', models.DO_NOTHING)
    verification_status = models.ForeignKey('ApiVerificationstatus', models.DO_NOTHING)
    processed_date = models.DateTimeField(blank=True, null=True)
    account = models.ForeignKey(ApiAccount, models.DO_NOTHING, blank=True, null=True)
    created_date_only = models.DateField(blank=True, null=True)
    first_lead_status = models.ForeignKey('MarketingStatus', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'api_sale'


class ApiSaledependant(models.Model):
    relation = models.SmallIntegerField()
    participant = models.ForeignKey(ApiParticipant, models.DO_NOTHING)
    sale = models.ForeignKey(ApiSale, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'api_saledependant'


class ApiSaledetaildependant(models.Model):
    relation = models.SmallIntegerField()
    participant = models.ForeignKey(ApiParticipant, models.DO_NOTHING)
    sale_product = models.ForeignKey('ApiSaleproduct', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'api_saledetaildependant'


class ApiSalenote(models.Model):
    note = models.TextField()
    created_date = models.DateTimeField(blank=True, null=True)
    created_by = models.ForeignKey('CoreAgent', models.DO_NOTHING, blank=True, null=True)
    sale = models.ForeignKey(ApiSale, models.DO_NOTHING)
    category = models.ForeignKey(ApiNotecategory, models.DO_NOTHING, blank=True, null=True)
    created_at = models.SmallIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'api_salenote'


class ApiSalepackage(models.Model):
    add_on = models.ForeignKey(ApiAddon, models.DO_NOTHING, blank=True, null=True)
    add_on_grade = models.ForeignKey(ApiAddongrade, models.DO_NOTHING, blank=True, null=True)
    package = models.ForeignKey(ApiPackage, models.DO_NOTHING)
    product = models.ForeignKey(ApiProduct, models.DO_NOTHING, blank=True, null=True)
    sale = models.ForeignKey(ApiSale, models.DO_NOTHING)
    plan_size = models.SmallIntegerField()
    enrollment_type = models.SmallIntegerField()

    class Meta:
        managed = False
        db_table = 'api_salepackage'


class ApiSaleproduct(models.Model):
    effective_date = models.DateField(blank=True, null=True)
    enrollment_date = models.DateField(blank=True, null=True)
    policy_number = models.CharField(max_length=32, blank=True, null=True)
    termination_date = models.DateField(blank=True, null=True)
    product = models.ForeignKey(ApiAbstractproduct, models.DO_NOTHING)
    sale = models.ForeignKey(ApiSale, models.DO_NOTHING)
    carrier_match = models.IntegerField()
    charged_back_date = models.DateField(blank=True, null=True)
    description = models.TextField()
    is_product_active = models.IntegerField()
    months_in_advance = models.SmallIntegerField()
    payment_date = models.DateField(blank=True, null=True)
    payment_status = models.SmallIntegerField()
    charged_back_log = models.ForeignKey(ApiPaymentlog, models.DO_NOTHING, blank=True, null=True)
    payment_log = models.ForeignKey(ApiPaymentlog, models.DO_NOTHING, blank=True, null=True)
    termination_log = models.ForeignKey(ApiPaymentlog, models.DO_NOTHING, blank=True, null=True)
    allowance_field = models.CharField(max_length=30)
    allowance_type = models.SmallIntegerField()
    allowance_value = models.IntegerField()
    agent_commission = models.DecimalField(max_digits=10, decimal_places=4, blank=True, null=True)
    hbc_commission = models.DecimalField(max_digits=10, decimal_places=4, blank=True, null=True)
    monthly_price = models.DecimalField(max_digits=10, decimal_places=4, blank=True, null=True)
    agent = models.ForeignKey('CoreAgent', models.DO_NOTHING, blank=True, null=True)
    sales_status = models.ForeignKey('ApiSalestatus', models.DO_NOTHING)
    enrollment_fee = models.DecimalField(max_digits=10, decimal_places=4, blank=True, null=True)
    max_reserve_fee = models.DecimalField(max_digits=10, decimal_places=4, blank=True, null=True)
    miscellaneous_fee = models.DecimalField(max_digits=10, decimal_places=4, blank=True, null=True)
    min_reserve_fee = models.DecimalField(max_digits=10, decimal_places=4, blank=True, null=True)
    reference_price_value = models.DecimalField(max_digits=10, decimal_places=4, blank=True, null=True)
    category = models.ForeignKey(ApiCategory, models.DO_NOTHING, blank=True, null=True)
    micellaneas_fee = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    aor = models.ForeignKey('CoreAgent', models.DO_NOTHING, blank=True, null=True)
    enrollment = models.ForeignKey(ApiEnrollment, models.DO_NOTHING, blank=True, null=True)
    advancing_fee = models.DecimalField(max_digits=10, decimal_places=4, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'api_saleproduct'


class ApiSaleproducttypeparticipant(models.Model):
    participant = models.ForeignKey(ApiParticipant, models.DO_NOTHING)
    product_type = models.ForeignKey(ApiProducttype, models.DO_NOTHING)
    sale = models.ForeignKey(ApiSale, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'api_saleproducttypeparticipant'


class ApiSalesboardagentweek(models.Model):
    week_index = models.DecimalField(max_digits=5, decimal_places=2)
    time_shift = models.CharField(max_length=1)
    week_start_date = models.DateField()
    sunday = models.IntegerField()
    monday = models.IntegerField()
    tuesday = models.IntegerField()
    wednesday = models.IntegerField()
    thursday = models.IntegerField()
    friday = models.IntegerField()
    saturday = models.IntegerField()
    agent = models.ForeignKey('CoreAgent', models.DO_NOTHING)
    branch = models.ForeignKey('CoreBranch', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'api_salesboardagentweek'


class ApiSalesboardcategory(models.Model):
    name = models.CharField(max_length=100)
    color = models.CharField(max_length=10)
    show_in_salesboard = models.IntegerField()
    cc_effective_date = models.CharField(max_length=10)
    e_check_effective_date = models.CharField(max_length=10)
    effective_date_behavior = models.SmallIntegerField()

    class Meta:
        managed = False
        db_table = 'api_salesboardcategory'


class ApiSalesboardweekconfiguration(models.Model):
    time_shift = models.CharField(max_length=1)
    week_start_date = models.DateField()
    sunday_goal = models.DecimalField(max_digits=10, decimal_places=2)
    monday_goal = models.DecimalField(max_digits=10, decimal_places=2)
    tuesday_goal = models.DecimalField(max_digits=10, decimal_places=2)
    wednesday_goal = models.DecimalField(max_digits=10, decimal_places=2)
    thursday_goal = models.DecimalField(max_digits=10, decimal_places=2)
    friday_goal = models.DecimalField(max_digits=10, decimal_places=2)
    saturday_goal = models.DecimalField(max_digits=10, decimal_places=2)
    branch = models.ForeignKey('CoreBranch', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'api_salesboardweekconfiguration'
        unique_together = (('branch', 'time_shift', 'week_start_date'),)


class ApiSalestatus(models.Model):
    name = models.CharField(max_length=30)

    class Meta:
        managed = False
        db_table = 'api_salestatus'


class ApiSalestmproduct(models.Model):
    price = models.DecimalField(max_digits=10, decimal_places=2)
    tax = models.DecimalField(max_digits=10, decimal_places=2)
    product = models.ForeignKey(ApiAbstractproduct, models.DO_NOTHING)
    sale = models.ForeignKey(ApiSale, models.DO_NOTHING)
    deductible = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        managed = False
        db_table = 'api_salestmproduct'


class ApiUnifiedscrapinglog(models.Model):
    created_date = models.DateTimeField()
    last_modify_date = models.DateTimeField()
    internal_id = models.CharField(max_length=40, blank=True, null=True)
    category = models.CharField(max_length=40, blank=True, null=True)
    pay_type = models.CharField(max_length=30, blank=True, null=True)
    inactive_reason = models.CharField(max_length=100, blank=True, null=True)
    system_id = models.CharField(max_length=40, blank=True, null=True)
    department = models.CharField(max_length=40, blank=True, null=True)
    contract_number = models.CharField(max_length=40, blank=True, null=True)
    probability = models.CharField(max_length=40, blank=True, null=True)
    fax = models.CharField(max_length=40, blank=True, null=True)
    agent_code_2 = models.CharField(max_length=40, blank=True, null=True)
    product_code = models.CharField(max_length=40, blank=True, null=True)
    company_name = models.CharField(max_length=40, blank=True, null=True)
    member_id = models.CharField(max_length=15, blank=True, null=True)
    other_address2 = models.CharField(max_length=50, blank=True, null=True)
    product_call_status = models.CharField(max_length=100, blank=True, null=True)
    assigned_agents = models.CharField(max_length=100, blank=True, null=True)
    address = models.CharField(max_length=100, blank=True, null=True)
    no_calls = models.CharField(max_length=50, blank=True, null=True)
    last_payment = models.CharField(max_length=40, blank=True, null=True)
    position = models.CharField(max_length=40, blank=True, null=True)
    administration_fee = models.CharField(max_length=5, blank=True, null=True)
    agent_label = models.CharField(max_length=40, blank=True, null=True)
    fax_ext = models.CharField(max_length=40, blank=True, null=True)
    product_agent_id = models.CharField(max_length=40, blank=True, null=True)
    phone_2_ext = models.CharField(max_length=40, blank=True, null=True)
    other_city = models.CharField(max_length=40, blank=True, null=True)
    disability = models.CharField(max_length=40, blank=True, null=True)
    zipcode = models.CharField(max_length=15, blank=True, null=True)
    renewal_date = models.CharField(max_length=40, blank=True, null=True)
    source = models.CharField(max_length=40, blank=True, null=True)
    state = models.CharField(max_length=2, blank=True, null=True)
    next_step_date = models.CharField(max_length=40, blank=True, null=True)
    product_estimated_close_date = models.CharField(max_length=20, blank=True, null=True)
    type = models.CharField(max_length=40, blank=True, null=True)
    email = models.CharField(max_length=50, blank=True, null=True)
    product_source = models.CharField(max_length=40, blank=True, null=True)
    phone_1_ext = models.CharField(max_length=20, blank=True, null=True)
    username = models.CharField(max_length=50, blank=True, null=True)
    other_address = models.CharField(max_length=100, blank=True, null=True)
    gender = models.CharField(max_length=5, blank=True, null=True)
    stage = models.CharField(max_length=50, blank=True, null=True)
    refund_requested_date = models.CharField(max_length=50, blank=True, null=True)
    refund_requested = models.CharField(max_length=50, blank=True, null=True)
    source_detail = models.CharField(max_length=50, blank=True, null=True)
    refund_provided_date = models.CharField(max_length=50, blank=True, null=True)
    product_status = models.CharField(max_length=50, blank=True, null=True)
    weight = models.CharField(max_length=5, blank=True, null=True)
    product_next_step = models.CharField(max_length=20, blank=True, null=True)
    last_name = models.CharField(max_length=50, blank=True, null=True)
    product_source_detail = models.CharField(max_length=100, blank=True, null=True)
    product_number_calls = models.CharField(max_length=5, blank=True, null=True)
    ssn = models.CharField(max_length=12, blank=True, null=True)
    note_date = models.CharField(max_length=45, blank=True, null=True)
    product_stage = models.CharField(max_length=45, blank=True, null=True)
    hold_return = models.CharField(max_length=45, blank=True, null=True)
    tpv_date = models.CharField(max_length=45, blank=True, null=True)
    phone_3 = models.CharField(max_length=15, blank=True, null=True)
    phone_2 = models.CharField(max_length=15, blank=True, null=True)
    phone_1 = models.CharField(max_length=15, blank=True, null=True)
    dob = models.CharField(max_length=15, blank=True, null=True)
    product_benefit = models.CharField(max_length=45, blank=True, null=True)
    next_step = models.CharField(max_length=45, blank=True, null=True)
    fulfillment_date = models.CharField(max_length=45, blank=True, null=True)
    status = models.CharField(max_length=45, blank=True, null=True)
    referral = models.CharField(max_length=45, blank=True, null=True)
    best_call_time = models.CharField(max_length=45, blank=True, null=True)
    permanent_bill_day = models.CharField(max_length=45, blank=True, null=True)
    address2 = models.CharField(max_length=55, blank=True, null=True)
    enroller_label = models.CharField(max_length=45, blank=True, null=True)
    paid = models.CharField(max_length=45, blank=True, null=True)
    product_next_step_date = models.CharField(max_length=45, blank=True, null=True)
    do_not_call = models.CharField(max_length=45, blank=True, null=True)
    underwriter = models.CharField(max_length=45, blank=True, null=True)
    product_created_date = models.CharField(max_length=45, blank=True, null=True)
    member_created_date = models.CharField(max_length=45, blank=True, null=True)
    language = models.CharField(max_length=45, blank=True, null=True)
    email_3 = models.CharField(max_length=45, blank=True, null=True)
    hold_reason = models.CharField(max_length=45, blank=True, null=True)
    quantity = models.CharField(max_length=45, blank=True, null=True)
    code = models.CharField(max_length=45, blank=True, null=True)
    period_label = models.CharField(max_length=45, blank=True, null=True)
    category_3 = models.CharField(max_length=45, blank=True, null=True)
    enroller_id = models.CharField(max_length=45, blank=True, null=True)
    height = models.CharField(max_length=10, blank=True, null=True)
    county = models.CharField(max_length=45, blank=True, null=True)
    agent_id = models.CharField(max_length=45, blank=True, null=True)
    product_agent_label = models.CharField(max_length=45, blank=True, null=True)
    agent_code = models.CharField(max_length=45, blank=True, null=True)
    active_date = models.CharField(max_length=45, blank=True, null=True)
    next_billing_date = models.CharField(max_length=45, blank=True, null=True)
    prospect_lead = models.CharField(max_length=45, blank=True, null=True)
    contract_length = models.CharField(max_length=45, blank=True, null=True)
    hold_amount = models.CharField(max_length=45, blank=True, null=True)
    ethnicity = models.CharField(max_length=45, blank=True, null=True)
    city = models.CharField(max_length=45, blank=True, null=True)
    product_fee = models.CharField(max_length=25, blank=True, null=True)
    sale_date = models.CharField(max_length=45, blank=True, null=True)
    refund_provided = models.CharField(max_length=45, blank=True, null=True)
    type_2 = models.CharField(max_length=45, blank=True, null=True)
    tpv_code = models.CharField(max_length=45, blank=True, null=True)
    first_name = models.CharField(max_length=45, blank=True, null=True)
    other_state = models.CharField(max_length=45, blank=True, null=True)
    category_4 = models.CharField(max_length=45, blank=True, null=True)
    call_status = models.CharField(max_length=45, blank=True, null=True)
    division = models.CharField(max_length=45, blank=True, null=True)
    product_id = models.CharField(max_length=45, blank=True, null=True)
    refund_comment = models.CharField(max_length=45, blank=True, null=True)
    password = models.CharField(max_length=45, blank=True, null=True)
    email_opt_out = models.CharField(max_length=45, blank=True, null=True)
    inactive_date = models.CharField(max_length=45, blank=True, null=True)
    other_zipcode = models.CharField(max_length=45, blank=True, null=True)
    country = models.CharField(max_length=25, blank=True, null=True)
    next_billing_amount = models.CharField(max_length=25, blank=True, null=True)
    hold_date = models.CharField(max_length=45, blank=True, null=True)
    first_billing_date = models.CharField(max_length=45, blank=True, null=True)
    drivers_license = models.CharField(max_length=45, blank=True, null=True)
    email2 = models.CharField(max_length=45, blank=True, null=True)
    termination_date = models.DateTimeField(blank=True, null=True)
    enrollment_fee = models.CharField(max_length=5, blank=True, null=True)
    product_label = models.CharField(max_length=35, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'api_unifiedscrapinglog'


class ApiVendordid(models.Model):
    did = models.CharField(max_length=15)
    lead_vendor = models.ForeignKey(ApiLeadvendor, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'api_vendordid'


class ApiVerificationscript(models.Model):
    name = models.CharField(max_length=255)
    introduction_code = models.TextField(blank=True, null=True)
    verification_code = models.TextField(blank=True, null=True)
    initialization_code = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'api_verificationscript'


class ApiVerificationscriptsetting(models.Model):
    name = models.CharField(max_length=255)
    value = models.TextField()

    class Meta:
        managed = False
        db_table = 'api_verificationscriptsetting'


class ApiVerificationstatus(models.Model):
    name = models.CharField(max_length=30)

    class Meta:
        managed = False
        db_table = 'api_verificationstatus'


class ApiVicitrack(models.Model):
    lead_id = models.IntegerField()
    action = models.CharField(max_length=50)
    action_time = models.DateTimeField()
    cluster = models.ForeignKey('CoreCluster', models.DO_NOTHING)
    agent_name = models.CharField(max_length=25, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'api_vicitrack'


class ApiWpascrapinglog(models.Model):
    created_date = models.DateTimeField()
    last_modify_date = models.DateTimeField()
    carrier_created_date = models.DateTimeField()
    last_transaction_status = models.CharField(max_length=100, blank=True, null=True)
    address = models.CharField(max_length=100, blank=True, null=True)
    city = models.CharField(max_length=50, blank=True, null=True)
    state = models.CharField(max_length=10, blank=True, null=True)
    phone = models.CharField(max_length=10, blank=True, null=True)
    full_name = models.CharField(max_length=100, blank=True, null=True)
    member_id = models.CharField(unique=True, max_length=20)
    termination_date = models.DateTimeField(blank=True, null=True)
    status = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'api_wpascrapinglog'


class AuditlogLogentry(models.Model):
    object_pk = models.CharField(max_length=255)
    object_id = models.BigIntegerField(blank=True, null=True)
    object_repr = models.TextField()
    action = models.SmallIntegerField()
    changes = models.TextField()
    timestamp = models.DateTimeField()
    actor = models.ForeignKey('EntitlementApiuser', models.DO_NOTHING, blank=True, null=True)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    remote_addr = models.CharField(max_length=39, blank=True, null=True)
    additional_data = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'auditlog_logentry'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=80)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class CallCenterBannedareacode(models.Model):
    code = models.CharField(unique=True, max_length=5)
    provider = models.ForeignKey('CallCenterLeadprovider', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'call_center_bannedareacode'
        unique_together = (('provider', 'code'),)


class CallCenterBannedemail(models.Model):
    email = models.CharField(unique=True, max_length=200)
    provider = models.ForeignKey('CallCenterLeadprovider', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'call_center_bannedemail'
        unique_together = (('provider', 'email'),)


class CallCenterBannedfirstname(models.Model):
    first_name = models.CharField(max_length=100)
    provider = models.ForeignKey('CallCenterLeadprovider', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'call_center_bannedfirstname'
        unique_together = (('provider', 'first_name'),)


class CallCenterBannedfullname(models.Model):
    fullname = models.CharField(unique=True, max_length=200)
    provider = models.ForeignKey('CallCenterLeadprovider', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'call_center_bannedfullname'
        unique_together = (('provider', 'fullname'),)


class CallCenterBannedlastname(models.Model):
    last_name = models.CharField(unique=True, max_length=100)
    provider = models.ForeignKey('CallCenterLeadprovider', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'call_center_bannedlastname'
        unique_together = (('provider', 'last_name'),)


class CallCenterBannedphone(models.Model):
    phone = models.CharField(unique=True, max_length=50)
    provider = models.ForeignKey('CallCenterLeadprovider', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'call_center_bannedphone'
        unique_together = (('provider', 'phone'),)


class CallCenterBannedstreet(models.Model):
    street = models.CharField(unique=True, max_length=250)
    provider = models.ForeignKey('CallCenterLeadprovider', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'call_center_bannedstreet'
        unique_together = (('provider', 'street'),)


class CallCenterCustomer(models.Model):
    code = models.CharField(max_length=10)
    name = models.CharField(max_length=50)
    index = models.SmallIntegerField()
    method = models.SmallIntegerField()
    format = models.SmallIntegerField()
    url = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'call_center_customer'


class CallCenterCustomerfieldmatch(models.Model):
    customer_field = models.CharField(max_length=50)
    sil_expression_type = models.SmallIntegerField()
    sil_expression = models.CharField(max_length=50)
    customer = models.ForeignKey(CallCenterCustomer, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'call_center_customerfieldmatch'


class CallCenterLead(models.Model):
    phone = models.CharField(max_length=15)
    first_name = models.CharField(max_length=50, blank=True, null=True)
    last_name = models.CharField(max_length=50, blank=True, null=True)
    email1 = models.CharField(max_length=254, blank=True, null=True)
    address = models.CharField(max_length=100, blank=True, null=True)
    address2 = models.CharField(max_length=100, blank=True, null=True)
    city = models.CharField(max_length=50, blank=True, null=True)
    state = models.CharField(max_length=2, blank=True, null=True)
    dob = models.DateField(blank=True, null=True)
    vicidial_list_id = models.CharField(max_length=12)
    lead_provider = models.ForeignKey('CallCenterLeadprovider', models.DO_NOTHING)
    zipcode = models.CharField(max_length=10, blank=True, null=True)
    created_date = models.DateTimeField(blank=True, null=True)
    last_touched = models.DateTimeField(blank=True, null=True)
    modified_date = models.DateTimeField(blank=True, null=True)
    transfer_date = models.DateTimeField(blank=True, null=True)
    budget = models.IntegerField()
    buy_in_30_days = models.IntegerField()
    result = models.CharField(max_length=50, blank=True, null=True)
    vici_lead_id = models.IntegerField(unique=True, blank=True, null=True)
    boberdoo_lead_type = models.IntegerField(blank=True, null=True)
    source_id = models.CharField(max_length=50, blank=True, null=True)
    called_count = models.SmallIntegerField()
    disposition = models.CharField(max_length=20)
    first_dial_attempt = models.DateTimeField(blank=True, null=True)
    second_dial_attempt = models.DateTimeField(blank=True, null=True)
    third_dial_attempt = models.DateTimeField(blank=True, null=True)
    transfer_number = models.CharField(max_length=20, blank=True, null=True)
    transfer_status = models.SmallIntegerField(blank=True, null=True)
    disposition_name = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'call_center_lead'


class CallCenterLeadprovider(models.Model):
    company_name = models.CharField(max_length=100)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.CharField(max_length=254, blank=True, null=True)
    phone = models.CharField(max_length=20)
    default_price_per_lead = models.DecimalField(max_digits=10, decimal_places=2)
    address = models.CharField(max_length=100)
    vicidial_list_id = models.BigIntegerField()
    active = models.IntegerField()
    min_billable_call_duration = models.IntegerField()
    city_state_zip = models.ForeignKey('CoreCitystatezip', models.DO_NOTHING, blank=True, null=True)
    add_to_hopper = models.IntegerField()
    dup_check = models.IntegerField()
    hopper_priority = models.SmallIntegerField()

    class Meta:
        managed = False
        db_table = 'call_center_leadprovider'


class CallCenterLeadprovidercustomer(models.Model):
    customer = models.ForeignKey(CallCenterCustomer, models.DO_NOTHING)
    lead_provider = models.ForeignKey(CallCenterLeadprovider, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'call_center_leadprovidercustomer'


class CallCenterLeadprovidercustomerfieldmatch(models.Model):
    customer_field = models.CharField(max_length=20)
    sil_expression_type = models.SmallIntegerField()
    sil_expression = models.CharField(max_length=50)
    lead_provider_customer = models.ForeignKey(CallCenterLeadprovidercustomer, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'call_center_leadprovidercustomerfieldmatch'


class CallCenterLeadproviderdateprice(models.Model):
    date = models.DateField(blank=True, null=True)
    price_per_lead = models.DecimalField(max_digits=10, decimal_places=2)
    provider = models.ForeignKey(CallCenterLeadprovider, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'call_center_leadproviderdateprice'
        unique_together = (('provider', 'date'),)


class CallDispAgent(models.Model):
    user = models.CharField(max_length=20, blank=True, null=True)
    status = models.CharField(max_length=6, blank=True, null=True)
    full_name = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'call_disp_agent'


class ConfigXmlconfig(models.Model):
    name = models.CharField(unique=True, max_length=36)
    xml = models.TextField()
    checksum = models.CharField(max_length=32)

    class Meta:
        managed = False
        db_table = 'config_xmlconfig'


class CoreAgent(models.Model):
    gender = models.CharField(max_length=10)
    created_date = models.DateTimeField(blank=True, null=True)
    created_by = models.CharField(max_length=60, blank=True, null=True)
    time_shift = models.CharField(max_length=1)
    branch = models.ForeignKey('CoreBranch', models.DO_NOTHING)
    commission_profile = models.ForeignKey('CoreProfile', models.DO_NOTHING)
    user = models.ForeignKey('EntitlementApiuser', models.DO_NOTHING, unique=True)
    vici_user = models.IntegerField(blank=True, null=True)
    recruiting_source = models.CharField(max_length=10)
    trainer_observation = models.TextField(blank=True, null=True)
    hii_fullname = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'core_agent'


class CoreBranch(models.Model):
    name = models.CharField(max_length=20)
    budget_profile = models.SmallIntegerField()
    to_be_notified = models.TextField()

    class Meta:
        managed = False
        db_table = 'core_branch'


class CoreCity(models.Model):
    name = models.CharField(max_length=30)

    class Meta:
        managed = False
        db_table = 'core_city'


class CoreCitystatezip(models.Model):
    state = models.CharField(max_length=2)
    zip_code = models.CharField(max_length=10)
    city = models.ForeignKey(CoreCity, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'core_citystatezip'


class CoreCluster(models.Model):
    name = models.CharField(max_length=50)
    active = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'core_cluster'


class CoreDnc(models.Model):
    phone_number = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'core_dnc'


class CoreMenu(models.Model):
    index = models.SmallIntegerField()
    name = models.CharField(max_length=50)
    link = models.CharField(max_length=250)
    parent = models.ForeignKey('self', models.DO_NOTHING, blank=True, null=True)
    ng_class = models.CharField(max_length=500, blank=True, null=True)
    active = models.IntegerField()
    resource = models.ForeignKey('EntitlementResource', models.DO_NOTHING, blank=True, null=True)
    icon_class = models.CharField(max_length=150)

    class Meta:
        managed = False
        db_table = 'core_menu'


class CoreProfile(models.Model):
    name = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'core_profile'


class CoreSetting(models.Model):
    name = models.CharField(max_length=60)
    value = models.TextField()

    class Meta:
        managed = False
        db_table = 'core_setting'


class CoreTrustedip(models.Model):
    title = models.CharField(max_length=100)
    network = models.CharField(max_length=18)

    class Meta:
        managed = False
        db_table = 'core_trustedip'


class CpaLead30Day(models.Model):
    state = models.CharField(max_length=2)
    cost = models.DecimalField(max_digits=10, decimal_places=4, blank=True, null=True)
    billable = models.IntegerField()
    created_date = models.DateTimeField()
    sale_date = models.DateTimeField(blank=True, null=True)
    transfer_date = models.DateTimeField(blank=True, null=True)
    lead_provider_provider_type = models.IntegerField()
    lead_provider_id = models.IntegerField()
    lead_company_name = models.CharField(max_length=100)
    agent_id = models.IntegerField()
    agent_fullname = models.CharField(max_length=100)
    branch_id = models.IntegerField(blank=True, null=True)
    branch_name = models.CharField(max_length=100)
    parent_company_id = models.IntegerField()
    parent_company_name = models.CharField(max_length=100)
    account_owner_id = models.IntegerField()
    account_owner_name = models.CharField(max_length=200)
    cpa_status_id = models.IntegerField()
    cpa_status_name = models.CharField(max_length=50)
    sales_status_id = models.IntegerField()
    sales_status_name = models.CharField(max_length=50)
    customer_id = models.IntegerField(blank=True, null=True)
    affiliate_ref = models.CharField(max_length=10)

    class Meta:
        managed = False
        db_table = 'cpa_lead30day'


class CpaLead7Day(models.Model):
    state = models.CharField(max_length=2)
    cost = models.DecimalField(max_digits=10, decimal_places=4, blank=True, null=True)
    billable = models.IntegerField()
    created_date = models.DateTimeField()
    sale_date = models.DateTimeField(blank=True, null=True)
    transfer_date = models.DateTimeField(blank=True, null=True)
    lead_provider_provider_type = models.IntegerField()
    lead_provider_id = models.IntegerField()
    lead_company_name = models.CharField(max_length=100)
    agent_id = models.IntegerField()
    agent_fullname = models.CharField(max_length=100)
    branch_id = models.IntegerField(blank=True, null=True)
    branch_name = models.CharField(max_length=100)
    parent_company_id = models.IntegerField()
    parent_company_name = models.CharField(max_length=100)
    account_owner_id = models.IntegerField()
    account_owner_name = models.CharField(max_length=200)
    cpa_status_id = models.IntegerField()
    cpa_status_name = models.CharField(max_length=50)
    sales_status_id = models.IntegerField()
    sales_status_name = models.CharField(max_length=50)
    customer_id = models.IntegerField(blank=True, null=True)
    affiliate_ref = models.CharField(max_length=10)

    class Meta:
        managed = False
        db_table = 'cpa_lead7day'


class CpaLeadlastmonth(models.Model):
    state = models.CharField(max_length=2)
    cost = models.DecimalField(max_digits=10, decimal_places=4, blank=True, null=True)
    billable = models.IntegerField()
    created_date = models.DateTimeField()
    sale_date = models.DateTimeField(blank=True, null=True)
    transfer_date = models.DateTimeField(blank=True, null=True)
    lead_provider_provider_type = models.IntegerField()
    lead_provider_id = models.IntegerField()
    lead_company_name = models.CharField(max_length=100)
    agent_id = models.IntegerField()
    agent_fullname = models.CharField(max_length=100)
    branch_id = models.IntegerField(blank=True, null=True)
    branch_name = models.CharField(max_length=100)
    parent_company_id = models.IntegerField()
    parent_company_name = models.CharField(max_length=100)
    account_owner_id = models.IntegerField()
    account_owner_name = models.CharField(max_length=200)
    cpa_status_id = models.IntegerField()
    cpa_status_name = models.CharField(max_length=50)
    sales_status_id = models.IntegerField()
    sales_status_name = models.CharField(max_length=50)
    customer_id = models.IntegerField(blank=True, null=True)
    affiliate_ref = models.CharField(max_length=10)

    class Meta:
        managed = False
        db_table = 'cpa_leadlastmonth'


class CpaLeadthismonth(models.Model):
    state = models.CharField(max_length=2)
    cost = models.DecimalField(max_digits=10, decimal_places=4, blank=True, null=True)
    billable = models.IntegerField()
    created_date = models.DateTimeField()
    sale_date = models.DateTimeField(blank=True, null=True)
    transfer_date = models.DateTimeField(blank=True, null=True)
    lead_provider_provider_type = models.IntegerField()
    lead_provider_id = models.IntegerField()
    lead_company_name = models.CharField(max_length=100)
    agent_id = models.IntegerField()
    agent_fullname = models.CharField(max_length=100)
    branch_id = models.IntegerField(blank=True, null=True)
    branch_name = models.CharField(max_length=100)
    parent_company_id = models.IntegerField()
    parent_company_name = models.CharField(max_length=100)
    account_owner_id = models.IntegerField()
    account_owner_name = models.CharField(max_length=200)
    cpa_status_id = models.IntegerField()
    cpa_status_name = models.CharField(max_length=50)
    sales_status_id = models.IntegerField()
    sales_status_name = models.CharField(max_length=50)
    customer_id = models.IntegerField(blank=True, null=True)
    affiliate_ref = models.CharField(max_length=10)

    class Meta:
        managed = False
        db_table = 'cpa_leadthismonth'


class CpaLeadtoday(models.Model):
    state = models.CharField(max_length=2)
    cost = models.DecimalField(max_digits=10, decimal_places=4, blank=True, null=True)
    billable = models.IntegerField()
    created_date = models.DateTimeField()
    sale_date = models.DateTimeField(blank=True, null=True)
    transfer_date = models.DateTimeField(blank=True, null=True)
    lead_provider_provider_type = models.IntegerField()
    lead_provider_id = models.IntegerField()
    lead_company_name = models.CharField(max_length=100)
    agent_id = models.IntegerField()
    agent_fullname = models.CharField(max_length=100)
    branch_id = models.IntegerField(blank=True, null=True)
    branch_name = models.CharField(max_length=100)
    parent_company_id = models.IntegerField()
    parent_company_name = models.CharField(max_length=100)
    account_owner_id = models.IntegerField()
    account_owner_name = models.CharField(max_length=200)
    cpa_status_id = models.IntegerField()
    cpa_status_name = models.CharField(max_length=50)
    sales_status_id = models.IntegerField()
    sales_status_name = models.CharField(max_length=50)
    customer_id = models.IntegerField(blank=True, null=True)
    affiliate_ref = models.CharField(max_length=10)

    class Meta:
        managed = False
        db_table = 'cpa_leadtoday'


class CpaLeadyesterday(models.Model):
    state = models.CharField(max_length=2)
    cost = models.DecimalField(max_digits=10, decimal_places=4, blank=True, null=True)
    billable = models.IntegerField()
    created_date = models.DateTimeField()
    sale_date = models.DateTimeField(blank=True, null=True)
    transfer_date = models.DateTimeField(blank=True, null=True)
    lead_provider_provider_type = models.IntegerField()
    lead_provider_id = models.IntegerField()
    lead_company_name = models.CharField(max_length=100)
    agent_id = models.IntegerField()
    agent_fullname = models.CharField(max_length=100)
    branch_id = models.IntegerField(blank=True, null=True)
    branch_name = models.CharField(max_length=100)
    parent_company_id = models.IntegerField()
    parent_company_name = models.CharField(max_length=100)
    account_owner_id = models.IntegerField()
    account_owner_name = models.CharField(max_length=200)
    cpa_status_id = models.IntegerField()
    cpa_status_name = models.CharField(max_length=50)
    sales_status_id = models.IntegerField()
    sales_status_name = models.CharField(max_length=50)
    customer_id = models.IntegerField(blank=True, null=True)
    affiliate_ref = models.CharField(max_length=10)

    class Meta:
        managed = False
        db_table = 'cpa_leadyesterday'


class CpaPerUserTemp(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50, blank=True, null=True)
    created_date = models.DateTimeField(blank=True, null=True)
    modified_date = models.DateTimeField(blank=True, null=True)
    lead_created_date = models.DateTimeField(blank=True, null=True)
    transfer_date = models.DateTimeField(blank=True, null=True)
    sale_date = models.DateTimeField(blank=True, null=True)
    first_call_duration = models.IntegerField(blank=True, null=True)
    state = models.CharField(max_length=2, blank=True, null=True)
    agent_id = models.IntegerField(blank=True, null=True)
    provider_id = models.IntegerField(blank=True, null=True)
    sales_status_id = models.IntegerField(blank=True, null=True)
    cpa_status_id = models.IntegerField(blank=True, null=True)
    user_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cpa_per_user_temp'


class CustsrvCalltracking(models.Model):
    phone = models.CharField(max_length=10)
    call_date = models.DateTimeField(blank=True, null=True)
    sale_date = models.DateTimeField(blank=True, null=True)
    call_status = models.CharField(max_length=10, blank=True, null=True)
    queue_seconds = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'custsrv_calltracking'


class CustsrvCase(models.Model):
    status = models.SmallIntegerField()
    priority = models.SmallIntegerField()
    case_origin = models.SmallIntegerField()
    subject = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    disposition = models.SmallIntegerField(blank=True, null=True)
    escalated_outcome = models.SmallIntegerField(blank=True, null=True)
    created_date = models.DateTimeField(blank=True, null=True)
    account = models.ForeignKey(ApiAccount, models.DO_NOTHING)
    case_owner = models.ForeignKey(CoreAgent, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'custsrv_case'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey('EntitlementApiuser', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class EnrollmentApifromsf(models.Model):
    user_name = models.CharField(max_length=100)
    full_post = models.TextField()
    url_quote = models.TextField()
    url_question = models.TextField(db_column='url_Question')  # Field name made lowercase.
    url_enrrollment = models.TextField(db_column='url_Enrrollment')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'enrollment_apifromsf'


class EnrollmentEnrollmentcarriercommunicationlog(models.Model):
    timestamp = models.DateTimeField()
    request = models.TextField()
    response = models.TextField()
    enrollment = models.ForeignKey(ApiEnrollment, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'enrollment_enrollmentcarriercommunicationlog'


class EnrollmentLogresponsecontent(models.Model):
    phone = models.CharField(max_length=20)
    full_name = models.CharField(max_length=20)
    url_post = models.CharField(max_length=200)
    content = models.TextField()
    created_date = models.DateTimeField(blank=True, null=True)
    request = models.TextField()

    class Meta:
        managed = False
        db_table = 'enrollment_logresponsecontent'


class EntitlementAction(models.Model):
    name = models.CharField(max_length=15)

    class Meta:
        managed = False
        db_table = 'entitlement_action'


class EntitlementApigroup(models.Model):
    group_ptr = models.ForeignKey(AuthGroup, models.DO_NOTHING, primary_key=True)

    class Meta:
        managed = False
        db_table = 'entitlement_apigroup'


class EntitlementApigroupAllowedPermissions(models.Model):
    apigroup = models.ForeignKey(EntitlementApigroup, models.DO_NOTHING)
    custompermission = models.ForeignKey('EntitlementCustompermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'entitlement_apigroup_allowed_permissions'
        unique_together = (('apigroup', 'custompermission'),)


class EntitlementApigroupDeniedPermissions(models.Model):
    apigroup = models.ForeignKey(EntitlementApigroup, models.DO_NOTHING)
    custompermission = models.ForeignKey('EntitlementCustompermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'entitlement_apigroup_denied_permissions'
        unique_together = (('apigroup', 'custompermission'),)


class EntitlementApiuser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=30)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()
    middle_initial = models.CharField(max_length=1)
    did = models.CharField(max_length=50, blank=True, null=True)
    extension = models.CharField(max_length=25, blank=True, null=True)
    photo = models.CharField(max_length=100, blank=True, null=True)
    title = models.CharField(max_length=50, blank=True, null=True)
    department = models.ForeignKey('EntitlementDepartment', models.DO_NOTHING, blank=True, null=True)
    location = models.ForeignKey('EntitlementLocation', models.DO_NOTHING, blank=True, null=True)
    domain_user = models.CharField(max_length=255, blank=True, null=True)
    force_reset_password = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'entitlement_apiuser'


class EntitlementApiuserCustomUserPermissions(models.Model):
    apiuser = models.ForeignKey(EntitlementApiuser, models.DO_NOTHING)
    custompermission = models.ForeignKey('EntitlementCustompermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'entitlement_apiuser_custom_user_permissions'
        unique_together = (('apiuser', 'custompermission'),)


class EntitlementApiuserDeniedPermissions(models.Model):
    apiuser = models.ForeignKey(EntitlementApiuser, models.DO_NOTHING)
    custompermission = models.ForeignKey('EntitlementCustompermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'entitlement_apiuser_denied_permissions'
        unique_together = (('apiuser', 'custompermission'),)


class EntitlementApiuserGroups(models.Model):
    apiuser = models.ForeignKey(EntitlementApiuser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'entitlement_apiuser_groups'
        unique_together = (('apiuser', 'group'),)


class EntitlementApiuserUserPermissions(models.Model):
    apiuser = models.ForeignKey(EntitlementApiuser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'entitlement_apiuser_user_permissions'
        unique_together = (('apiuser', 'permission'),)


class EntitlementApplication(models.Model):
    index = models.SmallIntegerField()
    name = models.CharField(max_length=20)
    active = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'entitlement_application'


class EntitlementCustompermission(models.Model):
    description = models.CharField(max_length=280)
    action = models.ForeignKey(EntitlementAction, models.DO_NOTHING)
    resource = models.ForeignKey('EntitlementResource', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'entitlement_custompermission'


class EntitlementDepartment(models.Model):
    name = models.CharField(max_length=120)

    class Meta:
        managed = False
        db_table = 'entitlement_department'


class EntitlementLocation(models.Model):
    name = models.CharField(max_length=120)

    class Meta:
        managed = False
        db_table = 'entitlement_location'


class EntitlementModule(models.Model):
    index = models.SmallIntegerField()
    name = models.CharField(max_length=20)
    active = models.IntegerField()
    application = models.ForeignKey(EntitlementApplication, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'entitlement_module'


class EntitlementResource(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'entitlement_resource'


class EntitlementSystembygroup(models.Model):
    use_system = models.CharField(max_length=1)
    emails = models.TextField()
    group = models.ForeignKey(EntitlementApigroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'entitlement_systembygroup'
        unique_together = (('group', 'use_system'),)


class EntitlementUserspendigconfirm(models.Model):
    username = models.CharField(max_length=50)
    confirmation_type = models.CharField(max_length=1)
    use_system = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'entitlement_userspendigconfirm'
        unique_together = (('username', 'use_system', 'confirmation_type'),)


class EntitlementViciusertemplate(models.Model):
    time_shift = models.CharField(max_length=1)
    db_name = models.CharField(max_length=25)
    username_template = models.CharField(max_length=25)
    agent_type = models.ForeignKey(EntitlementApigroup, models.DO_NOTHING)
    branch = models.ForeignKey(CoreBranch, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'entitlement_viciusertemplate'


class MarketingCampaigntype(models.Model):
    name = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'marketing_campaigntype'


class MarketingCompany(models.Model):
    name = models.CharField(max_length=255)
    active = models.IntegerField()
    created_date = models.DateTimeField()
    owner = models.ForeignKey(EntitlementApiuser, models.DO_NOTHING)
    contact = models.CharField(max_length=120, blank=True, null=True)
    email = models.CharField(max_length=254, blank=True, null=True)
    phone_number = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'marketing_company'


class MarketingCustomer(models.Model):
    code = models.CharField(max_length=10)
    name = models.CharField(max_length=50)
    index = models.SmallIntegerField()
    method = models.SmallIntegerField()
    format = models.SmallIntegerField()
    url = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'marketing_customer'


class MarketingCustomerfieldmatch(models.Model):
    customer_field = models.CharField(max_length=50)
    sil_expression_type = models.SmallIntegerField()
    sil_expression = models.CharField(max_length=50)
    customer = models.ForeignKey(MarketingCustomer, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'marketing_customerfieldmatch'


class MarketingCustomerrunningstate(models.Model):
    state = models.CharField(max_length=2)
    customer = models.ForeignKey(MarketingCustomer, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'marketing_customerrunningstate'


class MarketingDonotemailme(models.Model):
    email = models.CharField(unique=True, max_length=254)
    created_date = models.DateTimeField()
    source = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'marketing_donotemailme'


class MarketingLead(models.Model):
    vicidial_list_id = models.IntegerField(blank=True, null=True)
    created_date = models.DateTimeField(blank=True, null=True)
    modified_date = models.DateTimeField(blank=True, null=True)
    first_name = models.CharField(max_length=100, blank=True, null=True)
    last_name = models.CharField(max_length=100, blank=True, null=True)
    primary_email = models.CharField(max_length=100, blank=True, null=True)
    secondary_email = models.CharField(max_length=100, blank=True, null=True)
    phone = models.CharField(max_length=20)
    mobile = models.CharField(max_length=20, blank=True, null=True)
    address = models.CharField(max_length=200, blank=True, null=True)
    address2 = models.CharField(max_length=200, blank=True, null=True)
    city = models.CharField(max_length=50, blank=True, null=True)
    state = models.CharField(max_length=2, blank=True, null=True)
    zipcode = models.CharField(max_length=10, blank=True, null=True)
    src = models.CharField(max_length=50, blank=True, null=True)
    landing_page = models.CharField(max_length=300, blank=True, null=True)
    ip_address = models.CharField(max_length=50, blank=True, null=True)
    external_id = models.CharField(max_length=50, blank=True, null=True)
    age = models.CharField(max_length=4, blank=True, null=True)
    dob = models.DateField(blank=True, null=True)
    gender = models.CharField(max_length=1, blank=True, null=True)
    height_feet = models.CharField(max_length=50, blank=True, null=True)
    height_inches = models.CharField(max_length=50, blank=True, null=True)
    weight = models.IntegerField(blank=True, null=True)
    smoker = models.IntegerField()
    currently_insured = models.IntegerField()
    health_conditions = models.IntegerField()
    number_household = models.IntegerField(blank=True, null=True)
    pregnant = models.IntegerField()
    income = models.IntegerField(blank=True, null=True)
    conditions = models.TextField(blank=True, null=True)
    contact_time = models.CharField(max_length=50, blank=True, null=True)
    medications = models.TextField(blank=True, null=True)
    child_1_age = models.CharField(max_length=50, blank=True, null=True)
    child_1_dob = models.DateField(blank=True, null=True)
    child_1_gender = models.CharField(max_length=1, blank=True, null=True)
    child_1_height_fee = models.IntegerField(blank=True, null=True)
    child_1_height_inches = models.IntegerField(blank=True, null=True)
    child_1_weight = models.IntegerField(blank=True, null=True)
    child_2_age = models.CharField(max_length=10, blank=True, null=True)
    child_2_dob = models.DateField(blank=True, null=True)
    child_2_gender = models.CharField(max_length=1, blank=True, null=True)
    child_2_height_feet = models.IntegerField(blank=True, null=True)
    child_2_height_inches = models.IntegerField(blank=True, null=True)
    child_2_weight = models.IntegerField(blank=True, null=True)
    spouse_age = models.CharField(max_length=50, blank=True, null=True)
    spouse_dob = models.DateField(blank=True, null=True)
    spouse_gender = models.CharField(max_length=1, blank=True, null=True)
    spouse_height_feet = models.IntegerField(blank=True, null=True)
    spouse_height_inches = models.IntegerField(blank=True, null=True)
    spouse_smoker = models.IntegerField()
    spouse_weight = models.IntegerField(blank=True, null=True)
    updated_from_eap = models.IntegerField()
    notes = models.TextField(blank=True, null=True)
    al_dr = models.IntegerField()
    alz = models.IntegerField()
    art_d = models.IntegerField()
    bip = models.IntegerField()
    bon_d = models.IntegerField()
    acc_cer = models.IntegerField()
    obs_lung = models.IntegerField()
    obs_pul = models.IntegerField()
    crohn_d = models.IntegerField()
    emphy = models.IntegerField()
    fibro = models.IntegerField()
    heart_att = models.IntegerField()
    hepp = models.IntegerField()
    ins_dep = models.IntegerField()
    int_ca = models.IntegerField()
    kidn_d = models.IntegerField()
    liv_d = models.IntegerField()
    lou_d = models.IntegerField()
    lupus = models.IntegerField()
    hyperte = models.IntegerField()
    choles = models.IntegerField()
    depress = models.IntegerField()
    melo_ca = models.IntegerField()
    sclero = models.IntegerField()
    muscle_d = models.IntegerField()
    muscle_dy = models.IntegerField()
    myosi = models.IntegerField()
    organ_f = models.IntegerField()
    orga_t = models.IntegerField()
    brain_s = models.IntegerField()
    osteop = models.IntegerField()
    paraly = models.IntegerField()
    peri_va = models.IntegerField()
    rheu_ar = models.IntegerField()
    seni_de = models.IntegerField()
    stroke = models.IntegerField()
    sub_ab = models.IntegerField()
    isc_att = models.IntegerField()
    ulc = models.IntegerField()
    thyr = models.IntegerField()
    asmt = models.IntegerField()
    oth = models.IntegerField()
    pl_sz = models.TextField(blank=True, null=True)
    uni_le = models.TextField(blank=True, null=True)
    in_ch = models.TextField(blank=True, null=True)
    med_ty = models.TextField(blank=True, null=True)
    reas_in = models.TextField(blank=True, null=True)
    cu_in = models.TextField(blank=True, null=True)
    st_dt = models.DateField(blank=True, null=True)
    cu_inra = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    nu_med = models.IntegerField(blank=True, null=True)
    dr_vis = models.IntegerField(blank=True, null=True)
    ins_asp = models.TextField(blank=True, null=True)
    sho_ar = models.TextField(blank=True, null=True)
    agent = models.ForeignKey(CoreAgent, models.DO_NOTHING)
    lead_provider = models.ForeignKey('MarketingLeadprovider', models.DO_NOTHING, blank=True, null=True)
    status = models.ForeignKey('MarketingStatus', models.DO_NOTHING, blank=True, null=True)
    cost = models.DecimalField(max_digits=10, decimal_places=4, blank=True, null=True)
    middle_initial = models.CharField(max_length=1, blank=True, null=True)
    current_insurance = models.CharField(max_length=50)
    more_than_63days_uninsured = models.IntegerField()
    de_in = models.IntegerField()
    budget = models.IntegerField(blank=True, null=True)
    source_id = models.CharField(max_length=50, blank=True, null=True)
    plan_size = models.SmallIntegerField()
    carrier = models.CharField(max_length=20, blank=True, null=True)
    first_call = models.DateTimeField(blank=True, null=True)
    called_count = models.SmallIntegerField()
    last_call = models.DateTimeField(blank=True, null=True)
    cpa_status = models.ForeignKey(ApiCpastatus, models.DO_NOTHING)
    customer = models.ForeignKey(MarketingCustomer, models.DO_NOTHING, blank=True, null=True)
    last_touched = models.DateTimeField(blank=True, null=True)
    first_call_duration = models.IntegerField()
    created_by = models.SmallIntegerField()
    universal_lead_id = models.CharField(max_length=40, blank=True, null=True)
    sale_date = models.DateTimeField(blank=True, null=True)
    sales_status_id = models.IntegerField()
    transfer_date = models.DateTimeField(blank=True, null=True)
    sales_agent_disposition = models.ForeignKey(ApiDisposition, models.DO_NOTHING)
    sales_agent_branch = models.ForeignKey(CoreBranch, models.DO_NOTHING, blank=True, null=True)
    subscribed = models.IntegerField()
    boberdoo_lead_type = models.IntegerField(blank=True, null=True)
    auto_insurance = models.IntegerField()
    auto_insurance_date_to_be_call = models.DateTimeField(blank=True, null=True)
    auto_insurance_opt_in_date = models.DateTimeField(blank=True, null=True)
    billable = models.IntegerField()
    talk_time = models.IntegerField(blank=True, null=True)
    lead_provider_type = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'marketing_lead'


class MarketingLeadMem(models.Model):
    id = models.IntegerField(blank=True, null=True)
    lead_provider_id = models.IntegerField(blank=True, null=True)
    billable = models.IntegerField(blank=True, null=True)
    created_date = models.DateTimeField(blank=True, null=True)
    cost = models.DecimalField(max_digits=10, decimal_places=4, blank=True, null=True)
    sale_date = models.DateTimeField(blank=True, null=True)
    transfer_date = models.DateTimeField(blank=True, null=True)
    status_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'marketing_lead_mem'


class MarketingLeadprovider(models.Model):
    company_name = models.CharField(max_length=100)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.CharField(max_length=254, blank=True, null=True)
    phone = models.CharField(max_length=20)
    provider_type = models.CharField(max_length=1)
    default_price_per_lead = models.DecimalField(max_digits=10, decimal_places=2)
    address = models.CharField(max_length=100)
    city_state_zip = models.ForeignKey(CoreCitystatezip, models.DO_NOTHING, blank=True, null=True)
    active = models.IntegerField()
    vicidial_list_id = models.BigIntegerField()
    campaign_type = models.ForeignKey(MarketingCampaigntype, models.DO_NOTHING, blank=True, null=True)
    internal_dnc_trusted = models.IntegerField()
    national_dnc_trusted = models.IntegerField()
    add_to_hopper = models.IntegerField()
    hopper_priority = models.SmallIntegerField()
    hbc1 = models.ForeignKey(ApiLeadvendor, models.DO_NOTHING)
    hbc2 = models.ForeignKey(ApiLeadvendor, models.DO_NOTHING)
    min_billable_call_duration = models.IntegerField()
    parent_company = models.ForeignKey(MarketingCompany, models.DO_NOTHING, blank=True, null=True)
    lead_type = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'marketing_leadprovider'


class MarketingLeadprovidercustomer(models.Model):
    customer = models.ForeignKey(MarketingCustomer, models.DO_NOTHING)
    lead_provider = models.ForeignKey(MarketingLeadprovider, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'marketing_leadprovidercustomer'


class MarketingLeadprovidercustomerfieldmatch(models.Model):
    customer_field = models.CharField(max_length=20)
    sil_expression_type = models.SmallIntegerField()
    sil_expression = models.CharField(max_length=50)
    lead_provider_customer = models.ForeignKey(MarketingLeadprovidercustomer, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'marketing_leadprovidercustomerfieldmatch'


class MarketingLeadproviderdateprice(models.Model):
    date = models.DateField(blank=True, null=True)
    price_per_lead = models.DecimalField(max_digits=10, decimal_places=2)
    provider = models.ForeignKey(MarketingLeadprovider, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'marketing_leadproviderdateprice'
        unique_together = (('provider', 'date'),)


class MarketingStatus(models.Model):
    code = models.CharField(max_length=10, blank=True, null=True)
    name = models.CharField(max_length=30)
    description = models.TextField()
    is_transfer = models.IntegerField()
    billable = models.IntegerField()
    is_external_transfer = models.IntegerField()
    boberdoo_name = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'marketing_status'


class MedicareDisposition(models.Model):
    name = models.CharField(max_length=64)
    code = models.CharField(max_length=64, blank=True, null=True)
    boberdoo_name = models.CharField(max_length=30, blank=True, null=True)
    is_sale = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'medicare_disposition'


class MedicareLead(models.Model):
    vici_lead_id = models.IntegerField(unique=True, blank=True, null=True)
    phone = models.CharField(max_length=15)
    first_name = models.CharField(max_length=50, blank=True, null=True)
    last_name = models.CharField(max_length=50, blank=True, null=True)
    email1 = models.CharField(max_length=254, blank=True, null=True)
    address = models.CharField(max_length=100, blank=True, null=True)
    address2 = models.CharField(max_length=100, blank=True, null=True)
    city = models.CharField(max_length=50, blank=True, null=True)
    state = models.CharField(max_length=2, blank=True, null=True)
    zipcode = models.CharField(max_length=10, blank=True, null=True)
    dob = models.DateField(blank=True, null=True)
    vicidial_list_id = models.CharField(max_length=12)
    created_date = models.DateTimeField(blank=True, null=True)
    modified_date = models.DateTimeField(blank=True, null=True)
    last_touched = models.DateTimeField(blank=True, null=True)
    transfer_date = models.DateTimeField(blank=True, null=True)
    buy_in_30_days = models.IntegerField()
    boberdoo_lead_type = models.IntegerField(blank=True, null=True)
    source_id = models.CharField(max_length=50, blank=True, null=True)
    called_count = models.SmallIntegerField()
    disposition = models.ForeignKey('MedicareMarketingdisposition', models.DO_NOTHING)
    transfer_status = models.SmallIntegerField(blank=True, null=True)
    transfer_number = models.CharField(max_length=20, blank=True, null=True)
    lead_provider = models.ForeignKey('MedicareLeadprovider', models.DO_NOTHING)
    agent = models.ForeignKey(CoreAgent, models.DO_NOTHING)
    middle_initial = models.CharField(max_length=1, blank=True, null=True)
    budget = models.IntegerField(blank=True, null=True)
    income = models.IntegerField(blank=True, null=True)
    plan_type = models.SmallIntegerField(blank=True, null=True)
    gender = models.CharField(max_length=1, blank=True, null=True)
    cost = models.DecimalField(max_digits=10, decimal_places=4, blank=True, null=True)
    first_call = models.DateTimeField(blank=True, null=True)
    first_call_duration = models.IntegerField()
    last_call = models.DateTimeField(blank=True, null=True)
    billable = models.IntegerField()
    created_by = models.SmallIntegerField()
    conditions = models.TextField(blank=True, null=True)
    current_insurance = models.CharField(max_length=50)
    currently_insured = models.IntegerField()
    height_feet = models.CharField(max_length=50, blank=True, null=True)
    height_inches = models.CharField(max_length=50, blank=True, null=True)
    ip_address = models.CharField(max_length=39, blank=True, null=True)
    landing_page = models.CharField(max_length=300, blank=True, null=True)
    notes = models.TextField(blank=True, null=True)
    src = models.CharField(max_length=50, blank=True, null=True)
    universal_lead_id = models.CharField(max_length=40, blank=True, null=True)
    weight = models.IntegerField(blank=True, null=True)
    has_been_sold = models.IntegerField()
    sale_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'medicare_lead'


class MedicareLeadprovider(models.Model):
    company_name = models.CharField(max_length=100)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.CharField(max_length=254, blank=True, null=True)
    phone = models.CharField(max_length=20)
    default_price_per_lead = models.DecimalField(max_digits=10, decimal_places=2)
    address = models.CharField(max_length=100)
    vicidial_list_id = models.BigIntegerField()
    active = models.IntegerField()
    min_billable_call_duration = models.IntegerField()
    dup_check = models.IntegerField()
    hopper_priority = models.SmallIntegerField()
    add_to_hopper = models.IntegerField()
    city_state_zip = models.ForeignKey(CoreCitystatezip, models.DO_NOTHING, blank=True, null=True)
    parent_company = models.ForeignKey(MarketingCompany, models.DO_NOTHING, blank=True, null=True)
    campaign_type = models.ForeignKey(MarketingCampaigntype, models.DO_NOTHING, blank=True, null=True)
    provider_type = models.CharField(max_length=1)
    lead_vendor = models.ForeignKey('MedicareLeadvendor', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'medicare_leadprovider'


class MedicareLeadproviderdateprice(models.Model):
    date = models.DateField(blank=True, null=True)
    price_per_lead = models.DecimalField(max_digits=10, decimal_places=2)
    provider = models.ForeignKey(MedicareLeadprovider, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'medicare_leadproviderdateprice'
        unique_together = (('provider', 'date'),)


class MedicareLeadvendor(models.Model):
    company_name = models.CharField(max_length=100)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.CharField(max_length=254, blank=True, null=True)
    phone = models.CharField(max_length=20)
    provider_type = models.CharField(max_length=1)
    default_price_per_lead = models.DecimalField(max_digits=10, decimal_places=2)
    address = models.CharField(max_length=100)
    active = models.IntegerField()
    affiliate_ref = models.CharField(max_length=10, blank=True, null=True)
    city_state_zip = models.ForeignKey(CoreCitystatezip, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'medicare_leadvendor'


class MedicareLeadvendordateprice(models.Model):
    date = models.DateField(blank=True, null=True)
    price_per_lead = models.DecimalField(max_digits=10, decimal_places=2)
    lead_vendor = models.ForeignKey(MedicareLeadvendor, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'medicare_leadvendordateprice'


class MedicareMarketingdisposition(models.Model):
    name = models.CharField(max_length=64)
    code = models.CharField(max_length=64, blank=True, null=True)
    boberdoo_name = models.CharField(max_length=30, blank=True, null=True)
    is_external_transfer = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'medicare_marketingdisposition'


class MedicareOpportunity(models.Model):
    vicidial_lead_id = models.IntegerField(blank=True, null=True)
    universal_lead_id = models.CharField(max_length=40, blank=True, null=True)
    vicidial_list_id = models.IntegerField(blank=True, null=True)
    lead_created_date = models.DateTimeField(blank=True, null=True)
    src = models.CharField(max_length=50, blank=True, null=True)
    landing_page = models.CharField(max_length=300, blank=True, null=True)
    ip_address = models.CharField(max_length=39, blank=True, null=True)
    boberdoo_id = models.CharField(max_length=50, blank=True, null=True)
    boberdoo_lead_type = models.IntegerField(blank=True, null=True)
    cost = models.DecimalField(max_digits=10, decimal_places=4, blank=True, null=True)
    plan_type = models.SmallIntegerField(blank=True, null=True)
    state = models.CharField(max_length=2)
    created_date = models.DateTimeField(blank=True, null=True)
    modified_date = models.DateTimeField(blank=True, null=True)
    sale_date = models.DateTimeField(blank=True, null=True)
    created_by = models.SmallIntegerField()
    first_name = models.CharField(max_length=100, blank=True, null=True)
    last_name = models.CharField(max_length=100, blank=True, null=True)
    middle_initial = models.CharField(max_length=1, blank=True, null=True)
    primary_email = models.CharField(max_length=254, blank=True, null=True)
    phone = models.CharField(max_length=20, blank=True, null=True)
    mobile = models.CharField(max_length=20, blank=True, null=True)
    address = models.CharField(max_length=200, blank=True, null=True)
    address2 = models.CharField(max_length=200, blank=True, null=True)
    currently_insured = models.IntegerField()
    current_insurance = models.CharField(max_length=50)
    health_conditions = models.IntegerField()
    number_household = models.IntegerField(blank=True, null=True)
    income = models.IntegerField(blank=True, null=True)
    conditions = models.TextField(blank=True, null=True)
    contact_time = models.CharField(max_length=50, blank=True, null=True)
    medications = models.TextField(blank=True, null=True)
    more_than_63days_uninsured = models.IntegerField()
    budget = models.IntegerField(blank=True, null=True)
    notes = models.TextField(blank=True, null=True)
    agent = models.ForeignKey(CoreAgent, models.DO_NOTHING)
    disposition = models.ForeignKey(MedicareDisposition, models.DO_NOTHING, blank=True, null=True)
    lead = models.ForeignKey(MedicareLead, models.DO_NOTHING, blank=True, null=True)
    lead_vendor = models.ForeignKey(MedicareLeadvendor, models.DO_NOTHING, blank=True, null=True)
    secondary_email = models.CharField(max_length=254, blank=True, null=True)
    dob = models.DateField(blank=True, null=True)
    buy_in_30_days = models.IntegerField()
    gender = models.CharField(max_length=1, blank=True, null=True)
    height_feet = models.CharField(max_length=50, blank=True, null=True)
    height_inches = models.CharField(max_length=50, blank=True, null=True)
    weight = models.IntegerField(blank=True, null=True)
    cluster = models.ForeignKey(CoreCluster, models.DO_NOTHING, blank=True, null=True)
    city = models.CharField(max_length=50, blank=True, null=True)
    zipcode = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'medicare_opportunity'
        unique_together = (('phone', 'vicidial_list_id', 'created_date'),)


class MedicareOpportunityvicileadlog(models.Model):
    vicidial_lead_id = models.IntegerField()
    log_date = models.DateTimeField()
    cluster = models.ForeignKey(CoreCluster, models.DO_NOTHING)
    opportunity = models.ForeignKey(MedicareOpportunity, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'medicare_opportunityvicileadlog'


class MedicareSeniormarketsalescredential(models.Model):
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=50)
    agent = models.ForeignKey(CoreAgent, models.DO_NOTHING, unique=True)

    class Meta:
        managed = False
        db_table = 'medicare_seniormarketsalescredential'


class MedicareVendordid(models.Model):
    did = models.CharField(max_length=15)
    lead_vendor = models.ForeignKey(MedicareLeadvendor, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'medicare_vendordid'


class NewLead(models.Model):
    vicidial_list_id = models.IntegerField(blank=True, null=True)
    created_date = models.DateTimeField(blank=True, null=True)
    modified_date = models.DateTimeField(blank=True, null=True)
    first_name = models.CharField(max_length=100, blank=True, null=True)
    last_name = models.CharField(max_length=100, blank=True, null=True)
    primary_email = models.CharField(max_length=100, blank=True, null=True)
    secondary_email = models.CharField(max_length=100, blank=True, null=True)
    phone = models.CharField(max_length=20)
    mobile = models.CharField(max_length=20, blank=True, null=True)
    address = models.CharField(max_length=200, blank=True, null=True)
    address2 = models.CharField(max_length=200, blank=True, null=True)
    city = models.CharField(max_length=50, blank=True, null=True)
    state = models.CharField(max_length=2, blank=True, null=True)
    zipcode = models.CharField(max_length=10, blank=True, null=True)
    src = models.CharField(max_length=50, blank=True, null=True)
    landing_page = models.CharField(max_length=300, blank=True, null=True)
    ip_address = models.CharField(max_length=50, blank=True, null=True)
    external_id = models.CharField(max_length=50, blank=True, null=True)
    age = models.CharField(max_length=4, blank=True, null=True)
    dob = models.DateField(blank=True, null=True)
    gender = models.CharField(max_length=1, blank=True, null=True)
    height_feet = models.CharField(max_length=50, blank=True, null=True)
    height_inches = models.CharField(max_length=50, blank=True, null=True)
    weight = models.IntegerField(blank=True, null=True)
    smoker = models.IntegerField()
    currently_insured = models.IntegerField()
    health_conditions = models.IntegerField()
    number_household = models.IntegerField(blank=True, null=True)
    pregnant = models.IntegerField()
    income = models.IntegerField(blank=True, null=True)
    conditions = models.TextField(blank=True, null=True)
    contact_time = models.CharField(max_length=50, blank=True, null=True)
    medications = models.TextField(blank=True, null=True)
    child_1_age = models.CharField(max_length=50, blank=True, null=True)
    child_1_dob = models.DateField(blank=True, null=True)
    child_1_gender = models.CharField(max_length=1, blank=True, null=True)
    child_1_height_fee = models.IntegerField(blank=True, null=True)
    child_1_height_inches = models.IntegerField(blank=True, null=True)
    child_1_weight = models.IntegerField(blank=True, null=True)
    child_2_age = models.CharField(max_length=10, blank=True, null=True)
    child_2_dob = models.DateField(blank=True, null=True)
    child_2_gender = models.CharField(max_length=1, blank=True, null=True)
    child_2_height_feet = models.IntegerField(blank=True, null=True)
    child_2_height_inches = models.IntegerField(blank=True, null=True)
    child_2_weight = models.IntegerField(blank=True, null=True)
    spouse_age = models.CharField(max_length=50, blank=True, null=True)
    spouse_dob = models.DateField(blank=True, null=True)
    spouse_gender = models.CharField(max_length=1, blank=True, null=True)
    spouse_height_feet = models.IntegerField(blank=True, null=True)
    spouse_height_inches = models.IntegerField(blank=True, null=True)
    spouse_smoker = models.IntegerField()
    spouse_weight = models.IntegerField(blank=True, null=True)
    updated_from_eap = models.IntegerField()
    notes = models.TextField(blank=True, null=True)
    al_dr = models.IntegerField()
    alz = models.IntegerField()
    art_d = models.IntegerField()
    bip = models.IntegerField()
    bon_d = models.IntegerField()
    acc_cer = models.IntegerField()
    obs_lung = models.IntegerField()
    obs_pul = models.IntegerField()
    crohn_d = models.IntegerField()
    emphy = models.IntegerField()
    fibro = models.IntegerField()
    heart_att = models.IntegerField()
    hepp = models.IntegerField()
    ins_dep = models.IntegerField()
    int_ca = models.IntegerField()
    kidn_d = models.IntegerField()
    liv_d = models.IntegerField()
    lou_d = models.IntegerField()
    lupus = models.IntegerField()
    hyperte = models.IntegerField()
    choles = models.IntegerField()
    depress = models.IntegerField()
    melo_ca = models.IntegerField()
    sclero = models.IntegerField()
    muscle_d = models.IntegerField()
    muscle_dy = models.IntegerField()
    myosi = models.IntegerField()
    organ_f = models.IntegerField()
    orga_t = models.IntegerField()
    brain_s = models.IntegerField()
    osteop = models.IntegerField()
    paraly = models.IntegerField()
    peri_va = models.IntegerField()
    rheu_ar = models.IntegerField()
    seni_de = models.IntegerField()
    stroke = models.IntegerField()
    sub_ab = models.IntegerField()
    isc_att = models.IntegerField()
    ulc = models.IntegerField()
    thyr = models.IntegerField()
    asmt = models.IntegerField()
    oth = models.IntegerField()
    pl_sz = models.TextField(blank=True, null=True)
    uni_le = models.TextField(blank=True, null=True)
    in_ch = models.TextField(blank=True, null=True)
    med_ty = models.TextField(blank=True, null=True)
    reas_in = models.TextField(blank=True, null=True)
    cu_in = models.TextField(blank=True, null=True)
    st_dt = models.DateField(blank=True, null=True)
    cu_inra = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    nu_med = models.IntegerField(blank=True, null=True)
    dr_vis = models.IntegerField(blank=True, null=True)
    ins_asp = models.TextField(blank=True, null=True)
    sho_ar = models.TextField(blank=True, null=True)
    agent_id = models.IntegerField()
    lead_provider_id = models.IntegerField(blank=True, null=True)
    status_id = models.IntegerField(blank=True, null=True)
    cost = models.DecimalField(max_digits=10, decimal_places=4, blank=True, null=True)
    middle_initial = models.CharField(max_length=1, blank=True, null=True)
    current_insurance = models.CharField(max_length=50)
    more_than_63days_uninsured = models.IntegerField()
    de_in = models.IntegerField()
    budget = models.IntegerField(blank=True, null=True)
    source_id = models.CharField(max_length=50, blank=True, null=True)
    plan_size = models.SmallIntegerField()
    carrier = models.CharField(max_length=20, blank=True, null=True)
    first_call = models.DateTimeField(blank=True, null=True)
    called_count = models.SmallIntegerField()
    last_call = models.DateTimeField(blank=True, null=True)
    cpa_status_id = models.IntegerField()
    customer_id = models.IntegerField(blank=True, null=True)
    last_touched = models.DateTimeField(blank=True, null=True)
    first_call_duration = models.IntegerField()
    created_by = models.SmallIntegerField()
    universal_lead_id = models.CharField(max_length=40, blank=True, null=True)
    sale_date = models.DateTimeField(blank=True, null=True)
    sales_status_id = models.IntegerField()
    transfer_date = models.DateTimeField(blank=True, null=True)
    sales_agent_disposition_id = models.IntegerField()
    sales_agent_branch_id = models.IntegerField(blank=True, null=True)
    subscribed = models.IntegerField()
    boberdoo_lead_type = models.IntegerField(blank=True, null=True)
    auto_insurance = models.IntegerField()
    auto_insurance_date_to_be_call = models.DateTimeField(blank=True, null=True)
    auto_insurance_opt_in_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'new_lead'


class OriginalVicidialList(models.Model):
    lead_id = models.AutoField(primary_key=True)
    entry_date = models.DateTimeField(blank=True, null=True)
    modify_date = models.DateTimeField()
    status = models.CharField(max_length=6, blank=True, null=True)
    user = models.CharField(max_length=20, blank=True, null=True)
    vendor_lead_code = models.CharField(max_length=20, blank=True, null=True)
    source_id = models.CharField(max_length=50, blank=True, null=True)
    list_id = models.BigIntegerField()
    gmt_offset_now = models.DecimalField(max_digits=4, decimal_places=2, blank=True, null=True)
    called_since_last_reset = models.CharField(max_length=3, blank=True, null=True)
    phone_code = models.CharField(max_length=10, blank=True, null=True)
    phone_number = models.CharField(max_length=18)
    title = models.CharField(max_length=4, blank=True, null=True)
    first_name = models.CharField(max_length=30, blank=True, null=True)
    middle_initial = models.CharField(max_length=1, blank=True, null=True)
    last_name = models.CharField(max_length=30, blank=True, null=True)
    address1 = models.CharField(max_length=100, blank=True, null=True)
    address2 = models.CharField(max_length=100, blank=True, null=True)
    address3 = models.CharField(max_length=100, blank=True, null=True)
    city = models.CharField(max_length=50, blank=True, null=True)
    state = models.CharField(max_length=2, blank=True, null=True)
    province = models.CharField(max_length=50, blank=True, null=True)
    postal_code = models.CharField(max_length=10, blank=True, null=True)
    country_code = models.CharField(max_length=3, blank=True, null=True)
    gender = models.CharField(max_length=1, blank=True, null=True)
    date_of_birth = models.DateField(blank=True, null=True)
    alt_phone = models.CharField(max_length=12, blank=True, null=True)
    email = models.CharField(max_length=70, blank=True, null=True)
    security_phrase = models.CharField(max_length=100, blank=True, null=True)
    comments = models.CharField(max_length=255, blank=True, null=True)
    called_count = models.SmallIntegerField(blank=True, null=True)
    last_local_call_time = models.DateTimeField(blank=True, null=True)
    rank = models.SmallIntegerField()
    owner = models.CharField(max_length=20, blank=True, null=True)
    entry_list_id = models.BigIntegerField()
    priority = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'original_vicidial_list'


class SfAgent(models.Model):
    sf_id = models.CharField(primary_key=True, max_length=18)
    username = models.CharField(unique=True, max_length=30)
    product_profile = models.CharField(max_length=20)
    shift = models.CharField(max_length=7)
    first_name = models.CharField(max_length=80, blank=True, null=True)
    gender = models.CharField(max_length=1, blank=True, null=True)
    last_name = models.CharField(max_length=80, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sf_agent'


class SfEapp(models.Model):
    sf_id = models.CharField(primary_key=True, max_length=18)
    lead_id = models.IntegerField(blank=True, null=True)
    list_id = models.CharField(max_length=15, blank=True, null=True)
    name = models.CharField(max_length=25)
    phone = models.CharField(max_length=35)
    alt_phone = models.CharField(max_length=35, blank=True, null=True)
    created_date = models.DateTimeField()
    effective_date = models.DateTimeField(blank=True, null=True)
    submitted = models.IntegerField(blank=True, null=True)
    enrollment_date = models.DateTimeField(blank=True, null=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    status = models.CharField(max_length=100)
    agent = models.ForeignKey(SfAgent, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'sf_eapp'


class SfOpportunity(models.Model):
    sf_id = models.CharField(primary_key=True, max_length=18)
    name = models.CharField(max_length=25)
    status = models.CharField(max_length=100)
    secondary_stage = models.CharField(max_length=100, blank=True, null=True)
    phone = models.CharField(max_length=35)
    alt_phone = models.CharField(max_length=35, blank=True, null=True)
    created_date = models.DateTimeField()
    enrollment_date = models.DateTimeField(blank=True, null=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    agent = models.ForeignKey(SfAgent, models.DO_NOTHING, blank=True, null=True)
    eapp = models.ForeignKey(SfEapp, models.DO_NOTHING, unique=True, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sf_opportunity'


class SfarchiveAccount(models.Model):
    id = models.CharField(primary_key=True, max_length=20)
    is_deleted = models.IntegerField()
    name = models.CharField(max_length=255, blank=True, null=True)
    last_name = models.CharField(max_length=80, blank=True, null=True)
    first_name = models.CharField(max_length=40, blank=True, null=True)
    salutation = models.CharField(max_length=40, blank=True, null=True)
    middle_name = models.CharField(max_length=40, blank=True, null=True)
    type = models.CharField(max_length=40, blank=True, null=True)
    billing_street = models.TextField(blank=True, null=True)
    billing_city = models.CharField(max_length=40, blank=True, null=True)
    billing_state = models.CharField(max_length=80, blank=True, null=True)
    billing_postal_code = models.CharField(max_length=20, blank=True, null=True)
    billing_country = models.CharField(max_length=80, blank=True, null=True)
    billing_latitude = models.DecimalField(max_digits=18, decimal_places=15, blank=True, null=True)
    billing_longitude = models.DecimalField(max_digits=18, decimal_places=15, blank=True, null=True)
    billing_geocode_accuracy = models.CharField(max_length=40, blank=True, null=True)
    billing_address = models.TextField(blank=True, null=True)
    shipping_street = models.TextField(blank=True, null=True)
    shipping_city = models.CharField(max_length=40, blank=True, null=True)
    shipping_state = models.CharField(max_length=80, blank=True, null=True)
    shipping_postal_code = models.CharField(max_length=20, blank=True, null=True)
    shipping_country = models.CharField(max_length=80, blank=True, null=True)
    shipping_latitude = models.DecimalField(max_digits=18, decimal_places=15, blank=True, null=True)
    shipping_longitude = models.DecimalField(max_digits=18, decimal_places=15, blank=True, null=True)
    shipping_geocode_accuracy = models.CharField(max_length=40, blank=True, null=True)
    shipping_address = models.TextField(blank=True, null=True)
    phone = models.CharField(max_length=40, blank=True, null=True)
    fax = models.CharField(max_length=40, blank=True, null=True)
    website = models.CharField(max_length=200, blank=True, null=True)
    photo_url = models.CharField(max_length=200, blank=True, null=True)
    industry = models.CharField(max_length=40, blank=True, null=True)
    annual_revenue = models.DecimalField(max_digits=18, decimal_places=0, blank=True, null=True)
    number_of_employees = models.IntegerField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    created_date = models.DateTimeField()
    last_modified_date = models.DateTimeField()
    system_modstamp = models.DateTimeField()
    last_activity_date = models.DateField(blank=True, null=True)
    last_viewed_date = models.DateTimeField(blank=True, null=True)
    last_referenced_date = models.DateTimeField(blank=True, null=True)
    is_person_account = models.IntegerField()
    person_mailing_street = models.TextField(blank=True, null=True)
    person_mailing_city = models.CharField(max_length=40, blank=True, null=True)
    person_mailing_state = models.CharField(max_length=80, blank=True, null=True)
    person_mailing_postal_code = models.CharField(max_length=20, blank=True, null=True)
    person_mailing_country = models.CharField(max_length=80, blank=True, null=True)
    person_mailing_latitude = models.DecimalField(max_digits=18, decimal_places=15, blank=True, null=True)
    person_mailing_longitude = models.DecimalField(max_digits=18, decimal_places=15, blank=True, null=True)
    person_mailing_geocode_accuracy = models.CharField(max_length=40, blank=True, null=True)
    person_mailing_address = models.TextField(blank=True, null=True)
    person_other_street = models.TextField(blank=True, null=True)
    person_other_city = models.CharField(max_length=40, blank=True, null=True)
    person_other_state = models.CharField(max_length=80, blank=True, null=True)
    person_other_postal_code = models.CharField(max_length=20, blank=True, null=True)
    person_other_country = models.CharField(max_length=80, blank=True, null=True)
    person_other_latitude = models.DecimalField(max_digits=18, decimal_places=15, blank=True, null=True)
    person_other_longitude = models.DecimalField(max_digits=18, decimal_places=15, blank=True, null=True)
    person_other_geocode_accuracy = models.CharField(max_length=40, blank=True, null=True)
    person_other_address = models.TextField(blank=True, null=True)
    person_mobile_phone = models.CharField(max_length=40, blank=True, null=True)
    person_home_phone = models.CharField(max_length=40, blank=True, null=True)
    person_other_phone = models.CharField(max_length=40, blank=True, null=True)
    person_assistant_phone = models.CharField(max_length=40, blank=True, null=True)
    person_email = models.CharField(max_length=254, blank=True, null=True)
    person_title = models.CharField(max_length=80, blank=True, null=True)
    person_department = models.CharField(max_length=80, blank=True, null=True)
    person_assistant_name = models.CharField(max_length=40, blank=True, null=True)
    person_lead_source = models.CharField(max_length=40, blank=True, null=True)
    person_birthdate = models.DateField(blank=True, null=True)
    personlastcurequestdate = models.DateTimeField(db_column='PersonLastCURequestDate', blank=True, null=True)  # Field name made lowercase.
    personlastcuupdatedate = models.DateTimeField(db_column='PersonLastCUUpdateDate', blank=True, null=True)  # Field name made lowercase.
    person_email_bounced_reason = models.CharField(max_length=255, blank=True, null=True)
    person_email_bounced_date = models.DateTimeField(blank=True, null=True)
    jigsaw = models.CharField(max_length=20, blank=True, null=True)
    jigsaw_company_id = models.CharField(max_length=20, blank=True, null=True)
    account_source = models.CharField(max_length=40, blank=True, null=True)
    sic_desc = models.CharField(max_length=80, blank=True, null=True)
    alternate_phone_c = models.CharField(db_column='Alternate_Phone__c', max_length=40, blank=True, null=True)  # Field name made lowercase. Field renamed because it contained more than one '_' in a row.
    primary_dob_c = models.DateField(db_column='Primary_DOB__c', blank=True, null=True)  # Field name made lowercase. Field renamed because it contained more than one '_' in a row.
    primary_age_c = models.DecimalField(db_column='Primary_Age__c', max_digits=18, decimal_places=0, blank=True, null=True)  # Field name made lowercase. Field renamed because it contained more than one '_' in a row.
    primary_gender_c = models.CharField(db_column='Primary_Gender__c', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed because it contained more than one '_' in a row.
    primary_height_c = models.CharField(db_column='Primary_Height__c', max_length=80, blank=True, null=True)  # Field name made lowercase. Field renamed because it contained more than one '_' in a row.
    primary_middle_initial_c = models.CharField(db_column='Primary_Middle_Initial__c', max_length=1, blank=True, null=True)  # Field name made lowercase. Field renamed because it contained more than one '_' in a row.
    primary_social_c = models.CharField(db_column='Primary_Social__c', max_length=11, blank=True, null=True)  # Field name made lowercase. Field renamed because it contained more than one '_' in a row.
    primary_weight_c = models.DecimalField(db_column='Primary_Weight__c', max_digits=18, decimal_places=0, blank=True, null=True)  # Field name made lowercase. Field renamed because it contained more than one '_' in a row.
    spouse_first_name_c = models.CharField(db_column='Spouse_First_Name__c', max_length=80, blank=True, null=True)  # Field name made lowercase. Field renamed because it contained more than one '_' in a row.
    spouse_last_name_c = models.CharField(db_column='Spouse_Last_Name__c', max_length=80, blank=True, null=True)  # Field name made lowercase. Field renamed because it contained more than one '_' in a row.
    spouse_middle_initial_c = models.CharField(db_column='Spouse_Middle_Initial__c', max_length=1, blank=True, null=True)  # Field name made lowercase. Field renamed because it contained more than one '_' in a row.
    spouse_dob_c = models.DateField(db_column='Spouse_DOB__c', blank=True, null=True)  # Field name made lowercase. Field renamed because it contained more than one '_' in a row.
    spouse_age_c = models.DecimalField(db_column='Spouse_Age__c', max_digits=18, decimal_places=0, blank=True, null=True)  # Field name made lowercase. Field renamed because it contained more than one '_' in a row.
    spouse_gender_c = models.CharField(db_column='Spouse_Gender__c', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed because it contained more than one '_' in a row.
    spouse_height_c = models.CharField(db_column='Spouse_Height__c', max_length=80, blank=True, null=True)  # Field name made lowercase. Field renamed because it contained more than one '_' in a row.
    spouse_weight_c = models.DecimalField(db_column='Spouse_Weight__c', max_digits=18, decimal_places=0, blank=True, null=True)  # Field name made lowercase. Field renamed because it contained more than one '_' in a row.
    child_1_first_name_c = models.CharField(db_column='Child_1_First_Name__c', max_length=80, blank=True, null=True)  # Field name made lowercase. Field renamed because it contained more than one '_' in a row.
    child_1_middle_initial_c = models.CharField(db_column='Child_1_Middle_Initial__c', max_length=1, blank=True, null=True)  # Field name made lowercase. Field renamed because it contained more than one '_' in a row.
    child_1_last_name_c = models.CharField(db_column='Child_1_Last_Name__c', max_length=80, blank=True, null=True)  # Field name made lowercase. Field renamed because it contained more than one '_' in a row.
    child_1_dob_c = models.DateField(db_column='Child_1_DOB__c', blank=True, null=True)  # Field name made lowercase. Field renamed because it contained more than one '_' in a row.
    child_1_age_c = models.DecimalField(db_column='Child_1_Age__c', max_digits=18, decimal_places=0, blank=True, null=True)  # Field name made lowercase. Field renamed because it contained more than one '_' in a row.
    child_1_gender_c = models.CharField(db_column='Child_1_Gender__c', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed because it contained more than one '_' in a row.
    child_1_height_c = models.CharField(db_column='Child_1_Height__c', max_length=80, blank=True, null=True)  # Field name made lowercase. Field renamed because it contained more than one '_' in a row.
    child_1_weight_c = models.DecimalField(db_column='Child_1_Weight__c', max_digits=18, decimal_places=0, blank=True, null=True)  # Field name made lowercase. Field renamed because it contained more than one '_' in a row.
    child_2_first_name_c = models.CharField(db_column='Child_2_First_Name__c', max_length=80, blank=True, null=True)  # Field name made lowercase. Field renamed because it contained more than one '_' in a row.
    child_2_middle_initial_c = models.CharField(db_column='Child_2_Middle_Initial__c', max_length=1, blank=True, null=True)  # Field name made lowercase. Field renamed because it contained more than one '_' in a row.
    child_2_last_name_c = models.CharField(db_column='Child_2_Last_Name__c', max_length=80, blank=True, null=True)  # Field name made lowercase. Field renamed because it contained more than one '_' in a row.
    child_2_dob_c = models.DateField(db_column='Child_2_DOB__c', blank=True, null=True)  # Field name made lowercase. Field renamed because it contained more than one '_' in a row.
    child_2_age_c = models.DecimalField(db_column='Child_2_Age__c', max_digits=18, decimal_places=0, blank=True, null=True)  # Field name made lowercase. Field renamed because it contained more than one '_' in a row.
    child_2_gender_c = models.CharField(db_column='Child_2_Gender__c', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed because it contained more than one '_' in a row.
    child_2_height_c = models.CharField(db_column='Child_2_Height__c', max_length=80, blank=True, null=True)  # Field name made lowercase. Field renamed because it contained more than one '_' in a row.
    child_2_weight_c = models.DecimalField(db_column='Child_2_Weight__c', max_digits=18, decimal_places=0, blank=True, null=True)  # Field name made lowercase. Field renamed because it contained more than one '_' in a row.
    child_3_first_name_c = models.CharField(db_column='Child_3_First_Name__c', max_length=80, blank=True, null=True)  # Field name made lowercase. Field renamed because it contained more than one '_' in a row.
    child_3_middle_initial_c = models.CharField(db_column='Child_3_Middle_Initial__c', max_length=1, blank=True, null=True)  # Field name made lowercase. Field renamed because it contained more than one '_' in a row.
    child_3_last_name_c = models.CharField(db_column='Child_3_Last_Name__c', max_length=80, blank=True, null=True)  # Field name made lowercase. Field renamed because it contained more than one '_' in a row.
    child_3_dob_c = models.DateField(db_column='Child_3_DOB__c', blank=True, null=True)  # Field name made lowercase. Field renamed because it contained more than one '_' in a row.
    child_3_age_c = models.DecimalField(db_column='Child_3_Age__c', max_digits=18, decimal_places=0, blank=True, null=True)  # Field name made lowercase. Field renamed because it contained more than one '_' in a row.
    child_3_gender_c = models.CharField(db_column='Child_3_Gender__c', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed because it contained more than one '_' in a row.
    child_3_height_c = models.CharField(db_column='Child_3_Height__c', max_length=80, blank=True, null=True)  # Field name made lowercase. Field renamed because it contained more than one '_' in a row.
    child_3_weight_c = models.DecimalField(db_column='Child_3_Weight__c', max_digits=18, decimal_places=0, blank=True, null=True)  # Field name made lowercase. Field renamed because it contained more than one '_' in a row.
    child_4_first_name_c = models.CharField(db_column='Child_4_First_Name__c', max_length=80, blank=True, null=True)  # Field name made lowercase. Field renamed because it contained more than one '_' in a row.
    child_4_middle_initial_c = models.CharField(db_column='Child_4_Middle_Initial__c', max_length=1, blank=True, null=True)  # Field name made lowercase. Field renamed because it contained more than one '_' in a row.
    child_4_last_name_c = models.CharField(db_column='Child_4_Last_Name__c', max_length=80, blank=True, null=True)  # Field name made lowercase. Field renamed because it contained more than one '_' in a row.
    child_4_gender_c = models.CharField(db_column='Child_4_Gender__c', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed because it contained more than one '_' in a row.
    child_4_dob_c = models.DateField(db_column='Child_4_DOB__c', blank=True, null=True)  # Field name made lowercase. Field renamed because it contained more than one '_' in a row.
    child_4_age_c = models.DecimalField(db_column='Child_4_Age__c', max_digits=18, decimal_places=0, blank=True, null=True)  # Field name made lowercase. Field renamed because it contained more than one '_' in a row.
    child_4_height_c = models.CharField(db_column='Child_4_Height__c', max_length=80, blank=True, null=True)  # Field name made lowercase. Field renamed because it contained more than one '_' in a row.
    child_4_weight_c = models.DecimalField(db_column='Child_4_Weight__c', max_digits=18, decimal_places=0, blank=True, null=True)  # Field name made lowercase. Field renamed because it contained more than one '_' in a row.
    number_of_medications_c = models.CharField(db_column='Number_of_Medications__c', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed because it contained more than one '_' in a row.
    pre_existing_conditions_c = models.CharField(db_column='Pre_existing_Conditions__c', max_length=80, blank=True, null=True)  # Field name made lowercase. Field renamed because it contained more than one '_' in a row.
    dr_visits_per_year_c = models.DecimalField(db_column='Dr_Visits_per_Year__c', max_digits=2, decimal_places=0, blank=True, null=True)  # Field name made lowercase. Field renamed because it contained more than one '_' in a row.
    access_id_c = models.CharField(db_column='Access_id__c', max_length=50, blank=True, null=True)  # Field name made lowercase. Field renamed because it contained more than one '_' in a row.
    medication_type_c = models.CharField(db_column='Medication_Type__c', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed because it contained more than one '_' in a row.
    alcohol_or_drug_abuse_c = models.IntegerField(db_column='Alcohol_or_Drug_Abuse__c')  # Field name made lowercase. Field renamed because it contained more than one '_' in a row.
    alzheimer_s_disease_c = models.IntegerField(db_column='Alzheimer_s_Disease__c')  # Field name made lowercase. Field renamed because it contained more than one '_' in a row.
    arterial_disease_c = models.IntegerField(db_column='Arterial_Disease__c')  # Field name made lowercase. Field renamed because it contained more than one '_' in a row.
    bank_location_2_c = models.CharField(db_column='Bank_Location_2__c', max_length=180, blank=True, null=True)  # Field name made lowercase. Field renamed because it contained more than one '_' in a row.
    bank_location_3_c = models.CharField(db_column='Bank_Location_3__c', max_length=180, blank=True, null=True)  # Field name made lowercase. Field renamed because it contained more than one '_' in a row.
    bank_name_2_c = models.CharField(db_column='Bank_Name_2__c', max_length=180, blank=True, null=True)  # Field name made lowercase. Field renamed because it contained more than one '_' in a row.
    bank_name_3_c = models.CharField(db_column='Bank_Name_3__c', max_length=180, blank=True, null=True)  # Field name made lowercase. Field renamed because it contained more than one '_' in a row.
    billing_address_c = models.CharField(db_column='Billing_Address__c', max_length=100, blank=True, null=True)  # Field name made lowercase. Field renamed because it contained more than one '_' in a row.
    billing_city_c = models.CharField(db_column='Billing_City__c', max_length=50, blank=True, null=True)  # Field name made lowercase. Field renamed because it contained more than one '_' in a row.
    billing_state_c = models.CharField(db_column='Billing_State__c', max_length=2, blank=True, null=True)  # Field name made lowercase. Field renamed because it contained more than one '_' in a row.
    billing_zip_c = models.CharField(db_column='Billing_ZIP__c', max_length=10, blank=True, null=True)  # Field name made lowercase. Field renamed because it contained more than one '_' in a row.
    bipolar_disorder_manic_depression_c = models.IntegerField(db_column='Bipolar_Disorder_Manic_Depression__c')  # Field name made lowercase. Field renamed because it contained more than one '_' in a row.
    bone_disease_c = models.IntegerField(db_column='Bone_Disease__c')  # Field name made lowercase. Field renamed because it contained more than one '_' in a row.
    browser = models.CharField(max_length=100, blank=True, null=True)
    cerebrovascular_accident_cva_c = models.IntegerField(db_column='Cerebrovascular_Accident_CVA__c')  # Field name made lowercase. Field renamed because it contained more than one '_' in a row.
    checking_account_2_check_c = models.CharField(db_column='Checking_Account_2_Check__c', max_length=180, blank=True, null=True)  # Field name made lowercase. Field renamed because it contained more than one '_' in a row.
    checking_account_3_check_c = models.CharField(db_column='Checking_Account_3_Check__c', max_length=180, blank=True, null=True)  # Field name made lowercase. Field renamed because it contained more than one '_' in a row.
    checking_account_name_on_the_account_2_c = models.CharField(db_column='Checking_Account_Name_on_the_Account_2__c', max_length=180, blank=True, null=True)  # Field name made lowercase. Field renamed because it contained more than one '_' in a row.
    checking_account_name_on_the_account_3_c = models.CharField(db_column='Checking_Account_Name_on_the_Account_3__c', max_length=180, blank=True, null=True)  # Field name made lowercase. Field renamed because it contained more than one '_' in a row.
    checking_account_number_2_c = models.CharField(db_column='Checking_Account_Number_2__c', max_length=180, blank=True, null=True)  # Field name made lowercase. Field renamed because it contained more than one '_' in a row.
    checking_account_number_3_c = models.CharField(db_column='Checking_Account_Number_3__c', max_length=180, blank=True, null=True)  # Field name made lowercase. Field renamed because it contained more than one '_' in a row.
    chronic_obstructive_lung_disease_cold_c = models.IntegerField(db_column='Chronic_Obstructive_Lung_Disease_COLD__c')  # Field name made lowercase. Field renamed because it contained more than one '_' in a row.
    chronic_obstructive_pulmonary_disease_c_c = models.IntegerField(db_column='Chronic_Obstructive_Pulmonary_Disease_C__c')  # Field name made lowercase. Field renamed because it contained more than one '_' in a row.
    contact_time_c = models.CharField(db_column='Contact_Time__c', max_length=80, blank=True, null=True)  # Field name made lowercase. Field renamed because it contained more than one '_' in a row.
    credit_card_2_address_c = models.CharField(db_column='Credit_Card_2_Address__c', max_length=180, blank=True, null=True)  # Field name made lowercase. Field renamed because it contained more than one '_' in a row.
    credit_card_2_ccv_c = models.CharField(db_column='Credit_Card_2_CCV__c', max_length=18, blank=True, null=True)  # Field name made lowercase. Field renamed because it contained more than one '_' in a row.
    credit_card_2_city_c = models.CharField(db_column='Credit_Card_2_City__c', max_length=180, blank=True, null=True)  # Field name made lowercase. Field renamed because it contained more than one '_' in a row.
    credit_card_2_encrypted_c = models.CharField(db_column='Credit_Card_2_Encrypted__c', max_length=80, blank=True, null=True)  # Field name made lowercase. Field renamed because it contained more than one '_' in a row.
    credit_card_2_expiration_date_c = models.CharField(db_column='Credit_Card_2_Expiration_Date__c', max_length=18, blank=True, null=True)  # Field name made lowercase. Field renamed because it contained more than one '_' in a row.
    credit_card_2_state_c = models.CharField(db_column='Credit_Card_2_State__c', max_length=180, blank=True, null=True)  # Field name made lowercase. Field renamed because it contained more than one '_' in a row.
    credit_card_2_type_c = models.CharField(db_column='Credit_Card_2_Type__c', max_length=300, blank=True, null=True)  # Field name made lowercase. Field renamed because it contained more than one '_' in a row.
    credit_card_2_zip_code_c = models.CharField(db_column='Credit_Card_2_Zip_Code__c', max_length=180, blank=True, null=True)  # Field name made lowercase. Field renamed because it contained more than one '_' in a row.
    credit_card_2_c = models.CharField(db_column='Credit_Card_2__c', max_length=80, blank=True, null=True)  # Field name made lowercase. Field renamed because it contained more than one '_' in a row.
    credit_card_3_address_c = models.CharField(db_column='Credit_Card_3_Address__c', max_length=180, blank=True, null=True)  # Field name made lowercase. Field renamed because it contained more than one '_' in a row.
    credit_card_3_ccv_c = models.CharField(db_column='Credit_Card_3_CCV__c', max_length=18, blank=True, null=True)  # Field name made lowercase. Field renamed because it contained more than one '_' in a row.
    credit_card_3_city_c = models.CharField(db_column='Credit_Card_3_City__c', max_length=180, blank=True, null=True)  # Field name made lowercase. Field renamed because it contained more than one '_' in a row.
    credit_card_3_encrypted_c = models.CharField(db_column='Credit_Card_3_Encrypted__c', max_length=80, blank=True, null=True)  # Field name made lowercase. Field renamed because it contained more than one '_' in a row.
    credit_card_3_expiration_date_c = models.CharField(db_column='Credit_Card_3_Expiration_Date__c', max_length=18, blank=True, null=True)  # Field name made lowercase. Field renamed because it contained more than one '_' in a row.
    credit_card_3_state_c = models.CharField(db_column='Credit_Card_3_State__c', max_length=180, blank=True, null=True)  # Field name made lowercase. Field renamed because it contained more than one '_' in a row.
    credit_card_3_type_c = models.CharField(db_column='Credit_Card_3_Type__c', max_length=300, blank=True, null=True)  # Field name made lowercase. Field renamed because it contained more than one '_' in a row.
    credit_card_3_zip_code_c = models.CharField(db_column='Credit_Card_3_Zip_Code__c', max_length=180, blank=True, null=True)  # Field name made lowercase. Field renamed because it contained more than one '_' in a row.
    credit_card_3_c = models.CharField(db_column='Credit_Card_3__c', max_length=80, blank=True, null=True)  # Field name made lowercase. Field renamed because it contained more than one '_' in a row.
    crohn_s_disease_ileitis_c = models.IntegerField(db_column='Crohn_s_Disease_ileitis__c')  # Field name made lowercase. Field renamed because it contained more than one '_' in a row.
    emphysema = models.IntegerField()
    fibromyalgia = models.IntegerField()
    health_conditions_c = models.CharField(db_column='Health_Conditions__c', max_length=80, blank=True, null=True)  # Field name made lowercase. Field renamed because it contained more than one '_' in a row.
    heart_attack_heart_disease_heart_surge_c = models.IntegerField(db_column='Heart_Attack_Heart_Disease_Heart_Surge__c')  # Field name made lowercase. Field renamed because it contained more than one '_' in a row.
    hepatitis = models.IntegerField()
    ip_address_c = models.CharField(db_column='IP_Address__c', max_length=25, blank=True, null=True)  # Field name made lowercase. Field renamed because it contained more than one '_' in a row.
    insulin_dependent_diabetes_c = models.IntegerField(db_column='Insulin_Dependent_Diabetes__c')  # Field name made lowercase. Field renamed because it contained more than one '_' in a row.
    insurance_aspects_c = models.CharField(db_column='Insurance_Aspects__c', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed because it contained more than one '_' in a row.
    internal_cancer_c = models.IntegerField(db_column='Internal_Cancer__c')  # Field name made lowercase. Field renamed because it contained more than one '_' in a row.
    kidney_disease_c = models.IntegerField(db_column='Kidney_Disease__c')  # Field name made lowercase. Field renamed because it contained more than one '_' in a row.
    lead_date_c = models.DateField(db_column='Lead_Date__c', blank=True, null=True)  # Field name made lowercase. Field renamed because it contained more than one '_' in a row.
    lead_id_c = models.CharField(db_column='Lead_ID__c', max_length=10, blank=True, null=True)  # Field name made lowercase. Field renamed because it contained more than one '_' in a row.
    liver_disease_c = models.IntegerField(db_column='Liver_Disease__c')  # Field name made lowercase. Field renamed because it contained more than one '_' in a row.
    lou_gehrig_s_disease_als_c = models.IntegerField(db_column='Lou_Gehrig_s_Disease_ALS__c')  # Field name made lowercase. Field renamed because it contained more than one '_' in a row.
    lupus_erythematosus_c = models.IntegerField(db_column='Lupus_Erythematosus__c')  # Field name made lowercase. Field renamed because it contained more than one '_' in a row.
    major_depression_c = models.IntegerField(db_column='Major_Depression__c')  # Field name made lowercase. Field renamed because it contained more than one '_' in a row.
    medications = models.CharField(max_length=80, blank=True, null=True)
    melanoma_cancer_c = models.IntegerField(db_column='Melanoma_Cancer__c')  # Field name made lowercase. Field renamed because it contained more than one '_' in a row.
    multiple_sclerosis_c = models.IntegerField(db_column='Multiple_Sclerosis__c')  # Field name made lowercase. Field renamed because it contained more than one '_' in a row.
    muscle_disease_c = models.IntegerField(db_column='Muscle_Disease__c')  # Field name made lowercase. Field renamed because it contained more than one '_' in a row.
    muscular_dystrophy_c = models.IntegerField(db_column='Muscular_Dystrophy__c')  # Field name made lowercase. Field renamed because it contained more than one '_' in a row.
    myositis = models.IntegerField()
    name_of_primary_cc_c = models.CharField(db_column='Name_of_Primary_CC__c', max_length=80, blank=True, null=True)  # Field name made lowercase. Field renamed because it contained more than one '_' in a row.
    name_on_credit_card_2_c = models.CharField(db_column='Name_on_Credit_Card_2__c', max_length=80, blank=True, null=True)  # Field name made lowercase. Field renamed because it contained more than one '_' in a row.
    name_on_credit_card_3_c = models.CharField(db_column='Name_on_Credit_Card_3__c', max_length=80, blank=True, null=True)  # Field name made lowercase. Field renamed because it contained more than one '_' in a row.
    organ_failure_c = models.IntegerField(db_column='Organ_Failure__c')  # Field name made lowercase. Field renamed because it contained more than one '_' in a row.
    organ_transplant_c = models.IntegerField(db_column='Organ_Transplant__c')  # Field name made lowercase. Field renamed because it contained more than one '_' in a row.
    organic_brain_syndrome_c = models.IntegerField(db_column='Organic_Brain_Syndrome__c')  # Field name made lowercase. Field renamed because it contained more than one '_' in a row.
    osteoporosis_w_history_of_bone_fracture_c = models.IntegerField(db_column='Osteoporosis_w_history_of_bone_fracture__c')  # Field name made lowercase. Field renamed because it contained more than one '_' in a row.
    paralysis_any_type_of_degree_c = models.IntegerField(db_column='Paralysis_any_type_of_degree__c')  # Field name made lowercase. Field renamed because it contained more than one '_' in a row.
    peripheral_vascular_disease_c = models.IntegerField(db_column='Peripheral_Vascular_Disease__c')  # Field name made lowercase. Field renamed because it contained more than one '_' in a row.
    primary_bank_location_c = models.CharField(db_column='Primary_Bank_Location__c', max_length=180, blank=True, null=True)  # Field name made lowercase. Field renamed because it contained more than one '_' in a row.
    primary_bank_name_c = models.CharField(db_column='Primary_Bank_Name__c', max_length=180, blank=True, null=True)  # Field name made lowercase. Field renamed because it contained more than one '_' in a row.
    primary_cc_name_c = models.CharField(db_column='Primary_CC_Name__c', max_length=45, blank=True, null=True)  # Field name made lowercase. Field renamed because it contained more than one '_' in a row.
    primary_cc_c = models.CharField(db_column='Primary_CC__c', max_length=80, blank=True, null=True)  # Field name made lowercase. Field renamed because it contained more than one '_' in a row.
    primary_checking_account_check_c = models.CharField(db_column='Primary_Checking_Account_Check__c', max_length=180, blank=True, null=True)  # Field name made lowercase. Field renamed because it contained more than one '_' in a row.
    primary_checking_account_name_on_the_acc_c = models.CharField(db_column='Primary_Checking_Account_Name_on_the_Acc__c', max_length=180, blank=True, null=True)  # Field name made lowercase. Field renamed because it contained more than one '_' in a row.
    primary_checking_account_number_c = models.CharField(db_column='Primary_Checking_Account_Number__c', max_length=180, blank=True, null=True)  # Field name made lowercase. Field renamed because it contained more than one '_' in a row.
    primary_credit_card_address_c = models.CharField(db_column='Primary_Credit_Card_Address__c', max_length=180, blank=True, null=True)  # Field name made lowercase. Field renamed because it contained more than one '_' in a row.
    primary_credit_card_ccv_c = models.CharField(db_column='Primary_Credit_Card_CCV__c', max_length=18, blank=True, null=True)  # Field name made lowercase. Field renamed because it contained more than one '_' in a row.
    primary_credit_card_city_c = models.CharField(db_column='Primary_Credit_Card_City__c', max_length=180, blank=True, null=True)  # Field name made lowercase. Field renamed because it contained more than one '_' in a row.
    primary_credit_card_encrypted_c = models.CharField(db_column='Primary_Credit_Card_Encrypted__c', max_length=80, blank=True, null=True)  # Field name made lowercase. Field renamed because it contained more than one '_' in a row.
    primary_credit_card_expiration_date_c = models.CharField(db_column='Primary_Credit_Card_Expiration_Date__c', max_length=18, blank=True, null=True)  # Field name made lowercase. Field renamed because it contained more than one '_' in a row.
    primary_credit_card_state_c = models.CharField(db_column='Primary_Credit_Card_State__c', max_length=80, blank=True, null=True)  # Field name made lowercase. Field renamed because it contained more than one '_' in a row.
    primary_credit_card_type_c = models.CharField(db_column='Primary_Credit_Card_Type__c', max_length=300, blank=True, null=True)  # Field name made lowercase. Field renamed because it contained more than one '_' in a row.
    primary_credit_card_zip_code_c = models.CharField(db_column='Primary_Credit_Card_Zip_Code__c', max_length=180, blank=True, null=True)  # Field name made lowercase. Field renamed because it contained more than one '_' in a row.
    primary_credit_card_c = models.CharField(db_column='Primary_Credit_Card__c', max_length=80, blank=True, null=True)  # Field name made lowercase. Field renamed because it contained more than one '_' in a row.
    primary_occupation_c = models.CharField(db_column='Primary_Occupation__c', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed because it contained more than one '_' in a row.
    primary_routing_number_c = models.CharField(db_column='Primary_Routing_Number__c', max_length=180, blank=True, null=True)  # Field name made lowercase. Field renamed because it contained more than one '_' in a row.
    primary_social_encrypted_c = models.CharField(db_column='Primary_Social_Encrypted__c', max_length=11, blank=True, null=True)  # Field name made lowercase. Field renamed because it contained more than one '_' in a row.
    residential_address_c = models.CharField(db_column='Residential_Address__c', max_length=100, blank=True, null=True)  # Field name made lowercase. Field renamed because it contained more than one '_' in a row.
    residential_city_c = models.CharField(db_column='Residential_City__c', max_length=50, blank=True, null=True)  # Field name made lowercase. Field renamed because it contained more than one '_' in a row.
    residential_state_c = models.CharField(db_column='Residential_State__c', max_length=2, blank=True, null=True)  # Field name made lowercase. Field renamed because it contained more than one '_' in a row.
    residential_zip_c = models.CharField(db_column='Residential_ZIP__c', max_length=10, blank=True, null=True)  # Field name made lowercase. Field renamed because it contained more than one '_' in a row.
    rheumatoid_arthritis_c = models.IntegerField(db_column='Rheumatoid_Arthritis__c')  # Field name made lowercase. Field renamed because it contained more than one '_' in a row.
    routing_number_2_c = models.CharField(db_column='Routing_Number_2__c', max_length=180, blank=True, null=True)  # Field name made lowercase. Field renamed because it contained more than one '_' in a row.
    routing_number_3_c = models.CharField(db_column='Routing_Number_3__c', max_length=180, blank=True, null=True)  # Field name made lowercase. Field renamed because it contained more than one '_' in a row.
    senile_dementia_c = models.IntegerField(db_column='Senile_Dementia__c')  # Field name made lowercase. Field renamed because it contained more than one '_' in a row.
    session_id_c = models.CharField(db_column='Session_ID__c', max_length=50, blank=True, null=True)  # Field name made lowercase. Field renamed because it contained more than one '_' in a row.
    source_url_c = models.CharField(db_column='Source_URL__c', max_length=100, blank=True, null=True)  # Field name made lowercase. Field renamed because it contained more than one '_' in a row.
    spouse_occupation_c = models.CharField(db_column='Spouse_Occupation__c', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed because it contained more than one '_' in a row.
    stroke = models.IntegerField()
    substance_abuse_c = models.IntegerField(db_column='Substance_Abuse__c')  # Field name made lowercase. Field renamed because it contained more than one '_' in a row.
    tobacco_use_c = models.CharField(db_column='Tobacco_Use__c', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed because it contained more than one '_' in a row.
    transient_ischemic_attach_tia_c = models.IntegerField(db_column='Transient_Ischemic_Attach_TIA__c')  # Field name made lowercase. Field renamed because it contained more than one '_' in a row.
    ulcerative_colitis_c = models.IntegerField(db_column='Ulcerative_Colitis__c')  # Field name made lowercase. Field renamed because it contained more than one '_' in a row.
    unique_id_c = models.CharField(db_column='Unique_Id__c', unique=True, max_length=20)  # Field name made lowercase. Field renamed because it contained more than one '_' in a row.
    vendor_lead_id_c = models.CharField(db_column='Vendor_Lead_ID__c', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed because it contained more than one '_' in a row.
    spouse_social_c = models.CharField(db_column='Spouse_Social__c', max_length=60, blank=True, null=True)  # Field name made lowercase. Field renamed because it contained more than one '_' in a row.
    is_smartphone_c = models.IntegerField(db_column='Is_SmartPhone__c')  # Field name made lowercase. Field renamed because it contained more than one '_' in a row.
    child_1_ssn_c = models.CharField(db_column='Child_1_SSN__c', max_length=11, blank=True, null=True)  # Field name made lowercase. Field renamed because it contained more than one '_' in a row.
    child_2_ssn_c = models.CharField(db_column='Child_2_SSN__c', max_length=11, blank=True, null=True)  # Field name made lowercase. Field renamed because it contained more than one '_' in a row.
    child_3_ssn_c = models.CharField(db_column='Child_3_SSN__c', max_length=11, blank=True, null=True)  # Field name made lowercase. Field renamed because it contained more than one '_' in a row.
    child_4_ssn_c = models.CharField(db_column='Child_4_SSN__c', max_length=11, blank=True, null=True)  # Field name made lowercase. Field renamed because it contained more than one '_' in a row.
    primary_first_name_pc = models.CharField(db_column='Primary_First_Name__pc', max_length=300, blank=True, null=True)  # Field name made lowercase. Field renamed because it contained more than one '_' in a row.
    primary_last_name_pc = models.CharField(db_column='Primary_Last_Name__pc', max_length=300, blank=True, null=True)  # Field name made lowercase. Field renamed because it contained more than one '_' in a row.
    created_by = models.ForeignKey('SfarchiveUser', models.DO_NOTHING)
    last_modified_by = models.ForeignKey('SfarchiveUser', models.DO_NOTHING)
    owner = models.ForeignKey('SfarchiveUser', models.DO_NOTHING)
    person_contact = models.ForeignKey('SfarchiveContact', models.DO_NOTHING, blank=True, null=True)
    master_record_id = models.CharField(max_length=18, blank=True, null=True)
    parent_id = models.CharField(max_length=18, blank=True, null=True)
    record_type_id = models.CharField(max_length=18, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sfarchive_account'


class SfarchiveAgent(models.Model):
    id = models.CharField(primary_key=True, max_length=20)
    owner = models.CharField(max_length=18)
    is_deleted = models.IntegerField()
    name = models.CharField(max_length=80, blank=True, null=True)
    created_date = models.DateTimeField()
    last_modified_date = models.DateTimeField()
    system_modstamp = models.DateTimeField()
    last_viewed_date = models.DateTimeField(blank=True, null=True)
    last_referenced_date = models.DateTimeField(blank=True, null=True)
    first_name_c = models.CharField(db_column='First_Name__c', max_length=80, blank=True, null=True)  # Field name made lowercase. Field renamed because it contained more than one '_' in a row.
    last_name_c = models.CharField(db_column='Last_Name__c', max_length=80, blank=True, null=True)  # Field name made lowercase. Field renamed because it contained more than one '_' in a row.
    can_be_agent_of_record_c = models.IntegerField(db_column='Can_be_Agent_of_Record__c')  # Field name made lowercase. Field renamed because it contained more than one '_' in a row.
    password = models.CharField(max_length=100)
    username = models.CharField(unique=True, max_length=20)
    force_com_enabled_c = models.IntegerField(db_column='Force_com_Enabled__c')  # Field name made lowercase. Field renamed because it contained more than one '_' in a row.
    product_profile_c = models.CharField(db_column='product_profile__c', max_length=255, blank=True, null=True)  # Field renamed because it contained more than one '_' in a row.
    time_shift_c = models.CharField(db_column='Time_Shift__c', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed because it contained more than one '_' in a row.
    verification_agent_c = models.IntegerField(db_column='Verification_Agent__c')  # Field name made lowercase. Field renamed because it contained more than one '_' in a row.
    eapp_admin_c = models.IntegerField(db_column='eApp_Admin__c')  # Field name made lowercase. Field renamed because it contained more than one '_' in a row.
    security_profile_c = models.CharField(db_column='Security_Profile__c', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed because it contained more than one '_' in a row.
    payment_company_c = models.CharField(db_column='Payment_company__c', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed because it contained more than one '_' in a row.
    hii_agent_code_c = models.CharField(db_column='HII_Agent_Code__c', max_length=100, blank=True, null=True)  # Field name made lowercase. Field renamed because it contained more than one '_' in a row.
    commission_profile_c = models.CharField(db_column='Commission_Profile__c', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed because it contained more than one '_' in a row.
    gender = models.CharField(max_length=255, blank=True, null=True)
    status = models.CharField(max_length=255, blank=True, null=True)
    ending_date_c = models.DateField(db_column='Ending_Date__c', blank=True, null=True)  # Field name made lowercase. Field renamed because it contained more than one '_' in a row.
    default_id_c = models.CharField(db_column='Default_Id__c', max_length=100, blank=True, null=True)  # Field name made lowercase. Field renamed because it contained more than one '_' in a row.
    dds_id_c = models.CharField(db_column='DDS_Id__c', max_length=100, blank=True, null=True)  # Field name made lowercase. Field renamed because it contained more than one '_' in a row.
    processing = models.IntegerField()
    getmed_agent_code_c = models.CharField(db_column='GetMed_Agent_Code__c', max_length=100, blank=True, null=True)  # Field name made lowercase. Field renamed because it contained more than one '_' in a row.
    wpa_code_c = models.CharField(db_column='WPA_Code__c', max_length=100, blank=True, null=True)  # Field name made lowercase. Field renamed because it contained more than one '_' in a row.
    created_by = models.ForeignKey('SfarchiveUser', models.DO_NOTHING)
    last_modified_by = models.ForeignKey('SfarchiveUser', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'sfarchive_agent'


class SfarchiveBusinessprocess(models.Model):
    id = models.CharField(primary_key=True, max_length=20)
    name = models.CharField(max_length=80)
    namespace_prefix = models.CharField(max_length=15, blank=True, null=True)
    description = models.CharField(max_length=255, blank=True, null=True)
    table_enum_or_id = models.CharField(max_length=40)
    is_active = models.IntegerField()
    created_date = models.DateTimeField()
    last_modified_date = models.DateTimeField()
    system_modstamp = models.DateTimeField()
    created_by = models.ForeignKey('SfarchiveUser', models.DO_NOTHING)
    last_modified_by = models.ForeignKey('SfarchiveUser', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'sfarchive_businessprocess'


class SfarchiveCallcenter(models.Model):
    id = models.CharField(primary_key=True, max_length=20)
    name = models.CharField(max_length=255)
    internal_name = models.CharField(max_length=240)
    version = models.DecimalField(max_digits=18, decimal_places=3, blank=True, null=True)
    adapter_url = models.TextField(blank=True, null=True)
    custom_settings = models.TextField(blank=True, null=True)
    system_modstamp = models.DateTimeField()
    created_date = models.DateTimeField()
    last_modified_date = models.DateTimeField()
    created_by = models.ForeignKey('SfarchiveUser', models.DO_NOTHING)
    last_modified_by = models.ForeignKey('SfarchiveUser', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'sfarchive_callcenter'


class SfarchiveCampaign(models.Model):
    id = models.CharField(primary_key=True, max_length=20)
    is_deleted = models.IntegerField()
    name = models.CharField(max_length=80)
    type = models.CharField(max_length=40, blank=True, null=True)
    status = models.CharField(max_length=40, blank=True, null=True)
    start_date = models.DateField(blank=True, null=True)
    end_date = models.DateField(blank=True, null=True)
    expected_revenue = models.DecimalField(max_digits=18, decimal_places=0, blank=True, null=True)
    budgeted_cost = models.DecimalField(max_digits=18, decimal_places=0, blank=True, null=True)
    actual_cost = models.DecimalField(max_digits=18, decimal_places=0, blank=True, null=True)
    expected_response = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    number_sent = models.DecimalField(max_digits=18, decimal_places=0, blank=True, null=True)
    is_active = models.IntegerField()
    description = models.TextField(blank=True, null=True)
    number_of_leads = models.IntegerField()
    number_of_converted_leads = models.IntegerField()
    number_of_contacts = models.IntegerField()
    number_of_responses = models.IntegerField()
    number_of_opportunities = models.IntegerField()
    number_of_won_opportunities = models.IntegerField()
    amount_all_opportunities = models.DecimalField(max_digits=18, decimal_places=0)
    amount_won_opportunities = models.DecimalField(max_digits=18, decimal_places=0)
    created_date = models.DateTimeField()
    last_modified_date = models.DateTimeField()
    system_modstamp = models.DateTimeField()
    last_activity_date = models.DateField(blank=True, null=True)
    last_viewed_date = models.DateTimeField(blank=True, null=True)
    last_referenced_date = models.DateTimeField(blank=True, null=True)
    campaign_member_record_type = models.ForeignKey('SfarchiveRecordtype', models.DO_NOTHING, blank=True, null=True)
    created_by = models.ForeignKey('SfarchiveUser', models.DO_NOTHING)
    last_modified_by = models.ForeignKey('SfarchiveUser', models.DO_NOTHING)
    owner = models.ForeignKey('SfarchiveUser', models.DO_NOTHING)
    parent = models.ForeignKey('self', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sfarchive_campaign'


class SfarchiveCase(models.Model):
    id = models.CharField(primary_key=True, max_length=20)
    is_deleted = models.IntegerField()
    case_number = models.CharField(max_length=30)
    supplied_name = models.CharField(max_length=80, blank=True, null=True)
    supplied_email = models.CharField(max_length=254, blank=True, null=True)
    supplied_phone = models.CharField(max_length=40, blank=True, null=True)
    supplied_company = models.CharField(max_length=80, blank=True, null=True)
    type = models.CharField(max_length=40, blank=True, null=True)
    status = models.CharField(max_length=40, blank=True, null=True)
    reason = models.CharField(max_length=40, blank=True, null=True)
    origin = models.CharField(max_length=40, blank=True, null=True)
    subject = models.CharField(max_length=255, blank=True, null=True)
    priority = models.CharField(max_length=40, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    is_closed = models.IntegerField()
    closed_date = models.DateTimeField(blank=True, null=True)
    is_escalated = models.IntegerField()
    owner_id = models.CharField(max_length=18, blank=True, null=True)
    created_date = models.DateTimeField()
    last_modified_date = models.DateTimeField()
    system_modstamp = models.DateTimeField()
    last_viewed_date = models.DateTimeField(blank=True, null=True)
    last_referenced_date = models.DateTimeField(blank=True, null=True)
    disposition = models.CharField(max_length=255, blank=True, null=True)
    escalated_outcome_c = models.CharField(db_column='Escalated_Outcome__c', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed because it contained more than one '_' in a row.
    lock_compliance_c = models.IntegerField(db_column='Lock_Compliance__c')  # Field name made lowercase. Field renamed because it contained more than one '_' in a row.
    account = models.ForeignKey(SfarchiveAccount, models.DO_NOTHING, blank=True, null=True)
    contact = models.ForeignKey('SfarchiveContact', models.DO_NOTHING, blank=True, null=True)
    created_by = models.ForeignKey('SfarchiveUser', models.DO_NOTHING)
    last_modified_by = models.ForeignKey('SfarchiveUser', models.DO_NOTHING)
    parent = models.ForeignKey('self', models.DO_NOTHING, blank=True, null=True)
    record_type = models.ForeignKey('SfarchiveRecordtype', models.DO_NOTHING, blank=True, null=True)
    source = models.ForeignKey('SfarchiveSocialpost', models.DO_NOTHING, blank=True, null=True)
    asset_id = models.CharField(max_length=18, blank=True, null=True)
    is_closed_on_create = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'sfarchive_case'


class SfarchiveContact(models.Model):
    id = models.CharField(primary_key=True, max_length=20)
    is_deleted = models.IntegerField()
    is_person_account = models.IntegerField()
    last_name = models.CharField(max_length=80)
    first_name = models.CharField(max_length=40, blank=True, null=True)
    salutation = models.CharField(max_length=40, blank=True, null=True)
    middle_name = models.CharField(max_length=40, blank=True, null=True)
    name = models.CharField(max_length=121)
    other_street = models.TextField(blank=True, null=True)
    other_city = models.CharField(max_length=40, blank=True, null=True)
    other_state = models.CharField(max_length=80, blank=True, null=True)
    other_postal_code = models.CharField(max_length=20, blank=True, null=True)
    other_country = models.CharField(max_length=80, blank=True, null=True)
    other_latitude = models.DecimalField(max_digits=18, decimal_places=15, blank=True, null=True)
    other_longitude = models.DecimalField(max_digits=18, decimal_places=15, blank=True, null=True)
    other_geocode_accuracy = models.CharField(max_length=40, blank=True, null=True)
    other_address = models.TextField(blank=True, null=True)
    mailing_street = models.TextField(blank=True, null=True)
    mailing_city = models.CharField(max_length=40, blank=True, null=True)
    mailing_state = models.CharField(max_length=80, blank=True, null=True)
    mailing_postal_code = models.CharField(max_length=20, blank=True, null=True)
    mailing_country = models.CharField(max_length=80, blank=True, null=True)
    mailing_latitude = models.DecimalField(max_digits=18, decimal_places=15, blank=True, null=True)
    mailing_longitude = models.DecimalField(max_digits=18, decimal_places=15, blank=True, null=True)
    mailing_geocode_accuracy = models.CharField(max_length=40, blank=True, null=True)
    mailing_address = models.TextField(blank=True, null=True)
    phone = models.CharField(max_length=40, blank=True, null=True)
    fax = models.CharField(max_length=40, blank=True, null=True)
    mobile_phone = models.CharField(max_length=40, blank=True, null=True)
    home_phone = models.CharField(max_length=40, blank=True, null=True)
    other_phone = models.CharField(max_length=40, blank=True, null=True)
    assistant_phone = models.CharField(max_length=40, blank=True, null=True)
    email = models.CharField(max_length=254, blank=True, null=True)
    title = models.CharField(max_length=128, blank=True, null=True)
    department = models.CharField(max_length=80, blank=True, null=True)
    assistant_name = models.CharField(max_length=40, blank=True, null=True)
    lead_source = models.CharField(max_length=40, blank=True, null=True)
    birthdate = models.DateField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    created_date = models.DateTimeField()
    last_modified_date = models.DateTimeField()
    system_modstamp = models.DateTimeField()
    last_activity_date = models.DateField(blank=True, null=True)
    lastcurequestdate = models.DateTimeField(db_column='LastCURequestDate', blank=True, null=True)  # Field name made lowercase.
    lastcuupdatedate = models.DateTimeField(db_column='LastCUUpdateDate', blank=True, null=True)  # Field name made lowercase.
    last_viewed_date = models.DateTimeField(blank=True, null=True)
    last_referenced_date = models.DateTimeField(blank=True, null=True)
    email_bounced_reason = models.CharField(max_length=255, blank=True, null=True)
    email_bounced_date = models.DateTimeField(blank=True, null=True)
    is_email_bounced = models.IntegerField()
    photo_url = models.CharField(max_length=200, blank=True, null=True)
    jigsaw = models.CharField(max_length=20, blank=True, null=True)
    jigsaw_contact_id = models.CharField(max_length=20, blank=True, null=True)
    primary_first_name_c = models.CharField(db_column='Primary_First_Name__c', max_length=300, blank=True, null=True)  # Field name made lowercase. Field renamed because it contained more than one '_' in a row.
    primary_last_name_c = models.CharField(db_column='Primary_Last_Name__c', max_length=300, blank=True, null=True)  # Field name made lowercase. Field renamed because it contained more than one '_' in a row.
    master_record = models.ForeignKey('self', models.DO_NOTHING, blank=True, null=True)
    reports_to = models.ForeignKey('self', models.DO_NOTHING, blank=True, null=True)
    account_id = models.CharField(max_length=18, blank=True, null=True)
    created_by_id = models.CharField(max_length=18, blank=True, null=True)
    last_modified_by_id = models.CharField(max_length=18, blank=True, null=True)
    owner_id = models.CharField(max_length=18, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sfarchive_contact'


class SfarchiveContract(models.Model):
    id = models.CharField(primary_key=True, max_length=20)
    owner_expiration_notice = models.CharField(max_length=40, blank=True, null=True)
    start_date = models.DateField(blank=True, null=True)
    end_date = models.DateField(blank=True, null=True)
    billing_street = models.TextField(blank=True, null=True)
    billing_city = models.CharField(max_length=40, blank=True, null=True)
    billing_state = models.CharField(max_length=80, blank=True, null=True)
    billing_postal_code = models.CharField(max_length=20, blank=True, null=True)
    billing_country = models.CharField(max_length=80, blank=True, null=True)
    billing_latitude = models.DecimalField(max_digits=18, decimal_places=15, blank=True, null=True)
    billing_longitude = models.DecimalField(max_digits=18, decimal_places=15, blank=True, null=True)
    billing_geocode_accuracy = models.CharField(max_length=40, blank=True, null=True)
    billing_address = models.TextField(blank=True, null=True)
    shipping_street = models.TextField(blank=True, null=True)
    shipping_city = models.CharField(max_length=40, blank=True, null=True)
    shipping_state = models.CharField(max_length=80, blank=True, null=True)
    shipping_postal_code = models.CharField(max_length=20, blank=True, null=True)
    shipping_country = models.CharField(max_length=80, blank=True, null=True)
    shipping_latitude = models.DecimalField(max_digits=18, decimal_places=15, blank=True, null=True)
    shipping_longitude = models.DecimalField(max_digits=18, decimal_places=15, blank=True, null=True)
    shipping_geocode_accuracy = models.CharField(max_length=40, blank=True, null=True)
    shipping_address = models.TextField(blank=True, null=True)
    contract_term = models.IntegerField(blank=True, null=True)
    status = models.CharField(max_length=40)
    company_signed_date = models.DateField(blank=True, null=True)
    customer_signed_title = models.CharField(max_length=40, blank=True, null=True)
    customer_signed_date = models.DateField(blank=True, null=True)
    special_terms = models.TextField(blank=True, null=True)
    activated_date = models.DateTimeField(blank=True, null=True)
    status_code = models.CharField(max_length=40)
    description = models.TextField(blank=True, null=True)
    is_deleted = models.IntegerField()
    contract_number = models.CharField(max_length=30)
    last_approved_date = models.DateTimeField(blank=True, null=True)
    created_date = models.DateTimeField()
    last_modified_date = models.DateTimeField()
    system_modstamp = models.DateTimeField()
    last_activity_date = models.DateField(blank=True, null=True)
    last_viewed_date = models.DateTimeField(blank=True, null=True)
    last_referenced_date = models.DateTimeField(blank=True, null=True)
    account = models.ForeignKey(SfarchiveAccount, models.DO_NOTHING)
    activated_by = models.ForeignKey('SfarchiveUser', models.DO_NOTHING, blank=True, null=True)
    company_signed = models.ForeignKey('SfarchiveUser', models.DO_NOTHING, blank=True, null=True)
    created_by = models.ForeignKey('SfarchiveUser', models.DO_NOTHING)
    customer_signed = models.ForeignKey(SfarchiveContact, models.DO_NOTHING, blank=True, null=True)
    last_modified_by = models.ForeignKey('SfarchiveUser', models.DO_NOTHING)
    owner = models.ForeignKey('SfarchiveUser', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'sfarchive_contract'


class SfarchiveExternalsocialaccount(models.Model):
    id = models.CharField(primary_key=True, max_length=20)
    is_deleted = models.IntegerField()
    developer_name = models.CharField(max_length=80)
    language = models.CharField(max_length=40)
    master_label = models.CharField(max_length=80)
    created_date = models.DateTimeField()
    last_modified_date = models.DateTimeField()
    system_modstamp = models.DateTimeField()
    external_account_id = models.CharField(max_length=255)
    username = models.CharField(max_length=255, blank=True, null=True)
    provider = models.CharField(max_length=255)
    provider_user_id = models.CharField(max_length=255)
    externalpictureurl = models.CharField(db_column='ExternalPictureURL', max_length=200, blank=True, null=True)  # Field name made lowercase.
    is_active = models.IntegerField()
    social_property_id = models.CharField(max_length=255, blank=True, null=True)
    is_authenticated = models.IntegerField()
    topic_id = models.CharField(max_length=255, blank=True, null=True)
    data_source_id = models.CharField(max_length=255, blank=True, null=True)
    rule_id = models.CharField(max_length=255, blank=True, null=True)
    is_data_source_active = models.IntegerField()
    unique_name = models.CharField(max_length=255, blank=True, null=True)
    created_by = models.ForeignKey('SfarchiveUser', models.DO_NOTHING)
    default_response_account = models.ForeignKey('self', models.DO_NOTHING, blank=True, null=True)
    last_modified_by = models.ForeignKey('SfarchiveUser', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'sfarchive_externalsocialaccount'


class SfarchiveGroup(models.Model):
    id = models.CharField(primary_key=True, max_length=20)
    name = models.CharField(max_length=40)
    developer_name = models.CharField(max_length=80, blank=True, null=True)
    related = models.CharField(max_length=18, blank=True, null=True)
    type = models.CharField(max_length=40)
    email = models.CharField(max_length=254, blank=True, null=True)
    owner = models.CharField(max_length=20)
    does_send_email_to_members = models.IntegerField()
    does_include_bosses = models.IntegerField()
    created_date = models.DateTimeField()
    last_modified_date = models.DateTimeField()
    system_modstamp = models.DateTimeField()
    created_by = models.ForeignKey('SfarchiveUser', models.DO_NOTHING)
    last_modified_by = models.ForeignKey('SfarchiveUser', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'sfarchive_group'


class SfarchiveNote(models.Model):
    id = models.CharField(primary_key=True, max_length=20)
    is_deleted = models.IntegerField()
    title = models.CharField(max_length=80)
    is_private = models.IntegerField()
    body = models.TextField(blank=True, null=True)
    created_date = models.DateTimeField()
    last_modified_date = models.DateTimeField()
    system_modstamp = models.DateTimeField()
    created_by = models.ForeignKey('SfarchiveUser', models.DO_NOTHING)
    last_modified_by = models.ForeignKey('SfarchiveUser', models.DO_NOTHING)
    owner = models.ForeignKey('SfarchiveUser', models.DO_NOTHING)
    parent_id = models.CharField(max_length=18, blank=True, null=True)
    account_id = models.CharField(max_length=18, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sfarchive_note'


class SfarchiveOpportunity(models.Model):
    id = models.CharField(primary_key=True, max_length=20)
    is_deleted = models.IntegerField()
    is_private = models.IntegerField()
    name = models.CharField(max_length=120)
    description = models.TextField(blank=True, null=True)
    stage_name = models.CharField(max_length=40)
    amount = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    probability = models.DecimalField(max_digits=3, decimal_places=0, blank=True, null=True)
    expected_revenue = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    total_opportunity_quantity = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    close_date = models.DateField()
    type = models.CharField(max_length=40, blank=True, null=True)
    next_step = models.CharField(max_length=255, blank=True, null=True)
    lead_source = models.CharField(max_length=40, blank=True, null=True)
    is_closed = models.IntegerField()
    is_won = models.IntegerField()
    forecast_category = models.CharField(max_length=40)
    forecast_category_name = models.CharField(max_length=40, blank=True, null=True)
    has_opportunity_line_item = models.IntegerField()
    created_date = models.DateTimeField()
    last_modified_date = models.DateTimeField()
    system_modstamp = models.DateTimeField()
    last_activity_date = models.DateField(blank=True, null=True)
    fiscal_quarter = models.IntegerField(blank=True, null=True)
    fiscal_year = models.IntegerField(blank=True, null=True)
    fiscal = models.CharField(max_length=6, blank=True, null=True)
    last_viewed_date = models.DateTimeField(blank=True, null=True)
    last_referenced_date = models.DateTimeField(blank=True, null=True)
    has_open_activity = models.IntegerField()
    has_overdue_task = models.IntegerField()
    name_on_card_c = models.CharField(db_column='Name_on_Card__c', max_length=80, blank=True, null=True)  # Field name made lowercase. Field renamed because it contained more than one '_' in a row.
    credit_card_type_c = models.CharField(db_column='Credit_Card_Type__c', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed because it contained more than one '_' in a row.
    is_post_date = models.IntegerField()
    billing_information_same_c = models.IntegerField(db_column='Billing_Information_Same__c')  # Field name made lowercase. Field renamed because it contained more than one '_' in a row.
    credit_card_address_c = models.CharField(db_column='Credit_Card_Address__c', max_length=80, blank=True, null=True)  # Field name made lowercase. Field renamed because it contained more than one '_' in a row.
    credit_card_city_c = models.CharField(db_column='Credit_Card_City__c', max_length=80, blank=True, null=True)  # Field name made lowercase. Field renamed because it contained more than one '_' in a row.
    credit_card_state_c = models.CharField(db_column='Credit_Card_State__c', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed because it contained more than one '_' in a row.
    credit_card_zip_c = models.CharField(db_column='Credit_Card_Zip__c', max_length=80, blank=True, null=True)  # Field name made lowercase. Field renamed because it contained more than one '_' in a row.
    credit_card_number_c = models.CharField(db_column='Credit_Card_Number__c', max_length=80, blank=True, null=True)  # Field name made lowercase. Field renamed because it contained more than one '_' in a row.
    credit_card_exp_date_c = models.DateField(db_column='Credit_Card_Exp_Date__c', blank=True, null=True)  # Field name made lowercase. Field renamed because it contained more than one '_' in a row.
    credit_card_ccv_c = models.CharField(db_column='Credit_Card_CCV__c', max_length=10, blank=True, null=True)  # Field name made lowercase. Field renamed because it contained more than one '_' in a row.
    checking_account_name_on_the_account_c = models.CharField(db_column='Checking_Account_Name_on_the_Account__c', max_length=80, blank=True, null=True)  # Field name made lowercase. Field renamed because it contained more than one '_' in a row.
    bank_name_c = models.CharField(db_column='Bank_Name__c', max_length=80, blank=True, null=True)  # Field name made lowercase. Field renamed because it contained more than one '_' in a row.
    bank_location_c = models.CharField(db_column='Bank_Location__c', max_length=80, blank=True, null=True)  # Field name made lowercase. Field renamed because it contained more than one '_' in a row.
    routing_number_c = models.CharField(db_column='Routing_Number__c', max_length=80, blank=True, null=True)  # Field name made lowercase. Field renamed because it contained more than one '_' in a row.
    checking_account_number_c = models.CharField(db_column='Checking_Account_Number__c', max_length=80, blank=True, null=True)  # Field name made lowercase. Field renamed because it contained more than one '_' in a row.
    initial_billing_date_c = models.DateField(db_column='Initial_Billing_Date__c', blank=True, null=True)  # Field name made lowercase. Field renamed because it contained more than one '_' in a row.
    todays_date_c = models.DateField(db_column='Todays_Date__c', blank=True, null=True)  # Field name made lowercase. Field renamed because it contained more than one '_' in a row.
    effective_date_c = models.DateField(db_column='Effective_Date__c', blank=True, null=True)  # Field name made lowercase. Field renamed because it contained more than one '_' in a row.
    combined_total_c = models.DecimalField(db_column='Combined_Total__c', max_digits=18, decimal_places=2, blank=True, null=True)  # Field name made lowercase. Field renamed because it contained more than one '_' in a row.
    combined_enrollment_c = models.DecimalField(db_column='Combined_Enrollment__c', max_digits=18, decimal_places=2, blank=True, null=True)  # Field name made lowercase. Field renamed because it contained more than one '_' in a row.
    combined_first_payment_c = models.DecimalField(db_column='Combined_First_Payment__c', max_digits=18, decimal_places=2, blank=True, null=True)  # Field name made lowercase. Field renamed because it contained more than one '_' in a row.
    primary_middle_initial_c = models.CharField(db_column='Primary_Middle_Initial__c', max_length=300, blank=True, null=True)  # Field name made lowercase. Field renamed because it contained more than one '_' in a row.
    agent_id_c = models.CharField(db_column='Agent_ID__c', max_length=80, blank=True, null=True)  # Field name made lowercase. Field renamed because it contained more than one '_' in a row.
    primary_dob_c = models.DateField(db_column='Primary_DOB__c', blank=True, null=True)  # Field name made lowercase. Field renamed because it contained more than one '_' in a row.
    primary_age_c = models.DecimalField(db_column='Primary_Age__c', max_digits=18, decimal_places=0, blank=True, null=True)  # Field name made lowercase. Field renamed because it contained more than one '_' in a row.
    primary_gender_c = models.CharField(db_column='Primary_Gender__c', max_length=10, blank=True, null=True)  # Field name made lowercase. Field renamed because it contained more than one '_' in a row.
    primary_height_c = models.CharField(db_column='Primary_Height__c', max_length=30, blank=True, null=True)  # Field name made lowercase. Field renamed because it contained more than one '_' in a row.
    primary_weight_c = models.DecimalField(db_column='Primary_Weight__c', max_digits=18, decimal_places=0, blank=True, null=True)  # Field name made lowercase. Field renamed because it contained more than one '_' in a row.
    primary_social_c = models.CharField(db_column='Primary_Social__c', max_length=11, blank=True, null=True)  # Field name made lowercase. Field renamed because it contained more than one '_' in a row.
    opportunity_id_c = models.CharField(db_column='Opportunity_ID__c', max_length=30)  # Field name made lowercase. Field renamed because it contained more than one '_' in a row.
    spouse_first_name_c = models.CharField(db_column='Spouse_First_Name__c', max_length=50, blank=True, null=True)  # Field name made lowercase. Field renamed because it contained more than one '_' in a row.
    spouse_middle_initial_c = models.CharField(db_column='Spouse_Middle_Initial__c', max_length=1, blank=True, null=True)  # Field name made lowercase. Field renamed because it contained more than one '_' in a row.
    spouse_last_name_c = models.CharField(db_column='Spouse_Last_Name__c', max_length=50, blank=True, null=True)  # Field name made lowercase. Field renamed because it contained more than one '_' in a row.
    spouse_dob_c = models.DateField(db_column='Spouse_DOB__c', blank=True, null=True)  # Field name made lowercase. Field renamed because it contained more than one '_' in a row.
    spouse_age_c = models.DecimalField(db_column='Spouse_Age__c', max_digits=18, decimal_places=0, blank=True, null=True)  # Field name made lowercase. Field renamed because it contained more than one '_' in a row.
    spouse_gender_c = models.CharField(db_column='Spouse_Gender__c', max_length=10, blank=True, null=True)  # Field name made lowercase. Field renamed because it contained more than one '_' in a row.
    spouse_height_c = models.CharField(db_column='Spouse_Height__c', max_length=30, blank=True, null=True)  # Field name made lowercase. Field renamed because it contained more than one '_' in a row.
    spouse_weight_c = models.DecimalField(db_column='Spouse_Weight__c', max_digits=18, decimal_places=0, blank=True, null=True)  # Field name made lowercase. Field renamed because it contained more than one '_' in a row.
    child_1_first_name_c = models.CharField(db_column='Child_1_First_Name__c', max_length=50, blank=True, null=True)  # Field name made lowercase. Field renamed because it contained more than one '_' in a row.
    child_1_middle_initial_c = models.CharField(db_column='Child_1_Middle_Initial__c', max_length=1, blank=True, null=True)  # Field name made lowercase. Field renamed because it contained more than one '_' in a row.
    child_1_last_name_c = models.CharField(db_column='Child_1_Last_Name__c', max_length=50, blank=True, null=True)  # Field name made lowercase. Field renamed because it contained more than one '_' in a row.
    child_1_dob_c = models.DateField(db_column='Child_1_DOB__c', blank=True, null=True)  # Field name made lowercase. Field renamed because it contained more than one '_' in a row.
    child_1_age_c = models.DecimalField(db_column='Child_1_Age__c', max_digits=18, decimal_places=0, blank=True, null=True)  # Field name made lowercase. Field renamed because it contained more than one '_' in a row.
    child_1_gender_c = models.CharField(db_column='Child_1_Gender__c', max_length=10, blank=True, null=True)  # Field name made lowercase. Field renamed because it contained more than one '_' in a row.
    child_1_height_c = models.CharField(db_column='Child_1_Height__c', max_length=30, blank=True, null=True)  # Field name made lowercase. Field renamed because it contained more than one '_' in a row.
    child_1_weight_c = models.DecimalField(db_column='Child_1_Weight__c', max_digits=18, decimal_places=0, blank=True, null=True)  # Field name made lowercase. Field renamed because it contained more than one '_' in a row.
    child_2_first_name_c = models.CharField(db_column='Child_2_First_Name__c', max_length=50, blank=True, null=True)  # Field name made lowercase. Field renamed because it contained more than one '_' in a row.
    child_2_middle_initial_c = models.CharField(db_column='Child_2_Middle_Initial__c', max_length=1, blank=True, null=True)  # Field name made lowercase. Field renamed because it contained more than one '_' in a row.
    child_2_last_name_c = models.CharField(db_column='Child_2_Last_Name__c', max_length=50, blank=True, null=True)  # Field name made lowercase. Field renamed because it contained more than one '_' in a row.
    child_2_dob_c = models.DateField(db_column='Child_2_DOB__c', blank=True, null=True)  # Field name made lowercase. Field renamed because it contained more than one '_' in a row.
    child_2_age_c = models.DecimalField(db_column='Child_2_Age__c', max_digits=18, decimal_places=0, blank=True, null=True)  # Field name made lowercase. Field renamed because it contained more than one '_' in a row.
    child_2_gender_c = models.CharField(db_column='Child_2_Gender__c', max_length=10, blank=True, null=True)  # Field name made lowercase. Field renamed because it contained more than one '_' in a row.
    child_2_height_c = models.CharField(db_column='Child_2_Height__c', max_length=30, blank=True, null=True)  # Field name made lowercase. Field renamed because it contained more than one '_' in a row.
    child_2_weight_c = models.DecimalField(db_column='Child_2_Weight__c', max_digits=18, decimal_places=0, blank=True, null=True)  # Field name made lowercase. Field renamed because it contained more than one '_' in a row.
    child_3_first_name_c = models.CharField(db_column='Child_3_First_Name__c', max_length=50, blank=True, null=True)  # Field name made lowercase. Field renamed because it contained more than one '_' in a row.
    child_3_gender_c = models.CharField(db_column='Child_3_Gender__c', max_length=10, blank=True, null=True)  # Field name made lowercase. Field renamed because it contained more than one '_' in a row.
    child_4_gender_c = models.CharField(db_column='Child_4_Gender__c', max_length=10, blank=True, null=True)  # Field name made lowercase. Field renamed because it contained more than one '_' in a row.
    child_3_middle_initial_c = models.CharField(db_column='Child_3_Middle_Initial__c', max_length=1, blank=True, null=True)  # Field name made lowercase. Field renamed because it contained more than one '_' in a row.
    child_3_last_name_c = models.CharField(db_column='Child_3_Last_Name__c', max_length=50, blank=True, null=True)  # Field name made lowercase. Field renamed because it contained more than one '_' in a row.
    open_eapp_c = models.CharField(db_column='Open_eApp__c', max_length=300, blank=True, null=True)  # Field name made lowercase. Field renamed because it contained more than one '_' in a row.
    child_3_age_c = models.DecimalField(db_column='Child_3_Age__c', max_digits=18, decimal_places=0, blank=True, null=True)  # Field name made lowercase. Field renamed because it contained more than one '_' in a row.
    child_3_height_c = models.CharField(db_column='Child_3_Height__c', max_length=30, blank=True, null=True)  # Field name made lowercase. Field renamed because it contained more than one '_' in a row.
    child_3_weight_c = models.DecimalField(db_column='Child_3_Weight__c', max_digits=18, decimal_places=0, blank=True, null=True)  # Field name made lowercase. Field renamed because it contained more than one '_' in a row.
    child_4_first_name_c = models.CharField(db_column='Child_4_First_Name__c', max_length=50, blank=True, null=True)  # Field name made lowercase. Field renamed because it contained more than one '_' in a row.
    child_4_middle_initial_c = models.CharField(db_column='Child_4_Middle_Initial__c', max_length=1, blank=True, null=True)  # Field name made lowercase. Field renamed because it contained more than one '_' in a row.
    child_4_last_name_c = models.CharField(db_column='Child_4_Last_Name__c', max_length=50, blank=True, null=True)  # Field name made lowercase. Field renamed because it contained more than one '_' in a row.
    child_4_dob_c = models.DateField(db_column='Child_4_DOB__c', blank=True, null=True)  # Field name made lowercase. Field renamed because it contained more than one '_' in a row.
    child_4_age_c = models.DecimalField(db_column='Child_4_Age__c', max_digits=18, decimal_places=0, blank=True, null=True)  # Field name made lowercase. Field renamed because it contained more than one '_' in a row.
    child_4_height_c = models.CharField(db_column='Child_4_Height__c', max_length=30, blank=True, null=True)  # Field name made lowercase. Field renamed because it contained more than one '_' in a row.
    child_4_weight_c = models.DecimalField(db_column='Child_4_Weight__c', max_digits=18, decimal_places=0, blank=True, null=True)  # Field name made lowercase. Field renamed because it contained more than one '_' in a row.
    child_3_dob_c = models.DateField(db_column='Child_3_DOB__c', blank=True, null=True)  # Field name made lowercase. Field renamed because it contained more than one '_' in a row.
    plan_size_c = models.CharField(db_column='Plan_Size__c', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed because it contained more than one '_' in a row.
    agent_commssion_profile_c = models.CharField(db_column='Agent_Commssion_Profile__c', max_length=300, blank=True, null=True)  # Field name made lowercase. Field renamed because it contained more than one '_' in a row.
    current_insurance_c = models.CharField(db_column='Current_Insurance__c', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed because it contained more than one '_' in a row.
    reason_change_c = models.CharField(db_column='Reason_Change__c', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed because it contained more than one '_' in a row.
    uninsured_length_c = models.CharField(db_column='Uninsured_Length__c', max_length=80, blank=True, null=True)  # Field name made lowercase. Field renamed because it contained more than one '_' in a row.
    pre_existing_conditions_c = models.CharField(db_column='Pre_existing_Conditions__c', max_length=300, blank=True, null=True)  # Field name made lowercase. Field renamed because it contained more than one '_' in a row.
    dr_visits_year_c = models.DecimalField(db_column='Dr_Visits_Year__c', max_digits=18, decimal_places=0, blank=True, null=True)  # Field name made lowercase. Field renamed because it contained more than one '_' in a row.
    total_opp_line_c = models.DecimalField(db_column='Total_Opp_Line__c', max_digits=18, decimal_places=0, blank=True, null=True)  # Field name made lowercase. Field renamed because it contained more than one '_' in a row.
    gi_total_monthly_rate_c = models.DecimalField(db_column='GI_Total_Monthly_Rate__c', max_digits=18, decimal_places=2, blank=True, null=True)  # Field name made lowercase. Field renamed because it contained more than one '_' in a row.
    gi_enrollment_fee_c = models.DecimalField(db_column='GI_Enrollment_Fee__c', max_digits=18, decimal_places=2, blank=True, null=True)  # Field name made lowercase. Field renamed because it contained more than one '_' in a row.
    gi_first_payment_c = models.DecimalField(db_column='GI_First_Payment__c', max_digits=18, decimal_places=2, blank=True, null=True)  # Field name made lowercase. Field renamed because it contained more than one '_' in a row.
    stm_term_length_c = models.DecimalField(db_column='STM_Term_Length__c', max_digits=18, decimal_places=0, blank=True, null=True)  # Field name made lowercase. Field renamed because it contained more than one '_' in a row.
    stm_deductible_c = models.DecimalField(db_column='STM_Deductible__c', max_digits=18, decimal_places=2, blank=True, null=True)  # Field name made lowercase. Field renamed because it contained more than one '_' in a row.
    stm_ci_rate_c = models.DecimalField(db_column='STM_CI_Rate__c', max_digits=18, decimal_places=2, blank=True, null=True)  # Field name made lowercase. Field renamed because it contained more than one '_' in a row.
    stm_fs_add_c = models.DecimalField(db_column='STM_FS_ADD__c', max_digits=18, decimal_places=2, blank=True, null=True)  # Field name made lowercase. Field renamed because it contained more than one '_' in a row.
    stm_ame_c = models.DecimalField(db_column='STM_AME__c', max_digits=18, decimal_places=2, blank=True, null=True)  # Field name made lowercase. Field renamed because it contained more than one '_' in a row.
    stm_total_monthly_c = models.DecimalField(db_column='STM_Total_Monthly__c', max_digits=18, decimal_places=2, blank=True, null=True)  # Field name made lowercase. Field renamed because it contained more than one '_' in a row.
    stm_enrollment_fee_c = models.DecimalField(db_column='STM_Enrollment_Fee__c', max_digits=18, decimal_places=2, blank=True, null=True)  # Field name made lowercase. Field renamed because it contained more than one '_' in a row.
    stm_first_payment_c = models.DecimalField(db_column='STM_First_Payment__c', max_digits=18, decimal_places=2, blank=True, null=True)  # Field name made lowercase. Field renamed because it contained more than one '_' in a row.
    care_rx_c = models.IntegerField(db_column='Care_RX__c')  # Field name made lowercase. Field renamed because it contained more than one '_' in a row.
    rx_total_monthly_rate_c = models.DecimalField(db_column='RX_Total_Monthly_Rate__c', max_digits=18, decimal_places=2, blank=True, null=True)  # Field name made lowercase. Field renamed because it contained more than one '_' in a row.
    rx_first_payment_c = models.DecimalField(db_column='RX_First_Payment__c', max_digits=18, decimal_places=2, blank=True, null=True)  # Field name made lowercase. Field renamed because it contained more than one '_' in a row.
    combined_total_monthly_rate_c = models.DecimalField(db_column='Combined_Total_Monthly_Rate__c', max_digits=18, decimal_places=2, blank=True, null=True)  # Field name made lowercase. Field renamed because it contained more than one '_' in a row.
    combined_enrollment_fee_care_rx_c = models.DecimalField(db_column='Combined_Enrollment_Fee_Care_RX__c', max_digits=18, decimal_places=2, blank=True, null=True)  # Field name made lowercase. Field renamed because it contained more than one '_' in a row.
    combined_first_payment_care_rx_c = models.DecimalField(db_column='Combined_First_Payment_Care_RX__c', max_digits=18, decimal_places=2, blank=True, null=True)  # Field name made lowercase. Field renamed because it contained more than one '_' in a row.
    total_verified_c = models.DecimalField(db_column='Total_Verified__c', max_digits=18, decimal_places=0, blank=True, null=True)  # Field name made lowercase. Field renamed because it contained more than one '_' in a row.
    fidelity_total_monthly_rate_c = models.DecimalField(db_column='Fidelity_Total_Monthly_Rate__c', max_digits=18, decimal_places=2, blank=True, null=True)  # Field name made lowercase. Field renamed because it contained more than one '_' in a row.
    fidelity_face_value_c = models.CharField(db_column='Fidelity_Face_Value__c', max_length=100, blank=True, null=True)  # Field name made lowercase. Field renamed because it contained more than one '_' in a row.
    fidelity = models.CharField(max_length=80, blank=True, null=True)
    primary_beneficiary_c = models.CharField(db_column='Primary_Beneficiary__c', max_length=80, blank=True, null=True)  # Field name made lowercase. Field renamed because it contained more than one '_' in a row.
    contingent_beneficiary_c = models.CharField(db_column='Contingent_Beneficiary__c', max_length=80, blank=True, null=True)  # Field name made lowercase. Field renamed because it contained more than one '_' in a row.
    combined_total_monthly_rate_fidelity_c = models.DecimalField(db_column='Combined_Total_Monthly_Rate_Fidelity__c', max_digits=18, decimal_places=2, blank=True, null=True)  # Field name made lowercase. Field renamed because it contained more than one '_' in a row.
    combined_enrollment_fee_fidelity_c = models.DecimalField(db_column='Combined_Enrollment_Fee_Fidelity__c', max_digits=18, decimal_places=2, blank=True, null=True)  # Field name made lowercase. Field renamed because it contained more than one '_' in a row.
    combined_first_payment_fidelity_c = models.DecimalField(db_column='Combined_First_Payment_Fidelity__c', max_digits=18, decimal_places=2, blank=True, null=True)  # Field name made lowercase. Field renamed because it contained more than one '_' in a row.
    rx_enrollment_fee_c = models.DecimalField(db_column='RX_Enrollment_Fee__c', max_digits=18, decimal_places=2, blank=True, null=True)  # Field name made lowercase. Field renamed because it contained more than one '_' in a row.
    commission_payable_c = models.DecimalField(db_column='Commission_Payable__c', max_digits=18, decimal_places=2, blank=True, null=True)  # Field name made lowercase. Field renamed because it contained more than one '_' in a row.
    verifications_completed_c = models.DecimalField(db_column='Verifications_Completed__c', max_digits=18, decimal_places=0, blank=True, null=True)  # Field name made lowercase. Field renamed because it contained more than one '_' in a row.
    verifications_required_c = models.DecimalField(db_column='Verifications_Required__c', max_digits=18, decimal_places=0, blank=True, null=True)  # Field name made lowercase. Field renamed because it contained more than one '_' in a row.
    adb_enrollment_fee_c = models.DecimalField(db_column='ADB_Enrollment_Fee__c', max_digits=18, decimal_places=2, blank=True, null=True)  # Field name made lowercase. Field renamed because it contained more than one '_' in a row.
    adb_first_payment_c = models.DecimalField(db_column='ADB_First_Payment__c', max_digits=18, decimal_places=2, blank=True, null=True)  # Field name made lowercase. Field renamed because it contained more than one '_' in a row.
    adb_notes_c = models.TextField(db_column='ADB_Notes__c', blank=True, null=True)  # Field name made lowercase. Field renamed because it contained more than one '_' in a row.
    affordable_monthly_rate_c = models.CharField(db_column='Affordable_Monthly_Rate__c', max_length=50, blank=True, null=True)  # Field name made lowercase. Field renamed because it contained more than one '_' in a row.
    agent_first_name_c = models.CharField(db_column='Agent_First_Name__c', max_length=50, blank=True, null=True)  # Field name made lowercase. Field renamed because it contained more than one '_' in a row.
    agent_last_name_c = models.CharField(db_column='Agent_Last_Name__c', max_length=50, blank=True, null=True)  # Field name made lowercase. Field renamed because it contained more than one '_' in a row.
    alcohol_or_drug_abuse_c = models.IntegerField(db_column='Alcohol_or_Drug_Abuse__c')  # Field name made lowercase. Field renamed because it contained more than one '_' in a row.
    alternate_phone_number_c = models.CharField(db_column='Alternate_Phone_Number__c', max_length=300, blank=True, null=True)  # Field name made lowercase. Field renamed because it contained more than one '_' in a row.
    alzheimer_s_disease_c = models.IntegerField(db_column='Alzheimer_s_Disease__c')  # Field name made lowercase. Field renamed because it contained more than one '_' in a row.
    arterial_disease_c = models.IntegerField(db_column='Arterial_Disease__c')  # Field name made lowercase. Field renamed because it contained more than one '_' in a row.
    bank_account_1_account_number_c = models.CharField(db_column='Bank_Account_1_Account_Number__c', max_length=50, blank=True, null=True)  # Field name made lowercase. Field renamed because it contained more than one '_' in a row.
    bank_account_1_bank_location_c = models.CharField(db_column='Bank_Account_1_Bank_Location__c', max_length=300, blank=True, null=True)  # Field name made lowercase. Field renamed because it contained more than one '_' in a row.
    bank_account_1_bank_name_c = models.CharField(db_column='Bank_Account_1_Bank_Name__c', max_length=300, blank=True, null=True)  # Field name made lowercase. Field renamed because it contained more than one '_' in a row.
    bank_account_1_check_number_c = models.CharField(db_column='Bank_Account_1_Check_Number__c', max_length=50, blank=True, null=True)  # Field name made lowercase. Field renamed because it contained more than one '_' in a row.
    bank_account_1_name_on_account_c = models.CharField(db_column='Bank_Account_1_Name_on_Account__c', max_length=300, blank=True, null=True)  # Field name made lowercase. Field renamed because it contained more than one '_' in a row.
    bank_account_1_routing_number_c = models.CharField(db_column='Bank_Account_1_Routing_Number__c', max_length=50, blank=True, null=True)  # Field name made lowercase. Field renamed because it contained more than one '_' in a row.
    bank_account_2_account_number_c = models.CharField(db_column='Bank_Account_2_Account_Number__c', max_length=50, blank=True, null=True)  # Field name made lowercase. Field renamed because it contained more than one '_' in a row.
    bank_account_2_bank_location_c = models.CharField(db_column='Bank_Account_2_Bank_Location__c', max_length=300, blank=True, null=True)  # Field name made lowercase. Field renamed because it contained more than one '_' in a row.
    bank_account_2_bank_name_c = models.CharField(db_column='Bank_Account_2_Bank_Name__c', max_length=300, blank=True, null=True)  # Field name made lowercase. Field renamed because it contained more than one '_' in a row.
    bank_account_2_check_number_c = models.CharField(db_column='Bank_Account_2_Check_Number__c', max_length=50, blank=True, null=True)  # Field name made lowercase. Field renamed because it contained more than one '_' in a row.
    bank_account_2_name_on_account_c = models.CharField(db_column='Bank_Account_2_Name_on_Account__c', max_length=300, blank=True, null=True)  # Field name made lowercase. Field renamed because it contained more than one '_' in a row.
    bank_account_2_routing_number_c = models.CharField(db_column='Bank_Account_2_Routing_Number__c', max_length=50, blank=True, null=True)  # Field name made lowercase. Field renamed because it contained more than one '_' in a row.
    bank_account_3_account_number_c = models.CharField(db_column='Bank_Account_3_Account_Number__c', max_length=50, blank=True, null=True)  # Field name made lowercase. Field renamed because it contained more than one '_' in a row.
    bank_account_3_bank_location_c = models.CharField(db_column='Bank_Account_3_Bank_Location__c', max_length=300, blank=True, null=True)  # Field name made lowercase. Field renamed because it contained more than one '_' in a row.
    bank_account_3_bank_name_c = models.CharField(db_column='Bank_Account_3_Bank_Name__c', max_length=300, blank=True, null=True)  # Field name made lowercase. Field renamed because it contained more than one '_' in a row.
    bank_account_3_check_number_c = models.CharField(db_column='Bank_Account_3_Check_Number__c', max_length=50, blank=True, null=True)  # Field name made lowercase. Field renamed because it contained more than one '_' in a row.
    bank_account_3_name_on_the_account_c = models.CharField(db_column='Bank_Account_3_Name_on_the_Account__c', max_length=300, blank=True, null=True)  # Field name made lowercase. Field renamed because it contained more than one '_' in a row.
    bank_account_3_routing_number_c = models.CharField(db_column='Bank_Account_3_Routing_Number__c', max_length=50, blank=True, null=True)  # Field name made lowercase. Field renamed because it contained more than one '_' in a row.
    bipolar_disorder_manic_depression_c = models.IntegerField(db_column='Bipolar_Disorder_Manic_Depression__c')  # Field name made lowercase. Field renamed because it contained more than one '_' in a row.
    bone_disease_c = models.IntegerField(db_column='Bone_Disease__c')  # Field name made lowercase. Field renamed because it contained more than one '_' in a row.
    cerebrovascular_accident_cva_c = models.IntegerField(db_column='Cerebrovascular_Accident_CVA__c')  # Field name made lowercase. Field renamed because it contained more than one '_' in a row.
    child_1_name_c = models.CharField(db_column='Child_1_Name__c', max_length=100, blank=True, null=True)  # Field name made lowercase. Field renamed because it contained more than one '_' in a row.
    child_2_name_c = models.CharField(db_column='Child_2_Name__c', max_length=100, blank=True, null=True)  # Field name made lowercase. Field renamed because it contained more than one '_' in a row.
    child_3_name_c = models.CharField(db_column='Child_3_Name__c', max_length=100, blank=True, null=True)  # Field name made lowercase. Field renamed because it contained more than one '_' in a row.
    child_4_name_c = models.CharField(db_column='Child_4_Name__c', max_length=100, blank=True, null=True)  # Field name made lowercase. Field renamed because it contained more than one '_' in a row.
    chronic_obst_pulmonary_disease_copd_c = models.IntegerField(db_column='Chronic_Obst_Pulmonary_Disease_COPD__c')  # Field name made lowercase. Field renamed because it contained more than one '_' in a row.
    chronic_obstructive_lung_disease_cold_c = models.IntegerField(db_column='Chronic_Obstructive_Lung_Disease_COLD__c')  # Field name made lowercase. Field renamed because it contained more than one '_' in a row.
    combined_total_monthly_rate_rx_c = models.DecimalField(db_column='Combined_Total_Monthly_Rate_RX__c', max_digits=18, decimal_places=2, blank=True, null=True)  # Field name made lowercase. Field renamed because it contained more than one '_' in a row.
    contact_email_c = models.CharField(db_column='Contact_Email__c', max_length=120, blank=True, null=True)  # Field name made lowercase. Field renamed because it contained more than one '_' in a row.
    contact_mailing_city_c = models.CharField(db_column='Contact_Mailing_City__c', max_length=50, blank=True, null=True)  # Field name made lowercase. Field renamed because it contained more than one '_' in a row.
    contact_mailing_country_c = models.CharField(db_column='Contact_Mailing_Country__c', max_length=50, blank=True, null=True)  # Field name made lowercase. Field renamed because it contained more than one '_' in a row.
    contact_mailing_state_c = models.CharField(db_column='Contact_Mailing_State__c', max_length=50, blank=True, null=True)  # Field name made lowercase. Field renamed because it contained more than one '_' in a row.
    contact_mailing_street_c = models.CharField(db_column='Contact_Mailing_Street__c', max_length=300, blank=True, null=True)  # Field name made lowercase. Field renamed because it contained more than one '_' in a row.
    contact_mailing_zip_c = models.CharField(db_column='Contact_Mailing_Zip__c', max_length=50, blank=True, null=True)  # Field name made lowercase. Field renamed because it contained more than one '_' in a row.
    contingent_beneficiary_dob_c = models.DateField(db_column='Contingent_Beneficiary_DOB__c', blank=True, null=True)  # Field name made lowercase. Field renamed because it contained more than one '_' in a row.
    credit_card_2_billing_address_c = models.CharField(db_column='Credit_Card_2_Billing_Address__c', max_length=300, blank=True, null=True)  # Field name made lowercase. Field renamed because it contained more than one '_' in a row.
    credit_card_2_billing_city_c = models.CharField(db_column='Credit_Card_2_Billing_City__c', max_length=50, blank=True, null=True)  # Field name made lowercase. Field renamed because it contained more than one '_' in a row.
    credit_card_2_billing_state_c = models.CharField(db_column='Credit_Card_2_Billing_State__c', max_length=50, blank=True, null=True)  # Field name made lowercase. Field renamed because it contained more than one '_' in a row.
    credit_card_2_billing_zip_code_c = models.CharField(db_column='Credit_Card_2_Billing_Zip_Code__c', max_length=50, blank=True, null=True)  # Field name made lowercase. Field renamed because it contained more than one '_' in a row.
    credit_card_2_ccv_c = models.CharField(db_column='Credit_Card_2_CCV__c', max_length=10, blank=True, null=True)  # Field name made lowercase. Field renamed because it contained more than one '_' in a row.
    credit_card_2_exp_date_c = models.CharField(db_column='Credit_Card_2_Exp_Date__c', max_length=300, blank=True, null=True)  # Field name made lowercase. Field renamed because it contained more than one '_' in a row.
    credit_card_2_name_on_card_c = models.CharField(db_column='Credit_Card_2_Name_on_Card__c', max_length=300, blank=True, null=True)  # Field name made lowercase. Field renamed because it contained more than one '_' in a row.
    credit_card_2_number_c = models.CharField(db_column='Credit_Card_2_Number__c', max_length=300, blank=True, null=True)  # Field name made lowercase. Field renamed because it contained more than one '_' in a row.
    credit_card_2_type_c = models.CharField(db_column='Credit_Card_2_Type__c', max_length=300, blank=True, null=True)  # Field name made lowercase. Field renamed because it contained more than one '_' in a row.
    credit_card_3_billing_address_c = models.CharField(db_column='Credit_Card_3_Billing_Address__c', max_length=300, blank=True, null=True)  # Field name made lowercase. Field renamed because it contained more than one '_' in a row.
    credit_card_3_billing_city_c = models.CharField(db_column='Credit_Card_3_Billing_CIty__c', max_length=50, blank=True, null=True)  # Field name made lowercase. Field renamed because it contained more than one '_' in a row.
    credit_card_3_billing_state_c = models.CharField(db_column='Credit_Card_3_Billing_State__c', max_length=50, blank=True, null=True)  # Field name made lowercase. Field renamed because it contained more than one '_' in a row.
    credit_card_3_billing_zip_code_c = models.CharField(db_column='Credit_Card_3_Billing_Zip_Code__c', max_length=50, blank=True, null=True)  # Field name made lowercase. Field renamed because it contained more than one '_' in a row.
    credit_card_3_ccv_c = models.CharField(db_column='Credit_Card_3_CCV__c', max_length=10, blank=True, null=True)  # Field name made lowercase. Field renamed because it contained more than one '_' in a row.
    credit_card_3_exp_date_c = models.CharField(db_column='Credit_Card_3_Exp_Date__c', max_length=300, blank=True, null=True)  # Field name made lowercase. Field renamed because it contained more than one '_' in a row.
    credit_card_3_name_on_card_c = models.CharField(db_column='Credit_Card_3_Name_on_Card__c', max_length=300, blank=True, null=True)  # Field name made lowercase. Field renamed because it contained more than one '_' in a row.
    credit_card_3_number_c = models.CharField(db_column='Credit_Card_3_Number__c', max_length=50, blank=True, null=True)  # Field name made lowercase. Field renamed because it contained more than one '_' in a row.
    credit_card_3_type_c = models.CharField(db_column='Credit_Card_3_Type__c', max_length=300, blank=True, null=True)  # Field name made lowercase. Field renamed because it contained more than one '_' in a row.
    crohn_s_disease_ileitis_c = models.IntegerField(db_column='Crohn_s_Disease_ileitis__c')  # Field name made lowercase. Field renamed because it contained more than one '_' in a row.
    currently_insured_c = models.CharField(db_column='Currently_Insured__c', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed because it contained more than one '_' in a row.
    denied_insurance_reason_c = models.CharField(db_column='Denied_Insurance_Reason__c', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed because it contained more than one '_' in a row.
    denied_insurance_c = models.CharField(db_column='Denied_Insurance__c', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed because it contained more than one '_' in a row.
    dental_rx_c = models.CharField(db_column='Dental_RX__c', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed because it contained more than one '_' in a row.
    emphysema = models.IntegerField()
    fibromyalgia = models.IntegerField()
    fidelity_adb_c = models.CharField(db_column='Fidelity_ADB__c', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed because it contained more than one '_' in a row.
    fronter_s_name_c = models.CharField(db_column='Fronter_s_Name__c', max_length=50, blank=True, null=True)  # Field name made lowercase. Field renamed because it contained more than one '_' in a row.
    hii_plan_size_c = models.CharField(db_column='HII_Plan_Size__c', max_length=80, blank=True, null=True)  # Field name made lowercase. Field renamed because it contained more than one '_' in a row.
    hii_plan_type_c = models.CharField(db_column='HII_Plan_Type__c', max_length=80, blank=True, null=True)  # Field name made lowercase. Field renamed because it contained more than one '_' in a row.
    heart_attack_heart_disease_or_surgery_c = models.IntegerField(db_column='Heart_Attack_Heart_Disease_or_Surgery__c')  # Field name made lowercase. Field renamed because it contained more than one '_' in a row.
    hepatitis = models.IntegerField()
    insulin_dependent_diabetes_c = models.IntegerField(db_column='Insulin_Dependent_Diabetes__c')  # Field name made lowercase. Field renamed because it contained more than one '_' in a row.
    internal_cancer_c = models.IntegerField(db_column='Internal_Cancer__c')  # Field name made lowercase. Field renamed because it contained more than one '_' in a row.
    list_id_c = models.CharField(db_column='List_Id__c', max_length=50, blank=True, null=True)  # Field name made lowercase. Field renamed because it contained more than one '_' in a row.
    kidney_disease_c = models.IntegerField(db_column='Kidney_Disease__c')  # Field name made lowercase. Field renamed because it contained more than one '_' in a row.
    liver_disease_c = models.IntegerField(db_column='Liver_Disease__c')  # Field name made lowercase. Field renamed because it contained more than one '_' in a row.
    lou_gehrig_s_disease_als_c = models.IntegerField(db_column='Lou_Gehrig_s_Disease_ALS__c')  # Field name made lowercase. Field renamed because it contained more than one '_' in a row.
    lupus_erythematosus_c = models.IntegerField(db_column='Lupus_Erythematosus__c')  # Field name made lowercase. Field renamed because it contained more than one '_' in a row.
    major_depression_c = models.IntegerField(db_column='Major_Depression__c')  # Field name made lowercase. Field renamed because it contained more than one '_' in a row.
    medication_type_c = models.CharField(db_column='Medication_Type__c', max_length=300, blank=True, null=True)  # Field name made lowercase. Field renamed because it contained more than one '_' in a row.
    melanoma_cancer_c = models.IntegerField(db_column='Melanoma_Cancer__c')  # Field name made lowercase. Field renamed because it contained more than one '_' in a row.
    multiple_sclerosis_c = models.IntegerField(db_column='Multiple_Sclerosis__c')  # Field name made lowercase. Field renamed because it contained more than one '_' in a row.
    muscle_disease_c = models.IntegerField(db_column='Muscle_Disease__c')  # Field name made lowercase. Field renamed because it contained more than one '_' in a row.
    muscular_dystrophy_c = models.IntegerField(db_column='Muscular_Dystrophy__c')  # Field name made lowercase. Field renamed because it contained more than one '_' in a row.
    myositis = models.IntegerField()
    notes_bank_account_1_c = models.TextField(db_column='Notes_Bank_Account_1__c', blank=True, null=True)  # Field name made lowercase. Field renamed because it contained more than one '_' in a row.
    notes_bank_account_2_c = models.TextField(db_column='Notes_Bank_Account_2__c', blank=True, null=True)  # Field name made lowercase. Field renamed because it contained more than one '_' in a row.
    notes_bank_account_3_c = models.TextField(db_column='Notes_Bank_Account_3__c', blank=True, null=True)  # Field name made lowercase. Field renamed because it contained more than one '_' in a row.
    notes_credit_card_1_c = models.TextField(db_column='Notes_Credit_Card_1__c', blank=True, null=True)  # Field name made lowercase. Field renamed because it contained more than one '_' in a row.
    notes_credit_card_2_c = models.TextField(db_column='Notes_Credit_Card_2__c', blank=True, null=True)  # Field name made lowercase. Field renamed because it contained more than one '_' in a row.
    notes_credit_card_3_c = models.TextField(db_column='Notes_Credit_Card_3__c', blank=True, null=True)  # Field name made lowercase. Field renamed because it contained more than one '_' in a row.
    notes_pre_qual_c = models.TextField(db_column='Notes_Pre_Qual__c', blank=True, null=True)  # Field name made lowercase. Field renamed because it contained more than one '_' in a row.
    number_of_medications_c = models.TextField(db_column='Number_of_Medications__c', blank=True, null=True)  # Field name made lowercase. Field renamed because it contained more than one '_' in a row.
    organ_failure_c = models.IntegerField(db_column='Organ_Failure__c')  # Field name made lowercase. Field renamed because it contained more than one '_' in a row.
    organ_transplant_c = models.IntegerField(db_column='Organ_Transplant__c')  # Field name made lowercase. Field renamed because it contained more than one '_' in a row.
    organic_brain_syndrome_c = models.IntegerField(db_column='Organic_Brain_Syndrome__c')  # Field name made lowercase. Field renamed because it contained more than one '_' in a row.
    osteoporosis_w_history_of_bone_fracture_c = models.IntegerField(db_column='Osteoporosis_w_history_of_bone_fracture__c')  # Field name made lowercase. Field renamed because it contained more than one '_' in a row.
    paralysis_any_type_of_degree_c = models.IntegerField(db_column='Paralysis_any_type_of_degree__c')  # Field name made lowercase. Field renamed because it contained more than one '_' in a row.
    payment_method_c = models.CharField(db_column='Payment_Method__c', max_length=80, blank=True, null=True)  # Field name made lowercase. Field renamed because it contained more than one '_' in a row.
    percentage_to_contingent_c = models.DecimalField(db_column='Percentage_to_Contingent__c', max_digits=18, decimal_places=0, blank=True, null=True)  # Field name made lowercase. Field renamed because it contained more than one '_' in a row.
    percentage_to_primary_c = models.DecimalField(db_column='Percentage_to_Primary__c', max_digits=18, decimal_places=0, blank=True, null=True)  # Field name made lowercase. Field renamed because it contained more than one '_' in a row.
    peripheral_vascular_disease_c = models.IntegerField(db_column='Peripheral_Vascular_Disease__c')  # Field name made lowercase. Field renamed because it contained more than one '_' in a row.
    phone_number_c = models.CharField(db_column='Phone_Number__c', max_length=30, blank=True, null=True)  # Field name made lowercase. Field renamed because it contained more than one '_' in a row.
    plan_choice_gi_c = models.CharField(db_column='Plan_Choice_GI__c', max_length=80, blank=True, null=True)  # Field name made lowercase. Field renamed because it contained more than one '_' in a row.
    plan_choice_stm_c = models.CharField(db_column='Plan_Choice_STM__c', max_length=80, blank=True, null=True)  # Field name made lowercase. Field renamed because it contained more than one '_' in a row.
    primary_beneficiary_dob_c = models.DateField(db_column='Primary_Beneficiary_DOB__c', blank=True, null=True)  # Field name made lowercase. Field renamed because it contained more than one '_' in a row.
    primary_occupation_c = models.CharField(db_column='Primary_Occupation__c', max_length=300, blank=True, null=True)  # Field name made lowercase. Field renamed because it contained more than one '_' in a row.
    product_code_string_c = models.CharField(db_column='Product_Code_String__c', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed because it contained more than one '_' in a row.
    refund_amount_c = models.DecimalField(db_column='Refund_Amount__c', max_digits=18, decimal_places=2, blank=True, null=True)  # Field name made lowercase. Field renamed because it contained more than one '_' in a row.
    relationship_to_contingent_c = models.CharField(db_column='Relationship_to_Contingent__c', max_length=100, blank=True, null=True)  # Field name made lowercase. Field renamed because it contained more than one '_' in a row.
    relationship_to_primary_c = models.CharField(db_column='Relationship_to_Primary__c', max_length=100, blank=True, null=True)  # Field name made lowercase. Field renamed because it contained more than one '_' in a row.
    residential_address_c = models.CharField(db_column='Residential_Address__c', max_length=300, blank=True, null=True)  # Field name made lowercase. Field renamed because it contained more than one '_' in a row.
    residential_city_c = models.CharField(db_column='Residential_City__c', max_length=50, blank=True, null=True)  # Field name made lowercase. Field renamed because it contained more than one '_' in a row.
    residential_state_c = models.CharField(db_column='Residential_State__c', max_length=50, blank=True, null=True)  # Field name made lowercase. Field renamed because it contained more than one '_' in a row.
    residential_zip_c = models.CharField(db_column='Residential_ZIP__c', max_length=50, blank=True, null=True)  # Field name made lowercase. Field renamed because it contained more than one '_' in a row.
    rewrite_number_c = models.CharField(db_column='Rewrite_Number__c', max_length=100, blank=True, null=True)  # Field name made lowercase. Field renamed because it contained more than one '_' in a row.
    rheumatoid_arthritis_c = models.IntegerField(db_column='Rheumatoid_Arthritis__c')  # Field name made lowercase. Field renamed because it contained more than one '_' in a row.
    stm_hm_rate_c = models.DecimalField(db_column='STM_HM_Rate__c', max_digits=18, decimal_places=2, blank=True, null=True)  # Field name made lowercase. Field renamed because it contained more than one '_' in a row.
    stm_monthly_rate_for_selected_plan_c = models.DecimalField(db_column='STM_Monthly_Rate_for_Selected_Plan__c', max_digits=18, decimal_places=2, blank=True, null=True)  # Field name made lowercase. Field renamed because it contained more than one '_' in a row.
    senile_dementia_c = models.IntegerField(db_column='Senile_Dementia__c')  # Field name made lowercase. Field renamed because it contained more than one '_' in a row.
    spouse_name_c = models.CharField(db_column='Spouse_Name__c', max_length=100, blank=True, null=True)  # Field name made lowercase. Field renamed because it contained more than one '_' in a row.
    spouse_occupation_c = models.CharField(db_column='Spouse_Occupation__c', max_length=50, blank=True, null=True)  # Field name made lowercase. Field renamed because it contained more than one '_' in a row.
    start_date_c = models.DateField(db_column='Start_Date__c', blank=True, null=True)  # Field name made lowercase. Field renamed because it contained more than one '_' in a row.
    stroke = models.IntegerField()
    substance_abuse_c = models.IntegerField(db_column='Substance_Abuse__c')  # Field name made lowercase. Field renamed because it contained more than one '_' in a row.
    tcpa_verification_c = models.IntegerField(db_column='TCPA_Verification__c')  # Field name made lowercase. Field renamed because it contained more than one '_' in a row.
    tobacco_use_c = models.CharField(db_column='Tobacco_Use__c', max_length=300, blank=True, null=True)  # Field name made lowercase. Field renamed because it contained more than one '_' in a row.
    transient_ischemic_attach_tia_c = models.IntegerField(db_column='Transient_Ischemic_Attach_TIA__c')  # Field name made lowercase. Field renamed because it contained more than one '_' in a row.
    type_of_rewrite_c = models.CharField(db_column='Type_of_Rewrite__c', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed because it contained more than one '_' in a row.
    ulcerative_colitis_c = models.IntegerField(db_column='Ulcerative_Colitis__c')  # Field name made lowercase. Field renamed because it contained more than one '_' in a row.
    agent_username_c = models.CharField(db_column='Agent_Username__c', max_length=50, blank=True, null=True)  # Field name made lowercase. Field renamed because it contained more than one '_' in a row.
    verifications1_required_c = models.DecimalField(db_column='Verifications1_Required__c', max_digits=18, decimal_places=0, blank=True, null=True)  # Field name made lowercase. Field renamed because it contained more than one '_' in a row.
    products_with_policy_number_c = models.DecimalField(db_column='Products_With_Policy_Number__c', max_digits=1, decimal_places=0, blank=True, null=True)  # Field name made lowercase. Field renamed because it contained more than one '_' in a row.
    is_created_from_vici_dial_c = models.IntegerField(db_column='Is_Created_From_Vici_Dial__c')  # Field name made lowercase. Field renamed because it contained more than one '_' in a row.
    uninsured_length_months_c = models.CharField(db_column='Uninsured_Length_Months__c', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed because it contained more than one '_' in a row.
    spouse_social_c = models.CharField(db_column='Spouse_Social__c', max_length=11, blank=True, null=True)  # Field name made lowercase. Field renamed because it contained more than one '_' in a row.
    credit_card_1_billing_address_c = models.CharField(db_column='Credit_Card_1_Billing_Address__c', max_length=300, blank=True, null=True)  # Field name made lowercase. Field renamed because it contained more than one '_' in a row.
    credit_card_1_billing_city_c = models.CharField(db_column='Credit_Card_1_Billing_City__c', max_length=50, blank=True, null=True)  # Field name made lowercase. Field renamed because it contained more than one '_' in a row.
    credit_card_1_billing_state_c = models.CharField(db_column='Credit_Card_1_Billing_State__c', max_length=50, blank=True, null=True)  # Field name made lowercase. Field renamed because it contained more than one '_' in a row.
    credit_card_1_billing_zip_code_c = models.CharField(db_column='Credit_Card_1_Billing_Zip_Code__c', max_length=50, blank=True, null=True)  # Field name made lowercase. Field renamed because it contained more than one '_' in a row.
    credit_card_1_ccv_c = models.CharField(db_column='Credit_Card_1_CCV__c', max_length=5, blank=True, null=True)  # Field name made lowercase. Field renamed because it contained more than one '_' in a row.
    credit_card_1_exp_date_c = models.CharField(db_column='Credit_Card_1_Exp_Date__c', max_length=300, blank=True, null=True)  # Field name made lowercase. Field renamed because it contained more than one '_' in a row.
    credit_card_1_name_on_card_c = models.CharField(db_column='Credit_Card_1_Name_on_Card__c', max_length=300, blank=True, null=True)  # Field name made lowercase. Field renamed because it contained more than one '_' in a row.
    credit_card_1_number_c = models.CharField(db_column='Credit_Card_1_Number__c', max_length=300, blank=True, null=True)  # Field name made lowercase. Field renamed because it contained more than one '_' in a row.
    credit_card_1_type_c = models.CharField(db_column='Credit_Card_1_Type__c', max_length=300, blank=True, null=True)  # Field name made lowercase. Field renamed because it contained more than one '_' in a row.
    health_plan_type_c = models.CharField(db_column='Health_Plan_Type__c', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed because it contained more than one '_' in a row.
    preexisting_notes_c = models.TextField(db_column='PreExisting_Notes__c', blank=True, null=True)  # Field name made lowercase. Field renamed because it contained more than one '_' in a row.
    sale_notes_c = models.TextField(db_column='Sale_Notes__c', blank=True, null=True)  # Field name made lowercase. Field renamed because it contained more than one '_' in a row.
    combined_tax_c = models.DecimalField(db_column='Combined_Tax__c', max_digits=18, decimal_places=2, blank=True, null=True)  # Field name made lowercase. Field renamed because it contained more than one '_' in a row.
    adb2_contingent_beneficiary_c = models.CharField(db_column='ADB2_Contingent_Beneficiary__c', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed because it contained more than one '_' in a row.
    adb2_contingent_date_of_birth_c = models.DateField(db_column='ADB2_Contingent_Date_of_Birth__c', blank=True, null=True)  # Field name made lowercase. Field renamed because it contained more than one '_' in a row.
    adb2_contingent_percentage_c = models.DecimalField(db_column='ADB2_Contingent_Percentage__c', max_digits=18, decimal_places=2, blank=True, null=True)  # Field name made lowercase. Field renamed because it contained more than one '_' in a row.
    adb2_contingent_relationship_c = models.CharField(db_column='ADB2_Contingent_Relationship__c', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed because it contained more than one '_' in a row.
    adb2_notes_c = models.TextField(db_column='ADB2_Notes__c', blank=True, null=True)  # Field name made lowercase. Field renamed because it contained more than one '_' in a row.
    adb2_primary_beneficiary_percentage_c = models.DecimalField(db_column='ADB2_Primary_Beneficiary_Percentage__c', max_digits=18, decimal_places=2, blank=True, null=True)  # Field name made lowercase. Field renamed because it contained more than one '_' in a row.
    adb2_primary_beneficiary_relationship_c = models.CharField(db_column='ADB2_Primary_Beneficiary_Relationship__c', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed because it contained more than one '_' in a row.
    adb2_primary_beneficiary_c = models.TextField(db_column='ADB2_Primary_Beneficiary__c', blank=True, null=True)  # Field name made lowercase. Field renamed because it contained more than one '_' in a row.
    adb2_primary_date_of_birth_c = models.DateField(db_column='ADB2_Primary_Date_of_Birth__c', blank=True, null=True)  # Field name made lowercase. Field renamed because it contained more than one '_' in a row.
    adb_notes2_c = models.TextField(db_column='ADB_Notes2__c', blank=True, null=True)  # Field name made lowercase. Field renamed because it contained more than one '_' in a row.
    asthma = models.IntegerField()
    cholesterol = models.IntegerField()
    current_insurance_rate_c = models.DecimalField(db_column='Current_Insurance_Rate__c', max_digits=18, decimal_places=2, blank=True, null=True)  # Field name made lowercase. Field renamed because it contained more than one '_' in a row.
    high_blood_pressure_hypertension_c = models.IntegerField(db_column='High_Blood_Pressure_Hypertension__c')  # Field name made lowercase. Field renamed because it contained more than one '_' in a row.
    thyroid = models.IntegerField()
    eappform_c = models.CharField(db_column='eAppForm__c', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed because it contained more than one '_' in a row.
    secondary_stage_c = models.CharField(db_column='Secondary_Stage__c', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed because it contained more than one '_' in a row.
    agent_profile_c = models.TextField(db_column='agent_profile__c', blank=True, null=True)  # Field renamed because it contained more than one '_' in a row.
    is_fresh_sale_c = models.IntegerField(db_column='Is_Fresh_Sale__c')  # Field name made lowercase. Field renamed because it contained more than one '_' in a row.
    account = models.ForeignKey(SfarchiveAccount, models.DO_NOTHING, blank=True, null=True)
    adb2_product_c = models.ForeignKey('SfarchiveProduct2', models.DO_NOTHING, db_column='ADB2_Product__c', blank=True, null=True)  # Field name made lowercase. Field renamed because it contained more than one '_' in a row.
    agent_id_lookup_c = models.ForeignKey(SfarchiveAgent, models.DO_NOTHING, db_column='Agent_ID_Lookup__c', blank=True, null=True)  # Field name made lowercase. Field renamed because it contained more than one '_' in a row.
    agent_of_record_c = models.ForeignKey(SfarchiveAgent, models.DO_NOTHING, db_column='Agent_of_Record__c', blank=True, null=True)  # Field name made lowercase. Field renamed because it contained more than one '_' in a row.
    agent_verification_c = models.ForeignKey(SfarchiveAgent, models.DO_NOTHING, db_column='Agent_Verification__c', blank=True, null=True)  # Field name made lowercase. Field renamed because it contained more than one '_' in a row.
    campaign = models.ForeignKey(SfarchiveCampaign, models.DO_NOTHING, blank=True, null=True)
    contract = models.ForeignKey(SfarchiveContract, models.DO_NOTHING, blank=True, null=True)
    created_by = models.ForeignKey('SfarchiveUser', models.DO_NOTHING)
    gi_product_c = models.ForeignKey('SfarchiveProduct2', models.DO_NOTHING, db_column='GI_Product__c', blank=True, null=True)  # Field name made lowercase. Field renamed because it contained more than one '_' in a row.
    last_modified_by = models.ForeignKey('SfarchiveUser', models.DO_NOTHING)
    owner = models.ForeignKey('SfarchiveUser', models.DO_NOTHING)
    pricebook2 = models.ForeignKey('SfarchivePricebook2', models.DO_NOTHING, blank=True, null=True)
    record_type = models.ForeignKey('SfarchiveRecordtype', models.DO_NOTHING, blank=True, null=True)
    sales_board_product_type = models.ForeignKey('SfarchiveSalesboardproducttype', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sfarchive_opportunity'


class SfarchiveOrganization(models.Model):
    id = models.CharField(primary_key=True, max_length=20)
    name = models.CharField(max_length=80)
    division = models.CharField(max_length=80, blank=True, null=True)
    street = models.TextField(blank=True, null=True)
    city = models.CharField(max_length=40, blank=True, null=True)
    state = models.CharField(max_length=80, blank=True, null=True)
    postal_code = models.CharField(max_length=20, blank=True, null=True)
    country = models.CharField(max_length=80, blank=True, null=True)
    latitude = models.DecimalField(max_digits=18, decimal_places=15, blank=True, null=True)
    longitude = models.DecimalField(max_digits=18, decimal_places=15, blank=True, null=True)
    geocode_accuracy = models.CharField(max_length=40, blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    phone = models.CharField(max_length=40, blank=True, null=True)
    fax = models.CharField(max_length=40, blank=True, null=True)
    primary_contact = models.CharField(max_length=80, blank=True, null=True)
    default_locale_sid_key = models.CharField(max_length=40)
    language_locale_key = models.CharField(max_length=40)
    receives_info_emails = models.IntegerField()
    receives_admin_info_emails = models.IntegerField()
    preferences_require_opportunity_products = models.IntegerField()
    fiscal_year_start_month = models.IntegerField(blank=True, null=True)
    uses_start_date_as_fiscal_year_name = models.IntegerField()
    default_account_access = models.CharField(max_length=40, blank=True, null=True)
    default_contact_access = models.CharField(max_length=40, blank=True, null=True)
    default_opportunity_access = models.CharField(max_length=40, blank=True, null=True)
    default_lead_access = models.CharField(max_length=40, blank=True, null=True)
    default_case_access = models.CharField(max_length=40, blank=True, null=True)
    default_calendar_access = models.CharField(max_length=40, blank=True, null=True)
    default_pricebook_access = models.CharField(max_length=40, blank=True, null=True)
    default_campaign_access = models.CharField(max_length=40, blank=True, null=True)
    system_modstamp = models.DateTimeField()
    compliance_bcc_email = models.CharField(max_length=254, blank=True, null=True)
    ui_skin = models.CharField(max_length=40, blank=True, null=True)
    signup_country_iso_code = models.CharField(max_length=2, blank=True, null=True)
    trial_expiration_date = models.DateTimeField(blank=True, null=True)
    organization_type = models.CharField(max_length=40, blank=True, null=True)
    namespace_prefix = models.CharField(max_length=15, blank=True, null=True)
    instance_name = models.CharField(max_length=5, blank=True, null=True)
    is_sandbox = models.IntegerField()
    web_to_case_default_origin = models.CharField(max_length=40, blank=True, null=True)
    monthly_page_views_used = models.IntegerField(blank=True, null=True)
    monthly_page_views_entitlement = models.IntegerField(blank=True, null=True)
    is_read_only = models.IntegerField()
    created_date = models.DateTimeField()
    last_modified_date = models.DateTimeField()
    created_by = models.ForeignKey('SfarchiveUser', models.DO_NOTHING)
    last_modified_by = models.ForeignKey('SfarchiveUser', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'sfarchive_organization'


class SfarchivePricebook2(models.Model):
    id = models.CharField(primary_key=True, max_length=20)
    is_deleted = models.IntegerField()
    name = models.CharField(max_length=255)
    created_date = models.DateTimeField()
    last_modified_date = models.DateTimeField()
    system_modstamp = models.DateTimeField()
    last_viewed_date = models.DateTimeField(blank=True, null=True)
    last_referenced_date = models.DateTimeField(blank=True, null=True)
    is_active = models.IntegerField()
    description = models.CharField(max_length=255, blank=True, null=True)
    is_standard = models.IntegerField()
    created_by = models.ForeignKey('SfarchiveUser', models.DO_NOTHING)
    last_modified_by = models.ForeignKey('SfarchiveUser', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'sfarchive_pricebook2'


class SfarchiveProduct2(models.Model):
    id = models.CharField(primary_key=True, max_length=20)
    name = models.CharField(max_length=255)
    product_code = models.CharField(max_length=255, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    revenue_schedule_type = models.CharField(max_length=40, blank=True, null=True)
    revenue_installment_period = models.CharField(max_length=40, blank=True, null=True)
    number_of_revenue_installments = models.IntegerField(blank=True, null=True)
    can_use_revenue_schedule = models.IntegerField()
    is_active = models.IntegerField()
    created_date = models.DateTimeField()
    last_modified_date = models.DateTimeField()
    system_modstamp = models.DateTimeField()
    family = models.CharField(max_length=40, blank=True, null=True)
    is_deleted = models.IntegerField()
    last_viewed_date = models.DateTimeField(blank=True, null=True)
    last_referenced_date = models.DateTimeField(blank=True, null=True)
    plan_type_c = models.CharField(db_column='Plan_Type__c', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed because it contained more than one '_' in a row.
    monthly_rate_c = models.DecimalField(db_column='Monthly_Rate__c', max_digits=18, decimal_places=2, blank=True, null=True)  # Field name made lowercase. Field renamed because it contained more than one '_' in a row.
    enrollment_fee_c = models.DecimalField(db_column='Enrollment_Fee__c', max_digits=18, decimal_places=2, blank=True, null=True)  # Field name made lowercase. Field renamed because it contained more than one '_' in a row.
    first_payment_c = models.DecimalField(db_column='First_Payment__c', max_digits=18, decimal_places=2, blank=True, null=True)  # Field name made lowercase. Field renamed because it contained more than one '_' in a row.
    product_id_c = models.CharField(db_column='Product_ID__c', max_length=30)  # Field name made lowercase. Field renamed because it contained more than one '_' in a row.
    advances = models.CharField(max_length=180, blank=True, null=True)
    chargeback_allowance_months_c = models.DecimalField(db_column='Chargeback_Allowance_Months__c', max_digits=18, decimal_places=0, blank=True, null=True)  # Field name made lowercase. Field renamed because it contained more than one '_' in a row.
    commissionable = models.IntegerField()
    creates_plan_c = models.IntegerField(db_column='Creates_Plan__c')  # Field name made lowercase. Field renamed because it contained more than one '_' in a row.
    flat_commission_c = models.DecimalField(db_column='Flat_Commission__c', max_digits=18, decimal_places=2, blank=True, null=True)  # Field name made lowercase. Field renamed because it contained more than one '_' in a row.
    is_stm_c = models.IntegerField(db_column='Is_STM__c')  # Field name made lowercase. Field renamed because it contained more than one '_' in a row.
    monthly_rate_hbc_c = models.DecimalField(db_column='Monthly_Rate_HBC__c', max_digits=18, decimal_places=2, blank=True, null=True)  # Field name made lowercase. Field renamed because it contained more than one '_' in a row.
    no_of_advances_c = models.DecimalField(db_column='No_of_Advances__c', max_digits=18, decimal_places=0, blank=True, null=True)  # Field name made lowercase. Field renamed because it contained more than one '_' in a row.
    payment_terms_c = models.CharField(db_column='Payment_Terms__c', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed because it contained more than one '_' in a row.
    plan_package_c = models.CharField(db_column='Plan_Package__c', max_length=180, blank=True, null=True)  # Field name made lowercase. Field renamed because it contained more than one '_' in a row.
    need_recording_c = models.IntegerField(db_column='Need_Recording__c')  # Field name made lowercase. Field renamed because it contained more than one '_' in a row.
    no_of_revenue_installments_c = models.DecimalField(db_column='No_of_Revenue_Installments__c', max_digits=4, decimal_places=0, blank=True, null=True)  # Field name made lowercase. Field renamed because it contained more than one '_' in a row.
    stm_rate_type_c = models.CharField(db_column='STM_Rate_Type__c', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed because it contained more than one '_' in a row.
    is_variable_price_c = models.IntegerField(db_column='Is_Variable_Price__c')  # Field name made lowercase. Field renamed because it contained more than one '_' in a row.
    renewal_year_10_c = models.DecimalField(db_column='Renewal_Year_10__c', max_digits=5, decimal_places=2, blank=True, null=True)  # Field name made lowercase. Field renamed because it contained more than one '_' in a row.
    renewal_year_2_c = models.DecimalField(db_column='Renewal_Year_2__c', max_digits=5, decimal_places=2, blank=True, null=True)  # Field name made lowercase. Field renamed because it contained more than one '_' in a row.
    renewal_year_3_c = models.DecimalField(db_column='Renewal_Year_3__c', max_digits=5, decimal_places=2, blank=True, null=True)  # Field name made lowercase. Field renamed because it contained more than one '_' in a row.
    renewal_year_4_c = models.DecimalField(db_column='Renewal_Year_4__c', max_digits=5, decimal_places=2, blank=True, null=True)  # Field name made lowercase. Field renamed because it contained more than one '_' in a row.
    renewal_year_5_c = models.DecimalField(db_column='Renewal_Year_5__c', max_digits=5, decimal_places=2, blank=True, null=True)  # Field name made lowercase. Field renamed because it contained more than one '_' in a row.
    renewal_year_6_c = models.DecimalField(db_column='Renewal_Year_6__c', max_digits=5, decimal_places=2, blank=True, null=True)  # Field name made lowercase. Field renamed because it contained more than one '_' in a row.
    renewal_year_7_c = models.DecimalField(db_column='Renewal_Year_7__c', max_digits=5, decimal_places=2, blank=True, null=True)  # Field name made lowercase. Field renamed because it contained more than one '_' in a row.
    renewal_year_8_c = models.DecimalField(db_column='Renewal_Year_8__c', max_digits=5, decimal_places=2, blank=True, null=True)  # Field name made lowercase. Field renamed because it contained more than one '_' in a row.
    renewal_year_9_c = models.DecimalField(db_column='Renewal_Year_9__c', max_digits=5, decimal_places=2, blank=True, null=True)  # Field name made lowercase. Field renamed because it contained more than one '_' in a row.
    eapp_display_name_c = models.CharField(db_column='eApp_Display_Name__c', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed because it contained more than one '_' in a row.
    eapp_availability_c = models.CharField(db_column='eApp_Availability__c', max_length=100, blank=True, null=True)  # Field name made lowercase. Field renamed because it contained more than one '_' in a row.
    final_price_c = models.DecimalField(db_column='Final_Price__c', max_digits=18, decimal_places=2, blank=True, null=True)  # Field name made lowercase. Field renamed because it contained more than one '_' in a row.
    sales_board_category_c = models.CharField(db_column='Sales_Board_Category__c', max_length=150, blank=True, null=True)  # Field name made lowercase. Field renamed because it contained more than one '_' in a row.
    current_running_totals_category_c = models.CharField(db_column='Current_Running_Totals_Category__c', max_length=200, blank=True, null=True)  # Field name made lowercase. Field renamed because it contained more than one '_' in a row.
    running_total_subcategory_c = models.CharField(db_column='Running_Total_Subcategory__c', max_length=100, blank=True, null=True)  # Field name made lowercase. Field renamed because it contained more than one '_' in a row.
    commission1 = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    commission2 = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    commission3 = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    commission4 = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    commission5 = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    states = models.CharField(max_length=254, blank=True, null=True)
    age_range_c = models.CharField(db_column='Age_Range__c', max_length=254, blank=True, null=True)  # Field name made lowercase. Field renamed because it contained more than one '_' in a row.
    aor_category_c = models.CharField(db_column='AOR_Category__c', max_length=50, blank=True, null=True)  # Field name made lowercase. Field renamed because it contained more than one '_' in a row.
    final_first_payment_c = models.DecimalField(db_column='Final_First_Payment__c', max_digits=18, decimal_places=2, blank=True, null=True)  # Field name made lowercase. Field renamed because it contained more than one '_' in a row.
    fixed_sales_aor_c = models.CharField(db_column='Fixed_Sales_AOR__c', max_length=50, blank=True, null=True)  # Field name made lowercase. Field renamed because it contained more than one '_' in a row.
    add_ons_id_c = models.CharField(db_column='Add_ons_ID__c', max_length=50, blank=True, null=True)  # Field name made lowercase. Field renamed because it contained more than one '_' in a row.
    hii_product_name_c = models.CharField(db_column='HII_Product_Name__c', max_length=150, blank=True, null=True)  # Field name made lowercase. Field renamed because it contained more than one '_' in a row.
    addons_name_c = models.CharField(db_column='Addons_Name__c', max_length=50, blank=True, null=True)  # Field name made lowercase. Field renamed because it contained more than one '_' in a row.
    can_be_addon_of_c = models.TextField(db_column='Can_be_Addon_of__c', blank=True, null=True)  # Field name made lowercase. Field renamed because it contained more than one '_' in a row.
    product_blocking_c = models.IntegerField(db_column='Product_Blocking__c')  # Field name made lowercase. Field renamed because it contained more than one '_' in a row.
    final_enrollment_c = models.DecimalField(db_column='Final_Enrollment__c', max_digits=18, decimal_places=2, blank=True, null=True)  # Field name made lowercase. Field renamed because it contained more than one '_' in a row.
    new_month_advances_c = models.DecimalField(db_column='New_month_Advances__c', max_digits=4, decimal_places=0, blank=True, null=True)  # Field name made lowercase. Field renamed because it contained more than one '_' in a row.
    provider = models.CharField(max_length=50, blank=True, null=True)
    additional_product_1_c = models.ForeignKey('self', models.DO_NOTHING, db_column='Additional_Product_1__c', blank=True, null=True)  # Field name made lowercase. Field renamed because it contained more than one '_' in a row.
    additional_product_2_c = models.ForeignKey('self', models.DO_NOTHING, db_column='Additional_Product_2__c', blank=True, null=True)  # Field name made lowercase. Field renamed because it contained more than one '_' in a row.
    additional_product_3_c = models.ForeignKey('self', models.DO_NOTHING, db_column='Additional_Product_3__c', blank=True, null=True)  # Field name made lowercase. Field renamed because it contained more than one '_' in a row.
    additional_product_4_c = models.ForeignKey('self', models.DO_NOTHING, db_column='Additional_Product_4__c', blank=True, null=True)  # Field name made lowercase. Field renamed because it contained more than one '_' in a row.
    addon_100k_c = models.ForeignKey('self', models.DO_NOTHING, db_column='Addon_100k__c', blank=True, null=True)  # Field name made lowercase. Field renamed because it contained more than one '_' in a row.
    addon_50k_c = models.ForeignKey('self', models.DO_NOTHING, db_column='Addon_50k__c', blank=True, null=True)  # Field name made lowercase. Field renamed because it contained more than one '_' in a row.
    created_by = models.ForeignKey('SfarchiveUser', models.DO_NOTHING)
    enrollment_fee_lookup_c = models.ForeignKey('self', models.DO_NOTHING, db_column='Enrollment_Fee_Lookup__c', blank=True, null=True)  # Field name made lowercase. Field renamed because it contained more than one '_' in a row.
    last_modified_by = models.ForeignKey('SfarchiveUser', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'sfarchive_product2'


class SfarchiveProfile(models.Model):
    id = models.CharField(primary_key=True, max_length=20)
    name = models.CharField(max_length=255)
    permissions_email_single = models.IntegerField()
    permissions_email_mass = models.IntegerField()
    permissions_edit_task = models.IntegerField()
    permissions_edit_event = models.IntegerField()
    permissions_export_report = models.IntegerField()
    permissions_import_personal = models.IntegerField()
    permissions_data_export = models.IntegerField()
    permissions_manage_users = models.IntegerField()
    permissions_edit_public_templates = models.IntegerField()
    permissions_modify_all_data = models.IntegerField()
    permissions_manage_cases = models.IntegerField()
    permissions_mass_inline_edit = models.IntegerField()
    permissions_manage_solutions = models.IntegerField()
    permissions_customize_application = models.IntegerField()
    permissions_edit_readonly_fields = models.IntegerField()
    permissions_run_reports = models.IntegerField()
    permissions_view_setup = models.IntegerField()
    permissions_transfer_any_entity = models.IntegerField()
    permissions_new_report_builder = models.IntegerField()
    permissions_activate_contract = models.IntegerField()
    permissions_import_leads = models.IntegerField()
    permissions_manage_leads = models.IntegerField()
    permissions_transfer_any_lead = models.IntegerField()
    permissions_view_all_data = models.IntegerField()
    permissions_edit_public_documents = models.IntegerField()
    permissions_view_encrypted_data = models.IntegerField()
    permissions_edit_brand_templates = models.IntegerField()
    permissions_edit_html_templates = models.IntegerField()
    permissions_chatter_internal_user = models.IntegerField()
    permissions_delete_activated_contract = models.IntegerField()
    permissions_chatter_invite_external_users = models.IntegerField()
    permissions_send_sit_requests = models.IntegerField()
    permissions_api_user_only = models.IntegerField()
    permissions_manage_remote_access = models.IntegerField()
    permissions_can_use_new_dashboard_builder = models.IntegerField()
    permissions_manage_categories = models.IntegerField()
    permissions_convert_leads = models.IntegerField()
    permissions_password_never_expires = models.IntegerField()
    permissions_use_team_reassign_wizards = models.IntegerField()
    permissions_install_multiforce = models.IntegerField()
    permissions_publish_multiforce = models.IntegerField()
    permissions_chatter_own_groups = models.IntegerField()
    permissions_edit_opp_line_item_unit_price = models.IntegerField()
    permissions_create_multiforce = models.IntegerField()
    permissions_bulk_api_hard_delete = models.IntegerField()
    permissions_inbound_migration_tools_user = models.IntegerField()
    permissions_solution_import = models.IntegerField()
    permissions_manage_call_centers = models.IntegerField()
    permissions_manage_synonyms = models.IntegerField()
    permissions_outbound_migration_tools_user = models.IntegerField()
    permissions_view_content = models.IntegerField()
    permissions_manage_email_client_config = models.IntegerField()
    permissions_enable_notifications = models.IntegerField()
    permissions_manage_data_integrations = models.IntegerField()
    permissions_distribute_from_pers_wksp = models.IntegerField()
    permissions_view_data_categories = models.IntegerField()
    permissions_manage_data_categories = models.IntegerField()
    permissions_author_apex = models.IntegerField()
    permissions_manage_mobile = models.IntegerField()
    permissions_api_enabled = models.IntegerField()
    permissions_manage_custom_report_types = models.IntegerField()
    permissions_edit_case_comments = models.IntegerField()
    permissions_transfer_any_case = models.IntegerField()
    permissions_content_administrator = models.IntegerField()
    permissions_create_workspaces = models.IntegerField()
    permissions_manage_content_permissions = models.IntegerField()
    permissions_manage_content_properties = models.IntegerField()
    permissions_manage_content_types = models.IntegerField()
    permissions_schedule_job = models.IntegerField()
    permissions_manage_exchange_config = models.IntegerField()
    permissions_manage_analytic_snapshots = models.IntegerField()
    permissions_schedule_reports = models.IntegerField()
    permissions_manage_business_hour_holidays = models.IntegerField()
    permissions_custom_sidebar_on_all_pages = models.IntegerField()
    permissions_manage_interaction = models.IntegerField()
    permissions_view_my_teams_dashboards = models.IntegerField()
    permissions_moderate_chatter = models.IntegerField()
    permissions_reset_passwords = models.IntegerField()
    permissionsflowuflrequired = models.IntegerField(db_column='PermissionsFlowUFLRequired')  # Field name made lowercase.
    permissions_can_insert_feed_system_fields = models.IntegerField()
    permissions_email_template_management = models.IntegerField()
    permissions_email_administration = models.IntegerField()
    permissions_manage_chatter_messages = models.IntegerField()
    permissionsallowemailic = models.IntegerField(db_column='PermissionsAllowEmailIC')  # Field name made lowercase.
    permissions_chatter_file_link = models.IntegerField()
    permissions_force_two_factor = models.IntegerField()
    permissions_view_event_log_files = models.IntegerField()
    permissions_view_case_interaction = models.IntegerField()
    permissions_manage_auth_providers = models.IntegerField()
    permissions_run_flow = models.IntegerField()
    permissions_create_customize_dashboards = models.IntegerField()
    permissions_create_dashboard_folders = models.IntegerField()
    permissions_view_public_dashboards = models.IntegerField()
    permissions_manage_dashbds_in_pub_folders = models.IntegerField()
    permissions_create_customize_reports = models.IntegerField()
    permissions_create_report_folders = models.IntegerField()
    permissions_view_public_reports = models.IntegerField()
    permissions_manage_reports_in_pub_folders = models.IntegerField()
    permissions_edit_my_dashboards = models.IntegerField()
    permissions_edit_my_reports = models.IntegerField()
    permissions_view_all_users = models.IntegerField()
    permissions_connect_org_to_environment_hub = models.IntegerField()
    permissions_create_customize_filters = models.IntegerField()
    permissions_sales_console = models.IntegerField()
    permissions_two_factor_api = models.IntegerField()
    permissions_delete_topics = models.IntegerField()
    permissions_edit_topics = models.IntegerField()
    permissions_create_topics = models.IntegerField()
    permissions_assign_topics = models.IntegerField()
    permissions_identity_enabled = models.IntegerField()
    permissions_identity_connect = models.IntegerField()
    permissions_custom_mobile_apps_access = models.IntegerField()
    permissions_view_help_link = models.IntegerField()
    permissions_manage_profiles_permissionsets = models.IntegerField()
    permissions_assign_permission_sets = models.IntegerField()
    permissions_manage_roles = models.IntegerField()
    permissions_manage_ip_addresses = models.IntegerField()
    permissions_manage_sharing = models.IntegerField()
    permissions_manage_internal_users = models.IntegerField()
    permissions_manage_password_policies = models.IntegerField()
    permissions_manage_login_access_policies = models.IntegerField()
    permissions_manage_custom_permissions = models.IntegerField()
    permissions_manage_unlisted_groups = models.IntegerField()
    permissions_manage_two_factor = models.IntegerField()
    permissions_chatter_for_share_point = models.IntegerField()
    permissions_lightning_experience_user = models.IntegerField()
    permissions_config_custom_recs = models.IntegerField()
    permissions_submit_macros_allowed = models.IntegerField()
    permissions_bulk_macros_allowed = models.IntegerField()
    permissions_send_announcement_emails = models.IntegerField()
    permissions_chatter_edit_own_post = models.IntegerField()
    permissions_chatter_edit_own_record_post = models.IntegerField()
    permissions_manage_sandboxes = models.IntegerField()
    permissions_import_custom_objects = models.IntegerField()
    permissions_delegated_two_factor = models.IntegerField()
    permissions_chatter_compose_ui_codesnippet = models.IntegerField()
    permissions_select_files_from_salesforce = models.IntegerField()
    permissions_merge_topics = models.IntegerField()
    permissions_manage_pvt_rpts_and_dashbds = models.IntegerField()
    permissions_view_data_assessment = models.IntegerField()
    permissions_can_approve_feed_post = models.IntegerField()
    user_type = models.CharField(max_length=40, blank=True, null=True)
    created_date = models.DateTimeField()
    last_modified_date = models.DateTimeField()
    system_modstamp = models.DateTimeField()
    description = models.CharField(max_length=255, blank=True, null=True)
    last_viewed_date = models.DateTimeField(blank=True, null=True)
    last_referenced_date = models.DateTimeField(blank=True, null=True)
    created_by = models.ForeignKey('SfarchiveUser', models.DO_NOTHING)
    last_modified_by = models.ForeignKey('SfarchiveUser', models.DO_NOTHING)
    user_license = models.ForeignKey('SfarchiveUserlicense', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'sfarchive_profile'


class SfarchiveRecordtype(models.Model):
    id = models.CharField(primary_key=True, max_length=20)
    name = models.CharField(max_length=80)
    developer_name = models.CharField(max_length=80)
    namespace_prefix = models.CharField(max_length=15, blank=True, null=True)
    description = models.CharField(max_length=255, blank=True, null=True)
    sobject_type = models.CharField(max_length=40)
    is_active = models.IntegerField()
    is_person_type = models.IntegerField()
    created_date = models.DateTimeField()
    last_modified_date = models.DateTimeField()
    system_modstamp = models.DateTimeField()
    business_process_id = models.CharField(max_length=18, blank=True, null=True)
    created_by = models.ForeignKey('SfarchiveUser', models.DO_NOTHING)
    last_modified_by = models.ForeignKey('SfarchiveUser', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'sfarchive_recordtype'


class SfarchiveSalesboardproducttype(models.Model):
    id = models.CharField(primary_key=True, max_length=20)
    owner_id = models.CharField(max_length=18)
    is_deleted = models.IntegerField()
    name = models.CharField(max_length=80)
    created_date = models.DateTimeField()
    last_modified_date = models.DateTimeField()
    system_modstamp = models.DateTimeField()
    last_viewed_date = models.DateTimeField(blank=True, null=True)
    last_referenced_date = models.DateTimeField(blank=True, null=True)
    product_color_c = models.CharField(db_column='Product_Color__c', max_length=10, blank=True, null=True)  # Field name made lowercase. Field renamed because it contained more than one '_' in a row.
    product_name_c = models.CharField(db_column='Product_Name__c', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed because it contained more than one '_' in a row.
    show_in_board_c = models.IntegerField(db_column='Show_in_Board__c')  # Field name made lowercase. Field renamed because it contained more than one '_' in a row.
    credit_card_efective_day_c = models.CharField(db_column='Credit_Card_Efective_Day__c', max_length=50, blank=True, null=True)  # Field name made lowercase. Field renamed because it contained more than one '_' in a row.
    e_check_efective_day_c = models.CharField(db_column='E_Check_Efective_Day__c', max_length=50, blank=True, null=True)  # Field name made lowercase. Field renamed because it contained more than one '_' in a row.
    behaivor = models.CharField(max_length=255, blank=True, null=True)
    color_text_c = models.CharField(db_column='Color_Text__c', max_length=50, blank=True, null=True)  # Field name made lowercase. Field renamed because it contained more than one '_' in a row.
    created_by = models.ForeignKey('SfarchiveUser', models.DO_NOTHING)
    last_modified_by = models.ForeignKey('SfarchiveUser', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'sfarchive_salesboardproducttype'


class SfarchiveSocialpersona(models.Model):
    id = models.CharField(primary_key=True, max_length=20)
    is_deleted = models.IntegerField()
    name = models.CharField(max_length=255)
    created_date = models.DateTimeField()
    last_modified_date = models.DateTimeField()
    system_modstamp = models.DateTimeField()
    parent_id = models.CharField(max_length=18)
    provider = models.CharField(max_length=255)
    external_id = models.CharField(max_length=255, blank=True, null=True)
    is_default = models.IntegerField()
    externalpictureurl = models.CharField(db_column='ExternalPictureURL', max_length=200, blank=True, null=True)  # Field name made lowercase.
    profile_url = models.CharField(max_length=200, blank=True, null=True)
    topic_type = models.CharField(max_length=255, blank=True, null=True)
    is_blacklisted = models.IntegerField()
    klout = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    real_name = models.CharField(max_length=255, blank=True, null=True)
    is_following_us = models.IntegerField()
    are_we_following = models.IntegerField()
    media_type = models.CharField(max_length=255, blank=True, null=True)
    bio = models.TextField(blank=True, null=True)
    followers = models.IntegerField(blank=True, null=True)
    following = models.IntegerField(blank=True, null=True)
    number_of_friends = models.IntegerField(blank=True, null=True)
    listed_count = models.IntegerField(blank=True, null=True)
    media_provider = models.CharField(max_length=255, blank=True, null=True)
    profile_type = models.CharField(max_length=255, blank=True, null=True)
    r6_source_id = models.CharField(max_length=255, blank=True, null=True)
    number_of_tweets = models.IntegerField(blank=True, null=True)
    source_app = models.CharField(max_length=255, blank=True, null=True)
    created_by = models.ForeignKey('SfarchiveUser', models.DO_NOTHING)
    last_modified_by = models.ForeignKey('SfarchiveUser', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'sfarchive_socialpersona'


class SfarchiveSocialpost(models.Model):
    id = models.CharField(primary_key=True, max_length=20)
    owner_id = models.CharField(max_length=18)
    is_deleted = models.IntegerField()
    name = models.CharField(max_length=255)
    created_date = models.DateTimeField()
    last_modified_date = models.DateTimeField()
    system_modstamp = models.DateTimeField()
    last_viewed_date = models.DateTimeField(blank=True, null=True)
    last_referenced_date = models.DateTimeField(blank=True, null=True)
    headline = models.CharField(max_length=255, blank=True, null=True)
    content = models.TextField(blank=True, null=True)
    posted = models.DateTimeField()
    post_url = models.CharField(max_length=200, blank=True, null=True)
    provider = models.CharField(max_length=255, blank=True, null=True)
    handle = models.CharField(max_length=255, blank=True, null=True)
    spam_rating = models.CharField(max_length=255, blank=True, null=True)
    media_type = models.CharField(max_length=255, blank=True, null=True)
    media_provider = models.CharField(max_length=255, blank=True, null=True)
    sentiment = models.CharField(max_length=255, blank=True, null=True)
    post_priority = models.CharField(max_length=255, blank=True, null=True)
    status = models.CharField(max_length=255, blank=True, null=True)
    status_message = models.TextField(blank=True, null=True)
    recipient = models.CharField(max_length=255, blank=True, null=True)
    recipient_type = models.CharField(max_length=255, blank=True, null=True)
    message_type = models.CharField(max_length=255, blank=True, null=True)
    r6_post_id = models.CharField(unique=True, max_length=255, blank=True, null=True)
    r6_topic_id = models.CharField(max_length=255, blank=True, null=True)
    r6_source_id = models.CharField(max_length=255, blank=True, null=True)
    topic_type = models.CharField(max_length=255, blank=True, null=True)
    external_post_id = models.CharField(max_length=255, blank=True, null=True)
    harvest_date = models.DateTimeField(blank=True, null=True)
    is_outbound = models.IntegerField()
    post_tags = models.TextField(blank=True, null=True)
    source_tags = models.TextField(blank=True, null=True)
    classification = models.CharField(max_length=40, blank=True, null=True)
    thread_size = models.IntegerField(blank=True, null=True)
    comment_count = models.IntegerField(blank=True, null=True)
    shares = models.IntegerField(blank=True, null=True)
    view_count = models.IntegerField(blank=True, null=True)
    inbound_link_count = models.IntegerField(blank=True, null=True)
    unique_commentors = models.IntegerField(blank=True, null=True)
    likes_and_votes = models.IntegerField(blank=True, null=True)
    topic_profile_name = models.CharField(max_length=255, blank=True, null=True)
    keyword_group_name = models.CharField(max_length=255, blank=True, null=True)
    engagement_level = models.CharField(max_length=40, blank=True, null=True)
    assigned_to = models.CharField(max_length=255, blank=True, null=True)
    attachment_url = models.CharField(max_length=200, blank=True, null=True)
    attachment_type = models.CharField(max_length=255, blank=True, null=True)
    response_context_external_id = models.CharField(max_length=255, blank=True, null=True)
    liked_by = models.CharField(max_length=255, blank=True, null=True)
    analyzer_score = models.DecimalField(max_digits=18, decimal_places=3, blank=True, null=True)
    language = models.CharField(max_length=255, blank=True, null=True)
    created_by = models.ForeignKey('SfarchiveUser', models.DO_NOTHING)
    deleted_by = models.ForeignKey('SfarchiveUser', models.DO_NOTHING, blank=True, null=True)
    last_modified_by = models.ForeignKey('SfarchiveUser', models.DO_NOTHING)
    outbound_social_account = models.ForeignKey(SfarchiveExternalsocialaccount, models.DO_NOTHING, blank=True, null=True)
    parent = models.ForeignKey(SfarchiveCase, models.DO_NOTHING, blank=True, null=True)
    persona = models.ForeignKey(SfarchiveSocialpersona, models.DO_NOTHING, blank=True, null=True)
    reply_to = models.ForeignKey('self', models.DO_NOTHING, blank=True, null=True)
    who = models.ForeignKey(SfarchiveAccount, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sfarchive_socialpost'


class SfarchiveUser(models.Model):
    id = models.CharField(primary_key=True, max_length=20)
    username = models.CharField(max_length=80)
    last_name = models.CharField(max_length=80)
    first_name = models.CharField(max_length=40, blank=True, null=True)
    middle_name = models.CharField(max_length=40, blank=True, null=True)
    name = models.CharField(max_length=121)
    company_name = models.CharField(max_length=80, blank=True, null=True)
    division = models.CharField(max_length=80, blank=True, null=True)
    department = models.CharField(max_length=80, blank=True, null=True)
    title = models.CharField(max_length=80, blank=True, null=True)
    street = models.TextField(blank=True, null=True)
    city = models.CharField(max_length=40, blank=True, null=True)
    state = models.CharField(max_length=80, blank=True, null=True)
    postal_code = models.CharField(max_length=20, blank=True, null=True)
    country = models.CharField(max_length=80, blank=True, null=True)
    latitude = models.DecimalField(max_digits=18, decimal_places=15, blank=True, null=True)
    longitude = models.DecimalField(max_digits=18, decimal_places=15, blank=True, null=True)
    geocode_accuracy = models.CharField(max_length=40, blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    email = models.CharField(max_length=254)
    email_preferences_auto_bcc = models.IntegerField()
    email_preferences_auto_bcc_stay_in_touch = models.IntegerField()
    email_preferences_stay_in_touch_reminder = models.IntegerField()
    sender_email = models.CharField(max_length=254, blank=True, null=True)
    sender_name = models.CharField(max_length=80, blank=True, null=True)
    signature = models.CharField(max_length=1333, blank=True, null=True)
    stay_in_touch_subject = models.CharField(max_length=80, blank=True, null=True)
    stay_in_touch_signature = models.CharField(max_length=512, blank=True, null=True)
    stay_in_touch_note = models.CharField(max_length=512, blank=True, null=True)
    phone = models.CharField(max_length=40, blank=True, null=True)
    fax = models.CharField(max_length=40, blank=True, null=True)
    mobile_phone = models.CharField(max_length=40, blank=True, null=True)
    alias = models.CharField(max_length=8)
    community_nickname = models.CharField(max_length=40)
    badge_text = models.CharField(max_length=80, blank=True, null=True)
    is_active = models.IntegerField()
    time_zone_sid_key = models.CharField(max_length=40)
    locale_sid_key = models.CharField(max_length=40)
    receives_info_emails = models.IntegerField()
    receives_admin_info_emails = models.IntegerField()
    email_encoding_key = models.CharField(max_length=40)
    user_type = models.CharField(max_length=40, blank=True, null=True)
    language_locale_key = models.CharField(max_length=40)
    employee_number = models.CharField(max_length=20, blank=True, null=True)
    delegated_approver = models.CharField(max_length=18, blank=True, null=True)
    last_login_date = models.DateTimeField(blank=True, null=True)
    last_password_change_date = models.DateTimeField(blank=True, null=True)
    created_date = models.DateTimeField()
    last_modified_date = models.DateTimeField()
    system_modstamp = models.DateTimeField()
    offline_trial_expiration_date = models.DateTimeField(blank=True, null=True)
    offline_pda_trial_expiration_date = models.DateTimeField(blank=True, null=True)
    user_permissions_marketing_user = models.IntegerField()
    user_permissions_offline_user = models.IntegerField()
    user_permissions_avantgo_user = models.IntegerField()
    user_permissions_call_center_auto_login = models.IntegerField()
    user_permissions_mobile_user = models.IntegerField()
    userpermissionssfcontentuser = models.IntegerField(db_column='UserPermissionsSFContentUser')  # Field name made lowercase.
    user_permissions_interaction_user = models.IntegerField()
    user_permissions_support_user = models.IntegerField()
    user_permissions_chatter_answers_user = models.IntegerField()
    forecast_enabled = models.IntegerField()
    user_preferences_activity_reminders_popup = models.IntegerField()
    user_preferences_event_reminders_checkbox_default = models.IntegerField()
    user_preferences_task_reminders_checkbox_default = models.IntegerField()
    user_preferences_reminder_sound_off = models.IntegerField()
    user_preferences_disable_all_feeds_email = models.IntegerField()
    user_preferences_disable_followers_email = models.IntegerField()
    user_preferences_disable_profile_post_email = models.IntegerField()
    user_preferences_disable_change_comment_email = models.IntegerField()
    user_preferences_disable_later_comment_email = models.IntegerField()
    user_preferences_dis_prof_post_comment_email = models.IntegerField()
    user_preferences_apex_pages_developer_mode = models.IntegerField()
    userpreferenceshidecsngetchattermobiletask = models.IntegerField(db_column='UserPreferencesHideCSNGetChatterMobileTask')  # Field name made lowercase.
    user_preferences_disable_mentions_post_email = models.IntegerField()
    user_preferences_dis_mentions_comment_email = models.IntegerField()
    userpreferenceshidecsndesktoptask = models.IntegerField(db_column='UserPreferencesHideCSNDesktopTask')  # Field name made lowercase.
    user_preferences_hide_chatter_onboarding_splash = models.IntegerField()
    user_preferences_hide_second_chatter_onboarding_splash = models.IntegerField()
    user_preferences_dis_comment_after_like_email = models.IntegerField()
    user_preferences_disable_like_email = models.IntegerField()
    user_preferences_sort_feed_by_comment = models.IntegerField()
    user_preferences_disable_message_email = models.IntegerField()
    user_preferences_disable_bookmark_email = models.IntegerField()
    user_preferences_disable_share_post_email = models.IntegerField()
    user_preferences_enable_auto_sub_for_feeds = models.IntegerField()
    user_preferences_disable_file_share_notifications_for_api = models.IntegerField()
    user_preferences_show_title_to_external_users = models.IntegerField()
    user_preferences_show_manager_to_external_users = models.IntegerField()
    user_preferences_show_email_to_external_users = models.IntegerField()
    user_preferences_show_work_phone_to_external_users = models.IntegerField()
    user_preferences_show_mobile_phone_to_external_users = models.IntegerField()
    user_preferences_show_fax_to_external_users = models.IntegerField()
    user_preferences_show_street_address_to_external_users = models.IntegerField()
    user_preferences_show_city_to_external_users = models.IntegerField()
    user_preferences_show_state_to_external_users = models.IntegerField()
    user_preferences_show_postal_code_to_external_users = models.IntegerField()
    user_preferences_show_country_to_external_users = models.IntegerField()
    user_preferences_show_profile_pic_to_guest_users = models.IntegerField()
    user_preferences_show_title_to_guest_users = models.IntegerField()
    user_preferences_show_city_to_guest_users = models.IntegerField()
    user_preferences_show_state_to_guest_users = models.IntegerField()
    user_preferences_show_postal_code_to_guest_users = models.IntegerField()
    user_preferences_show_country_to_guest_users = models.IntegerField()
    userpreferenceshides1browserui = models.IntegerField(db_column='UserPreferencesHideS1BrowserUI')  # Field name made lowercase.
    user_preferences_disable_endorsement_email = models.IntegerField()
    user_preferences_path_assistant_collapsed = models.IntegerField()
    user_preferences_cache_diagnostics = models.IntegerField()
    user_preferences_show_email_to_guest_users = models.IntegerField()
    user_preferences_show_manager_to_guest_users = models.IntegerField()
    user_preferences_show_work_phone_to_guest_users = models.IntegerField()
    user_preferences_show_mobile_phone_to_guest_users = models.IntegerField()
    user_preferences_show_fax_to_guest_users = models.IntegerField()
    user_preferences_show_street_address_to_guest_users = models.IntegerField()
    user_preferences_lightning_experience_preferred = models.IntegerField()
    user_preferences_preview_lightning = models.IntegerField()
    user_preferences_hide_end_user_onboarding_assistant_modal = models.IntegerField()
    user_preferences_hide_lightning_migration_modal = models.IntegerField()
    user_preferences_hide_sfx_welcome_mat = models.IntegerField()
    user_preferences_hide_bigger_photo_callout = models.IntegerField()
    extension = models.CharField(max_length=40, blank=True, null=True)
    federation_identifier = models.CharField(max_length=512, blank=True, null=True)
    about_me = models.TextField(blank=True, null=True)
    full_photo_url = models.CharField(max_length=200, blank=True, null=True)
    small_photo_url = models.CharField(max_length=200, blank=True, null=True)
    medium_photo_url = models.CharField(max_length=200, blank=True, null=True)
    digest_frequency = models.CharField(max_length=40)
    default_group_notification_frequency = models.CharField(max_length=40)
    last_viewed_date = models.DateTimeField(blank=True, null=True)
    last_referenced_date = models.DateTimeField(blank=True, null=True)
    banner_photo_url = models.CharField(max_length=200, blank=True, null=True)
    is_profile_photo_active = models.IntegerField()
    account_id = models.CharField(max_length=18, blank=True, null=True)
    call_center_id = models.CharField(max_length=18, blank=True, null=True)
    contact_id = models.CharField(max_length=18, blank=True, null=True)
    created_by_id = models.CharField(max_length=18, blank=True, null=True)
    last_modified_by_id = models.CharField(max_length=18, blank=True, null=True)
    manager_id = models.CharField(max_length=18, blank=True, null=True)
    profile_id = models.CharField(max_length=18, blank=True, null=True)
    user_role_id = models.CharField(max_length=18, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sfarchive_user'


class SfarchiveUserlicense(models.Model):
    id = models.CharField(primary_key=True, max_length=20)
    license_definition_key = models.CharField(max_length=40)
    name = models.CharField(max_length=40)
    system_modstamp = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'sfarchive_userlicense'


class SfarchiveUserrole(models.Model):
    id = models.CharField(primary_key=True, max_length=20)
    name = models.CharField(max_length=80)
    rollup_description = models.CharField(max_length=80, blank=True, null=True)
    opportunity_access_for_account_owner = models.CharField(max_length=40)
    case_access_for_account_owner = models.CharField(max_length=40, blank=True, null=True)
    contact_access_for_account_owner = models.CharField(max_length=40, blank=True, null=True)
    may_forecast_manager_share = models.IntegerField()
    last_modified_date = models.DateTimeField()
    system_modstamp = models.DateTimeField()
    developer_name = models.CharField(max_length=80, blank=True, null=True)
    portal_type = models.CharField(max_length=40, blank=True, null=True)
    forecast_user = models.ForeignKey(SfarchiveUser, models.DO_NOTHING, blank=True, null=True)
    last_modified_by = models.ForeignKey(SfarchiveUser, models.DO_NOTHING)
    parent_role = models.ForeignKey('self', models.DO_NOTHING, blank=True, null=True)
    portal_account = models.ForeignKey(SfarchiveAccount, models.DO_NOTHING, blank=True, null=True)
    portal_account_owner = models.ForeignKey(SfarchiveUser, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sfarchive_userrole'


class ValidatorsBannedareacode(models.Model):
    code = models.CharField(unique=True, max_length=5)

    class Meta:
        managed = False
        db_table = 'validators_bannedareacode'


class ValidatorsBannedemail(models.Model):
    email = models.CharField(unique=True, max_length=200)

    class Meta:
        managed = False
        db_table = 'validators_bannedemail'


class ValidatorsBannedfirstname(models.Model):
    first_name = models.CharField(unique=True, max_length=100)

    class Meta:
        managed = False
        db_table = 'validators_bannedfirstname'


class ValidatorsBannedfullname(models.Model):
    fullname = models.CharField(unique=True, max_length=200)

    class Meta:
        managed = False
        db_table = 'validators_bannedfullname'


class ValidatorsBannedlastname(models.Model):
    last_name = models.CharField(unique=True, max_length=100)

    class Meta:
        managed = False
        db_table = 'validators_bannedlastname'


class ValidatorsBannedphone(models.Model):
    phone = models.CharField(unique=True, max_length=50)

    class Meta:
        managed = False
        db_table = 'validators_bannedphone'


class ValidatorsBannedstreet(models.Model):
    street = models.CharField(unique=True, max_length=250)

    class Meta:
        managed = False
        db_table = 'validators_bannedstreet'


class VicidialListTemp(models.Model):
    lead_id = models.AutoField(primary_key=True)
    entry_date = models.DateTimeField(blank=True, null=True)
    modify_date = models.DateTimeField()
    status = models.CharField(max_length=6, blank=True, null=True)
    user = models.CharField(max_length=20, blank=True, null=True)
    vendor_lead_code = models.CharField(max_length=20, blank=True, null=True)
    source_id = models.CharField(max_length=50, blank=True, null=True)
    list_id = models.BigIntegerField()
    gmt_offset_now = models.DecimalField(max_digits=4, decimal_places=2, blank=True, null=True)
    called_since_last_reset = models.CharField(max_length=3, blank=True, null=True)
    phone_code = models.CharField(max_length=10, blank=True, null=True)
    phone_number = models.CharField(max_length=18)
    title = models.CharField(max_length=4, blank=True, null=True)
    first_name = models.CharField(max_length=30, blank=True, null=True)
    middle_initial = models.CharField(max_length=1, blank=True, null=True)
    last_name = models.CharField(max_length=30, blank=True, null=True)
    address1 = models.CharField(max_length=100, blank=True, null=True)
    address2 = models.CharField(max_length=100, blank=True, null=True)
    address3 = models.CharField(max_length=100, blank=True, null=True)
    city = models.CharField(max_length=50, blank=True, null=True)
    state = models.CharField(max_length=2, blank=True, null=True)
    province = models.CharField(max_length=50, blank=True, null=True)
    postal_code = models.CharField(max_length=10, blank=True, null=True)
    country_code = models.CharField(max_length=3, blank=True, null=True)
    gender = models.CharField(max_length=1, blank=True, null=True)
    date_of_birth = models.DateField(blank=True, null=True)
    alt_phone = models.CharField(max_length=12, blank=True, null=True)
    email = models.CharField(max_length=70, blank=True, null=True)
    security_phrase = models.CharField(max_length=100, blank=True, null=True)
    comments = models.CharField(max_length=255, blank=True, null=True)
    called_count = models.SmallIntegerField(blank=True, null=True)
    last_local_call_time = models.DateTimeField(blank=True, null=True)
    rank = models.SmallIntegerField()
    owner = models.CharField(max_length=20, blank=True, null=True)
    entry_list_id = models.BigIntegerField()
    priority = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'vicidial_list_temp'
