from django.db import models

CAMPAIGN_TYPES = (('shirt', 'shirt'),
                  ('sticker', 'sticker'))


class Campaign(models.Model):
    name = models.CharField(max_length=255, unique=True)
    slug = models.CharField(max_length=100)
    campaign_type = models.CharField(max_length=50, choices=CAMPAIGN_TYPES, default=CAMPAIGN_TYPES[0][0])
    user = models.ForeignKey('auth.User', related_name='campaigns', default=None, null=True)

    @property
    def foo(self):
        return 'bar'

    def bar(self):
        return 'baz'

    @property
    def baz(self):
        return self.__cls__.qux()

    @classmethod
    def qux(self):
        return 'waz'

    class Meta:
        pass

