from test_data.util.test_data_fetching import create_test_data
from api_operations import ApiOperations
from static_data.config import API_BASE_URL
from endpoints.create_resource import create_resource


# Create an ApiOperations object to use to access different endpoints
# The same object can be used for all features
# This code also ensures a valid API ID is passed via the command line
def before_all(context):
    api_id = context.config.userdata.get("id", "")
    if not api_id:
        print("Please provide API ID via the command line: "
              "'behave -D id=API_ID' (replace API_ID with the actual API ID) ")
        exit()
    context.api_operations = ApiOperations(API_BASE_URL, api_id)


# This will run once before every feature
# Load test data for the endpoints under test
# The feature name must be of the format: "endpoint_name endpoint"
def before_feature(context, feature):
    resource_name = feature.name.split(" ")[0]
    context.resource = create_resource(resource_name)
    context.test_data = create_test_data(resource_name)