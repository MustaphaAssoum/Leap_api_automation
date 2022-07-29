# Base class for all resources
# Every resource added should inherit from this class and define its schema, post headers,
# and resource name

import jsonschema
from jsonschema import validate


class Resource:

    def __init__(self, schema: dict, resource_name: str, post_headers: dict):
        self.schema = schema
        self.resource_name = resource_name
        self.post_headers = post_headers

    def validate_data(self, data_to_validate: dict, method: str):
        try:
            validate(instance=data_to_validate, schema=self.schema[method])
        except jsonschema.exceptions.ValidationError:
            return False
        return True
        pass

    def get_full_resource(self, *args, **kwargs):
        pass

