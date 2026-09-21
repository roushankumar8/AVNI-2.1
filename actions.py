import os
import subprocess
import webbrowser


class ActionManager:

    def __init__(self):
        pass

    def execute(self, command):

        text = command.lower().strip()

        # =========================
        # NOTEPAD
        # =========================

        if any(word in text for word in [
            "notepad",
            "note pad",
            "notes",
            "नोटपैड",
            "नोट पैड"
        ]):

            subprocess.Popen(["notepad.exe"])

            return "नोटपैड खोल रही हूँ।"

        # =========================
        # CALCULATOR
        # =========================

        if any(word in text for word in [
            "calculator",
            "calc",
            "calculate",
            "कैलकुलेटर",
            "कैलकुलेटर खोलो"
        ]):

            subprocess.Popen(["calc.exe"])

            return "कैलकुलेटर खोल रही हूँ।"

        # =========================
        # YOUTUBE
        # =========================

        if any(word in text for word in [
            "youtube",
            "you tube",
            "युटुब",
            "युटुब खोलो"
        ]):

            webbrowser.open(
                "https://www.youtube.com"
            )

            return "YouTube खोल रही हूँ।"

        # =========================
        # YOUTUBE MUSIC
        # =========================

        if any(word in text for word in [
            "youtube music",
            "youtube music kholo",
            "यूट्यूब म्यूजिक",
            "म्यूजिक खोलो",
            "music kholo"
        ]):

            webbrowser.open(
                "https://music.youtube.com"
            )

            return "YouTube Music खोल रही हूँ।"

        # =========================
        # SPOTIFY
        # =========================

        if any(word in text for word in [
            "spotify",
            "स्पॉटिफाई",
            "spotify kholo"
        ]):

            webbrowser.open(
                "https://open.spotify.com"
            )

            return "Spotify खोल रही हूँ।"

        # =========================
        # WHATSAPP
        # =========================

        if any(word in text for word in [
            "whatsapp",
            "what's app",
            "व्हाट्सएप",
            "व्हाट्स ऐप",
            "whatsapp kholo"
        ]):

            webbrowser.open(
                "https://web.whatsapp.com"
            )

            return "WhatsApp खोल रही हूँ।"

        # =========================
        # WEATHER
        # =========================

        if any(word in text for word in [
            "weather",
            "temperature",
            "मौसम",
            "मौसम बताओ",
            "weather kholo"
        ]):

            webbrowser.open(
                "https://www.google.com/search?q=weather"
            )

            return "Weather खोल रही हूँ।"

        # =========================
        # GOOGLE
        # =========================

        if any(word in text for word in [
            "google",
            "गूगल",
            "google kholo"
        ]):

            webbrowser.open(
                "https://www.google.com"
            )

            return "Google खोल रही हूँ।"

        # =========================
        # GMAIL
        # =========================

        if any(word in text for word in [
            "gmail",
            "mail",
            "email",
            "जीमेल",
            "मेल"
        ]):

            webbrowser.open(
                "https://mail.google.com"
            )

            return "Gmail खोल रही हूँ।"

        # =========================
        # INSTAGRAM
        # =========================

        if any(word in text for word in [
            "instagram",
            "इंस्टाग्राम"
        ]):

            webbrowser.open(
                "https://www.instagram.com"
            )

            return "Instagram खोल रही हूँ।"

        # =========================
        # FACEBOOK
        # =========================

        if any(word in text for word in [
            "facebook",
            "फेसबुक"
        ]):

            webbrowser.open(
                "https://www.facebook.com"
            )

            return "Facebook खोल रही हूँ।"

        # =========================
        # FILE EXPLORER
        # =========================

        if any(word in text for word in [
            "file explorer",
            "explorer",
            "files",
            "फाइल एक्सप्लोरर",
            "फाइल खोलो"
        ]):

            subprocess.Popen(
                ["explorer.exe"]
            )

            return "File Explorer खोल रही हूँ।"

        # =========================
        # COMMAND PROMPT
        # =========================

        if any(word in text for word in [
            "command prompt",
            "cmd",
            "कमांड प्रॉम्प्ट"
        ]):

            subprocess.Popen(
                ["cmd.exe"]
            )

            return "Command Prompt खोल रही हूँ।"

        # =========================
        # POWERSHELL
        # =========================

        if any(word in text for word in [
            "powershell",
            "पावरशेल"
        ]):

            subprocess.Popen(
                ["powershell.exe"]
            )

            return "PowerShell खोल रही हूँ।"

        # =========================
        # NO ACTION
        # =========================

        return None