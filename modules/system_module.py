import os
import subprocess

def process_system_command(command, speak_func):
    """
    Handles Windows system commands.

    Examples:
        "launch notepad"
        "launch calculator"
        "launch cmd"
        "launch explorer"
    """

    cmd = command.lower().strip()

    if "launch notepad" in cmd:
        speak_func("Opening Notepad")
        subprocess.Popen("notepad.exe")

    elif "launch calculator" in cmd:
        speak_func("Opening Calculator")
        subprocess.Popen("calc.exe")

    elif "launch cmd" in cmd or "launch command" in cmd or "launch command prompt" in cmd:
        speak_func("Opening Command Prompt")
        subprocess.Popen("cmd.exe")

    # ============================================================
    # FILE EXPLORER
    # ============================================================

    elif "launch explorer" in cmd or "launch file explorer" in cmd:
        speak_func("Opening File Explorer")
        subprocess.Popen("explorer.exe")

    # ============================================================
    # TASK MANAGER
    # ============================================================

    elif "launch task manager" in cmd:
        speak_func("Opening Task Manager")
        subprocess.Popen("taskmgr.exe")

    # ============================================================
    # WINDOWS SETTINGS
    # ============================================================

    elif "launch settings" in cmd:
        speak_func("Opening Windows Settings")
        os.system("start ms-settings:")

    # ============================================================
    # CONTROL PANEL
    # ============================================================

    elif "launch control panel" in cmd:
        speak_func("Opening Control Panel")
        subprocess.Popen("control.exe")

    # ============================================================
    # UNKNOWN SYSTEM COMMAND
    # ============================================================

    else:
        speak_func("Sorry, I don't know that system command yet.")