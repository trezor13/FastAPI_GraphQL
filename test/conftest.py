import graphene
import pytest
from graphene.test import Client
from orator import DatabaseManager, Model, Schema
from orator.migrations import DatabaseMigrationRepository, Migrator

from models.product import Product
from schema import Query, Mutation


@pytest.fixture(autouse=True)
def setup_database():
    DATABASES = {
        "sqlite": {
            "driver": "sqlite",
            "database": "test.db"
        }
    }

    db = DatabaseManager(DATABASES)
    Schema(db)

    Model.set_connection_resolver(db)

    repository = DatabaseMigrationRepository(db, "migrations")
    migrator = Migrator(repository, db)

    if not repository.repository_exists():
        repository.create_repository()

    migrator.reset("migrations")
    migrator.run("migrations")


@pytest.fixture(scope="module")
def client():
    client = Client(schema=graphene.Schema(query=Query, mutation=Mutation))
    return client


@pytest.fixture(scope="function")
def product():
    product = Product()
    product.id = 1
    product.name = "Dodo"
    product.price = 50
    product.category = 1
    product.save()

    return product