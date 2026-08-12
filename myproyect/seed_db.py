import os 
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myproyect.settings')
django.setup()

from catalog.models import Product

def change_data():
    products = [
  {
    "item": "GY-BRO-001",
    "title": "Brocha Profesional Goya Pro-Finish 4\"",
    "price": 18500.00,
    "area": "Brochería",
    "description": "Cerda sintética de alta densidad para pintura vinílica y esmaltes."
  },
  {
    "item": "GY-ROD-002",
    "title": "Rodillo Antigoteo Goya Microfibra 9\"",
    "price": 24000.00,
    "area": "Rodillos y Rodelería",
    "description": "Cubierta de microfibra de alta absorción para acabado liso."
  },
  {
    "item": "GY-BRO-003",
    "title": "Brocha Angular para Acabados Goya 2\"",
    "price": 12300.00,
    "area": "Brochería",
    "description": "Corte angular diseñado para recortes precisos en bordes y marcos."
  },
  {
    "item": "GY-HER-004",
    "title": "Espátula de Acero Inoxidable Goya 3\"",
    "price": 9800.00,
    "area": "Metalmecánica y Formado",
    "description": "Mango ergonómico de hule para preparación y nivelado de muros."
  },
  {
    "item": "GY-INJ-005",
    "title": "Bandeja Pintora Heavy-Duty Goya",
    "price": 15000.00,
    "area": "Inyección de Plásticos",
    "description": "Plástico reciclado de alta resistencia con estriado anti-deslizamiento."
  },
  {
    "item": "GY-ACC-006",
    "title": "Mano de Chango / Alargador Antideslizante Goya",
    "price": 21500.00,
    "area": "Armado y Ensamblado",
    "description": "Adaptador multiángulo para brochas y rodillos en alturas."
  },
  {
    "item": "GY-ROD-007",
    "title": "Rodillo Texturizador de Espuma Goya 7\"",
    "price": 19000.00,
    "area": "Rodillos y Rodelería",
    "description": "Espuma de alta densidad para efectos decorativos en revoque."
  },
  {
    "item": "GY-INJ-008",
    "title": "Plato Mezclador y Graduado Goya 5L",
    "price": 14200.00,
    "area": "Inyección de Plásticos",
    "description": "Cubeta con escala de medición en litros y galones para mezcla homogénea."
  },
  {
    "item": "GY-EMP-009",
    "title": "Cinta de Enmascarar de Alta Precisión Goya 24mm",
    "price": 7500.00,
    "area": "Empaque y Convertidores",
    "description": "Adhesivo medio que no daña ni levanta la pintura base."
  },
  {
    "item": "GY-HER-010",
    "title": "Mezclador de Pintura para Taladro Goya",
    "price": 16800.00,
    "area": "Metalmecánica y Formado",
    "description": "Varilla metálica en hélice para homogenizar esmaltes y epóxicos."
  },
  {
    "item": "GY-BRO-011",
    "title": "Brocha Económica de Cerda Natural 3\"",
    "price": 8900.00,
    "area": "Brochería",
    "description": "Ideal para aplicación de imprimantes, selladores y barnices."
  },
  {
    "item": "GY-ACC-012",
    "title": "Pad Aplicador de Pintura con Mango Goya",
    "price": 13600.00,
    "area": "Armado y Ensamblado",
    "description": "Almohadilla de microfibra para esquinas y áreas de difícil acceso."
  },
  {
    "item": "GY-EMP-013",
    "title": "Plástico Protector con Cinta Integrada Goya (20m)",
    "price": 11000.00,
    "area": "Empaque y Convertidores",
    "description": "Film electrostático protector para pisos y muebles."
  },
  {
    "item": "GY-HER-014",
    "title": "Cepillo de Alambre con Rascador Goya",
    "price": 10500.00,
    "area": "Metalmecánica y Formado",
    "description": "Remoción intensiva de pintura descascarada, óxido y escamas."
  },
  {
    "item": "GY-ACC-015",
    "title": "Lijadora Manual con Prensas Goya",
    "price": 17400.00,
    "area": "Armado y Ensamblado",
    "description": "Soporte ergonómico con base de neopreno para lijado plano."
  },
  {
    "item": "GY-HER-016",
    "title": "Cúter Profesional Aislado Goya 18mm",
    "price": 6800.00,
    "area": "Metalmecánica y Formado",
    "description": "Cuchilla retráctil de seguridad para corte de plásticos y cintas."
  },
  {
    "item": "GY-EMP-017",
    "title": "Lona de Protección Textil Absorbente Goya 3x4m",
    "price": 42000.00,
    "area": "Empaque y Convertidores",
    "description": "Cubierta reutilizable para protección contra goteo de pintura."
  },
  {
    "item": "GY-ROD-018",
    "title": "Rodillo Mini de Esponja para Acabados 4\"",
    "price": 9200.00,
    "area": "Rodillos y Rodelería",
    "description": "Ideal para lacas, barnices y puertas de madera."
  },
  {
    "item": "GY-HER-019",
    "title": "Rascador de Vidrios y Cerámica Goya",
    "price": 8100.00,
    "area": "Metalmecánica y Formado",
    "description": "Mango largo con hoja intercambiable para limpieza de sobrantes."
  },
  {
    "item": "GY-BRO-020",
    "title": "Limpiador y Conservador de Cerda Goya",
    "price": 12000.00,
    "area": "Brochería",
    "description": "Peine metálico doble función para restauración de brocha."
  }
]

#Delete the preovious data
    
    Product.objects.all().delete()
    print("Cleaned database")

#Insert the products in the database
    for prod in products:
        Product.objects.create(
            item=prod["item"],
            title=prod["title"],
            price=prod["price"],
            area=prod["area"],
            description=prod["description"]
        )
    print(f"Inserted products")
  
    print("¡All products have been successfully uploaded")


if __name__ == '__main__':
    change_data()