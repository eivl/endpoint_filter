import logging
from typing import Any


class EndpointFilter(logging.Filter):
    def __init__(
        self,
        path: str,
        *args: Any,
        **kwargs: Any,
    ):
        """
        EndpointFilter instances are used to perform endpoint filtering
        of LogRecords.

        Loggers and Handlers can optionally use Filter instances to filter
        record paths as desired.

        Example:
        uvicorn_logger = logging.getLogger("uvicorn.access")
        uvicorn_logger.addFilter(EndpointFilter(path="/live"))
        uvicorn_logger.addFilter(EndpointFilter(path="/endpoint"))

        :param path: The endpoint path to filter.
        :param args: Additional positional arguments.
        :param kwargs: Additional keyword arguments.
        """
        super().__init__(*args, **kwargs)
        self._path = path

    def filter(self, record: logging.LogRecord) -> bool:
        return record.getMessage().find(self._path) == -1
