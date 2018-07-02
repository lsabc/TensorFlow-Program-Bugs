import tensorflow as tf
import sys
import os
import subprocess

try:
    assert len(sys.argv) == 2
    version = ["-buggy", "-fix"][int(sys.argv[1])]
except:
    print(
        "Please run 'python test_script 0' for testing the buggy-version and "
        "'python test_script 1' for testing the fix-version.\nAborted...")
    exit(1)

interpreter_path = sys.executable
print("Running at: ", interpreter_path)

assert tf.__version__[:len("0.12.")] == "0.12."


def get_target_dir():
    for x in os.listdir(os.path.dirname(os.path.abspath(__file__))):
        if version in x:
            return x
    raise ValueError("No dir ends with %s!" % version)


'''
please refer to ./models-buggy/inception/README.md to get the data
'''

subprocess.call(
    [interpreter_path, "./%s/inception/inception/imagenet_train.py" % get_target_dir(), "--data_dir=/tmp/imagenet_data",
     "--train_dir=/tmp/imagenet_train"])
