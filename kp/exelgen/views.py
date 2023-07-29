from django.shortcuts import render
from django.views.decorators.csrf import csrf_protect
from .utils.utils import valid_data
from .models import XLModel
from .utils.excelgen_v1 import ff
from .utils.word import word_gen
from django.http import FileResponse


@csrf_protect
def index(request):
    if request.method == 'POST':
        mod = request.POST.get('param_name')
        data, name = valid_data(request)
        model = XLModel(data=data, name=name)
        model.save()
        if int(mod) == 2:
            file_path = word_gen(data, name)
            response = FileResponse(open(file_path, 'rb'))

        elif int(mod) == 1:
            file_path = ff(data1=data['data1'], data2=data['data2'])
            response = FileResponse(open(file_path, 'rb'))
        return response
    template = 'index.html'
    return render(request, template)
