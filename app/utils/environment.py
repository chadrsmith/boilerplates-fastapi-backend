from os import environ


def safe_get_env_var(key: str):
    try:
        return environ[key]
    except KeyError:
        raise NameError(f'Missing {key} from .env')