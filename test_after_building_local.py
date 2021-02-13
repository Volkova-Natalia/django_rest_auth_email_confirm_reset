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
    _delete_folder(folder=r"django_rest_auth_email_confirm_reset.egg-info")
    _delete_folder(folder=r"dist")


    subprocess.run(["python", "setup.py", "sdist"])
    subprocess.run(["pip", "install", "virtualenv"])
    subprocess.run(["virtualenv", r"project_sample\backend_django\venv"])
    # subprocess.run([r"project_sample\backend_django\venv\Scripts\pip", "install", "-r", r"project_sample\backend_django\requirements\work_after_building_local.txt"])
    subprocess.run([r"project_sample\backend_django\venv\Scripts\pip", "install", "-r", r"project_sample\backend_django\requirements\work_after_building_base.txt"])
    subprocess.run([r"project_sample\backend_django\venv\Scripts\pip", "install", r"dist\django_rest_auth_email_confirm_reset-0.1.tar.gz"])
    subprocess.run([r"project_sample\backend_django\venv\Scripts\python", r"project_sample\backend_django\manage.py", "test"])

    _delete_folder(folder=r"project_sample\backend_django\venv")
# ==================================================


# ==================================================
if __name__ == '__main__':
    test()
# ==================================================
