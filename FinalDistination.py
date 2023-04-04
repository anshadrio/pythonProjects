import os
import shutil


def is_resume(file_path):
    """Checks if the file at the given path contains any resume-related keywords."""
    resume_keywords = ['resume', 'cv', 'curriculum vitae', 'project']
    with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
        text = f.read().lower()
    for keyword in resume_keywords:
        if keyword in text:
            return True
    return False

def scan_for_resumes(input_folder, output_folder):
    """Scans the input folder for files that contain resume-related keywords and copies them to the output folder."""
    resume_files = []
    for root, dirs, files in os.walk(input_folder):
        for file in files:
            file_path = os.path.join(root, file)
            if file.endswith('.pdf') or file.endswith('.docx') or file.endswith('.doc'):
                if is_resume(file_path):
                    output_path = os.path.join(output_folder, file)
                    shutil.copyfile(file_path, output_path)
                    resume_files.append(output_path)
    return resume_files


if __name__ == '__main__':
    input_folder = r'C:\\'
    output_folder = r'C:\Users\SSLTP11238\Pictures\Saved Pictures'
    resume_files = scan_for_resumes(input_folder, output_folder)
    print(resume_files)
