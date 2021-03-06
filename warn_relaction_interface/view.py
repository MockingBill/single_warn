from django.http import HttpResponse
from . import settings
from .core.warn_realation import warn_relation
from .core import systen_unit as su
import threading
import os
import re
import json
import logging

logger = logging.getLogger('log')


def start(req):
    return HttpResponse(json.dumps({
        "success": True,
        "msg": "心跳检测成功..."
    }))


def warn_realtion(req):
    if req.method == "POST" and req.body != None:
        try:
            req_para = json.loads(req.body)
            wr = warn_relation(0.02,0.02,0.02)
            wr.all_gr_data = req_para['warn_data']
            print(wr.all_gr_data)
            resu = wr.do_apriori()


            return HttpResponse(json.dumps({
                "code": 200,
                "msg": "success",
                "body": {
                    "resu": resu
                }
            }))
        except Exception as e:
            logger.error(str(e))
            return HttpResponse(json.dumps({
                "code": 500,
                "msg": "unknown exception",
                "body": {
                    "resu": ""
                }
            }))
    else:
        return HttpResponse(json.dumps({
            "code": 500,
            "msg": "only accept http post",
            "body": {
                "resu": ""
            }
        }))



