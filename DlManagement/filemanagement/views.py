from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from .models import UploadedFile
from .forms import UploadFileForm

# @method_decorator(login_required, name='dispatch')
def upload_file(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            uploaded_file = form.save(commit=False)
            uploaded_file.user = request.user
            uploaded_file.save()
            return redirect('upload_file')
    else:
        form = UploadFileForm()
    
    files = UploadedFile.objects.filter(user=request.user)
    return render(request, 'filemanagement/upload.html', {'form': form, 'files': files})

# @method_decorator(login_required, name='dispatch')
def download_file(request, file_id):
    uploaded_file = get_object_or_404(UploadedFile, id=file_id, user=request.user)
    response = HttpResponse(uploaded_file.file, content_type='application/octet-stream')
    response['Content-Disposition'] = f'attachment; filename="{uploaded_file.file.name}"'
    return response