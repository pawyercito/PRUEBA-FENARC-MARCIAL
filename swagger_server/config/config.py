import os
import json
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# Get the directory where this script file is located
dir_path = os.path.dirname(os.path.realpath(__file__))

# Construct the full path to config_access.json
config_path = os.path.join(dir_path, 'config_access.json')

# Carga la configuración desde el archivo JSON
with open(config_path, 'r') as config_file:
    config = json.load(config_file)

# Obtén la URL de conexión a la base de datos desde la configuración
db_url = config['database']['db_url']

# Crea una instancia de SQLAlchemy Engine
engine = create_engine(db_url)

# Crea una clase Session que puede utilizarse para crear sesiones individuales
Session = sessionmaker(bind=engine)
