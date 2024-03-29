from django.db import models


class Product(models.Model):
    p_id = models.AutoField(primary_key=True)
    price = models.FloatField(default=10.00)
    p_name = models.CharField(max_length=32)
    quantity = models.IntegerField(default=500)
    p_description = models.TextField()


class CustomerAddress(models.Model):
    street = models.CharField(max_length=64)
    city = models.CharField(max_length=32)
    state = models.CharField(max_length=2)
    zip_code = models.IntegerField(max_length=5)


class OrderHistory(models.Model):
    PROCESS = 'P'
    SHIPPING = 'S'
    DELIVERED = 'D'
    status_choice = [
        (PROCESS, 'Process'),
        (SHIPPING, 'Shipping'),
        (DELIVERED, 'Delivered'),
    ]

    o_id = models.AutoField(primary_key=True)
    o_status = models.CharField(max_length=16, choices=status_choice)
    o_time = models.DateTimeField()
    product = models.ForeignKey(Product, on_delete=models.CASCADE)


class Customer(models.Model):
    c_id = models.AutoField(primary_key=True)
    c_name = models.CharField(max_length=32)
    c_email = models.EmailField(unique=True)
    c_phone = models.IntegerField(max_length=10, unique=True)
    company = models.CharField(max_length=64)
    income = models.PositiveIntegerField(null=True)
    c_address = models.OneToOneField(CustomerAddress, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, null=True, on_delete=models.CASCADE)
    order_history = models.ForeignKey(OrderHistory, null=True, on_delete=models.CASCADE)


class EmployeeAddress(models.Model):
    street = models.CharField(max_length=64)
    city = models.CharField(max_length=32)
    state = models.CharField(max_length=2)
    zip_code = models.IntegerField(max_length=5)


class Employee(models.Model):
    DATABASE_ADMINISTRATOR = 'DBA'
    SALESPERSON = 'Sales'
    job_choice = [
        (DATABASE_ADMINISTRATOR, 'Database_Administrator'),
        (SALESPERSON, 'Salesperson')
    ]

    e_id = models.AutoField(primary_key=True)
    e_name = models.CharField(max_length=32)
    e_email = models.EmailField(unique=True)
    e_phone = models.IntegerField(max_length=10, unique=True)
    job_title = models.CharField(max_length=16, choices=job_choice)
    e_address = models.OneToOneField(EmployeeAddress, on_delete=models.CASCADE)


class Case(models.Model):
    OPEN = 'O'
    CLOSE = 'C'
    status_choice = [
        (OPEN, 'Open'),
        (CLOSE, 'Close')
    ]

    ca_id = models.AutoField(primary_key=True)
    summary = models.CharField(max_length=128)
    ca_description = models.TextField(default="the product was damaged after washed.")
    ca_time = models.DateTimeField()
    ca_status = models.CharField(choices=status_choice)
    comment = models.TextField(default="We are so sorry for hearing that.")
    customer = models.OneToOneField(Customer, unique=True, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    employee = models.OneToOneField(Employee, unique=True, on_delete=models.CASCADE)


class Resolution(models.Model):
    CHANGE = 'C'
    RETURN = 'R'
    ADD = 'A'
    name_choice = [
        (CHANGE, 'Change'),
        (RETURN, 'Return'),
        (ADD, 'Add')
    ]

    PENDING = 'P'
    APPROVED = 'AD'
    step_choice = [
        (PENDING, 'Pending'),
        (APPROVED, 'Approve')
    ]

    resolution_name = models.CharField(choices=name_choice)
    step = models.CharField(choices=step_choice)
    customer = models.OneToOneField(Customer, on_delete=models.CASCADE)
    product = models.OneToOneField(OrderHistory, on_delete=models.CASCADE)
    employee = models.OneToOneField(Employee, on_delete=models.CASCADE)

