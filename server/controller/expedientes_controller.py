from typing import List


from server.schemas.expedientes_schemas import NewRecordRequest, RecordResponse, RecordRequest
from server.exceptions import BaseHTTPException, InternalServerError
from server.service import ExpedientesService

class ExpedientesController:
    def __init__(self):
        self.service = ExpedientesService()

    
    def create(self, new_record: NewRecordRequest) -> RecordResponse:
        try:
            return self.service.create(new_record)
        except BaseHTTPException as ex:
             # TODO: implementar logging
             raise ex
        except Exception:
            # TODO log: Error no contemplado en ExpedientesController.create
            raise InternalServerError()

    def get_list(self, limit: int, offset: int) -> List[RecordResponse]:
        try:
            return self.service.get_list(limit, offset)
        except BaseHTTPException as ex:
             # TODO: implementar logging
             raise ex
        except Exception:
            # TODO log: Error no contemplado en ExpedientesController.create
            raise InternalServerError()

 

    def get_by_id(self, id: int) -> RecordResponse:
        try:
            return self.service.get_by_id(id)
        except BaseHTTPException as ex:
             # TODO: implementar logging
             raise ex
        except Exception:
            # TODO log: Error no contemplado en ExpedientesController.create
            raise InternalServerError()

        

    def update(self, id: int, new_data: RecordRequest) -> RecordResponse:
        try:
            return self.service.update(id, new_data)
        except BaseHTTPException as ex:
             # TODO: implementar logging
             raise ex
        except Exception:
            # TODO log: Error no contemplado en ExpedientesController.create
            raise InternalServerError()

        

    def delete(self, id: int) -> None:
        try:
            self.delete(id)
        except BaseHTTPException as ex:
             # TODO: implementar logging
             raise ex
        except Exception:
            # TODO log: Error no contemplado en ExpedientesController.create
            raise InternalServerError()

        
