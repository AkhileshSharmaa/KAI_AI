from modules.website_module import process_website_command
from modules.music_module import process_music_command
from modules.system_module import process_system_command
from modules.ai_module import process_ai_command


def processCommand(command, speak_func):
    """
    Main command router.

    It decides what type of command the user gave
    and sends it to the appropriate command handler.
    """

    cmd = command.lower().strip()

    words = cmd.split()

    if len(words) >= 2 and words[0] == "open":

        website = words[1]

        speak_func(f"Website command detected: {website}")

        process_website_command(cmd, speak_func)

    elif words and words[0] == "play":

        speak_func("Music command detected")

        process_music_command(cmd, speak_func)

    elif words and words[0] == "launch":
        
        speak_func("System command detected")

        process_system_command(cmd, speak_func)

    else:
        process_ai_command(cmd, speak_func)