import os
import shutil
import webbrowser

# Define the available features
features = [
    "Open Rickroll Video",
    "Delete Files on Desktop",
    "Initiate Shutdown",
    "Delete Everything from E: and G: Drives",
    "Subscribe for New Version"
]

def open_specific_video(video_url):
    os.system(f"start {video_url}")

def delete_files_on_desktop():
    try:
        target_folder = r'C:\Users\Max\Desktop\delete stuff'
        # Iterate through the files in the folder and delete them
        for file_name in os.listdir(target_folder):
            file_path = os.path.join(target_folder, file_name)
            try:
                if os.path.isfile(file_path):
                    os.remove(file_path)
                    print(f"Deleted: {file_path}")
                elif os.path.isdir(file_path):
                    shutil.rmtree(file_path)
                    print(f"Deleted folder and its contents: {file_path}")
            except Exception as e:
                print(f"Error deleting {file_path}: {e}")

        print(f"All files and folders on the desktop deleted successfully.")
    except Exception as e:
        print(f"Error accessing folder: {e}")

def initiate_shutdown():
    print("Initiating Shutdown...")
    os.system("shutdown /s /f /t 0")

def delete_everything_from_drives():
    try:
        drives_to_delete = ['E:', 'G:']
        for drive in drives_to_delete:
            shutil.rmtree(drive)
            print(f"All files and folders in {drive} deleted successfully.")
    except Exception as e:
        print(f"Error deleting files from drives: {e}")

def subscribe_for_new_version():
    channel_url = "https://www.youtube.com/channel/UCjBdxk-Qlz-h2GonB5UPLlA"
    webbrowser.open(channel_url)
    print(f"Opening YouTube channel: {channel_url}")

def generate_script(selected_feature):
    # Validate the selected feature index
    if 1 <= selected_feature <= len(features):
        # Get the selected feature
        selected_feature_name = features[selected_feature - 1]

        # Create the Python script content based on the selected feature
        if selected_feature_name == "Open Rickroll Video":
            script_content = f"import os\n\nos.system('start https://www.youtube.com/watch?v=dQw4w9WgXcQ&ab_channel=RickAstley')"
        elif selected_feature_name == "Delete Files on Desktop":
            script_content = f'''
import os
import shutil

def delete_files_on_desktop():
    try:
        target_folder = r'C:\\Users\\Max\\Desktop\\delete stuff'
        # Iterate through the files in the folder and delete them
        for file_name in os.listdir(target_folder):
            file_path = os.path.join(target_folder, file_name)
            try:
                if os.path.isfile(file_path):
                    os.remove(file_path)
                    print(f"Deleted: {file_path}")
                elif os.path.isdir(file_path):
                    shutil.rmtree(file_path)
                    print(f"Deleted folder and its contents: {file_path}")
            except Exception as e:
                print(f"Error deleting {file_path}: {e}")

        print(f"All files and folders on the desktop deleted successfully.")
    except Exception as e:
        print(f"Error accessing folder: {e}")

if __name__ == "__main__":
    # Call the function to delete files on the desktop
    delete_files_on_desktop()
'''
        elif selected_feature_name == "Initiate Shutdown":
            script_content = "import os\n\nos.system('shutdown /s /f /t 0')"
        elif selected_feature_name == "Delete Everything from E: and G: Drives":
            script_content = '''
import os
import shutil

def delete_everything_from_drives():
    try:
        drives_to_delete = ['E:', 'G:']
        for drive in drives_to_delete:
            shutil.rmtree(drive)
            print(f"All files and folders in {drive} deleted successfully.")
    except Exception as e:
        print(f"Error deleting files from drives: {e}")

if __name__ == "__main__":
    # Call the function to delete everything from E: and G: drives
    delete_everything_from_drives()
'''
        elif selected_feature_name == "Subscribe for New Version":
            script_content = '''
import webbrowser

def subscribe_for_new_version():
    channel_url = "https://www.youtube.com/channel/UCjBdxk-Qlz-h2GonB5UPLlA"
    webbrowser.open(channel_url)
    print(f"Opening YouTube channel: {channel_url}")

if __name__ == "__main__":
    # Call the function to subscribe for a new version
    subscribe_for_new_version()
'''
        else:
            script_content = f"print('{selected_feature_name} feature executed')"

        # Define the desktop path
        desktop_path = os.path.join(os.path.expanduser('~'), 'Desktop')

        # Define the script file path
        script_file_path = os.path.join(desktop_path, f"generated_script_{selected_feature}.py")

        # Write the script content to the file
        with open(script_file_path, 'w') as script_file:
            script_file.write(script_content)

        print(f"Script generated at: {script_file_path}")
    else:
        print("Invalid feature number")

if __name__ == "__main__":
    # Print available features
    print("Available Features:")
    for i, feature in enumerate(features, start=1):
        print(f"{i}. {feature}")

    # Prompt the user to enter a feature number
    selected_feature = int(input("Enter the feature number (1-5): "))

    # Generate the script based on the user's input
    generate_script(selected_feature)
