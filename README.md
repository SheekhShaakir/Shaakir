# WhatsApp MD User Bot

A powerful and feature-rich WhatsApp bot supporting multiple sessions, designed for seamless automation and enhanced user experience.

### Features

- **Multi-Session Support** – Manage multiple accounts effortlessly.
- **Customizable Responses** – Configure responses in different languages.
- **Automated Task Execution** – Perform actions without manual intervention.
- **Easy Deployment** – Multiple hosting options for quick setup.

### Supported Languages

This bot supports multiple languages for responses. Set your preferred language using the `BOT_LANG` variable in the `config.env` file.

**Available languages:**

- **bn** – Bengali  
- **en** – English  
- **es** – Spanish  
- **hi** – Hindi  
- **id** – Indonesian  
- **ur** – Urdu  
- **tr** – Turkish  
- **fr** – French  
- **ru** – Russian  
- **ar** – Arabic
- **so** – Somali
To set the bot language to Spanish, add the following line to your `config.env` file:

```env
BOT_LANG=so
```
---

### Deployment Guide

### 1️⃣ Deploy on Koyeb

[Deploy Now](https://levanter-delta.vercel.app/) to set up your bot on Koyeb.

### 2️⃣ Deploy on Render

[Deploy Now](https://levanter-delta.vercel.app/) to set up your bot on Render.

### 3️⃣ Deploy on a VPS or PC (Ubuntu Example)

#### **Quick Installation**

Run the following command:

```sh
bash <(curl -fsSL http://bit.ly/43JqREw)
```

#### **Manual Installation**

1. **Update System and Install Dependencies:**

   ```sh
   sudo apt update && sudo apt upgrade -y
   sudo apt install git ffmpeg curl -y
   ```

2. **Install Node.js (Version 20.x Recommended):**

   ```sh
   curl -fsSL https://deb.nodesource.com/setup_20.x | sudo -E bash -
   sudo apt install nodejs -y
   ```

3. **Install Yarn and PM2 for Process Management:**

   ```sh
   sudo npm install -g yarn
   yarn global add pm2
   ```

4. **Clone the Repository and Install Dependencies:**

   ```sh
   git clone https://github.com/lyfe00011/levanter botName
   cd botName
   yarn install
   ```

5. **Configure Environment Variables:**

   Create a `config.env` file and add the following lines:

   ```sh
   SESSION_ID=your_session_id_here
   PREFIX=.
   STICKER_PACKNAME=LyFE
   ALWAYS_ONLINE=false
   RMBG_KEY=null
   LANGUAG=en
   BOT_LANG=en
   WARN_LIMIT=3
   FORCE_LOGOUT=false
   BRAINSHOP=159501,6pq8dPiYt7PdqHz3
   MAX_UPLOAD=200
   REJECT_CALL=false
   SUDO=989876543210
   TZ=Asia/Kolkata
   VPS=true
   AUTO_STATUS_VIEW=true
   SEND_READ=true
   AJOIN=true
   DISABLE_START_MESSAGE=false
   PERSONAL_MESSAGE=null
   ```

6. **Start the Bot Using PM2:**

   To start the bot, run:

   ```sh
   pm2 start . --name botName --attach --time
   ```

   To stop the bot, run:

   ```sh
   pm2 stop botName
   ```
---

### Credits & Acknowledgments

A special thanks to:

- **[Yusuf Usta](https://github.com/Quiec)** – Creator of [WhatsAsena](https://github.com/yusufusta/WhatsAsena).  
- **[@adiwajshing](https://github.com/adiwajshing)** – Developer of [Baileys](https://github.com/adiwajshing/Baileys).

---

## 🛠 Need Help?

For more information on setting up environment variables and FAQs, please visit:

- [Bot Environment Variables](https://levanter-delta.vercel.app/)  
- [Frequently Asked Questions](https://levanter-delta.vercel.app/)
