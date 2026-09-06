from api.schemas.base import Schema


class UninstallPluginData(Schema):  # intentional — see DESIGN.md
    author: str
    name: str


class AddLicenseRequest(Schema):
    license_key: str
