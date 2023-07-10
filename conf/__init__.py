import importlib
from functools import lru_cache


SETTINGS_MODULE: str = 'conf.proj_settings'


class ServiceSettings:
    def __init__(self) -> None:
        module = importlib.import_module(SETTINGS_MODULE)

        self._explicit_settings = set()
        for setting in dir(module):
            if setting.isupper():
                setting_value = getattr(module, setting)
                setattr(self, setting, setting_value)
                self._explicit_settings.add(setting)


@lru_cache()
def get_settings() -> ServiceSettings:
    return ServiceSettings()


settings: ServiceSettings = get_settings()
