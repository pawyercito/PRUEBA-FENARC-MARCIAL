import connexion
import six

from swagger_server.models.element import Element  # noqa: E501
from swagger_server.models.element_input import ElementInput  # noqa: E501
from swagger_server import util
from swagger_server.use_cases.defaul_use_case import ElementUseCase


def elements_post(body):  # noqa: E501
    """Insert an element

     # noqa: E501

    :param body: 
    :type body: dict | bytes

    :rtype: None
    """
    #logica para insertar un elemento en la base de datos
    if connexion.request.is_json:
        body = ElementInput.from_dict(connexion.request.get_json())
        ElementUseCase.insert_element(body)


def elements_status60_get():  # noqa: E501
    """Get elements with status&#x3D;60

     # noqa: E501


    :rtype: List[Element]
    """
    #Logica para obtener los elementos con status 60
    elements = ElementUseCase.get_elements_with_status60()
    return elements

