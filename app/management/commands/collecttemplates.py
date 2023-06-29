from django.core.management.base import BaseCommand
from django.conf import settings
import os
import shutil

class Command(BaseCommand):
    help = 'Collect templates for deployment'

    def handle(self, *args, **options):
        template_dir = os.path.join(settings.BASE_DIR, 'templates')
        target_dir = os.path.join(settings.STATIC_ROOT, 'templates')

        if not os.path.exists(target_dir):
            os.makedirs(target_dir)

        for root, dirs, files in os.walk(template_dir):
            for file in files:
                source_path = os.path.join(root, file)
                target_path = os.path.join(target_dir, os.path.relpath(source_path, template_dir))
                shutil.copyfile(source_path, target_path)

        self.stdout.write(self.style.SUCCESS('Templates collected successfully'))