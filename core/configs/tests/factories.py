import factory
from ..models import CFG_TYPE_STRING


from core.utils.tests import read_fixture_file

class ConfigFactory(factory.DjangoModelFactory):
    key = factory.Sequence(lambda n: 'key_{0}'.format(n))
    value_type = CFG_TYPE_STRING
    value_name = factory.Sequence(lambda n: 'Value {0} name'.format(n))
    value_string = "test string"

    class Meta:
        model = 'configs.AppConfig'
