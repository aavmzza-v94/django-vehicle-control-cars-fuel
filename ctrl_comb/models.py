from django.db import models
from django.urls import reverse # para reverse
from bases.models import ClaseModelo # importar de bases la clasemodelo....

# Create your models here.
class Mark(ClaseModelo): # esta es la CLASE DEFINIDA PARA EXPORTAR A URLS, FORMS Y DEMAS... define los campos...
    # Aquí defines una clase llamada Mark, que hereda de models.Model. 
    # Esto indica que Mark es un modelo de Django y que se mapeará a una tabla en la base de datos.
    descript = models.CharField(
        # models.CharField: Es un tipo de campo que almacena datos de texto con una longitud máxima especificada.
        max_length=50, # Especifica que la longitud máxima del texto almacenado en este campo es de 50 caracteres.
        unique=True # Indica que los valores en este campo deben ser únicos en toda la tabla, es decir, 
        # no puede haber dos filas en la base de datos con el mismo valor en el campo descript.
    )

    def __str__(self):
        return self.descript # ya esta declarado en la clase.. retorno... nombre de marca..
    
    # En el contexto de una aplicación, este modelo podría representar una "Marca" (por ejemplo, marcas de automóviles, marcas de productos, etc.). 
    # La propiedad descript 
    # almacenaría el nombre o descripción de la marca, asegurándose de que no haya duplicados gracias al atributo unique=True.

    # django puede tener una clase dentro de otra clase... como META... metadatos adicionales.. info como se comporta el modelo.. 
    # y personaliza el comportamiento de django en ese modelo... campo unico, orden, unit, etcetera varios campos en clase meta...

    class Meta:
        verbose_name = "Marca" # para que django lo ponga en espanhol como marca... en la seccion de admin...
        verbose_name_plural = "Marcas" # en plural... MIGRAR Y CREARA UN ORM... SE CONECTARA A LA BASE DE DATOS Y APLICA LOS CAMBIOS
        # CREARA DJANGO UNA TABLA EN LA BASE DE DATOS... PSQL... NOMBRE DE TABLA ES MARK... ctrl_comb_marca... se llamara...

class Modelo(ClaseModelo): # hereda model..  ahora clasemodelo... LUEGO MIGRAR...
    descript = models.CharField( # tipo de datos charfield...
        max_length=50, # tamanho de los campos...
        db_comment="Descripcion del Modelo de Vehiculo",  # comentario en la base de datos.. 1er campo, a nivel de campo
    ) # tipo de datos charfield...

    # 2do campo.. 
    mark = models.ForeignKey(Mark,
                             on_delete= models.PROTECT) # relacion de marca con modelo por foreign key.. especificar nombre de modelo
    # PROTECT ES CUANDO SE QUIERA ELIMINAR UN REGISTRO EL SISTEMA NO PERMITA PORQUE TIENE REGISTROS A TABLAS ASOCIADAS... 
    # NO SE BORRE SU DETALLE... cascade si se borra marcas que se borre todo los modelos
    
    def __str__(self):
        return f"{self.mark} - {self.descript}" # imprimir en fstring o cadenas dinamicas la marca... y descripcion de modelo..
    
    class Meta:  # para las orm... 
        verbose_name_plural = "Modelos" # en plural... MIGRAR Y CREARA UN ORM... SE CONECTARA A LA BASE DE DATOS Y APLICA LOS CAMBIOS
        # comentario a nivel de tabla abajo
        db_table_comment = "Modelos de Vehiculos" # asociado por medio del foreign key.. LUEGO TOCA CREAR LAS MIGRACIONES...
        # el init en migrations de ctrl_comb es el codigo fuente de python y django para trabajar con la base de datos...

        # AGREGAR PROPIEDAD PERMISSION, LISTA DE TUPLAS... PERMISOS PERSONALIZADOS... NO PUEDEN SER MODIFICADOS...
        permissions = [
            {"permiso_especial","Puede Leer y Editar Modelos"}, # 1ER PERMISO
            

        ]

