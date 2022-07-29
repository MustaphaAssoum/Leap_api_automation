# Automated API Testing

This code was developed to demonstrate the automated testing of the API served by 
[crudcrud](https://crudcrud.com/)

This code uses [Behave](
) to describe and execute test scenarios

This code tests the <em>employee</em> Resource. However, it can be easily scaled to test any number of Resources

## Prerequisites
This code uses Python (version >= 3.7 is required). Run the following commands to install the required modules:
- Requests module:
```python
pip3 install requests
```
- Behave module: 
```python
pip3 install behave
```
- jsonschema module:
```python
pip3 install jsonschema
```

## How to use

After installing the required modules, navigate to the main directory and run the following command:

```python
behave -D id=api_id
```
Where api_id is the endpoint's API ID provided by [crudcrud](https://crudcrud.com/)

## Results

After running the command above, Behave will test every scenario in the feature files. 
Any failures encountered will be highlighted during the execution.

Once the execution is complete, a summary of the results will be displayed at the bottom.
Below is an example of what a report summary can look like
```python
1 feature passed, 1 failed, 0 skipped
9 scenarios passed, 2 failed, 0 skipped
42 steps passed, 2 failed, 2 skipped, 0 undefined
Took 0m30.882s
```
