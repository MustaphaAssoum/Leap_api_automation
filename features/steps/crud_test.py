from behave import *
import json


def create(data_to_create, resource_name, headers, api):
    data = json.dumps(data_to_create)
    return api.create(resource_name, data, headers=headers)


def read_data_using_id(context):
    created_data = json.loads(context.created_data.text)
    _id = created_data["_id"]
    context.response = context.api_operations.read(context.resource.get_full_resource(employee_id=_id))
    context.read_data = context.response


@given('I can access the API endpoint')
def step_impl(context):
    assert context.api_operations.check_endpoint().status_code == 200


@given('I have successfully created "{number}" entity')
def step_impl(context, number):
    context.created_data = []
    for i in range(int(number)):
        context.response = create(context.test_data["valid"]["CREATE"][i],
                                  context.resource.resource_name, context.resource.post_headers, context.api_operations)

        assert context.response.status_code == 201
        context.created_data.extend(context.response)


@given('I have successfully created 1 entity using the "{resource}" resource')
def step_impl(context, resource):
    context.response = create(context.test_data["valid"]["CREATE"][0],
                              resource, context.resource.post_headers, context.api_operations)
    assert context.response.status_code == 201
    context.created_data = context.response


@when('I UPDATE one of its properties "{prop}" to a new value "{value}"')
def step_impl(context, prop, value):
    data = json.loads(context.response.text)
    data_update = context.test_data["valid"]["CREATE"][0]
    data_update[prop] = value
    context.updated_data = data_update
    data_update = json.dumps(data_update)

    _id = data["_id"]
    context.response = context.api_operations.update(context.resource.get_full_resource(employee_id=_id), data_update,
                                                     headers=context.resource.post_headers)


@when('I use the UPDATE method on the main Resource')
def step_impl(context):
    context.response = context.api_operations.update(context.resource.resource_name, {})


@when('I CREATE "{test_data_type}" data with index "{test_data_id}"')
def step_impl(context, test_data_type, test_data_id):

    context.response = create(context.test_data[test_data_type]["CREATE"][int(test_data_id)],
                              context.resource.resource_name, context.resource.post_headers, context.api_operations)
    context.created_data = context.response


@when('I READ the data using its id')
def step_impl(context):
    read_data_using_id(context)


@when('I DELETE this entity using its id')
def step_impl(context):
    created_data = json.loads(context.created_data.text)
    _id = created_data["_id"]
    context.response = context.api_operations.delete(context.resource.get_full_resource(employee_id=_id))
    context.read_data = context.response


@when('I READ all the data')
def step_impl(context):
    context.response = context.api_operations.read(context.resource.resource_name)
    context.read_data = context.response


@then('I can READ the data using its id')
def step_impl(context):
    read_data_using_id(context)


@then('the received data matches what I created')
def step_impl(context):
    data = json.loads(context.created_data.text)
    del data["_id"]
    assert data == context.test_data["valid"]["CREATE"][0]


@then('the received data matches what I updated')
def step_impl(context):
    data = json.loads(context.read_data.text)
    del data["_id"]
    assert data == context.updated_data


@then('I get a "{expected_status_code}" response code')
def step_impl(context, expected_status_code):
    assert context.response.status_code == int(expected_status_code)


@then('schema validation should be "{expected_result}" for the "{method}" method')
def step_impl(context, expected_result, method):
    json_data = json.loads(context.response.text)
    if expected_result == "successful":
        assert context.resource.validate_data(json_data, method)
    elif expected_result == "failed":
        assert not context.resource.validate_data(json_data, method)


@then('the data must contain the entities I just created')
def step_impl(context):
    data = json.loads(context.response.text)
    for item in data:
        del item["_id"]
        assert item in context.test_data["valid"]["CREATE"]

