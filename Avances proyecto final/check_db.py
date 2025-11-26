import os
import django
from django.db import connection

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'seccion3.settings')
django.setup()

def check_columns():
    with connection.cursor() as cursor:
        try:
            cursor.execute("SELECT column_name FROM information_schema.columns WHERE table_name = 'producto_producto';")
            columns = [row[0] for row in cursor.fetchall()]
            print("Columnas en producto_producto:", columns)
        except Exception as e:
            print("Error:", e)

if __name__ == "__main__":
    check_columns()
