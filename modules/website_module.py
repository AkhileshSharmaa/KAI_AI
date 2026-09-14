import webbrowser

def process_website_command(command, speak_func):
    """
    Processes web-opening shortcuts.

    Example:
        process_website_command("open youtube", speak)
    """

    cmd = command.lower().strip()

    # ============================================================
    # SEARCH ENGINES
    # ============================================================

    if "open google" in cmd:
        speak_func("Opening Google")
        webbrowser.open("https://www.google.com")

    elif "open bing" in cmd:
        speak_func("Opening Bing")
        webbrowser.open("https://www.bing.com")

    elif "open duckduckgo" in cmd:
        speak_func("Opening DuckDuckGo")
        webbrowser.open("https://duckduckgo.com")

    elif "open yahoo" in cmd:
        speak_func("Opening Yahoo")
        webbrowser.open("https://www.yahoo.com")

    elif "open brave search" in cmd:
        speak_func("Opening Brave Search")
        webbrowser.open("https://search.brave.com")

    # ============================================================
    # VIDEO / STREAMING
    # ============================================================

    elif "open youtube" in cmd:
        speak_func("Opening YouTube")
        webbrowser.open("https://www.youtube.com")

    elif "open netflix" in cmd:
        speak_func("Opening Netflix")
        webbrowser.open("https://www.netflix.com")

    elif "open twitch" in cmd:
        speak_func("Opening Twitch")
        webbrowser.open("https://www.twitch.tv")

    elif "open prime video" in cmd:
        speak_func("Opening Prime Video")
        webbrowser.open("https://www.primevideo.com")

    elif "open disney plus" in cmd or "open disney+" in cmd:
        speak_func("Opening Disney Plus")
        webbrowser.open("https://www.disneyplus.com")

    elif "open hulu" in cmd:
        speak_func("Opening Hulu")
        webbrowser.open("https://www.hulu.com")

    elif "open crunchyroll" in cmd:
        speak_func("Opening Crunchyroll")
        webbrowser.open("https://www.crunchyroll.com")

    elif "open peacock" in cmd:
        speak_func("Opening Peacock")
        webbrowser.open("https://www.peacocktv.com")

    elif "open max" in cmd:
        speak_func("Opening Max")
        webbrowser.open("https://www.max.com")

    # ============================================================
    # SOCIAL MEDIA
    # ============================================================

    elif "open twitter" in cmd or "open x" in cmd:
        speak_func("Opening X")
        webbrowser.open("https://x.com")

    elif "open facebook" in cmd:
        speak_func("Opening Facebook")
        webbrowser.open("https://www.facebook.com")

    elif "open instagram" in cmd:
        speak_func("Opening Instagram")
        webbrowser.open("https://www.instagram.com")

    elif "open linkedin" in cmd:
        speak_func("Opening LinkedIn")
        webbrowser.open("https://www.linkedin.com")

    elif "open reddit" in cmd:
        speak_func("Opening Reddit")
        webbrowser.open("https://www.reddit.com")

    elif "open pinterest" in cmd:
        speak_func("Opening Pinterest")
        webbrowser.open("https://www.pinterest.com")

    elif "open tumblr" in cmd:
        speak_func("Opening Tumblr")
        webbrowser.open("https://www.tumblr.com")

    elif "open threads" in cmd:
        speak_func("Opening Threads")
        webbrowser.open("https://www.threads.net")

    elif "open snapchat" in cmd:
        speak_func("Opening Snapchat")
        webbrowser.open("https://www.snapchat.com")

    elif "open tiktok" in cmd:
        speak_func("Opening TikTok")
        webbrowser.open("https://www.tiktok.com")

    # ============================================================
    # DEVELOPMENT / PROGRAMMING
    # ============================================================

    elif "open github" in cmd:
        speak_func("Opening GitHub")
        webbrowser.open("https://github.com")

    elif "open gitlab" in cmd:
        speak_func("Opening GitLab")
        webbrowser.open("https://gitlab.com")

    elif "open bitbucket" in cmd:
        speak_func("Opening Bitbucket")
        webbrowser.open("https://bitbucket.org")

    elif "open stackoverflow" in cmd or "open stack overflow" in cmd:
        speak_func("Opening Stack Overflow")
        webbrowser.open("https://stackoverflow.com")

    elif "open stack exchange" in cmd:
        speak_func("Opening Stack Exchange")
        webbrowser.open("https://stackexchange.com")

    elif "open npm" in cmd:
        speak_func("Opening NPM")
        webbrowser.open("https://www.npmjs.com")

    elif "open pypi" in cmd:
        speak_func("Opening PyPI")
        webbrowser.open("https://pypi.org")

    elif "open hugging face" in cmd:
        speak_func("Opening Hugging Face")
        webbrowser.open("https://huggingface.co")

    elif "open repl" in cmd or "open replit" in cmd:
        speak_func("Opening Replit")
        webbrowser.open("https://replit.com")

    elif "open codepen" in cmd:
        speak_func("Opening CodePen")
        webbrowser.open("https://codepen.io")

    elif "open jsfiddle" in cmd:
        speak_func("Opening JSFiddle")
        webbrowser.open("https://jsfiddle.net")

    elif "open geeksforgeeks" in cmd or "open geeks for geeks" in cmd:
        speak_func("Opening GeeksforGeeks")
        webbrowser.open("https://www.geeksforgeeks.org")

    elif "open w3schools" in cmd:
        speak_func("Opening W3Schools")
        webbrowser.open("https://www.w3schools.com")

    # ============================================================
    # AI TOOLS
    # ============================================================

    elif "open chatgpt" in cmd:
        speak_func("Opening ChatGPT")
        webbrowser.open("https://chatgpt.com")

    elif "open claude" in cmd:
        speak_func("Opening Claude")
        webbrowser.open("https://claude.ai")

    elif "open gemini" in cmd:
        speak_func("Opening Gemini")
        webbrowser.open("https://gemini.google.com")

    elif "open perplexity" in cmd:
        speak_func("Opening Perplexity")
        webbrowser.open("https://www.perplexity.ai")

    elif "open copilot" in cmd:
        speak_func("Opening Copilot")
        webbrowser.open("https://copilot.microsoft.com")

    # ============================================================
    # MUSIC
    # ============================================================

    elif "open spotify" in cmd:
        speak_func("Opening Spotify")
        webbrowser.open("https://open.spotify.com")

    elif "open soundcloud" in cmd:
        speak_func("Opening SoundCloud")
        webbrowser.open("https://soundcloud.com")

    elif "open apple music" in cmd:
        speak_func("Opening Apple Music")
        webbrowser.open("https://music.apple.com")

    elif "open bandcamp" in cmd:
        speak_func("Opening Bandcamp")
        webbrowser.open("https://bandcamp.com")

    elif "open deezer" in cmd:
        speak_func("Opening Deezer")
        webbrowser.open("https://www.deezer.com")

    # ============================================================
    # SHOPPING
    # ============================================================

    elif "open amazon" in cmd:
        speak_func("Opening Amazon")
        webbrowser.open("https://www.amazon.com")

    elif "open ebay" in cmd:
        speak_func("Opening eBay")
        webbrowser.open("https://www.ebay.com")

    elif "open walmart" in cmd:
        speak_func("Opening Walmart")
        webbrowser.open("https://www.walmart.com")

    elif "open target" in cmd:
        speak_func("Opening Target")
        webbrowser.open("https://www.target.com")

    elif "open etsy" in cmd:
        speak_func("Opening Etsy")
        webbrowser.open("https://www.etsy.com")

    elif "open aliexpress" in cmd:
        speak_func("Opening AliExpress")
        webbrowser.open("https://www.aliexpress.com")

    elif "open flipkart" in cmd:
        speak_func("Opening Flipkart")
        webbrowser.open("https://www.flipkart.com")

    elif "open myntra" in cmd:
        speak_func("Opening Myntra")
        webbrowser.open("https://www.myntra.com")

    elif "open meesho" in cmd:
        speak_func("Opening Meesho")
        webbrowser.open("https://www.meesho.com")

    elif "open ajio" in cmd:
        speak_func("Opening AJIO")
        webbrowser.open("https://www.ajio.com")

    # ============================================================
    # COMMUNICATION
    # ============================================================

    elif "open whatsapp" in cmd:
        speak_func("Opening WhatsApp")
        webbrowser.open("https://web.whatsapp.com")

    elif "open discord" in cmd:
        speak_func("Opening Discord")
        webbrowser.open("https://discord.com")

    elif "open telegram" in cmd:
        speak_func("Opening Telegram")
        webbrowser.open("https://web.telegram.org")

    elif "open messenger" in cmd:
        speak_func("Opening Messenger")
        webbrowser.open("https://www.messenger.com")

    elif "open signal" in cmd:
        speak_func("Opening Signal")
        webbrowser.open("https://signal.org")

    # ============================================================
    # GOOGLE SERVICES
    # ============================================================

    elif "open gmail" in cmd:
        speak_func("Opening Gmail")
        webbrowser.open("https://mail.google.com")

    elif "open google drive" in cmd:
        speak_func("Opening Google Drive")
        webbrowser.open("https://drive.google.com")

    elif "open google docs" in cmd:
        speak_func("Opening Google Docs")
        webbrowser.open("https://docs.google.com")

    elif "open google sheets" in cmd:
        speak_func("Opening Google Sheets")
        webbrowser.open("https://sheets.google.com")

    elif "open google slides" in cmd:
        speak_func("Opening Google Slides")
        webbrowser.open("https://slides.google.com")

    elif "open google calendar" in cmd:
        speak_func("Opening Google Calendar")
        webbrowser.open("https://calendar.google.com")

    elif "open google maps" in cmd:
        speak_func("Opening Google Maps")
        webbrowser.open("https://maps.google.com")

    elif "open google photos" in cmd:
        speak_func("Opening Google Photos")
        webbrowser.open("https://photos.google.com")

    elif "open google translate" in cmd:
        speak_func("Opening Google Translate")
        webbrowser.open("https://translate.google.com")

    elif "open google meet" in cmd:
        speak_func("Opening Google Meet")
        webbrowser.open("https://meet.google.com")

    # ============================================================
    # MICROSOFT SERVICES
    # ============================================================

    elif "open outlook" in cmd:
        speak_func("Opening Outlook")
        webbrowser.open("https://outlook.live.com")

    elif "open microsoft teams" in cmd or "open teams" in cmd:
        speak_func("Opening Microsoft Teams")
        webbrowser.open("https://teams.microsoft.com")

    elif "open microsoft" in cmd:
        speak_func("Opening Microsoft")
        webbrowser.open("https://www.microsoft.com")

    elif "open onedrive" in cmd:
        speak_func("Opening OneDrive")
        webbrowser.open("https://onedrive.live.com")

    elif "open office" in cmd:
        speak_func("Opening Microsoft Office")
        webbrowser.open("https://www.office.com")

    # ============================================================
    # EDUCATION
    # ============================================================

    elif "open wikipedia" in cmd:
        speak_func("Opening Wikipedia")
        webbrowser.open("https://www.wikipedia.org")

    elif "open khan academy" in cmd:
        speak_func("Opening Khan Academy")
        webbrowser.open("https://www.khanacademy.org")

    elif "open coursera" in cmd:
        speak_func("Opening Coursera")
        webbrowser.open("https://www.coursera.org")

    elif "open udemy" in cmd:
        speak_func("Opening Udemy")
        webbrowser.open("https://www.udemy.com")

    elif "open edx" in cmd:
        speak_func("Opening edX")
        webbrowser.open("https://www.edx.org")

    elif "open freecodecamp" in cmd or "open free code camp" in cmd:
        speak_func("Opening freeCodeCamp")
        webbrowser.open("https://www.freecodecamp.org")

    elif "open mit" in cmd:
        speak_func("Opening MIT")
        webbrowser.open("https://www.mit.edu")

    # ============================================================
    # NEWS
    # ============================================================

    elif "open bbc" in cmd:
        speak_func("Opening BBC")
        webbrowser.open("https://www.bbc.com")

    elif "open cnn" in cmd:
        speak_func("Opening CNN")
        webbrowser.open("https://www.cnn.com")

    elif "open reuters" in cmd:
        speak_func("Opening Reuters")
        webbrowser.open("https://www.reuters.com")

    elif "open guardian" in cmd:
        speak_func("Opening The Guardian")
        webbrowser.open("https://www.theguardian.com")

    elif "open times of india" in cmd:
        speak_func("Opening Times of India")
        webbrowser.open("https://timesofindia.indiatimes.com")

    elif "open indian express" in cmd:
        speak_func("Opening Indian Express")
        webbrowser.open("https://indianexpress.com")

    # ============================================================
    # FINANCE
    # ============================================================

    elif "open yahoo finance" in cmd:
        speak_func("Opening Yahoo Finance")
        webbrowser.open("https://finance.yahoo.com")

    elif "open tradingview" in cmd:
        speak_func("Opening TradingView")
        webbrowser.open("https://www.tradingview.com")

    elif "open investing" in cmd:
        speak_func("Opening Investing.com")
        webbrowser.open("https://www.investing.com")

    elif "open coinmarketcap" in cmd:
        speak_func("Opening CoinMarketCap")
        webbrowser.open("https://coinmarketcap.com")

    # ============================================================
    # TRAVEL
    # ============================================================

    elif "open booking" in cmd:
        speak_func("Opening Booking.com")
        webbrowser.open("https://www.booking.com")

    elif "open airbnb" in cmd:
        speak_func("Opening Airbnb")
        webbrowser.open("https://www.airbnb.com")

    elif "open tripadvisor" in cmd:
        speak_func("Opening TripAdvisor")
        webbrowser.open("https://www.tripadvisor.com")

    elif "open uber" in cmd:
        speak_func("Opening Uber")
        webbrowser.open("https://www.uber.com")

    elif "open ola" in cmd:
        speak_func("Opening Ola")
        webbrowser.open("https://www.olacabs.com")

    # ============================================================
    # FOOD
    # ============================================================

    elif "open zomato" in cmd:
        speak_func("Opening Zomato")
        webbrowser.open("https://www.zomato.com")

    elif "open swiggy" in cmd:
        speak_func("Opening Swiggy")
        webbrowser.open("https://www.swiggy.com")

    elif "open doordash" in cmd:
        speak_func("Opening DoorDash")
        webbrowser.open("https://www.doordash.com")

    # ============================================================
    # DESIGN / CREATIVE
    # ============================================================

    elif "open canva" in cmd:
        speak_func("Opening Canva")
        webbrowser.open("https://www.canva.com")

    elif "open figma" in cmd:
        speak_func("Opening Figma")
        webbrowser.open("https://www.figma.com")

    elif "open adobe" in cmd:
        speak_func("Opening Adobe")
        webbrowser.open("https://www.adobe.com")

    elif "open photopea" in cmd:
        speak_func("Opening Photopea")
        webbrowser.open("https://www.photopea.com")

    elif "open remove bg" in cmd or "open removebg" in cmd:
        speak_func("Opening Remove Background")
        webbrowser.open("https://www.remove.bg")

    # ============================================================
    # PRODUCTIVITY
    # ============================================================

    elif "open notion" in cmd:
        speak_func("Opening Notion")
        webbrowser.open("https://www.notion.so")

    elif "open trello" in cmd:
        speak_func("Opening Trello")
        webbrowser.open("https://trello.com")

    elif "open slack" in cmd:
        speak_func("Opening Slack")
        webbrowser.open("https://slack.com")

    elif "open evernote" in cmd:
        speak_func("Opening Evernote")
        webbrowser.open("https://evernote.com")

    elif "open dropbox" in cmd:
        speak_func("Opening Dropbox")
        webbrowser.open("https://www.dropbox.com")

    # ============================================================
    # JOBS / PROFESSIONAL
    # ============================================================

    elif "open indeed" in cmd:
        speak_func("Opening Indeed")
        webbrowser.open("https://www.indeed.com")

    elif "open glassdoor" in cmd:
        speak_func("Opening Glassdoor")
        webbrowser.open("https://www.glassdoor.com")

    elif "open monster" in cmd:
        speak_func("Opening Monster")
        webbrowser.open("https://www.monster.com")

    # ============================================================
    # GAMING
    # ============================================================

    elif "open steam" in cmd:
        speak_func("Opening Steam")
        webbrowser.open("https://store.steampowered.com")

    elif "open epic games" in cmd:
        speak_func("Opening Epic Games")
        webbrowser.open("https://store.epicgames.com")

    elif "open roblox" in cmd:
        speak_func("Opening Roblox")
        webbrowser.open("https://www.roblox.com")

    elif "open minecraft" in cmd:
        speak_func("Opening Minecraft")
        webbrowser.open("https://www.minecraft.net")

    elif "open xbox" in cmd:
        speak_func("Opening Xbox")
        webbrowser.open("https://www.xbox.com")

    elif "open playstation" in cmd:
        speak_func("Opening PlayStation")
        webbrowser.open("https://www.playstation.com")

    # ============================================================
    # OTHER POPULAR WEBSITES
    # ============================================================

    elif "open imdb" in cmd:
        speak_func("Opening IMDb")
        webbrowser.open("https://www.imdb.com")

    elif "open quora" in cmd:
        speak_func("Opening Quora")
        webbrowser.open("https://www.quora.com")

    elif "open medium" in cmd:
        speak_func("Opening Medium")
        webbrowser.open("https://medium.com")

    elif "open archive of our own" in cmd:
        speak_func("Opening Archive of Our Own")
        webbrowser.open("https://archiveofourown.org")

    elif "open archive" in cmd:
        speak_func("Opening Internet Archive")
        webbrowser.open("https://archive.org")

    # ============================================================
    # UNKNOWN COMMAND
    # ============================================================

    else:
        speak_func("Sorry, I don't know that website command yet.")