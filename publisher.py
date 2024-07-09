import redis
from dotenv import load_dotenv
import os

# Cargar variables de entorno
load_dotenv()

# Configuración de Redis
redis_host = os.getenv('REDIS_HOST')
redis_port = int(os.getenv('REDIS_PORT'))
redis_password = os.getenv('REDIS_PASSWORD')

# Conexión a Redis
redis_client = redis.StrictRedis(host=redis_host, port=redis_port, password=redis_password, decode_responses=True)

# Publicador
def publisher():
    while True:
        message = input("Introduce un mensaje para publicar: ")
        redis_client.publish('canal_prueba', message)
        print(f"Publicado: {message}")

if __name__ == "__main__":
    publisher()
