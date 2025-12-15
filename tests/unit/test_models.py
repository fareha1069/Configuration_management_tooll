from Backend.models import Namespace, Resource
from Backend import db


def test_namespace_model(app):
    with app.app_context():
        ns = Namespace(name="test-namespace")
        db.session.add(ns)
        db.session.commit()

        stored = Namespace.query.first()
        assert stored.name == "test-namespace"


def test_resource_model(app):
    with app.app_context():
        ns = Namespace(name="default")
        db.session.add(ns)
        db.session.commit()

        res = Resource(
            name="db-password",
            arn="arn:test",
            value="secret",
            resource_type="secret",
            namespace="default"
        )

        db.session.add(res)
        db.session.commit()

        stored = Resource.query.first()
        assert stored.name == "db-password"
