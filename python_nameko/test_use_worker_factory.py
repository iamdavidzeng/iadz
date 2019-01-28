# -*- coding: utf-8 -*-


from nameko.rpc import RpcProxy, rpc
from nameko.testing.services import worker_factory


class ConversionServie(object):

    name = "conversions"

    maths_rpc = RpcProxy("maths")

    @rpc
    def inches_to_cm(self, inches):
        return self.maths_rpc.multiply(inches, 2.54)

    @rpc
    def cms_to_inches(self, cms):
        return self.maths_rpc.divide(cms, 2.54)


def test_conversion_service():
    service = worker_factory(ConversionServie)

    service.maths_rpc.multiply.side_effect = lambda x, y: x * y
    service.maths_rpc.divide.side_effect = lambda x, y : x / y

    assert service.inches_to_cm(300) == 762
    service.maths_rpc.multiply.assert_called_once_with(300, 2.54)

    assert service.cms_to_inches(762) == 300
    service.maths_rpc.divide.assert_called_once_with(762, 2.54)
