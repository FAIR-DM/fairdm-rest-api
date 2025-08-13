from django.utils.translation import gettext_lazy as _
from fairdm.menus import SiteNavigation, SubMenuItem

SiteNavigation.get("More").append(
    SubMenuItem(
        _("API Documentation"),
        view_name="api:swagger-ui",
        icon="api",
        description=_(
            "View the API documentation and learn how to interact programatically with this portal."
        ),
    )
)
