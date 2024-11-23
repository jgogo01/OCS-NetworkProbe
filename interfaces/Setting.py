from py_directus.models import DirectusModel

class Setting(DirectusModel):
    id: str
    internal_gateway: str
    internal_speedtest: str
    external_gateway: str
    ping_count: str
    url_check_dns_resolver: str
