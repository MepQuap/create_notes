
from models import User
from . import db


def test_simple_pass():
    assert True


def test_simple_fail():
    assert False


""" def test_login():
    user = User.query.filter_by(email="123@email.com").first()
    print(user) """
