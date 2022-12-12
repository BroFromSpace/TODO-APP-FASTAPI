import subprocess
import sys

from  app.core.config import ROOT

subprocess.run([sys.executable, "./app/backend_pre_start.py"])
subprocess.run([sys.executable, "./app/initial_data.py"])
