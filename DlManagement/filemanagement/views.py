import os
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
from .models import UploadedFile , Folder 
from .forms import UploadFileForm , FolderForm

@login_required
def upload_file(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            file_instance = form.save(commit=False)
            file_instance.user = request.user  
            file_instance.save()
            return redirect('upload_file')
    else:
        form = UploadFileForm()

    files = UploadedFile.objects.filter(user=request.user)  
    folders = Folder.objects.filter(owner=request.user)  
    return render(request, 'upload.html', {'form': form, 'files': files, 'folders': folders})

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
        files = parent_folder.files.all()
    else:
        parent_folder = None
        folders = Folder.objects.filter(parent__isnull=True, owner=request.user)
        files = UploadedFile.objects.filter(folder__isnull=True, user=request.user)
    
    return render(request, 'folder_list.html', {'folders': folders, 'files': files, 'parent_folder': parent_folder})

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
@require_POST
def delete_folder(request, folder_id):
    folder = get_object_or_404(Folder, id=folder_id, owner=request.user)
    parent_id = folder.parent.id if folder.parent else 0
    folder.delete()
    return redirect('folder_list', parent_id=parent_id)

@login_required
@require_POST
def move_file(request, file_id):
    file = get_object_or_404(UploadedFile, id=file_id, user=request.user) 
    folder_id = request.POST.get('folder')
    if folder_id:
        folder = get_object_or_404(Folder, id=folder_id, owner=request.user)  
        file.folder = folder
    else:
        file.folder = None
    file.save()
    return redirect('upload_file')

@login_required
def delete_file(request, file_id):
    file = get_object_or_404(UploadedFile, pk=file_id)
    file_path = file.file.path
    file.delete()
    if os.path.exists(file_path):
        os.remove(file_path)
    return redirect(reverse('folder_list'))