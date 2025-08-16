from pathlib import Path

project_root = Path(__file__).resolve().parent

EMULATOR_NAME = "emulator-5554"
APP_PATH = Path(project_root, "..", "android_app", "buggy_calc_debug.apk")
APP_NAME = "com.admsqa.buggycalc"
