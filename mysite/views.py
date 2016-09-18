#from django.template.loader import get_template
#from django.http import HttpResponse
#from django.template import Template,Context
from django.shortcuts import render_to_response
import datetime
from mysite import settings
def current_datetime(request):
        now = datetime.datetime.now()
	return render_to_response('current_datetime.html',{'current_date': now})
def hours_ahead(request,offset):
	offset = int(offset)
	dt = datetime.datetime.now() + datetime.timedelta(hours=offset)
	return render_to_response('hours_ahead.html',{'hour_offset': offset,'next_time': dt})
#	html = "<html><body>in %s hour(s),it will be %s.</body></html>"% (offset,dt)
#	return HttpResponse(html)
