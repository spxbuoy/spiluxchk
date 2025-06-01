from pyrogram import Client, filters
import random

welcome_gif = [
    "https://telegra.ph/file/a5a2bb456bf3eecdbbb99.mp4",
    "https://telegra.ph/file/03c6e49bea9ce6c908b87.mp4",
    "https://telegra.ph/file/9ebf412f09cd7d2ceaaef.mp4",
    "https://telegra.ph/file/293cc10710e57530404f8.mp4",
    "https://telegra.ph/file/506898de518534ff68ba0.mp4",
    "https://telegra.ph/file/dae0156e5f48573f016da.mp4",
    "https://telegra.ph/file/3e2871e714f435d173b9e.mp4",
    "https://telegra.ph/file/714982b9fedfa3b4d8d2b.mp4",
    "https://telegra.ph/file/876edfcec678b64eac480.mp4",
    "https://telegra.ph/file/6b1ab5aec5fa81cf40005.mp4",
    "https://telegra.ph/file/b4834b434888de522fa49.mp4",
]

MESSAGE = """<b>
🔥 LISTEN UP, {name} — 
RULES ARE RULES. BREAK ‘EM, AND YOU’RE DONE. 🔥
1.🚫 No fucking around with unwanted links.

2.🚫 Spam? Hell no. One message at a time or you’re ghosted.

3.🚫 No pimping your shit here. 

4.🤐 Respect the squad or face the silence. 

5.⚔️ Play smart. Play fair. Or get out. No second chances.

6.🔥 Follow these or step the fuck out.

✅ Ready to roll? Hit /register and prove you belong.
</b>"""

@Client.on_message(filters.new_chat_members)
async def welcome(client, message):
    try:
        new_members = [u.mention for u in message.new_chat_members]
        names = ", ".join(new_members)
        text = MESSAGE.format(name=names)
        img = random.choice(welcome_gif)

        await message.reply_video(video=img, caption=text, quote=True)
    except Exception:
        pass
