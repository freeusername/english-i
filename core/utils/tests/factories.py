import factory

from core.utils.tests import read_fixture_file

class UserFactory(factory.DjangoModelFactory):
    first_name = 'John'
    last_name = 'Doe'
    email = factory.Sequence(lambda n: 'person{0}@test.com'.format(n))
    username = email
    is_active = True

    class Meta:
        model = 'auth.User'
