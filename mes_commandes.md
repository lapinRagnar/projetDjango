################################### 
# instlation et initialiasisation
################################### 
aie
le site du tuto : https://www.youtube.com/watch?v=wIPHER2UBB4&list=PL-51WBLyFTg2vW-_6XBoUpE7vpmoR3ztO&index=6


django-admin
 .\venv\Scripts\activate
 pip freeze > requierement.txt
 pip freeze list
python manage.py
startapp accounts

pip install --upgrade pip

dans tuto_1/settings.py
-----------------------

INSTALLED_APPS = [
    .................,
    'accounts',
]

## urls et views
dans accounts
-------------------
- créer urls.py
- créer views.py

dans accounts/urls.py
-------------------
from . import views
from django.urls import path


urlpatterns = [
    path('', views.home),
    path('products/', views.products),
    path('customers', views.customers),

]

dans accounts/views.py
-------------------

from django.http import HttpResponse



def home(request):
    return HttpResponse('Home page!')


def products(request):
    return HttpResponse('Page Products!')


def customers(request):
    return HttpResponse('page costumer')

dans tuto_1/urls.py
-------------------
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('accounts.urls'))

]

dans accounts/urls.py
---------------------
from . import views
from django.urls import path

urlpatterns = [
    path('', views.home),
    path('products/', views.products),
    path('customers', views.customers),

]

templates et heritage
-------------------------------
- créer templates/accounts/dashboard.html
- créer templates/accounts/main.html
- créer templates/partials/_navbar.html et _footer.html

dans templates/accounts/main.html
-----------------------------------
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>
        {% block title %}

        {% endblock %}
        Mon super Site
    </title>
</head>
<body>
    <h1>Navbar</h1>
    <hr>

    {% block content %}{% endblock %}

    <hr>
    <h1>Footer</h1>

</body>
</html>

dans templates/dashboard.html
-----------------------------
{% extends 'accounts/main.html' %}

{% block title %} Dashboard {{ title }} {% endblock %}

{% block content %}
    <h1>Dashboard</h1>
{% endblock %}

----------------------------------------------------
et on fait pareil pour cusmters.htmln products.html
--------------------------------------------------

dans layouts/partials/_navbar.html
------------------------------------
    <hr>
    <h1>Footer</h1>

dans layouts/partials/_footer.html
------------------------------------
    <hr>
    <h1>Footer</h1>


les codes
--------------
https://github.com/divanov11/crash-course-CRM/tree/Part-3-Templates-and-Inheritance


###################################################
#   ameliorer les templates - avec bootstrap et le reste
###################################################
on modifier accounts/dashboard.html
-------------------------------------

<br>

<div class="row">
    <div class="col">
        <div class="col-md">
            <div class="card text-center text-white  mb-3" id="total-orders">
                <div class="card-header">
                    <h5 class="card-title">Total Orders</h5>
                </div>
                <div class="card-body">
                    <h3 class="card-title"></h3>
                </div>
            </div>
        </div>
    </div>

    <div class="col">
        <div class="col-md">
            <div class="card text-center text-white  mb-3" id="orders-delivered">
                <div class="card-header">
                    <h5 class="card-title">Orders Delivered</h5>
                </div>
                <div class="card-body">
                    <h3 class="card-title"></h3>
                </div>
            </div>
        </div>
    </div>

    <div class="col">
        <div class="col-md">
            <div class="card text-center text-white  mb-3" id="orders-pending">
                <div class="card-header">
                    <h5 class="card-title">Orders Pending</h5>
                </div>
                <div class="card-body">
                    <h3 class="card-title"></h3>
                </div>
            </div>
        </div>
    </div>
</div>



- creer : accounts/status.html
et mettre ce code
----------------------------------



dans accounts/main.html, on ajoute l'include
------------------------------------------------


<style>

        #logo{
        }

        body{
            background-color: #ebeff5;
        }


        #total-orders{
            background-color: #4cb4c7;
        }


        #orders-delivered{
            background-color: #7abecc;
        }

        #orders-pending{
            background-color: #7CD1C0;
    }

</style>

.......

    {% block content %}{% endblock %}

    {% include 'accounts/status.html' %}                        <!--On ajoute ceci-->
    
    {% include 'accounts/partials/_footer.html' %}

.....

modifier accounts/products.html comme cela
----------------------------------------------
{% extends 'accounts/main.html' %}

{% block title %} {{ title }} {% endblock %}

{% block content %}
    
    <br>

    <div class="row">
        <div class="col-md">
            <div class="card card-body">
                <h5>Products</h5>
            </div>
            <div class="card card-body">
                <table class="table">
                    <tr>
                        <th>Product</th>
                        <th>Category</th>
                        <th>Price</th>
                    </tr>
                    
                </table>
            </div>
        </div>
        
    </div>
    
    
{% endblock %}


modifier le accounts/custmomer.html comme cela
----------------------------------------------------

{% extends 'accounts/main.html' %}

{% block title %} {{ title }} {% endblock %}

