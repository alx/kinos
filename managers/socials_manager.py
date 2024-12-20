import os
import requests
from utils.logger import Logger
from dotenv import load_dotenv

class SocialsManager:
    """Manager class for handling social media posts."""
    
    def __init__(self, model=None):
        """Initialize the socials manager."""
        self.logger = Logger(model=model)
        self.model = model
        load_dotenv()
        self.telegram_api_key = os.getenv('TELEGRAM_API_KEY')
        self.telegram_channel = "-1001699255893"
        
        # Add debug logging for initialization
        self.logger.debug(f"🔧 SocialsManager initialized")
        self.logger.debug(f"📡 Telegram API key present: {bool(self.telegram_api_key)}")
        self.logger.debug(f"📢 Telegram channel: {self.telegram_channel}")
        
        # Add debug logging for initialization
        self.logger.debug(f"🔧 SocialsManager initialized")
        self.logger.debug(f"📡 Telegram API key present: {bool(self.telegram_api_key)}")
        self.logger.debug(f"📢 Telegram channel: {self.telegram_channel}")
        
    def post_to_telegram(self, summary):
        """Post a summary to Telegram channel."""
        if not self.telegram_api_key:
            self.logger.warning("⚠️ Telegram API key not found, skipping post")
            self.logger.debug("💡 Add TELEGRAM_API_KEY to your .env file to enable posting")
            return False
            
        try:
            url = f"https://api.telegram.org/bot{self.telegram_api_key}/sendMessage"
            data = {
                "chat_id": self.telegram_channel,
                "text": summary,
                "parse_mode": "Markdown"
            }
            
            self.logger.debug(f"🔍 Attempting Telegram post to channel {self.telegram_channel}")
            self.logger.debug(f"🔗 API URL: {url}")
            self.logger.debug(f"📝 Data payload: {data}")
            
            response = requests.post(url, json=data)
            
            if response.status_code == 200:
                self.logger.success("✨ Posted summary to Telegram")
                self.logger.debug(f"📨 Response: {response.json()}")
                return True
            else:
                self.logger.error(f"❌ Failed to post to Telegram: {response.text}")
                self.logger.debug(f"🔍 Response status code: {response.status_code}")
                self.logger.debug(f"🔍 Response headers: {dict(response.headers)}")
                return False
                
        except Exception as e:
            self.logger.error(f"❌ Error posting to Telegram: {str(e)}")
            self.logger.debug(f"💥 Exception type: {type(e).__name__}")
            self.logger.debug(f"💥 Exception details: {str(e)}")
            return False
