import os
import shutil
import subprocess


# --------------------------------------------------
def _delete_folder(folder):
    if os.path.exists(folder):
        shutil.rmtree(folder)
# --------------------------------------------------


# ==================================================
def test():
    _delete_folder(folder=r"project_sample\backend_django\venv")

    subprocess.run(["pip", "install", "virtualenv"])
    subprocess.run(["virtualenv", r"project_sample\backend_django\venv"])
    subprocess.run([r"project_sample\backend_django\venv\Scripts\pip", "install", "-r", r"project_sample\backend_django\requirements\work_after_building_commit.txt"])
    subprocess.run([r"project_sample\backend_django\venv\Scripts\python", r"project_sample\backend_django\manage.py", "test"])

    _delete_folder(folder=r"project_sample\backend_django\venv")
# ==================================================


# ==================================================
if __name__ == '__main__':
    test()
# ==================================================
