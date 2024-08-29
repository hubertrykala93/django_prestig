import os
from PIL import Image


class SaveMixin:
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
                                    super(SaveMixin, self).save(*args, **kwargs)


                            else:
                                print("Instance Image Name == Image Name")
                                super(SaveMixin, self).save(*args, **kwargs)

                                self.resize_image()
                                self.update_attributes()

                        else:
                            print("Instance Image Name == default_profile_image.png.")
                            super(SaveMixin, self).save(*args, **kwargs)

                            self.resize_image()
                            self.update_attributes()

                            if instance.profile.firstname and instance.profile.lastname:
                                print("Is Firstname and Lastname.")
                                self.alt = f"{instance.profile.firstname.capitalize()} {instance.profile.lastname.capitalize()} profile picture"

                            else:
                                print("Not is Firstname and Lastname.")
                                self.alt = f"{instance.profile.user.username} profile picture"

                            super(SaveMixin, self).save(update_fields=["size", "format", "alt"])

                    else:
                        print("Instance Does Not Exists.")
                        super(SaveMixin, self).save(*args, **kwargs)
                        self.resize_image()
                        self.update_attributes()

                        super(SaveMixin, self).save(update_fields=["size", "width", "height", "format"])

                else:
                    print("Class Name is not ProfilePicture.")

            else:
                print("If not Image")

        else:
            print("If Get Attribute '_is_saving'.")

    def resize_image(self):
        image = Image.open(fp=self.image.path)

        if image.mode == "RGBA":
            image = image.convert(mode="RGB")

        if image.width > image.height:
            output_width = 1100
            output_height = image.height * output_width / image.width

            image.thumbnail(size=(output_width, output_height))

        else:
            image.thumbnail(size=(300, 300))

        image.save(fp=self.image.path)

    def update_attributes(self):
        image = Image.open(fp=self.image.path)

        self.size = os.path.getsize(filename=self.image.path)
        self.width, self.height = image.size
        self.format = image.format
