import webbrowser
import yt_dlp


music = {
    "time": "https://www.youtube.com/results?search_query=Hans+Zimmer+Time",
    "now we are free": "https://www.youtube.com/results?search_query=Hans+Zimmer+Now+We+Are+Free",
    "arrival of the birds": "https://www.youtube.com/results?search_query=Arrival+of+the+Birds+Cinematic+Orchestra",
    "interstellar": "https://www.youtube.com/results?search_query=Interstellar+Main+Theme+Hans+Zimmer",
    "rise": "https://www.youtube.com/results?search_query=Rise+Instrumental+Marc+Eschmann",
}


def search_youtube(song_name):
    """
    Searches YouTube and returns the first video URL.
    """

    ydl_opts = {
        "quiet": True,
        "extract_flat": True,
        "noplaylist": True,
    }

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            result = ydl.extract_info(
                f"ytsearch1:{song_name}",
                download=False
            )

            if result and "entries" in result:
                video = result["entries"][0]

                if video:
                    return video["url"]

    except Exception as e:
        print("YouTube search error:", e)

    return None


def process_music_command(command, speak_func):
    """
    Handles music commands.

    Examples:
        "play stealth"
        "play believer"
        "play shape of you"
        "play skyfall"
    """

    cmd = command.lower().strip()

    # Make sure command starts with "play"
    if not cmd.startswith("play "):
        speak_func("Please tell me which song you want to play.")
        return

    # Remove "play " from command
    song_name = cmd[5:].strip()

    if not song_name:
        speak_func("Please tell me which song you want to play.")
        return

    # Check your saved music library first
    if song_name in music:
        speak_func(f"Playing {song_name}")
        webbrowser.open(music[song_name])
        return

    # If not found, search YouTube automatically
    speak_func(f"Searching YouTube for {song_name}")

    video_url = search_youtube(song_name)

    if video_url:
        speak_func(f"Playing {song_name}")
        webbrowser.open(video_url)
    else:
        speak_func(
            f"Sorry, I couldn't find {song_name} on YouTube."
        )
