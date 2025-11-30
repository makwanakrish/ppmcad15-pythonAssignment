# This script copies files from a SOURCE folder to a DESTINATION folder.
# It adds a timestamp (date and time) to the file name if the file already exists.

import os
import shutil
import sys
from datetime import datetime

def backup_files(source_dir, destination_dir):
    """
    Copies files from source_dir to destination_dir with unique names.
    """
    print(f"\n--- Starting Backup ---")
    print(f"Source: {source_dir}")
    print(f"Destination: {destination_dir}")

    # Check if the SOURCE folder exists. If not, stop.
    if not os.path.isdir(source_dir):
        print(f"\nERROR: The source folder was not found at: {source_dir}")
        return

    # Check if the DESTINATION folder exists. If not, try to create it.
    if not os.path.isdir(destination_dir):
        print(f"Destination folder does not exist. Creating it now...")
        try:
            os.makedirs(destination_dir)
        except OSError as e:
            print(f"ERROR: Could not create destination folder. Reason: {e}")
            return

    # Start the copy process
    try:
        # Look at all files inside the source folder
        for item_name in os.listdir(source_dir):
            source_path = os.path.join(source_dir, item_name)
            
            # We only want to copy actual files, not folders.
            if os.path.isfile(source_path):
                
                # Create the full path for the destination file.
                destination_path = os.path.join(destination_dir, item_name)
                
                # Check if the file already exists in the destination folder.
                if os.path.exists(destination_path):
                    print(f"File exists: {item_name}. Creating unique copy...")

                    # Get the current date and time to use as a unique stamp.
                    timestamp = datetime.now().strftime("_%Y%m%d_%H%M%S")
                    
                    # Separate the file name from its extension (e.g., 'report' and '.txt')
                    file_name, file_extension = os.path.splitext(item_name)
                    
                    # Create the new, unique file name (e.g., 'report_20240101_103000.txt')
                    new_item_name = f"{file_name}{timestamp}{file_extension}"
                    new_destination_path = os.path.join(destination_dir, new_item_name)

                    # Copy the file to the new path
                    shutil.copy2(source_path, new_destination_path)
                    print(f"  -> Copied as: {new_item_name}")

                else:
                    # If the file does NOT exist, just copy it normally.
                    shutil.copy2(source_path, destination_path)
                    print(f"File copied successfully: {item_name}")
                    
        print("\n--- Backup Finished Successfully! ---")

    except Exception as e:
        print(f"\nAn unexpected error occurred during copy: {e}")


# --- Main script check for command-line arguments ---

if __name__ == "__main__":
    # sys.argv is a list of all words typed in the command line.
    # We need 3 things: the script name, the source path, and the destination path.
    if len(sys.argv) != 3:
        print("\nERROR: You need to provide exactly two folder paths.")
        print("Usage Example:")
        print("  python Q3_backup_script.py /path/to/source_folder /path/to/destination_folder")
    else:
        # sys.argv[1] is the source folder path
        source = sys.argv[1]
        # sys.argv[2] is the destination folder path
        destination = sys.argv[2]
        
        backup_files(source, destination)