# -*- encoding:utf-8 -*-
from setuptools import setup, find_packages
from notification.version import __version__ as ver
import sys


sys.path.append('./notification')
sys.path.append('./notification/tests/')

if __name__ == "__main__":
    setup(
        name = "django-notification",
        version = ver,
        author = "Shota Shimazu",
        author_email = "hornet.live.mf@gmail.com",
        classifiers=[
            'Programming Language :: Python :: 3.6',
            'Programming Language :: Python :: 3.7',
        ],
        packages = find_packages(exclude=('example')),
        include_package_data = True,
        zip_safe = False,
        install_requires = [
            "Django"
        ],
        entry_points = {
            'console_scripts':[
                'ntfy = notification.bin:main',
            ],
        },
        description = "Notification Django plugin",
        long_description = "",
        url = "https://github.com/shotastage/django-push-notification/",
        license = "Apache",
        platforms = ["POSIX", "Windows", "Mac OS X"],
        test_suite = "mirage_test.suite",
    )
