from swagger_server.models.db.elements_to_process_model import ElementsToProcess  # Reemplaza 'YourDatabaseModel' con el nombre real de tu modelo de base de datos
from swagger_server.config.config import Session  # Reemplaza 'Session' con el nombre real de tu objeto de sesión de SQLAlchemy

class ElementRepository:
    @staticmethod
    def get_elements_with_status60():
        try:
            session = Session()
            elements = session.query(ElementsToProcess).filter(ElementsToProcess.status == 60).all()
            return elements
        except Exception as e:
            # Manejar excepciones en caso de error
            raise e
        finally:
            session.close()

    @staticmethod
    def insert_element(element_data):
        try:
            new_element = ElementsToProcess(
                idBulk=element_data.idBulk,
                status=element_data.status,
                name=element_data.name
            )

            session = Session()
            session.add(new_element)
            session.commit()
        except Exception as e:
            # Manejar excepciones en caso de error
            session.rollback()
            raise e
        finally:
            session.close()