{% block content %}

    <br>

    <div class="row">
        <div class="col-md">
            <div class="card card-body">
                <h5>Customer:</h5>
                <hr>
                <a class="btn btn-outline-info  btn-sm btn-block" href="">Update Customer</a>
                <a class="btn btn-outline-danger  btn-sm btn-block" href="">Delete Customer</a>

            </div>
        </div>

        <div class="col-md">
            <div class="card card-body">
                <h5>Contact Information</h5>
                <hr>
                <p>Email: </p>
                <p>Phone: </p>
            </div>
        </div>

        <div class="col-md">
            <div class="card card-body">
                <h5>Total Orders</h5>
                <hr>
                <h1 style="text-align: center;padding: 10px"></h1>
            </div>
        </div>
    </div>


    <br>
    <div class="row">
        <div class="col">
            <div class="card card-body">
                <form method="get">

                <button class="btn btn-primary" type="submit">Search</button>
              </form>
            </div>
        </div>

    </div>
    <br>

    <div class="row">
        <div class="col-md">
            <div class="card card-body">
                <table class="table table-sm">
                    <tr>
                        <th>Product</th>
                        <th>Category</th>
                        <th>Date Orderd</th>
                        <th>Status</th>
                        <th>Update</th>
                        <th>Remove</th>
                    </tr>

                </table>
            </div>
        </div>
    </div>


{% endblock %}

######################################################"
#   Static files
#####################################################

ensuite cree :
------------------->

static
├───css
├───img
└───js

dans tuto_1/settings.py, on ajoute
-----------------------------------
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static')
]

dans le main.html, on ajoute le style
--------------------------------------------
{% load static %}

....
....
<link rel="stylesheet" type="text/css" href="{% static '/css/main.css' %}">


dans static/css/main.css, on met 
---------------------------------

#logo{
}

body{
    background-color: #ebeff5;
}


#total-orders{
    background-color: #4cb4c7;
}


#orders-delivered{
    background-color: #7abecc;
}

#orders-pending{
    background-color: #7CD1C0;
}

*****************************************
# ajouter images 
*****************************************

--------------
on ajoute l'image du logo dans static/images/

dans le tuto_1/settings.py, on ajoute
-------------------------------------

MEDIA_URL = '/images/'

et dans la _navbar.html
------------------------------>

{% load static %}

...
....

<img src="{% static 'images/logo.png' %}" alt="">


##################################################################################
##  database, model, admin panel  
##################################################################################

commande : faire la premiere mogration
------------------------------------------
> py manage.py migrate
> py manage.py createsuperuser
Username (leave blank to use 'lapin'): lapinragnar
Email address: lapinragnar@gmail.com
Password:
Password (again):
Superuser created successfully.

ensuite, faire un runserver
--------------------------
... 
et on se connecte dans l'espace admin:
http://127.0.0.1:8000/admin

ensuite, on creer un deuxieme utilisateur: beloub


#############################"
#   models
#############################"

dans accounts/models.py, on ajoute
--------------------------------------------
from django.db import models


class Customer(models.Model):
    name = models.CharField(max_length=200, null=True)
    phone = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200, null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
    return f" {self.id} - {self.name} - {self.date_created} - {self.email}"

commande line
--------------------->

> py manage.py makemigrations

Migrations for 'accounts':
  accounts\migrations\0001_initial.py
    - Create model Customer

> py manage.py migrate

Operations to perform:
  Apply all migrations: accounts, admin, auth, contenttypes, sessions
Running migrations:
  Applying accounts.0001_initial... OK


ensuite, dans accounts/admin.py
-------------------------------------->

from django.contrib import admin
from .models import Customer

admin.site.register(Customer)

==> http://127.0.0.1:8000/admin/
ensuite on peut voir Custumer dans l'admin panel

==> et on ajoute quelques customers


dans notre accounts/models.py, on ajoute 2 class Product et Customer
-------------------------------------------------------------------------

