# FILE-ORGANIZER
This command-line application sorts files (Images, Documents, Videos, etc.) into categorized folders based on their file extensions, helping you keep your Downloads and Desktop clutter-free
PROJECT TITLE

PYTHON FILE ORGANIZER 

 OVERVIEW OF THE PROJECT

The Python File Organizer is a practical command-line utility designed to automate the organization and cleanup of cluttered local directories, such as Downloads or Desktop folders. By analyzing file extensions, the tool intelligently moves files into predefined, categorized subfolders (like Images, Documents, and Videos), significantly reducing digital clutter and improving user workflow. It provides a simple, robust, and extensible solution for automated file management.

 KEY FEATURES 

  Intelligent Categorization: Files are sorted into common, logical categories based on their extensions.
  Conflict Resolution: Handles files with identical names gracefully by appending an index or timestamp, ensuring no data loss during the move operation.
  Simple Command Line Interface (CLI): Easy execution with minimal arguments.
  Extensible Mapping: The file extension-to-folder mapping logic is clearly defined and easily editable within the source code (organizer.py) for custom categorization.
  Non-Destructive: Only moves files; it never deletes them or modifies their content.

 TECHNOLOGY/TOOLS USED
 Python- The primary language used for core logic and file system manipulation
 OS Module - used for interacting with the operating system,path manipulation and directory creation
 Shutil Module- used for high-level file operations ,specifically moving files between directories 

 STEPS TO INSTALL AND RUN A PROJECT 
This tool requires Python 3.6 or higher.
No dependencies are required beyond standard Python libraries.

Run the script:
Execute the main script (organizer.py) followed by the absolute or relative path to the directory you wish to organize.

A. Organize the Current Directory

If you run the script from the folder you want to clean:
python organizer.py

B. Organize a Specific Folder 
python organizer.py /path/to/your/downloads/

INSTRUCTIONS FOR TESTING 

To ensure the organizer is working correctly, you should create a test directory containing a mix of files before running the script.

Setup the Test Environment:
mkdir test_folder
touch test_folder/document.pdf
touch test_folder/photo.jpg
touch test_folder/video.mp4
touch test_folder/archive.zip
touch test_folder/script.py
touch test_folder/misc_file.dat

Execute the Script on the Test Folder:
python organizer.py ./test_folder

VEERRIFICATION:
After execution, the test_folder directory should contain the following new subdirectories:
./test_folder/Documents/ (containing document.pdf)
./test_folder/Images/ (containing photo.jpg)
./test_folder/Videos/ (containing video.mp4)
./test_folder/Archives/ (containing archive.zip)
./test_folder/Code/ (containing script.py)
./test_folder/Others/ (containing misc_file.dat)
The root test_folder should now only contain the newly created category folders.

DEFAULT CATEGORIES
Documents -.pdf, .docx, .txt, .xlsx, .pptx
Images -.jpg, .png, .svg, .gif, .heic
Videos -.mp4, .mov, .avi, .mkv
Audio - .mp3, .wav, .flac, .aac
Archives- .zip, .rar, .7z, .tar.gz
Code -.py, .js, .html, .css, .json
Others -Any file not matching the above categories
