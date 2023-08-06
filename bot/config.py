import yaml
from typing import Optional
from pathlib import Path
from pydantic import BaseSettings, validator


config_dir = Path(__file__).parent.parent.resolve() / "conf"


class Config(BaseSettings):
    telegram_token: str
    openai_api_key: str
    allowed_telegram_usernames: list[str] = ["thucpk"]
    new_dialog_timeout: int = 600
    enable_message_streaming: bool = True
    return_n_generated_images: int = 1
    n_chat_modes_per_page: int = 5
    mongodb_uri: str
    chat_modes: Optional[dict]
    models: Optional[dict]
    help_group_chat_video_path: Optional[Path]
    listen_host: str = "0.0.0.0"
    listen_port: int = 8000

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"

    @validator("chat_modes", pre=True)
    def valid_chat_modes(cls, v: Optional[dict], values: dict) -> dict:
        if v:
            return v
        with open(config_dir / "chat_modes.yml", "r") as f:
            chat_modes = yaml.safe_load(f)
        return chat_modes

    @validator("models", pre=True)
    def valid_models(cls, v: Optional[dict], values: dict) -> dict:
        if v:
            return v
        with open(config_dir / "models.yml", "r") as f:
            models = yaml.safe_load(f)
        return models

    @validator("help_group_chat_video_path", pre=True)
    def valid_help_group_chat_video_path(cls, v: Optional[Path], values: dict) -> Path:
        if v:
            return v
        return Path(__file__).parent.parent.resolve() / "static" / "help_group_chat.mp4"


settings = Config()
