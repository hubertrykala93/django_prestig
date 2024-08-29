import os
from uuid import uuid4
from django.utils.text import slugify
from django.conf import settings
from PIL import Image


class SaveMixin:
    slug_source = None

    def save(self, *args, **kwargs):
        if not getattr(self, "_is_saving", False):
            print("Not get attribute _is_saving.")
            self._is_saving = True

            if hasattr(self, "image") and self.image:
                print("Has attribute 'image' and self image.")
                if self.__class__.objects.filter(pk=self.pk).exists():
                    print(
                        "Self class objects filter exists (kiedy object w bazie danych już istnieje i jest robiony jego update).")
                    instance = self.__class__.objects.get(pk=self.pk)

                    if self.image != instance.image:
                        print(
                            "Self image != instance image (ta sytuacja wystąpić może, jeśli jest obiekt już utworzony i jest zmiana jego zdjęcia na nowe).")

                        try:
                            os.remove(path=instance.image.path)

                        except FileNotFoundError:
                            pass

                        super(SaveMixin, self).save(*args, **kwargs)

                        original_path = self.image.path

                        image = Image.open(fp=original_path)
                        img_width, img_height = image.width, image.height

                        output_width = 1100
                        output_height = img_height * output_width / img_width

                        image.thumbnail(size=(output_width, output_height))

                        file_extension = original_path.split(".")[-1]
                        new_name = str(uuid4()) + "." + file_extension
                        new_path = os.path.join(os.path.dirname(p=original_path), new_name)

                        os.remove(path=original_path)
                        image.save(fp=new_path)

                        os.path.relpath(path=new_path, start=settings.MEDIA_ROOT)

                if hasattr(self, "name") or hasattr(self, "title"):
                    print(
                        "Has attribute name or title (Wywołuje się to wtedy kiedy jest atrybut image i self image, czyli przy tworzeniu nowego obiektu lub jego update)")

                    if not hasattr(self, "slug") or self.slug_source != getattr(self, self.slug_source) or not getattr(
                            self,
                            "slug"):
                        print(
                            f"Not has attr slug or slug_source -> {self.slug_source} != get attribute slug source or not get attr slug")
                        self.slug = slugify(self.slug_source)

                    super(SaveMixin, self).save(update_fields=["slug", "image"])

            else:
                print("Else of if hasattr 'image' and self.image")
                super(SaveMixin, self).save(*args, **kwargs)

            self._is_saving = False

        else:
            print("Is attribute _is_saving.")
