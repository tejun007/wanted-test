import json
import os

from alembic.command import upgrade
from alembic.config import Config

from server.common.config import TestConfig


def apply_migrations():
    """Applies all alembic migrations."""
    config = Config(TestConfig.ALEMBIC_INI)
    upgrade(config, 'head')


def read_data_set(fname):
    with open('{}/datasets/{}.dat'.format(os.path.dirname(os.path.realpath(__file__)), fname), 'r') as f:
        return json.load(f)
