from fastapi import FastAPI, Request
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse


async def http_error_handler(_: Request, exc: Exception) -> JSONResponse:
    return JSONResponse({"detail": str(exc)}, status_code=500)


async def validation_exception_handler(
    _: Request, exc: RequestValidationError
) -> JSONResponse:
    return JSONResponse({"detail": exc.errors()}, status_code=422)


def register_exception_handlers(app: FastAPI) -> None:
    app.add_exception_handler(Exception, http_error_handler)
    app.add_exception_handler(RequestValidationError, validation_exception_handler)
