from shop.models import DeliveryDetails
from rest_framework import serializers
import re


class DeliveryDetailsSerializer(serializers.ModelSerializer):
    phone = serializers.CharField(allow_blank=True)
    country = serializers.CharField(allow_blank=True)
    state = serializers.CharField(allow_blank=True)
    city = serializers.CharField(allow_blank=True)
    street = serializers.CharField(allow_blank=True)
    housenumber = serializers.CharField(allow_blank=True)
    apartmentnumber = serializers.CharField(allow_blank=True, required=False)
    postalcode = serializers.CharField(allow_blank=True)

    class Meta:
        model = DeliveryDetails
        exclude = ["uuid"]

    def validate_phone(self, phone):
        if phone == "":
            raise serializers.ValidationError(
                detail="Phone number is required.",
            )

        if not phone.isdigit():
            raise serializers.ValidationError(
                detail="The phone number should consist of digits only.",
            )

        if len(phone) < 8:
            raise serializers.ValidationError(
                detail="The phone number should contain a minimum of 8 digits.",
            )

        if len(phone) > 20:
            raise serializers.ValidationError(
                detail="The phone number should contain a maximum of 20 digits.",
            )
        return phone

    def validate_country(self, country):
        if country == "":
            raise serializers.ValidationError(
                detail="Country is required.",
            )

        if len(country) < 3:
            raise serializers.ValidationError(
                detail="The country name should contain a minimum of 3 letters.",
            )

        if len(country) > 56:
            raise serializers.ValidationError(
                detail="The country name should contain a maximum of 56 letters.",
            )

        return country

    def validate_state(self, state):
        if state == "":
            raise serializers.ValidationError(
                detail="State is required.",
            )

        if len(state) < 3:
            raise serializers.ValidationError(
                detail="The state name should contain a minimum of 3 letters.",
            )

        if len(state) > 56:
            raise serializers.ValidationError(
                detail="The state name should contain a maximum of 56 letters.",
            )
        return state

    def validate_city(self, city):
        if city == "":
            raise serializers.ValidationError(
                detail="City is required.",
            )

        if len(city) < 3:
            raise serializers.ValidationError(
                detail="The city name should contain a minimum of 3 letters.",
            )

        if len(city) > 169:
            raise serializers.ValidationError(
                detail="The city name should contain a maximum of 169 letters.",
            )
        return city

    def validate_street(self, street):
        if street == "":
            raise serializers.ValidationError(
                detail="Street is required.",
            )

        if len(street) < 3:
            raise serializers.ValidationError(
                detail="The street name should contain a minimum of 3 letters.",
            )

        if len(street) > 50:
            raise serializers.ValidationError(
                detail="The street name should contain a maximum of 50 letters.",
            )
        return street

    def validate_housenumber(self, housenumber):
        if housenumber == "":
            raise serializers.ValidationError(
                detail="House number is required.",
            )

        if not re.match(pattern=r'^[a-zA-Z0-9]+$', string=housenumber):
            raise serializers.ValidationError(
                detail="The house number must consist of letters or digits only.",
            )

        if len(housenumber) > 5:
            raise serializers.ValidationError(
                detail="The house number should contain a maximum of 5 characters.",
            )
        return housenumber

    def validate_apartmentnumber(self, apartmentnumber):
        if not apartmentnumber == "":
            if not re.match(pattern=r'^[a-zA-Z0-9]+$', string=apartmentnumber):
                raise serializers.ValidationError(
                    detail="The apartment number must consist of letters or digits only.",
                )

        if len(apartmentnumber) > 5:
            raise serializers.ValidationError(
                detail="The apartment number should contain a maximum of 5 characters.",
            )

        return apartmentnumber

    def validate_postalcode(self, postalcode):
        if postalcode == "":
            raise serializers.ValidationError(
                detail="Postal Code is required.",
            )

        if len(postalcode) < 5:
            raise serializers.ValidationError(
                detail="The postal code should contain a minimum of 5 characters.",
            )

        if len(postalcode) > 10:
            raise serializers.ValidationError(
                detail="The postal code should contain a maximum of 10 characters.",
            )

        return postalcode

    def update(self, instance, validated_data):
        for attr, value in validated_data.items():
            setattr(instance, attr, value)

        instance.save()

        return instance

    def run_validation(self, data):
        try:
            validated_data = super().run_validation(data=data)

        except serializers.ValidationError as exc:
            new_errors = {field: value[0] if isinstance(value, list) else value for field, value in exc.detail.items()}

            raise serializers.ValidationError(detail=new_errors)

        return validated_data
