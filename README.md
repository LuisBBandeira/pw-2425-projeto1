## Project Overview

This project is a Django-based data management system named "DlManagement". It allows users to upload, download, and manage files within a structured folder system. Users can create folders, move files between folders, and delete files or folders. The system also supports user authentication, including registration, login, and logout functionalities, and a forgot password feature to assist users in recovering their accounts.

## Features

- **User Authentication**: Users can sign up, sign in, and log out. The system supports custom user registration and authentication forms.
- **File Management**: Users can upload files, download files, and delete files. Each file is associated with a user and optionally a folder.
- **Folder Management**: Users can create folders, list folders, and delete folders. Folders can have a parent-child relationship to support a hierarchical structure.
- **Admin Features**: Staff users are redirected to the admin dashboard upon login.

## Technical Details

### Dependencies

- **Python**: Version 3.12
- **Django**: Version 5.0.6

### Models

- **Folder**: Represents a folder that can contain files and other folders.
- **UploadedFile**: Represents a file uploaded by a user. It can belong to a folder.

### Forms

- **RegisterForm**: For new user registration.
- **LoginForm**: For user login.
- **UploadFileForm**: For uploading new files.
- **FolderForm**: For creating new folders.

### Views

- **Authentication Views**: Handle user registration, login, and logout.
- **File and Folder Views**: Handle uploading, downloading, creating folders, and managing files and folders.

### URLs

The project defines specific URLs for file and folder management operations, such as uploading, downloading, creating, and deleting files and folders.

## Setup and Installation

1. **Install Dependencies**: Run `make install` to install Poetry and manage dependencies.
2. **Database Migrations**: Execute `make migrate` to set up your database.
3. **Create Superuser**: Use `make createsuperuser` to create an admin account.
4. **Running the Project**: Use `make up` to build and run the project.

## Docker Support

The project includes a Dockerfile for containerization, allowing for easy setup and deployment.

## License

This project is licensed under the MIT License.

## Authors

- LuisBBandeira <luisfilipebentobandeira@gmail.com>

---