# MODELO PARA EL VEHICULO... VENIR ACA PARA CONSTRUIR... SECCION 19... NO OLVIDAR APLICAR EL CHOICE...

class Vehiculo(ClaseModelo): # heredamos clase modelo para el usuario que modifique.. crear referencia al modelo de vehiculo
    # importado de bases.models... para crear campos.. models.Modelo hace referencia para CREAR CAMPOS EN LA BASE DE DATOS...
    modelo = models.ForeignKey(Modelo, on_delete=models.RESTRICT) # los modelos nos permite borrar porque se vincula a los vehiculos
    register = models.CharField(   # definir la matricula del modelo....
        max_length=50, # longiud de 50 de campo
        db_column="Matricula Vehiculo", # comentario de columna, no olvidar la coma
        help_text="Matricula Vehiculo", # ESTO CREA UNA TABLA PARA LUEGO HACER LA MIGRACION!!! OJO!!!
    )
    year = models.PositiveSmallIntegerField(help_text="Año del Vehiculo") # anho del vehiculo, 4 enteros... nomas

    TIPO_CHOICES = [ # TUPLA, SIEMPRE EN MODELOS....
        ('MOT','Motocicleta'), # PRIMER ELEMENTO, ELEMENTOS A ELEGIR... 
        ('CAP','Caponera'),
        ('SUV','Camioneta (SUV)'),
        ('PIK', 'PickUp'),
        ('SED', 'Sedán'),
        ('TAX', 'Taxi'),
        ('MIC', 'Microbús'),
        ('BUS', '(Auto)BUS'),
        ('CAM', 'Camión'),
    ]

    tipo = models.CharField(choices=TIPO_CHOICES, max_length=3, 
                            default='SED') # para almacenar en la base de datos tipo de vehiculo... OJO! migrar
    
    class UnidadMedida(models.IntegerChoices): # VALORES DE LITROS... EN GALONES TBN, para el combustible...
        GALONES = 1
        LITROS = 2

    # CREAR EL CAMPO...
    unidad_medida = models.IntegerField(choices=UnidadMedida.choices,
                                        default=1) # que sea por defecto la 1ra unidad galones..
    # HACER LA MIGRACION A CTRL_COMB PARA LA TABLA DE BASE DE DATOS... POR EMPLEAR MODELS...


    # AGREGAR CAMPO PARA VALOR CALCULADO POR CONSULTA... LITROS Y GALONES...

    @property # hacer migracion en ctrl_comb no habra cambios.... por propiedad...
    def factor(self): # no recibe ningun valor...
        f = 1 # la columna no recibe valor, por default es 1... si la unidad de medida es 1... pero si es 2 es factor multiplicativo
        if self.unidad_medida == 2:
            f = 0.264172 # factor para litros..
        return f # kilometros por unidad seleccionada... kilometros/litro o kilometros/galon debemos saber xq valor multiplicar...



    def __str__(self):
        return self.register # retornaremos la matricula del registro.. METODO GET ABSOLUTE URL.. GENERA URL ABSOLUTA AL 
        # CREAR UN OBJETO O REGISTRO... DE MODELO ESPECIFICO
    
    def get_absolute_url(self): # sin recibir parametros...
        return reverse("vehiculo_edit", kwargs={"pk": self.pk}) # retorno URL basada, no olvidar importar reverse...
        # apunta a vehiculo_edit.. por kwargs pasar la id del vehiculo por pk y pasamos por self:pk el modelo

    class Meta:
        verbose_name_plural = "Vehiculos" # en plural por clase meta instanciar...
        db_table_comment = "Vehiculos" # comentar, CREAR LA MIGRACION.... por cada modelo creado...
        # LUEGO CREAR LA VISTA DE VEHICULOS EN CTRL_COMB... 
    

    

