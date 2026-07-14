from importlib.metadata import PackageNotFoundError, version

try:
    __version__ = version("kivy_garden.ebs.core")
except PackageNotFoundError:
    # Running directly from a source tree without installation.
    # This is intentionally unsupported.
    raise