import os
from PIL import Image


class SaveMixin:
    def save(self, *args, **kwargs):
        if getattr(self, "_is_saving", False):
            print("If Get Attribute '_is_saving'.")
            return True

        print("If not Get Attribute '_is_saving'.")

        if not self.image.path:
            print("If not Image Path.")
            return True

        instance = self._get_existing_instance()

        if instance:
            print("Instance exists.")

            if not self._is_default_image(instance=instance):
                print("Instance Image is not Default.")
                if not self._is_same_image(instance=instance):
                    print("Instance Image is not the same as uploaded image.")
                    self.save_image_and_attributes()

                    self._remove_image(instance=instance)

                else:
                    print("Instance image is the same as uploaded image.")
                    self.save_image_and_attributes()

                    self._remove_image(instance=instance)

            else:
                print("Instance Image is Default")
                self.save_image_and_attributes()

        else:
            print("Instance does not Exists.")
            self.save_image_and_attributes()

    def _get_instance(self):
        return self.__class__

    def _get_existing_instance(self):
        if self.__class__.objects.filter(pk=self.pk).exists():
            return self.__class__.objects.get(pk=self.pk)

        return None

    def _is_default_image(self, instance):
        return instance.image.name.split(sep="/")[-1] == "default_profile_image.png"

    def _is_same_image(self, instance):
        return instance.image.name.split(sep="/")[-1] == self.image.name.split(sep="/")[-1]

    def _remove_image(self, instance):
        try:
            if os.path.exists(path=instance.image.path):
                os.remove(path=instance.image.path)

        except FileNotFoundError:
            pass

    def _resize_image(self):
        image = Image.open(fp=self.image.path)

        if image.mode == "RGBA":
            image = image.convert(mode="RGB")

        output_size = (1100, image.height * 1100 / image.width) if image.width > image.height else (300, 300)
        image.thumbnail(size=(output_size))
        image.save(fp=self.image.path)

    def _update_attributes(self):
        image = Image.open(fp=self.image.path)

        self.size = os.path.getsize(filename=self.image.path)
        self.width, self.height = image.width, image.height
        self.format = image.format

    def save_image_and_attributes(self):
        super(SaveMixin, self).save()

        self._resize_image()
        self._update_attributes()

        super(SaveMixin, self).save(update_fields=["size", "width", "height", "format", "image"])
