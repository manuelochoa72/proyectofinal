from django.db import models

# Create your models here.
class Cliente(models.Model):
    Nombre=models.CharField(max_length=50)
    Edad=models.IntegerField()
    Fecha=models.DateTimeField('Fecha de registro')

    def __str__(self) -> str:
        return "Nombre de Cliente: "+ self.Nombre

class Prestamo(models.Model):
    cliente_fk= models.ForeignKey(Cliente, on_delete=models.CASCADE)
    monto=models.FloatField()
    num_prestamo=models.IntegerField()
    fecha=models.DateField('Fecha que se otorga el prestamo: ')
    interes=models.FloatField()
    total_pago=models.FloatField()

    
    def save(self, *args, **kwargs):
       self.total_pago=self.monto*(1+(self.interes/100))
       return super(Prestamo, self).save(*args, **kwargs)


    def __str__(self) -> str:
        return str(self.cliente_fk.Nombre)
    

