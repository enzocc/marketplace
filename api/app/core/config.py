"""App environment settings."""


class Settings:
    """Application settings."""

    # Note: below are magical env vars populated on instantiation

    POSTGRES_USER: str = "api"
    POSTGRES_DATABASE: str = "api"
    POSTGRES_PASSWORD: str = "super-secret"
    POSTGRES_URL: str = "database"

    SQLALCHEMY_DATABASE_URI = f"postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_URL}/{POSTGRES_DATABASE}"


settings = Settings()
