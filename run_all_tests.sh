#!/bin/bash

PROJECT_DIR=$(dirname "$(realpath "$0")")
echo "Running tests from $PROJECT_DIR"

# 1. Run all Android app tests
echo "Running Android app tests..."
pytest "$PROJECT_DIR/android_app_tests/android_app_test.py"

# 2. Run Gherkin Behave Android app test
echo "Running Behave tests..."
behave "$PROJECT_DIR/android_app_tests/features/"

# 3. Run all HTTP Flask server API tests
echo "Running Flask API tests..."
(
  cd "$PROJECT_DIR/api_testing" || exit 1
  pytest api_calls_test.py
)

# 4. Copy all test logs to main project catalog
echo "Copying test log files..."
find "$PROJECT_DIR" -type f -name "test_log_file*" -exec cp -n {} "$PROJECT_DIR" \;

# 5. Run adb logcat and save output in a file
echo "Running ADB LOGCAT..."
adb logcat -d > adb_logcat_output.log

# 6. Run adb dumpsys and save output in a file
echo "Running ADB DUMP SYS..."
adb shell dumpsys > adb_dumpsys_output.log

echo "All tests finished. Logs copied to $PROJECT_DIR"
