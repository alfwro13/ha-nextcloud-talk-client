"""The Nextcloud Talk Client integration."""
from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant

DOMAIN = "nextcloud_talk_client"


async def async_setup(hass: HomeAssistant, config: dict):
    """Set up the Nextcloud Talk Client integration."""
    # Do nothing, as the integration does not support YAML configuration.

    return True


async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry):
    """Set up the Nextcloud Talk Client entry."""
    hass.async_add_job(hass.config_entries.async_forward_entry_setup(entry, "sensor"))

    return True


async def async_unload_entry(hass: HomeAssistant, entry: ConfigEntry):
    """Unload the Nextcloud Talk Client entry."""
    return await hass.config_entries.async_forward_entry_unload(entry, "sensor")
