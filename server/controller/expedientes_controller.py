from typing import List

from fastapi import HTTPException

from server.schemas.expedientes_schemas import NewRecordRequest, RecordResponse, RecordRequest
from server.exceptions import BaseHTTPException, InternalServerError, NotFound


class ExpedientesController:
    def __init__(self):
        pass # TODO: referencia a servicio

    
    def create(self, new_record: NewRecordRequest) -> RecordResponse:
        try:
            # TODO: llamar a la capa de servicio para que gestione la acción correspondiente
            # Retornar data de ejemplo
            return RecordResponse(id=1, **new_record.model_dump())
        except BaseHTTPException as ex:
             # TODO: implementar logging
             raise ex
        except Exception:
            # TODO log: Error no contemplado en ExpedientesController.create
            raise InternalServerError()

    def get_list(self, limit: int, offset: int) -> List[RecordResponse]:
        try:
            # TODO: llamar a la capa de servicio para que gestione la acción correspondiente
            # Código de ejemplo
            return []
        except BaseHTTPException as ex:
             # TODO: implementar logging
             raise ex
        except Exception:
            # TODO log: Error no contemplado en ExpedientesController.create
            raise InternalServerError()

        

    def get_by_id(self, id: int) -> RecordResponse:
        try:
            # TODO: llamar a la capa de servicio para que gestione la acción correspondiente
            # Ejemplo de error
            raise NotFound(f'Proyecto #{id} no encontrado')
        except BaseHTTPException as ex:
             # TODO: implementar logging
             raise ex
        except Exception:
            # TODO log: Error no contemplado en ExpedientesController.create
            raise InternalServerError()

        

    def update(self, id: int, new_data: RecordRequest) -> RecordResponse:
        try:
            # TODO: llamar a la capa de servicio para que gestione la acción correspondiente
            # Ejemplo
            return RecordResponse(id=id, **new_data.model_dump())
        except BaseHTTPException as ex:
             # TODO: implementar logging
             raise ex
        except Exception:
            # TODO log: Error no contemplado en ExpedientesController.create
            raise InternalServerError()

        

    def delete(self, id: int) -> None:
        try:
            # TODO: llamar a la capa de servicio para que gestione la acción correspondiente
            return
        except BaseHTTPException as ex:
             # TODO: implementar logging
             raise ex
        except Exception:
            # TODO log: Error no contemplado en ExpedientesController.create
            raise InternalServerError()

        
