__author__ = 'mudasserhussain'
from django.views.generic import View
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
import os, tempfile, zipfile
from django.core.servers.basehttp import FileWrapper
from django.conf import settings
import mimetypes
from settings import STATIC_URL

class GadgetSpec(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, *args, **kwargs):
        return super(GadgetSpec, self).dispatch(*args, **kwargs)


    def get(self, request, format=None):
        filename     = STATIC_URL + "gadget-spec.xml" # Select your file here.
        download_name ="example.xml"
        wrapper      = FileWrapper(open(filename))
        content_type = mimetypes.guess_type(filename)[0]
        response     = HttpResponse(wrapper,content_type=content_type)
        response['Content-Length']      = os.path.getsize(filename)
        response['Content-Disposition'] = "attachment; filename=%s"%download_name
        return response
