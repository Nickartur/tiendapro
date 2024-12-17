from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Product(models.Model):
    sku = models.CharField(max_length=64)
    name = models.CharField(max_length=256)
    # 2 decimales a la derecha
    price = models.DecimalField(decimal_places=2, max_digits=6)
    weight = models.DecimalField(decimal_places=2, max_digits=6)
    description = models.TextField()
    thumbnail = models.ImageField(upload_to="products_thumbs/")
    image = models.ImageField(upload_to="products_images/")
    create_date = models.DateField()
    stock = models.DecimalField(decimal_places=2, max_digits=6)
# Este sería el modelo del producto (lo anterior)

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=128)
    descripcion = models.TextField()

    def __str__(self):
        return self.name


class ProductCategory(models.Model):
    # PROTECT, default = 1 esto es en caso no estuviese el registro
    product = models.ForeignKey(Product, on_delete=models.PROTECT)
    # Es decir, antes no estaba, fue migrado antes de estar creado
    category = models.ForeignKey(Category, on_delete=models.PROTECT)

    def __str__(self):
        return self.category.name + " > " + self.product.name


class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.PROTECT)
    billing_address = models.TextField()
    shipping_address = models.TextField()
    phone = models.CharField(max_length=64)

    def __str__(self):
        return self.user.username + " Telefono: " + self.phone
# Se agrega esto desde las pruebas realizadas, aunque en vez de nuevo_customer se pone =self
    def get_current_order(self):
        nueva_order = Order.objects.filter(customer=self, status = "PENDIENTE").first()
        # Si nueva_order NO es None, lo retornamos
        if nueva_order is None:
            # Si nueva_order is None, lo creamos
            nueva_order = Order()
            nueva_order.customer = self
            nueva_order.shipping_address = self.shipping_address
            nueva_order.status = "PENDIENTE"
            nueva_order.save()
        return nueva_order
    
class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.PROTECT)
    shipping_address = models.TextField()
    order_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=32) # PENDIENTE # PAGADO
    
    def __str__(self):
        return self.customer.user.username + " Estado Orden: " + self.status
    
class OrderDetail(models.Model):
    order = models.ForeignKey(Order, on_delete=models.PROTECT) # Se podria poner CASCADE, pero eliminaria todo de un tiron
    # con PROTECT se tendría que ir desde abajo hasta arriba borrando
    product = models.ForeignKey(Product, on_delete=models.PROTECT)
    price = models.DecimalField(decimal_places=2, max_digits=6) #9999.12
    quantity = models.DecimalField(decimal_places=2, max_digits=6) # 9999.12
    
    def __str__(self):
        return self.order.id + " " + self.product.name
    
