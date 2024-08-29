import os
from PIL import Image


class ImageSaveMixin:
    def save(self, *args, **kwargs):
        if not getattr(self, "_is_saving", False):
            print("If not Get Attribute '_is_saving'.")
            self._is_saving = True

            if self.image.path:
                print(f"Image -> {self.image}")
                print(
                    f"Instance -> {self.__class__.objects.get(pk=self.pk).image.name if self.__class__.objects.filter(pk=self.pk).exists() else NotImplemented}")
                print("If Image Path.")

                if self.__class__.__name__ == "ProfilePicture":
                    print("Class Name is ProfilePicture.")

                    if self.__class__.objects.filter(pk=self.pk).exists():
                        print("Instance Exists.")
                        instance = self.__class__.objects.get(pk=self.pk)

                        if instance.image.name.split(sep="/")[-1] != "default_profile_image.png":
                            print("Instance Image Name != default_profile_image.png.")

                            if instance.image.name.split(sep="/")[-1] != self.image.name:
                                print("Instange Image Name != Image Name")
                                try:
                                    if os.path.exists(path=instance.image.path):
                                        os.remove(path=instance.image.path)

                                except FileNotFoundError:
                                    super(ImageSaveMixin, self).save(*args, **kwargs)


                            else:
                                print("Instance Image Name == Image Name")
                                super(ImageSaveMixin, self).save(*args, **kwargs)

                                self.resize_image(path=self.image.path)

                        else:
                            print("Instance Image Name == default_profile_image.png.")
                            super(ImageSaveMixin, self).save(*args, **kwargs)

                            self.resize_image(path=self.image.path)

                    else:
                        print("Instance Does Not Exists.")
                        super(ImageSaveMixin, self).save(*args, **kwargs)

                        self.resize_image(path=self.image.path)

                else:
                    print("Class Name is not ProfilePicture.")

            else:
                print("If not Image")

        else:
            print("If Get Attribute '_is_saving'.")

    def resize_image(self, path):
        image = Image.open(fp=path)

        if image.mode == "RGBA":
            image = image.convert(mode="RGB")

        if image.width > image.height:
            output_width = 1100
            output_height = image.height * output_width / image.width

            image.thumbnail(size=(output_width, output_height))

        else:
            image.thumbnail(size=(300, 300))

        image.save(fp=path)
