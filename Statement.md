1. PROBLEM STATEMENT 

In today's digital environment, users frequently download and create numerous files, leading to severe clutter in common directories like "Downloads," "Desktop," and root folders. This disorganized state results in:

Reduced Productivity: Users waste time manually searching for files, leading to task switching and frustration.
Increased Storage Consumption: Duplicate or forgotten files accumulate unnecessarily
Risk of Data Mismanagement: Important files can be inadvertently misplaced or overlooked amidst the clutter.
There is a clear need for an automated, lightweight, and accessible solution to maintain an organized digital workspace without requiring continuous manual intervention.

2. SCOPE OF PROJECT

The scope of the Python File Organizer project is limited to local file system management within a single, user-defined directory at a time.

INCLUDED IN SCOPE :
Scanning a specified source directory for files.
Identifying file types based on standard extensions.
Creating necessary destination folders (e.g., Images, Documents) within the source directory if they do not exist.
Moving files from the root of the source directory into the correct categorized subfolders.
Implementing a robust conflict resolution mechanism for handling duplicate filenames.
Providing a simple command-line interface (CLI) for execution.

EXCLUDED FFROM SCOPE:
Recursively organizing subdirectories (only files in the top level of the source directory are moved).
Cloud storage integration (e.g., Google Drive, Dropbox).
Graphical User Interface (GUI) development.
File content analysis (sorting is strictly based on file extension).
Deleting files or empty folders.

3. TARGET USERS 

The primary users of the File Organizer are individuals who frequently interact with digital files and experience directory clutter.
Students and Academics: Need to organize lecture slides, notes, papers, and downloaded research articles.
Developers and Engineers: Dealing with countless configuration files, dependency downloads, and temporary build outputs.
General Computer Users: Anyone who uses the "Downloads" folder and wants an immediate, automated cleanup solution.
Power Users: Individuals looking for a lightweight, scriptable solution for routine system maintenance.

HIGH LEVEL FEATURES :
Core Organization - Automatically sorts files by type (e.g., Image, Document, Video) into dedicated, self-created subfolders.
Directory Input - Accepts any local directory path as an argument, allowing flexibility in which folder to clean
Conflict Handling - Ensures files with the same name are not overwritten by renaming duplicates using a sequential index or timestamp.
Extensibility - Uses an easily modifiable dictionary/mapping within the script to allow users to quickly add or change file extension categories
Non-Intrusive Design - Operates non-destructively, only moving files and creating necessary directories.