class Product(models.Model):
    CATEGORY = (
        ('Indoor', 'Indoor'),
        ('Out Door', 'Out Door')
    )
    name = models.CharField(max_length=200, null=True)
    price = models.FloatField(null=True)
    category = models.CharField(max_length=200, null=True, choices=CATEGORY)
    description = models.CharField(max_length=200, null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return f" {self.id} - {self.name} - {self.category} - {self.description} - {self.date_created}"


class Order(models.Model):
    STATUS = (
        ('Pending', 'Pending'),
        ('Out of delivery', 'Out of delivery'),
        ('Delivered', 'Delivered')
    )
    # customer =
    # product =
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    status = models.CharField(max_length=200, null=True, choices=STATUS)

    def __str__(self):
        return f" {self.id} - {self.date_created} - {self.status}"


et en commande line
---------------------->
> py manage.py makemigrations
> py mange.py migrate

et dans accounts/admin.py, on enregiste les classes
------------------------------------------------------->

from .models import Product
from .models import Order

...
...

admin.site.register(Product)
admin.site.register(Order)


#############################################################
#   base de données relation - One To Many && Many To Many
#############################################################

dans notre accounts/models.py, on change créee la relation :
----------------------------------------------------------------


class Order(models.Model):
    STATUS = (
        ('Pending', 'Pending'),
        ('Out of delivery', 'Out of delivery'),
        ('Delivered', 'Delivered')
    )
    customer = models.ForeignKey(Customer, null=True, on_delete=models.SET_NULL)    # on ajoute cette ligne
    product = models.ForeignKey(Product, null=True, on_delete=models.SET_NULL)      # on ajoute cette ligne
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    status = models.CharField(max_length=200, null=True, choices=STATUS)

    def __str__(self):
        return f" {self.id} - {self.date_created} - {self.status}"

et en commande line
---------------------->
> py manage.py makemigrations
> py mange.py migrate


ensuite, accounts/models.py, encore
------------------------------------------>

class Tag(models.Model):                                                                    # on ajoute cette ligne
    name = models.CharField(max_length=200, null=True)                                      # on ajoute cette ligne

    def __str__(self):                                                                      # on ajoute cette ligne
        return f" {self.name} "                                                             # on ajoute cette ligne



class Product(models.Model):
    CATEGORY = (
        ('Indoor', 'Indoor'),
        ('Out Door', 'Out Door')
    )
    name = models.CharField(max_length=200, null=True)
    price = models.FloatField(null=True)
    category = models.CharField(max_length=200, null=True, choices=CATEGORY)
    description = models.CharField(max_length=200, null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    tags = models.ManyToManyField(Tag)                                                      # on ajoute cette ligne

et en commande line
---------------------->
> py manage.py makemigrations
> py mange.py migrate


et dans accounts/admin.py, on enregiste les classes
------------------------------------------------------->

from .models import Product
from .models import Order
from .models import Tag                                                                    # on ajoute cette ligne

...
...

admin.site.register(Product)
admin.site.register(Order)
admin.site.register(Tag)                                                                   # on ajoute cette ligne


==> et on ajoute quelques customers, Product, Order, Tag
-------------------------------------------------------------

##################################################################################################
# query dans la base de données
###################################################################################################

from accounts.models import *

#***(1)Returns all customers from customer table
customers = Customer.objects.all()

#(2)Returns first customer in table
firstCustomer = Customer.objects.first()

#(3)Returns last customer in table
lastCustomer = Customer.objects.last()

#(4)Returns single customer by name
customerByName = Customer.objects.get(name='Peter Piper')

#***(5)Returns single customer by name
customerById = Customer.objects.get(id=4)

#***(6)Returns all orders related to customer (firstCustomer variable set above)
firstCustomer.order_set.all()

#(7)***Returns orders customer name: (Query parent model values)
order = Order.objects.first() 
parentName = order.customer.name

#(8)***Returns products from products table with value of "Out Door" in category attribute
products = Product.objects.filter(category="Out Door")

#(9)***Order/Sort Objects by id
leastToGreatest = Product.objects.all().order_by('id') 
greatestToLeast = Product.objects.all().order_by('-id') 


#(10) Returns all products with tag of "Sports": (Query Many to Many Fields)
productsFiltered = Product.objects.filter(tags__name="Sports")

'''
(11)Bonus
Q: If the customer has more than 1 ball, how would you reflect it in the database?
A: Because there are many different products and this value changes constantly you would most 
likly not want to store the value in the database but rather just make this a function we can run
each time we load the customers profile
'''


#Returns the total count for number of time a "Ball" was ordered by the first customer
ballOrders = firstCustomer.order_set.filter(product__name="Ball").count()

#Returns total count for each product orderd
allOrders = {}

for order in firstCustomer.order_set.all():
	if order.product.name in allOrders:
		allOrders[order.product.name] += 1
	else:
		allOrders[order.product.name] = 1

#Returns: allOrders: {'Ball': 2, 'BBQ Grill': 1}


#RELATED SET EXAMPLE
class ParentModel(models.Model):
	name = models.CharField(max_length=200, null=True)

class ChildModel(models.Model):
	parent = models.ForeignKey(Customer)
	name = models.CharField(max_length=200, null=True)

parent = ParentModel.objects.first()
#Returns all child models related to parent
parent.childmodel_set.all()

###########################################################################"""
#   rendering data to templates
###########################################################################"""

dans notre accounts/views.py
-----------------------------------

from .models import *                                                                   # on ajoute cette ligne

........
........

def products(request):
    products = Product.objects.all()                                                    # on ajoute cette ligne

    return render(request, 'accounts/products.html', {'products': products})            # on ajoute cette ligne


et dans notre tempate accounts/products.html, on affiche les données
--------------------------------------------------------------------------

{% extends 'accounts/main.html' %}

{% block title %} {{ title }} {% endblock %}

{% block content %}

    <br>

    <div class="row">
        <div class="col-md">
            <div class="card card-body">
                <h5>Products</h5>
            </div>
            <div class="card card-body">
                <table class="table">
                    <tr>
                        <th>Product</th>
                        <th>Category</th>
                        <th>Price</th>
                    </tr>

                    {% for i in products %}                                                 # on ajoute cette ligne
                        <tr>                                                                # on ajoute cette ligne
                            <td> {{ i.name }} </td>                                         # on ajoute cette ligne
                            <td> {{ i.category }}</td>                                      # on ajoute cette ligne
                            <td> {{ i.price }}</td>                                         # on ajoute cette ligne
                        </tr>                                                               # on ajoute cette ligne
                    {% endfor %}                                                            # on ajoute cette ligne

                </table>
            </div>
        </div>

    </div>


{% endblock %}


dans notre accounts/views.py, on va passer les données 
---------------------------------------------------------------
from django.shortcuts import render
from .models import *


def home(request):
    orders = Order.objects.all()
    customers = Customer.objects.all()

    total_customers = customers.count()
    total_orders = orders.count()
    delivered = orders.filter(status='Delivered').count()
    pending = orders.filter(status='Pending').count()

    context = {
        'orders': orders,
        'customers': customers,
        'total_customers': total_customers,
        'total_orders': total_orders,
        'delivered': delivered,
        'pending': pending,
    }

    return render(request, 'accounts/dashboard.html', context)


def products(request):
    products = Product.objects.all()

    return render(request, 'accounts/products.html', {'products': products})


def customers(request):
    return render(request, 'accounts/customers.html')

dans accounts/dashboard.html
---------------------------------
{% extends 'accounts/main.html' %}

{% block title %} Dashboard {{ title }} {% endblock %}

{% block content %}
    <div class="row">
        <div class="col-md-5">
            <h5>CUSTOMERS:</h5>
            <hr>
            <div class="card card-body">
                <a class="btn btn-primary  btn-sm btn-block" href="">Create Customer</a>
                <table class="table table-sm">
                    <tr>
                        <th>Customer</th>
                        <th>phone</th>
                    </tr>


                    {% for customer in customers %}

                        <tr>
                            <td>{{ customer.name }}</td>
                            <td>{{ customer.phone }}</td>
                        </tr>

                    {% endfor %}

                </table>
            </div>
        </div>

        <div class="col-md-7">
            <h5>LAST 5 ORDERS</h5>
            <hr>
            <div class="card card-body">
                <a class="btn btn-primary  btn-sm btn-block" href="">Create Order</a>
                <table class="table table-sm">
                    <tr>
                        <th>Product</th>
                        <th>Date Orderd</th>
                        <th>Status</th>
                        <th>Update</th>
                        <th>Remove</th>
                    </tr>

                    {% for order in orders %}

                        <tr>
                            <td>{{ order.product }}</td>
                            <td>{{ order.date_created }}</td>
                            <td>{{ order.status }}</td>
                            <td><a href="">Update</a></td>
                            <td><a href="">Delete</a></td>
                        </tr>

                    {% endfor %}

                </table>
            </div>
        </div>

    </div>
{% endblock %}


dans accounts/status.html
---------------------------------



<br>

<div class="row">
    <div class="col">
        <div class="col-md">
            <div class="card text-center text-white  mb-3" id="total-orders">
                <div class="card-header">
                    <h5 class="card-title">Total Orders</h5>
                </div>
                <div class="card-body">
                    <h3 class="card-title">{{ total_orders }}</h3>
                </div>
            </div>
        </div>
    </div>

    <div class="col">
        <div class="col-md">
            <div class="card text-center text-white  mb-3" id="orders-delivered">
                <div class="card-header">
                    <h5 class="card-title">Orders Delivered</h5>
                </div>
                <div class="card-body">
                    <h3 class="card-title">{{ delivered }}</h3>
                </div>
            </div>
        </div>
    </div>

    <div class="col">
        <div class="col-md">
            <div class="card text-center text-white  mb-3" id="orders-pending">
                <div class="card-header">
                    <h5 class="card-title">Orders Pending</h5>
                </div>
                <div class="card-body">
                    <h3 class="card-title">{{ pending }}</h3>
                </div>
            </div>
        </div>
    </div>
</div>


dans accounts/products.html
---------------------------------


{% extends 'accounts/main.html' %}

{% block title %} {{ title }} {% endblock %}

{% block content %}

    <br>

    <div class="row">
        <div class="col-md">
            <div class="card card-body">
                <h5>Products</h5>
            </div>
            <div class="card card-body">
                <table class="table">
                    <tr>
                        <th>Product</th>
                        <th>Category</th>
                        <th>Price</th>
                    </tr>

                    {% for i in products %}
                        <tr>
                            <td> {{ i.name }} </td>
                            <td> {{ i.category }}</td>
                            <td> {{ i.price }}</td>
                        </tr>
                    {% endfor %}

                </table>
            </div>
        </div>

    </div>


{% endblock %}



##############################################################
# dynamic url - routing - templates
##############################################################


on veut avoir des urls comme ca http://127.0.0.1:8000/customers/1......
donc, dans accounts/views.py
--------------------------------------------------------------------------

....
....

def customers(request, pk_test):                                    # On passe pk_test c important
    customer = Customer.objects.get(id=pk_test)                     # et ca aussi
    orders = customer.order_set.all()
    order_count = orders.count()
    context = {
        'customer': customer,
        'orders': orders,
        'order_count': order_count,
    }
    return render(request, 'accounts/customers.html', context)


dans accounts/urls.py
------------------------------------------------->
...
...

urlpatterns = [
    path('', views.home),
    path('products/', views.products),
    path('customers/<str:pk_test>', views.customers),                                    # on modifie cette ligne
    
]



et dans accounts/customers.html
------------------------------------------->

{% extends 'accounts/main.html' %}

{% block title %} {{ title }} {% endblock %}

{% block content %}

    <br>

    <div class="row">
        <div class="col-md">
            <div class="card card-body">
                <h5>Customer:</h5>
                <hr>
                <a class="btn btn-outline-info  btn-sm btn-block" href="">Update Customer</a>
                <a class="btn btn-outline-danger  btn-sm btn-block" href="">Delete Customer</a>

            </div>
        </div>

        <div class="col-md">
            <div class="card card-body">
                <h5>Contact Information</h5>
                <hr>
                <p>Email: {{ customer.email }} </p>
                <p>Phone: {{ customer.phone }} </p>
            </div>
        </div>

        <div class="col-md">
            <div class="card card-body">
                <h5>Total Orders</h5>
                <hr>
                <h1 style="text-align: center;padding: 10px">{{ order_count }}</h1>
            </div>
        </div>
    </div>


    <br>
    <div class="row">
        <div class="col">
            <div class="card card-body">
                <form method="get">

                <button class="btn btn-primary" type="submit">Search</button>
              </form>
            </div>
        </div>

    </div>
    <br>

    <div class="row">
        <div class="col-md">
            <div class="card card-body">
                <table class="table table-sm">
                    <tr>
                        <th>Product</th>
                        <th>Category</th>
                        <th>Date Orderd</th>
                        <th>Status</th>
                        <th>Update</th>
                        <th>Remove</th>
                    </tr>

                    {% for order in orders %}

                        <tr>
                            <td>{{ order.product }}</td>
                            <td>{{ order.product.category }}</td>
                            <td>{{ order.date_created }}</td>
                            <td>{{ order.status }}</td>

                            <td><a class="btn btn-sm btn-info" href="">Update</a></td>
                            <td><a class="btn btn-sm btn-danger" href="">Delete</a></td>

                        </tr>

                    {% endfor %}

                </table>
            </div>
        </div>
    </div>


{% endblock %}


##################################################################################
#   CRUD with model form
##################################################################################


- creer accounts/order_form.html, mettre un formulaire simple d'abord
------------------------------------------------------------------------

{% extends 'accounts/main.html' %}
{% load static %}
{% block title %} {% endblock %}

{% block content %}

    <form action="" method="POST">

        <input type="submit" name="Submit">
    </form>


{% endblock %}


- dans accounts/views.py, on va ajouter une 
- ---------------------------------------
def createOrder(request):
    context = {

    }
    return render(request, 'accounts/order_form.html', context)

dans accounts/urls.py, on ajoute une urls 
--------------------------------------------------
urlpatterns = [
    ......
    ........,
    path('create_order/', views.createOrder, name='create_order'),
]


dans accounts/dashboard.html, on ajoute le lien
-----------------------------------------------------
...
...
<a class="btn btn-primary  btn-sm btn-block" href="{% url 'create_order' %}">Create Order</a>
...
...

creer accounts/forms.py
----------------------------
from django.forms import ModelForm
from .models import Order


class OrderForm(ModelForm):
    class Meta:
        model = Order
        fields = '__all__'




dans accounts/view.py, on importe cette OrderForm, comme ca on peut l'utiliser dans notre templates
-----------------------------------------------------------------------------------------------------

from .forms import OrderForm                                                    # nouveau

...
...
def createOrder(request):
    form = OrderForm()                                                          # nouveau
    context = {
        'form': form,

    }
    return render(request, 'accounts/order_form.html', context)


dans notre template accounts/order_form.html
-------------------------------------------------


on revient dans notre dans accounts/view.py,
-----------------------------------------------------
from django.shortcuts import ......, redirect

....
....

def createOrder(request):
    form = OrderForm()
    if request.method == 'POST':                                                        # nouveau
        # print('printing POST', request.POST)  
        form = OrderForm(request.POST)                                                  # nouveau

        if form.is_valid():                                                             # nouveau
            form.save()                                                                 # nouveau
            return redirect('/')                                                        # nouveau    

    context = {
        'form': form,

    }
    return render(request, 'accounts/order_form.html', context)

et on essaie de creer un nouvel order, et boom ca marche
------------------------------------------------------------

maintenant, on va implementer l'update
dans accounts/views.py
-------------------------------------

def updateOrder(request, pk):

    form = OrderForm()
    context = {
        'form': form,

    }
    return render(request, 'accounts/order_form.html', context)



dans accounts/urls.py
---------------------------
urlpatterns = [
    ...,
    path('update_order/<str:pk>/', views.updateOrder, name='update_order'),

]


et on creer un lien dans accounts/dashboard.html
--------------------------------------------------------

..............
<td><a class="btn btn-sm btn-info" href="{% url 'update_order' order.id %}">Update</a></td>
..............


et on verifie et le lien marche
ensuite, on va pré-remplir le formulaire avec ce code dans accounts/views.py
---------------------------------------------------------------------------------

def updateOrder(request, pk):

    order = Order.objects.get(id=pk)                                            # on ajoute ca
    form = OrderForm(instance=order)                                            # on ajoute ca
    context = {
        'form': form,

    }
    return render(request, 'accounts/order_form.html', context)


ensuite, on va mettre a jour la base de donnée avec ca, encore dans accounts/views.py
-------------------------------------------------------------------------------------------

def updateOrder(request, pk):

    order = Order.objects.get(id=pk)
    form = OrderForm(instance=order)

    if request.method == 'POST':
        # print('printing POST', request.POST)
        form = OrderForm(request.POST, instance=order)

        if form.is_valid():
            form.save()
            return redirect('/')

    context = {
        'form': form,

    }
    return render(request, 'accounts/order_form.html', context)

et on verifie et ca marrche
maintenant, on va implementer le delete, dans accounts/views.py
----------------------------------------------------------------------------------

def deleteOrder(request, pk):
    order = Order.objects.get(id=pk)
    if request.method == 'POST':
        order.delete()
        return redirect('/')

    context = {
        'item': order
    }
    return render(request, 'accounts/delete.html', context)

creer accounts/delete.html avec
---------------------------------
{% extends 'accounts/main.html' %}
{% load static %}
{% block title %} {{ title }} {% endblock %}

{% block content %}

    <p>Are you are sure to delete an "{{ item }}?"</p>
    <form action="{% url 'delete_order' item.id %}" method="POST">
        {% csrf_token %}
        <a href="{% url 'home' %}">Cancel</a>
        <input type="submit" name="Confirm">
    </form>

{% endblock %}


dans accounts/urls.py
-------------------------

urlpatterns = [
    ....,
    path('delete_order/<str:pk>/', views.deleteOrder, name='delete_order'),

]


dans accounts/dashboard.html
---------------------------------
....
<td><a class="btn btn-sm btn-danger" href="{% url 'delete_order' order.id %}">Delete</a></td>
.....


et on stylise un peu notre accounts/delete.html
----------------------------------------------------

{% extends 'accounts/main.html' %}
{% load static %}
{% block title %} {{ title }} {% endblock %}

{% block content %}

    <br>
    <div class="row">
        <div class="col-md-6">
            <div class="card card-body">
                <p>Are you are sure to delete an "{{ item }}?"</p>
                <form action="{% url 'delete_order' item.id %}" method="POST">
                    {% csrf_token %}
                    <a class="btn btn-warning" href="{% url 'home' %}">Cancel</a>
                    <input class="btn btn-danger" type="submit" name="Confirm">
                </form>
            </div>
        </div>

    </div>
    
{% endblock %}


styliser un peu notre accounts/order_form.html
--------------------------------------------------
{% extends 'accounts/main.html' %}
{% load static %}
{% block title %} {% endblock %}

{% block content %}

    <div class="row">
        <div class="col-md-6">
            <div class="card card-body">
                <form action="" method="POST">
                    {% csrf_token %}
                    {{ form }}
                    <input type="submit" name="Submit">
                </form>

            </div>
        </div>
    </div>


{% endblock %}


###############################################################
#   inline formsets
###############################################################


###############################################################
#   User registration
###############################################################

on ajoute l'urls
----------------------
from . import views
from django.urls import path


urlpatterns = [
    path('register/', views.registerPage, name='register'),
    path('login/', views.loginPage, name='login'),
    path('logout/', views.logoutUser, name='logout'),
...

on ajoute les views
-----------------------
from django.contrib.auth.forms import UserCreationForm


def registerPage(request):
    form = UserCreationForm()
    context = {'form': form}
    return render(request, 'accounts/register.html', context)

def loginPage(request):
    context = {}
    return render(request, 'accounts/login.html', context)

on creer register.html, et on code
-------------------------------------
<h3>Register</h3>

<form action="" method="POST">
    {{ form }}
</form>

on verifie avec http://127.0.0.1:8000/register/
-----------------------------------------------
et ca marche on a la page par defaut de register de django


Mais comment pour créer notre propre formulaire
--------------------------------------------------

dans form.py, on crée une nouvelle class CreateUserForm
--------------------------------------------------------

from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = [
            'username',
            'email',
            'password1',
            'password2'
        ]

dans views.py, on modifie la fonction register et importer notre propre CreateUserForm
qui herite UserCreationForm de django
-----------------------------------------

def registerPage(request):
    form = CreateUserForm()

    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()

    context = {'form': form}
    return render(request, 'accounts/register.html', context)

on test avec http://127.0.0.1:8000/register/
-------------------------------------------
et le champ email apparait!

on va maintenant manuellement faire le rendu du formulaire dans 
notre register.html
-----------------------------------------------------------------

<h3>Register</h3>

<form action="" method="POST">
    {% csrf_token %}

    {% for field in form %}
        {{ field.label }}
        {{ field }}
    {% endfor %}

    <input type="submit" name="Create User">
</form>

on test avec http://127.0.0.1:8000/register/, ca marche
mais on a pas encore de controle sur chaque champ du formulaire,
pour faire on change le code comme suivant
---------------------------------------------------------------------
<h3>Register</h3>

<form action="" method="POST">
    {% csrf_token %}

    {{ form.username.label }}
    {{ form.username }}

    {{ form.email.label }}
    {{ form.email }}

    {{ form.password1.label }}
    {{ form.password1 }}

    {{ form.password2.label }}
    {{ form.password2 }}

    <input type="submit" name="Create User">
</form>


on verifie avec http://127.0.0.1:8000/register/ et ca marche,
il nous reste qu'à styliser avec
dans register.html
------------------------------------------------------------------

<!DOCTYPE html>
<html>

<head>
	<title>Login</title>
	<link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.1.3/css/bootstrap.min.css" integrity="sha384-MCw98/SFnGE8fJT3GXwEOngsV7Zt27NXFoaoApmYm81iuXoPkFOJwJ8ERdknLPMO" crossorigin="anonymous">
	<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.3.1/jquery.min.js"></script>
	<link rel="stylesheet" href="https://use.fontawesome.com/releases/v5.6.1/css/all.css" integrity="sha384-gfdkjb5BdAXd+lj+gudLWI+BXq4IuLW5IT+brZEZsLFm++aCMlF1V92rMkPaX4PP" crossorigin="anonymous">

	<style>
		body,
		html {
			margin: 0;
			padding: 0;
			height: 100%;
			background: #7abecc !important;
		}
		.user_card {
			width: 350px;
			margin-top: auto;
			margin-bottom: auto;
			background: #74cfbf;
			position: relative;
			display: flex;
			justify-content: center;
			flex-direction: column;
			padding: 10px;
			box-shadow: 0 4px 8px 0 rgba(0, 0, 0, 0.2), 0 6px 20px 0 rgba(0, 0, 0, 0.19);
			-webkit-box-shadow: 0 4px 8px 0 rgba(0, 0, 0, 0.2), 0 6px 20px 0 rgba(0, 0, 0, 0.19);
			-moz-box-shadow: 0 4px 8px 0 rgba(0, 0, 0, 0.2), 0 6px 20px 0 rgba(0, 0, 0, 0.19);
			border-radius: 5px;

		}

		.form_container {
			margin-top: 20px;
		}

		#form-title{
			color: #fff;
		}
		.login_btn {
			width: 100%;
			background: #33ccff !important;
			color: white !important;
		}
		.login_btn:focus {
			box-shadow: none !important;
			outline: 0px !important;
		}
		.login_container {
			padding: 0 2rem;
		}
		.input-group-text {
			background: #f7ba5b !important;
			color: white !important;
			border: 0 !important;
			border-radius: 0.25rem 0 0 0.25rem !important;
		}
		.input_user,
		.input_pass:focus {
			box-shadow: none !important;
			outline: 0px !important;
		}

	</style>

</head>
<body>
	<div class="container h-100">
		<div class="d-flex justify-content-center h-100">
			<div class="user_card">
				<div class="d-flex justify-content-center">
					<h3 id="form-title">REGISTER ACCOUNT</h3>
				</div>
				<div class="d-flex justify-content-center form_container">

					<form method="POST" action="">

                        {% csrf_token %}

						<div class="input-group mb-3">
							<div class="input-group-append">
								<span class="input-group-text"><i class="fas fa-user"></i></span>
							</div>
{#							<input type="text" name="username">#}
                            {{ form.username }}
						</div>
						<div class="input-group mb-2">
							<div class="input-group-append">
								<span class="input-group-text"><i class="fas fa-envelope-square"></i></span>
							</div>
{#							<input type="email" name="email">#}
                            {{ form.email }}
						</div>
						<div class="input-group mb-2">
							<div class="input-group-append">
								<span class="input-group-text"><i class="fas fa-key"></i></span>
							</div>
{#							<input type="text" name="password1">#}
                            {{ form.password1 }}
						</div>
						<div class="input-group mb-2">
							<div class="input-group-append">
								<span class="input-group-text"><i class="fas fa-key"></i></span>
							</div>
{#							<input type="text" name="password2">#}
                            {{ form.password2 }}
						</div>

				   		<div class="d-flex justify-content-center mt-3 login_container">
				 			<input class="btn login_btn" type="submit" value="Register Account">
				   		</div>
					</form>
				</div>

                {{ form.errors }}

				<div class="mt-4">
					<div class="d-flex justify-content-center links">
						Already have an account? <a href="{% url 'login' %}" class="ml-2">Login</a>
					</div>
				</div>
			</div>
		</div>
	</div>
	<script>
						/* Because i didnt set placeholder values in forms.py they will be set here using vanilla Javascript
		//We start indexing at one because CSRF_token is considered and input field
		 */

		//Query All input fields
		var form_fields = document.getElementsByTagName('input')
		form_fields[1].placeholder='Username..';
		form_fields[2].placeholder='Email..';
		form_fields[3].placeholder='Enter password...';
		form_fields[4].placeholder='Re-enter Password...';


		for (var field in form_fields){
			form_fields[field].className += ' form-control'
		}
	</script>
</body>
</html>


dans login.html
-------------------


<!DOCTYPE html>
<html>

<head>
	<title>Login</title>
	<link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.1.3/css/bootstrap.min.css" integrity="sha384-MCw98/SFnGE8fJT3GXwEOngsV7Zt27NXFoaoApmYm81iuXoPkFOJwJ8ERdknLPMO" crossorigin="anonymous">
	<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.3.1/jquery.min.js"></script>
	<link rel="stylesheet" href="https://use.fontawesome.com/releases/v5.6.1/css/all.css" integrity="sha384-gfdkjb5BdAXd+lj+gudLWI+BXq4IuLW5IT+brZEZsLFm++aCMlF1V92rMkPaX4PP" crossorigin="anonymous">


	<style>
		body,
		html {
			margin: 0;
			padding: 0;
			height: 100%;
			background: #7abecc !important;
		}
		.user_card {
			width: 350px;
			margin-top: auto;
			margin-bottom: auto;
			background: #74cfbf;
			position: relative;
			display: flex;
			justify-content: center;
			flex-direction: column;
			padding: 10px;
			box-shadow: 0 4px 8px 0 rgba(0, 0, 0, 0.2), 0 6px 20px 0 rgba(0, 0, 0, 0.19);
			-webkit-box-shadow: 0 4px 8px 0 rgba(0, 0, 0, 0.2), 0 6px 20px 0 rgba(0, 0, 0, 0.19);
			-moz-box-shadow: 0 4px 8px 0 rgba(0, 0, 0, 0.2), 0 6px 20px 0 rgba(0, 0, 0, 0.19);
			border-radius: 5px;

		}

		.form_container {
			margin-top: 20px;
		}

		#form-title{
			color: #fff;

		}

		.login_btn {
			width: 100%;
			background: #33ccff !important;
			color: white !important;
		}
		.login_btn:focus {
			box-shadow: none !important;
			outline: 0px !important;
		}
		.login_container {
			padding: 0 2rem;
		}
		.input-group-text {
			background: #f7ba5b !important;
			color: white !important;
			border: 0 !important;
			border-radius: 0.25rem 0 0 0.25rem !important;
		}
		.input_user,
		.input_pass:focus {
			box-shadow: none !important;
			outline: 0px !important;
		}

		#messages{
			background-color: grey;
			color: #fff;
			padding: 10px;
			margin-top: 10px;
		}
	</style>

</head>
<body>
	<div class="container h-100">
		<div class="d-flex justify-content-center h-100">
			<div class="user_card">
				<div class="d-flex justify-content-center">


					<h3 id="form-title">LOGIN</h3>
				</div>
				<div class="d-flex justify-content-center form_container">

					<form method="POST" action="">

                        {% csrf_token %}

						<div class="input-group mb-3">
							<div class="input-group-append">
								<span class="input-group-text"><i class="fas fa-user"></i></span>
							</div>
							<input type="text" name="username" placeholder="Username..." class="form-control">
						</div>
						<div class="input-group mb-2">
							<div class="input-group-append">
								<span class="input-group-text"><i class="fas fa-key"></i></span>
							</div>
								<input type="password" name="password" placeholder="Password..." class="form-control" >
						</div>

							<div class="d-flex justify-content-center mt-3 login_container">
				 				<input class="btn login_btn" type="submit" value="Login">
				   			</div>
					</form>

				</div>

                {% for message in messages %}
                    <p id="messages">{{ message }}</p>
                {% endfor %}

				<div class="mt-4">
					<div class="d-flex justify-content-center links">
						Don't have an account? <a href="{% url 'register' %}" class="ml-2">Sign Up</a>
					</div>

				</div>
			</div>
		</div>
	</div>
</body>

</html>


maintenant, on va gerer la views de register
------------------------------------------------

from django.contrib import messages


def registerPage(request):
    form = CreateUserForm()

    if request.method == 'POST':

        form = CreateUserForm(request.POST)

        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, 'Account was created for' + user)

            return redirect('login')

    context = {'form': form}
    return render(request, 'accounts/register.html', context)


on va maintenant implementer la views login
---------------------------------------------------

from django.contrib.auth import authenticate, login, logout

....

def loginPage(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.info(request, 'Username or password is incorrect')

    context = {}
    return render(request, 'accounts/login.html', context)

def logoutUser(request):
    logout(request)
    return redirect('login')


et la version finale de l'implementation du l'utilisateur
-----------------------------------------------------------

from django.shortcuts import render, redirect
from .models import *

from .forms import OrderForm, CreateUserForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required



from .filters import OrderFilter


def registerPage(request):

    if request.user.is_authenticated:
        return redirect('home')

    else:

        form = CreateUserForm()

        if request.method == 'POST':

            form = CreateUserForm(request.POST)

            if form.is_valid():
                form.save()
                user = form.cleaned_data.get('username')
                messages.success(request, 'Account was created for' + user)

                return redirect('login')

        context = {'form': form}
        return render(request, 'accounts/register.html', context)


def loginPage(request):

    if request.user.is_authenticated:
        return redirect('home')

    else:

        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                messages.info(request, 'Username or password is incorrect')

        context = {}
        return render(request, 'accounts/login.html', context)


def logoutUser(request):
    logout(request)
    return redirect('login')


#####################################################################
#   User Role Based Permissions & Authentication 
#   Créer notre propre decorator fait maison
#####################################################################

creer un template accounts/user.html
----------------------------------------
{% extends 'accounts/main.html' %}

{% block content %}

    <h3>User Profile</h3>

{% endblock %}

dans views.py on creer la vue
----------------------------------
def userPage(request):
    context = {}
    return render(request, 'accounts/user.html', context)


on va créer notre propre decorators pour gerer la registerPage de la views
créer un fichier accounts/decorators.py
--------------------------------------------------------------------------
from django.http import HttpResponse
from django.shortcuts import redirect


def unauthenticated_user(view_func):
    def wrapper_func(request, *args, **kwargs):

        if request.user.is_authenticated:
            return redirect('home')

        return view_func(request, *args, **kwargs)

    return wrapper_func


et on peut modifier notre views.py comme ca avec notre decorator
----------------------------------------------------------------------

from .decorators import unauthenticated_user

@unauthenticated_user
def registerPage(request):

    form = CreateUserForm()

    if request.method == 'POST':

        form = CreateUserForm(request.POST)

        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, 'Account was created for' + user)

            return redirect('login')

    context = {'form': form}
    return render(request, 'accounts/register.html', context)


@unauthenticated_user
def loginPage(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.info(request, 'Username or password is incorrect')

    context = {}
    return render(request, 'accounts/login.html', context)



maintenant on va ajouter dans http://127.0.0.1:8000/admin/
un groupe admin et customer
--------------------------

ensuite on ajoute beloub dans le groupe admin
et bl dans le groupe customer


ensuite on va creer un décorator pour gerer les roles dans notre
fichier docorators.py
----------------------------------------------------------------->

from django.http import HttpResponse
from django.shortcuts import redirect


def unauthenticated_user(view_func):
    def wrapper_func(request, *args, **kwargs):

        if request.user.is_authenticated:
            return redirect('home')

        return view_func(request, *args, **kwargs)

    return wrapper_func


def allowed_users(allowed_roles=[]):
    def decorator(view_func):
        def weapper_func(request, *args, **kwargs):

            print("ca marche!", allowed_roles)
            group = None
            if request.user.groups.exists():
                group = request.user.groups.all()[0].name

            if group in allowed_roles:
                return view_func(request, *args, **kwargs)
            else:
                return HttpResponse('You are not authorized to view this page!')
        return weapper_func
    return decorator


def admin_only(view_func):
    def wrapper_function(request, *args, **kwargs):
        group = None
        if request.user.groups.exists():
            group = request.user.groups.all()[0].name

        if group == 'customer':
            return redirect('user-page')

        if group == 'admin':
            return view_func(request, *args, **kwargs)

    return wrapper_function

dans views.py on va utiliser cette decorator
pour permettre seulement au groupe admin d'acceder à la page home
------------------------------------------------------------------

et mettre 
@allowed_users(allowed_roles=['admin'])

avant les fonctions













