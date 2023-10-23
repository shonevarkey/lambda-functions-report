import boto3
import json
import csv
from datetime import datetime

def generate_lambda_report():
    
    lambda_client = boto3.client('lambda')

    sts_client = boto3.client('sts')
    account_id = sts_client.get_caller_identity()['Account']

    current_datetime = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')

    json_report_filename = f"lambda_report_{account_id}_{current_datetime}.json"
    csv_report_filename = f"lambda_report_{account_id}_{current_datetime}.csv"

    response = lambda_client.list_functions()

    lambda_report = []

    for function in response['Functions']:
        function_details = {
            'LambdaFunctionName': function['FunctionName'],
            'Runtime': function['Runtime'],
            'Timeout': function['Timeout'],
            'ExecutionRole': function['Role']
            # Add other important properties here if needed
        }

        lambda_report.append(function_details)

    with open(json_report_filename, 'w') as json_file:
        json.dump(lambda_report, json_file, indent=4)

    with open(csv_report_filename, 'w', newline='') as csv_file:
        csv_writer = csv.DictWriter(csv_file, fieldnames=function_details.keys())
        csv_writer.writeheader()
        for function_details in lambda_report:
            csv_writer.writerow(function_details)

    print(f'Report generated and saved as JSON: {json_report_filename}')
    print(f'Report generated and saved as CSV: {csv_report_filename}')

if __name__ == '__main__':
    generate_lambda_report()
