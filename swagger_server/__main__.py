#!/usr/bin/env python3

import connexion
from sqlalchemy import create_engine
from swagger_server import encoder
from sqlalchemy.orm import sessionmaker


def main():
    app = connexion.App(__name__, specification_dir='./swagger/')
    app.app.json_encoder = encoder.JSONEncoder
    app.add_api('swagger.yaml', arguments={'title': 'Element Processing API'}, pythonic_params=True)
    app.run(port=8080)

    # Crear la instancia de SQLAlchemy Engine
    engine = create_engine('mysql://root:123456@localhost:3306/sys')

    # Crear la clase Session que puede utilizarse para crear sesiones individuales
    Session = sessionmaker(bind=engine)


if __name__ == '__main__':
    main()
