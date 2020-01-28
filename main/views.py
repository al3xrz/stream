from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
import os


def main(request):
    return render(request, 'test.html', {})



def open_stream(request, id):
    print(id)
    os.system('./scripts/stream.sh {}'.format(id))
    return  JsonResponse({'id' : id})

def ffserver(request, command):
    if command == 'start':
        os.system('./scripts/ffserver.sh')
        print('restart ffserver')
    if command == 'stop':
        os.system('./scripts/kill_ffserver.sh')
        pass
    return  JsonResponse({})


def close_stream(request, id):
    if id == 0:
        os.system('./scripts/kill_all_streams.sh')
        return HttpResponse('Close all streams')
    else:
        os.system('./scripts/kill_stream.sh {}'.format(id))
        return HttpResponse('Close stream {}'.format(id))
