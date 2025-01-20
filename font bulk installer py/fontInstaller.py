import os
import shutil
import platform

def install_fonts(folder_path):
    # Detect the OS and set the font directory
    if platform.system() == "Windows":
        font_dir = os.path.join(os.environ['WINDIR'], 'Fonts')
    elif platform.system() == "Darwin":  # macOS
        font_dir = os.path.expanduser("~/Library/Fonts")
    elif platform.system() == "Linux":
        font_dir = os.path.expanduser("~/.fonts")
        if not os.path.exists(font_dir):
            os.makedirs(font_dir)
    else:
        print("Unsupported operating system!")
        return
    
    # Install each .otf font in the folder
    for file_name in os.listdir(folder_path):
        if file_name.endswith(".otf"):
            src_path = os.path.join(folder_path, file_name)
            dest_path = os.path.join(font_dir, file_name)
            try:
                shutil.copy(src_path, dest_path)
                print(f"Installed: {file_name}")
            except Exception as e:
                print(f"Failed to install {file_name}: {e}")

    print("Font installation completed!")

# Example usage
folder_path = input("Enter the path to the folder containing .otf files: ")
install_fonts(folder_path)
