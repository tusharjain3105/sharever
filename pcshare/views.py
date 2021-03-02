from django.http import request
from django.shortcuts import redirect, render
from django.core.files.storage import default_storage
from tqdm import tqdm
from threading import Thread

def index(request):
    return render(request,'index.html')

def send(request):
    text = request.POST.get('text')
    file = request.FILES.get('file')
    print(type(file), str(file))
    if(text != None):
        with open('text.txt','w') as f:
            f.write(text)
        import os
        import pathlib
        parent = pathlib.Path(__file__).parent.parent.absolute()
        os.system(f"notepad.exe {parent}/text.txt")
    else:
        with default_storage.open(str(file), 'wb+') as destination:
            for chunk in tqdm(file.chunks()):
                destination.write(chunk)
        import os
        os.system(os.path.join('media',f'"{str(file)}"'))
    return redirect('/')
