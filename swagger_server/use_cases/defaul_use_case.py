from swagger_server.models.db.elements_to_process_model import ElementsToProcess  
from swagger_server.config.config import Session  # Reemplaza 'Session' con el nombre real de tu objeto de sesión de SQLAlchemy
from swagger_server.models.element import Element
from sqlalchemy.exc import IntegrityError
from flask import Response, json

class ElementUseCase:
    @staticmethod
    def get_elements_with_status60():
        try:
            session = Session()
            elements = session.query(ElementsToProcess).filter(ElementsToProcess.status == 60).all()

            element_list = []
            for element in elements:
                element_item = Element(
                    id=element.id,
                    idBulk=element.idBulk,
                    retries=element.retries,
                    status=element.status,
                    name=element.name
                )
                element_list.append(element_item)

            # Respuesta exitosa con una lista de elementos
            response_data = [element.to_dict() for element in element_list]
            return Response(response=json.dumps(response_data), status=200, content_type="application/json")

        except Exception as e:
            # Manejar excepciones en caso de error
            return Response(response=f"Error: {str(e)}", status=500, content_type="text/plain")
        finally:
            session.close()

    @staticmethod
    def insert_element(element_data):
        # Crear una nueva sesión
        session = Session()

        try:
            # Aquí puedes realizar la operación de inserción en la base de datos
            new_element = ElementsToProcess(idBulk=element_data.idBulk, status=element_data.status, name=element_data.name)
            session.add(new_element)
            session.commit()

            # Respuesta exitosa después de la inserción
            return Response(response="Elemento insertado con éxito", status=201, content_type="text/plain")

        except IntegrityError as e:
            # En caso de una excepción relacionada con la integridad de la base de datos, realiza un rollback
            session.rollback()
            return Response(response=f"Error al insertar elemento: {str(e)}", status=400, content_type="text/plain")

        except Exception as e:
            print(f"Error inesperado: {str(e)}")
            # Maneja otros errores de manera adecuada
            session.rollback()
            return Response(response=f"Error inesperado: {str(e)}", status=500, content_type="text/plain")

        finally:
            # Cierra la sesión
            session.close()
