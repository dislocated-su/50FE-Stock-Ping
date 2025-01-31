# =================================
# Product Configuration
# =================================
# Set to True/False to enable/disable checking for specific products
PRODUCT_CONFIG = {
    "NVGFT590": {  # RTX 5090 FE
        "enabled": False,
        "name": "RTX 5090 FE"
    },
    "NVGFT580": {  # RTX 5080 FE
        "enabled": False,
        "name": "RTX 5080 FE"
    },
    "NVGFT570T": {  # RTX 5070 Ti FE
        "enabled": False,
        "name": "RTX 5070 Ti FE"
    },
    "NVGFT570": {  # RTX 5070 FE
        "enabled": False,
        "name": "RTX 5070 FE"
    }
}

# =================================
# Notification Configuration
# =================================
NOTIFICATION_CONFIG = {
    "play_sound": True,    # Whether to play a sound when stock is found
    "open_browser": True,  # Whether to auto open the browser when stock is found
}
# =================================
# Status Updates Configuration
# This sends a notification to the console and/or Telegram to show you that the script is still running properly.
# THIS IS NOT THE STOCK NOTIFIER.
# =================================
STATUS_UPDATES = {
    "console": {
        "enabled": True,              # Enable/disable console status updates
        "interval": 15 * 60,         # Console update interval in seconds (15 minutes default - edit the first number)
    },
    "telegram": {
        "enabled": False,              # Enable/disable Telegram status updates
        "interval": 30 * 60,         # Telegram update interval in seconds (30 minutes default - edit the first number)
    }
}

# =================================
# Telegram Configuration
# =================================
TELEGRAM_CONFIG = {
    "enabled": False,             # Master switch for Telegram functionality (WARNING DONT USE BROWSER OPEN AT THE SAME TIME)
    "bot_token": "XXXXXXXXXXXX",  # Your bot token
    "chat_id": "XXXXXXXX",        # Your chat ID
    "polling_timeout": 30,        # Seconds to wait in each polling request (Leave at default if you don't know what this means)
    "polling_retries": 3,         # Number of retries before entering backoff (Leave at default if you don't know what this means)
    "initial_backoff": 60,        # Initial backoff time in seconds (Leave at default if you don't know what this means)
    "max_backoff": 3600,          # Maximum backoff time in seconds (1 hour) (Leave at default if you don't know what this means)
}

# =================================
# API Configuration
# LEAVE THIS SECTION ALONE IF YOU DON'T KNOW WHAT THIS MEANS.
# =================================
API_CONFIG = {
    "url": "https://api.store.nvidia.com/partner/v1/feinventory",
    "params": {
        "locale": "en-gb",    # Change locale if needed
        "cooldown": 120,       # Seconds to wait after finding stock before resuming checks (60 seconds default)
        "check_interval": 10   # Seconds between checks (10secs default)
    },
    "headers": {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:133.0) Gecko/20100101 Firefox/133.0",
        "Accept": "application/json, text/plain, */*",
        "Referer": "https://marketplace.nvidia.com",
        "Origin": "https://marketplace.nvidia.com",
        "Connection": "keep-alive",
    },
    "base_url": "https://marketplace.nvidia.com/en-gb/consumer/graphics-cards/?locale=en-gb&page=1&limit=12&category=GPU&manufacturer=NVIDIA&manufacturer_filter=NVIDIA~2,ASUS~31,GAINWARD~5,GIGABYTE~18,INNO3D~3,KFA2~1,MSI~22,PALIT~10,PNY~7,ZOTAC~14"
}
# LEAVE THIS SECTION ALONE IF YOU DON'T KNOW WHAT THIS MEANS.