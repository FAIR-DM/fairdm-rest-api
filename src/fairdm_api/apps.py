from django.apps import AppConfig


class FairDMAPI(AppConfig):
    name = "fairdm_api"

    def ready(self):
        """
        Updates the default field mapping of Django Rest Framework's ModelSerializer to include proper serializers for
        some of the custom model fields included in FairDM. Doing this means that we don't have to specify the
        serializer for these fields every time we create a new serializer.

        Note: At the moment, `QuantityField` serializer is used for all `QuantityField` types. However, this will need to be updated if non-readonly models are to be supported.

        This function is called during the `FairDMConfig.ready` method.
        """
        from fairdm.db import models
        from rest_framework.serializers import ModelSerializer

        from . import fields

        # if settings.GIS_ENABLED:
        #     from django.contrib.gis.db import models as gis_models
        #     from rest_framework_gis.fields import GeometryField

        #     ModelSerializer.serializer_field_mapping.update(
        #         {
        #             gis_models.PointField: GeometryField,
        #         }
        #     )

        # at the moment we are using the QuantifyField serializer for all QuantityField types
        # however, we will need to update this if we want to support non-readonly models
        ModelSerializer.serializer_field_mapping.update(
            {
                models.QuantityField: fields.QuantityField,
                models.DecimalQuantityField: fields.QuantityDecimalField,
                models.IntegerQuantityField: fields.QuantityField,
                models.BigIntegerQuantityField: fields.QuantityField,
                models.PositiveIntegerQuantityField: fields.QuantityField,
            }
        )
