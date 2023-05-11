import subprocess
import time
from appium import webdriver
import json


def appium_driver(config_file):
    with open(config_file, 'r') as file:
        config = json.load(file)

    driver = webdriver.Remote('http://0.0.0.0:4723/wd/hub', config)
    driver.implicitly_wait(20)

    return driver


def start_appium_server():
    appium_command = 'appium'  # Command to run the Appium server

    # Start the Appium server using subprocess
    appium_process = subprocess.Popen(appium_command, shell=True)

    # Check if the server started successfully
    if appium_process.poll() is None:
        print("Appium server started successfully.")
        return appium_process
    else:
        print("Failed to start Appium server.")
        return None


def stop_appium_server(appium_process):
    # Check if the server process exists
    if appium_process is not None:
        # Terminate the Appium server process
        appium_process.terminate()

        # Wait for the process to terminate
        appium_process.wait()

        # Check if the server stopped successfully
        if appium_process.poll() is not None:
            print("Appium server stopped successfully.")
        else:
            print("Failed to stop Appium server.")
    else:
        print("No Appium server process to stop.")
