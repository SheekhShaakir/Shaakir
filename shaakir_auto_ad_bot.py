
import replicate
import requests
import telegram
import schedule
import time
import os

# CONFIGURATION
REPLICATE_API_TOKEN = "r8_IzrNuFSFfOntdMFX5VC6DjgUdDM1wek2dQfDe"
TELEGRAM_BOT_TOKEN = "7901449245:AAEfdlx26ArR_NuHZ0ueekDGCNiMcLbf5Ro"
TELEGRAM_CHANNEL_ID = "@Shaakirdata"

# Initialize Replicate client
os.environ["REPLICATE_API_TOKEN"] = REPLICATE_API_TOKEN

# Function to generate AI image using Replicate
def generate_ai_image():
    import replicate
    prompt = """
    Design a promotional banner for a mobile data reseller called 'Shaakir Data'.
    Include elements like smartphones, internet icons, and network waves.
    Use blue and green colors. Show prices like '5GB for 12,000s'.
    Include contact number '616313335'. Make it modern and simple.
    """
    output = replicate.run(
        "stability-ai/stable-diffusion:db21e45c4c39a46b569ab56d0d6f29bfdf4bfaaf71fbd4d0b88b0f2e71b90c63",
        input={"prompt": prompt, "width": 512, "height": 512}
    )
    return output[0] if output else None

# Function to send image to Telegram channel
def send_image_to_telegram():
    image_url = generate_ai_image()
    if not image_url:
        print("❌ Failed to generate image")
        return
    bot = telegram.Bot(token=TELEGRAM_BOT_TOKEN)
    caption = "📢 *Shaakir Data Promo!*
✅ Qiimo jaban maanta
☎️ 616313335"
    photo = requests.get(image_url).content
    with open("ad.jpg", "wb") as f:
        f.write(photo)
    with open("ad.jpg", "rb") as photo_file:
        bot.send_photo(chat_id=TELEGRAM_CHANNEL_ID, photo=photo_file, caption=caption, parse_mode="Markdown")
    print("✅ Sawir + xayeysiis ayaa la diray!")

# Schedule: 08:00 & 17:00
schedule.every().day.at("08:00").do(send_image_to_telegram)
schedule.every().day.at("17:00").do(send_image_to_telegram)

print("🤖 Bot-ka Shaakir Data Auto Poster wuu socdaa...")

# Main loop
while True:
    schedule.run_pending()
    time.sleep(60)
