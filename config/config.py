from pathlib import Path, PosixPath

from pydantic import PostgresDsn, computed_field
from pydantic_core import MultiHostUrl
from pydantic_settings import BaseSettings, SettingsConfigDict


class _Settings(BaseSettings):
    # 项目的根目录
    root_dir: PosixPath = Path(__file__).resolve().parent.parent

    model_config = SettingsConfigDict(
        # 配置文件位置，项目根目录 .env 文件
        env_file=root_dir.joinpath(".env"),
        env_ignore_empty=True,
        extra="ignore",
    )

    # 日志文件位置
    @computed_field
    @property
    def log_file(self) -> str:
        log_path = self.root_dir.joinpath("logs")
        if not log_path.is_dir():
            log_path.mkdir(exist_ok=True)
        return str(log_path.joinpath("system.log"))

    # 数据库配置
    db_host: str
    db_port: int
    db_name: str
    db_password: str
    db_database: str

    @computed_field  # type: ignore[prop-decorator]
    @property
    def sqlmodel_database_uri(self) -> PostgresDsn:
        return MultiHostUrl.build(
            scheme="mysql+pymysql",
            username=self.db_name,
            password=self.db_password,
            host=self.db_host,
            port=self.db_port,
            path=self.db_database,
        )

    # redis配置
    redis_host: str
    redis_port: int
    redis_password: str


settings = _Settings()

if __name__ == "__main__":
    print(settings.root_dir)
