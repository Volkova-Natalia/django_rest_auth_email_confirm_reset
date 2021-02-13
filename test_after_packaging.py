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

    subprocess.run(["pip", "install", "virtualenv"])
    subprocess.run(["virtualenv", r"project_sample\backend_django\venv"])
    # subprocess.run([r"project_sample\backend_django\venv\Scripts\pip", "install", "-r", r"project_sample\backend_django\requirements\test_after_packaging.txt"])
    subprocess.run([r"project_sample\backend_django\venv\Scripts\pip", "install", r"."])
    subprocess.run([r"project_sample\backend_django\venv\Scripts\pip", "install", r"django-cors-headers==3.7.0"])
    subprocess.run([r"project_sample\backend_django\venv\Scripts\pip", "install", r"python-dotenv==0.15.0"])
    subprocess.run([r"project_sample\backend_django\venv\Scripts\python", r"project_sample\backend_django\manage.py", "test"])

    _delete_folder(folder=r"project_sample\backend_django\venv")
# ==================================================


# ==================================================
if __name__ == '__main__':
    test()
# ==================================================
