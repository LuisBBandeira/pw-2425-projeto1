from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from .models import UploadedFile , Folder
from .forms import UploadFileForm , FolderForm

@login_required
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
    return render(request, 'upload.html', {'form': form, 'files': files})

@login_required
def download_file(request, file_id):
    uploaded_file = get_object_or_404(UploadedFile, id=file_id, user=request.user)
    response = HttpResponse(uploaded_file.file, content_type='application/octet-stream')
    response['Content-Disposition'] = f'attachment; filename="{uploaded_file.file.name}"'
    return response

@login_required
def folder_list(request, parent_id=0):
    if parent_id != 0:
        parent_folder = get_object_or_404(Folder, id=parent_id, owner=request.user)
        folders = parent_folder.subfolders.filter(owner=request.user)
    else:
        parent_folder = None
        folders = Folder.objects.filter(parent__isnull=True, owner=request.user)
    
    return render(request, 'folder_list.html', {'folders': folders, 'parent_folder': parent_folder})

@login_required
def create_folder(request, parent_id=0):
    if parent_id != 0:
        parent_folder = get_object_or_404(Folder, id=parent_id, owner=request.user)
    else:
        parent_folder = None

    if request.method == 'POST':
        form = FolderForm(request.POST)
        if form.is_valid():
            folder = form.save(commit=False)
            folder.parent = parent_folder
            folder.owner = request.user
            folder.save()
            return redirect('folder_list', parent_id=parent_folder.id if parent_folder else 0)
    else:
        form = FolderForm(initial={'parent': parent_folder})

    return render(request, 'create_folder.html', {'form': form, 'parent_folder': parent_folder})

@login_required
def delete_folder(request, folder_id):
    folder = get_object_or_404(Folder, id=folder_id, owner=request.user)
    parent_id = folder.parent.id if folder.parent else 0
    folder.delete()
    return redirect('folder_list', parent_id=parent_id)