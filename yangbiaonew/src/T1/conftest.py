#!/usr/bin/python
#-*-coding:utf8-*-
#美好生活从python开始！
import pytest
@pytest.fixture()
def   clean():
    print('当账号密码输错的时候，执行删除数据的操作')

