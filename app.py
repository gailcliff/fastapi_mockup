from typing import Callable


def get(fn: Callable):
    return lambda request: fn({"GET": f"{request}"})


def post(fn: Callable):
    return lambda request: fn({"POST": f"{request}"})


def put(fn: Callable):
    return lambda request: fn({"PUT": f"{request}"})


def delete(fn: Callable):
    return lambda request: fn({"DELETE": f"{request}"})
