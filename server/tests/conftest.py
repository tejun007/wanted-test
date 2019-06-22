import os

import pytest

from server.common.config import TestConfig
from server.common.main import create_app
from server.models.mariadb import Company, db as _db
from server.tests.utils import read_data_set, apply_migrations

MODELS = dict(
    company=Company
)


@pytest.fixture(scope='session')
def app(request):
    app = create_app(TestConfig)

    ctx = app.app_context()
    ctx.push()

    def teardown():
        ctx.pop()

    request.addfinalizer(teardown)
    return app


@pytest.fixture(scope='session')
def db(app, request):
    """Session-wide test database."""
    if os.path.exists(TestConfig.TESTDB_PATH):
        os.unlink(TestConfig.TESTDB_PATH)

    def teardown():
        _db.drop_all()
        os.unlink(TestConfig.TESTDB_PATH)

    _db.app = app
    _db.create_all()
    # apply_migrations()

    request.addfinalizer(teardown)
    return _db


@pytest.fixture(scope='function')
def session(db, request):
    """Creates a new database session for a test."""
    connection = db.engine.connect()
    transaction = connection.begin()

    options = dict(bind=connection, binds={})
    session = db.create_scoped_session(options=options)

    db.session = session

    def teardown():
        transaction.rollback()
        connection.close()
        session.remove()

    request.addfinalizer(teardown)
    return session


@pytest.fixture(scope='function')
def company_search(session):
    table = 'company'
    dataset = read_data_set('company')
    for row in dataset[table]:
        session.add(MODELS[table](**row))
    session.commit()

    yield
    session.query(Company).delete()
    session.commit()


@pytest.fixture(scope='function')
def add_company_tags(session):
    table = 'company'
    dataset = read_data_set('company')
    for row in dataset[table]:
        session.add(MODELS[table](**row))
    session.commit()

    yield
    session.query(Company).delete()
    session.commit()


@pytest.fixture(scope='function')
def delete_company_tags(session):
    table = 'company'
    dataset = read_data_set('company')
    for row in dataset[table]:
        session.add(MODELS[table](**row))
    session.flush()
    session.commit()
    yield
    session.query(Company).delete()
    session.commit()
