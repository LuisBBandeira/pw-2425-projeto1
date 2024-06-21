const dragAndDrop = document.getElementById('drag-and-drop');
const fileInput = document.getElementById('file-input');
const uploadForm = document.getElementById('upload-form');

dragAndDrop.addEventListener('click', () => fileInput.click());

fileInput.addEventListener('change', () => {
    if (fileInput.files.length > 0) {
        uploadForm.submit();
    }
});

dragAndDrop.addEventListener('dragover', (event) => {
    event.preventDefault();
    event.stopPropagation();
    dragAndDrop.classList.add('dragover');
});

dragAndDrop.addEventListener('dragleave', (event) => {
    event.preventDefault();
    event.stopPropagation();
    dragAndDrop.classList.remove('dragover');
});

dragAndDrop.addEventListener('drop', (event) => {
    event.preventDefault();
    event.stopPropagation();
    dragAndDrop.classList.remove('dragover');

    const files = event.dataTransfer.files;
    if (files.length > 0) {
        fileInput.files = files;
        uploadForm.submit();
    }
});