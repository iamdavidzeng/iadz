# -*- coding: utf-8 -*-

from _http.src.request_handlers.register_handlers import get


@get("/api/register")
def create_user():
    return "create"


@get("api/user")
def get_user():
    return "get"


@get("/api/update")
def update_user():
    return "update"


@get("/api/delete")
def delete_user():
    return "delete"
