import os
import subprocess

from util.secrets import KaggleSecrets

# Read in the secret API key
kaggle_key_path = os.path.join(os.getcwd(),"secrets", "kaggle.json")
print(f"Reading kaggle key from {kaggle_key_path}")
secret = KaggleSecrets(kaggle_key_path)
os.environ['KAGGLE_USERNAME'] = secret.username
os.environ['KAGGLE_KEY'] = secret.key

# Download the lego dataset into data folder
# Documentation: https://github.com/Kaggle/kaggle-api
save_dir = os.path.join(os.getcwd(),"data")
print(f"Saving kaggle data to dir {save_dir}")
subprocess.call(["kaggle", "datasets", "download", "-d", "rtatman/lego-database", "--unzip", "-p", save_dir])
