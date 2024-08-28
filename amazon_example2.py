import boto3
from textractprettyprinter.t_pretty_print_expense import get_string, Textract_Expense_Pretty_Print, Pretty_Print_Table_Format


# AWS credentials
AWS_ACCESS_KEY_ID = "<AWS_ACCESS_KEY_ID>"
AWS_SECRET_ACCESS_KEY = "<AWS_SECRET_ACCESS_KEY>"

# Initialize Textract client
textract = boto3.Session(aws_access_key_id=AWS_ACCESS_KEY_ID,
                         aws_secret_access_key=AWS_SECRET_ACCESS_KEY,
                         region_name='eu-central-1').client('textract')

# Call Textract to extract text from the document
response = textract.analyze_document(
    Document={
        'S3Object': {
            'Bucket': "nunobispo-text",
            'Name': "nasa-apollo.pdf"
        }
    },
    FeatureTypes=["TABLES", "FORMS"]
)

# Print the extracted text
for block in response['Blocks']:
    if block['BlockType'] == 'LINE':
        print('Detected text: ' + block['Text'])
    elif block['BlockType'] == 'KEY_VALUE_SET' and 'KEY' in block['EntityTypes']:
        print('Key: ' + block['Text'])
    elif block['BlockType'] == 'TABLE':
        print('Table detected:')
        for relationship in block['Relationships']:
            for id in relationship['Ids']:
                for cell in response['Blocks']:
                    if cell['Id'] == id:
                        print('Cell text: ' + cell['Text'])
