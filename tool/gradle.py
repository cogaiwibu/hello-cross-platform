import logging
import os
import subprocess
import sys


class Gradle:
    def __init__(self, root_path):
        self.root_path = root_path
        self.logger = logging.getLogger(__name__)

    def get_build_tool_path(self, tool):
        path = os.path.join(self.root_path, tool)
        if sys.platform == "win32":
            if os.path.exists(path + ".bat"):
                path += ".bat"
            elif os.path.exists(path + ".exe"):
                path += ".exe"

        if not os.path.exists(path):
            raise Exception("Couldn't find %s" % tool)

        return path

    def run_task(self, task_name: str):
        gradle_wrapper_path = self.get_build_tool_path("gradlew")

        arguments = ["\"" + gradle_wrapper_path + "\"", task_name]

        exit_code = subprocess.call(" ".join(arguments), shell=True, cwd=self.root_path, env=self.get_tool_env())
        if exit_code != 0:
            raise Exception("%s" % arguments)

    def get_tool_env(self):
        tool_env = os.environ
        tool_env["ANDROID_HOME"] = self.get_android_home()
        return tool_env

    def get_android_home(self):
        android_home_dir = os.environ.get("ANDROID_HOME")
        if android_home_dir:
            return android_home_dir.replace('\\', '/')

        if sys.platform.startswith("linux"):
            android_home_dir = os.path.expanduser("~/Android/Sdk")
            if os.path.exists(android_home_dir):
                self.logger.info("Android home directory automatically detected as: %s", android_home_dir)
            else:
                android_home_dir = None

        if sys.platform == "darwin":
            android_home_dir = os.path.expanduser("~/Library/Android/sdk")

            if os.path.exists(android_home_dir):
                self.logger.info("Android home directory automatically detected as: %s", android_home_dir)
            else:
                android_home_dir = None

        if sys.platform == "win32":
            android_home_dir = os.path.expanduser("~/AppData/Local/Android/SDK")

            if os.path.exists(android_home_dir):
                self.logger.info("Android home directory automatically detected as: %s", android_home_dir)
            else:
                android_home_dir = None

        if not android_home_dir:
            raise Exception(
                "ANDROID_HOME environment variable is not set. Please point it to the root of the android SDK "
                "installation.")

        return android_home_dir.replace('\\', '/')
