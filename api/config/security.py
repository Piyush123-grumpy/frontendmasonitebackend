"""Security Related Config"""

# Cross-Origin Resource Sharing
CORS = {
    "paths": ["*"],
    "allowed_methods": ["*"],
    "allowed_origins": ["*"],
    "allowed_headers": ["*"],
    "exposed_headers": [],
    "max_age": None,
    "supports_credentials": False,
}
