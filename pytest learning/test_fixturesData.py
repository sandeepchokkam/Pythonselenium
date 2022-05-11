# Data driven and parameterization techniques
import logging

import pytest
from BaseClass import BaseClass


@pytest.mark.usefixtures("dataload")
class TestLoad(BaseClass):
    def test_getdata(self, dataload):
        print(dataload[0])
        log = self.getlogger()
        log.info(dataload[2])
        log.info(dataload[0])
        logging.info('hi')
        # print(dataload[2])


def test_getbrowser(senddata):
    print(senddata[2])
