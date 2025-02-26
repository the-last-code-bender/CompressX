# CHANGELOG

## [1.1.1] - 2025-02-26
### Fixed
- Fixed an issue where the application attempted to compress itself when running as an executable.
- Now correctly excludes the currently running `.exe` or script file from the compression list.
- Improved file scanning logic to ensure only target file types are processed.
---

## [1.1.0] - 2024-02-25
### Added
- **Working Directory Display:**  
  - The program now displays the current working directory before starting the process.  
  - Users are informed that all files in this directory and its subdirectories will be scanned. 
- **File Count in Confirmation Prompt:**  
  - Before compression starts, the program shows the **total number of matching files** found.  
  - This number is displayed in the confirmation message for user approval.
### Changed
- **Separated Functions for Better Clarity:**  
  - The file searching and compression processes have been split into two distinct functions:
    - `find_matching_files()` → Locates all matching files.  
    - `compress_and_delete_files()` → Handles compression and deletion.
- **Progress Tracking During Compression:**  
  - While compressing, the program now shows the **current file number** and **total file count**  
    (e.g., `[3/10] Compressed and deleted: filename.ext`).
### Fixed
- **Empty Extension Handling:**  
  - If the user presses **Enter** without typing a file extension, the program now exits gracefully with a message.
- **No Files Found Handling:**  
  - When no files match the entered extension, the program informs the user and terminates without errors.
---

## [1.0.0] 2025-02-16
### Initial release:
- Added the CompressX tool for compressing files in a directory and its subdirectories.
- Users can specify file extensions (e.g., .bin, .txt) for compression.
- Supports ZIP_LZMA compression algorithm for high compression ratios.
- Files are automatically deleted after compression.
- Added user confirmation prompt before starting compression and file deletion.
- Implemented a user-friendly interface for easy interaction.
- README included with detailed instructions for usage.
- .exe version of the application created for easier execution on Windows systems.
---