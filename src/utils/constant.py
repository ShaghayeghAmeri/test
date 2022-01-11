from types import SimpleNamespace

from utils.keyboards import create_keyboard

keys = SimpleNamespace(
    settings=':wrench:settings',
    random_connect=':bust_in_silhouette:random_connect',
)

keyboards = SimpleNamespace(
    main=create_keyboard(keys.settings, keys.random_connect)
)
