import os

from pymongo import MongoClient

database_name = os.getenv("name")
database_username = os.getenv("username")
database_password = os.getenv("password")
database_host = os.getenv("host")
database_port = os.getenv("port")
database_args = os.getenv("args")

connection_string = f"mongodb://{database_username}:{database_password}@{database_host}:{database_port}"

if database_args is not None:
    connection_string = connection_string + '/?' + database_args

client = MongoClient(connection_string)

database = client[database_name]
