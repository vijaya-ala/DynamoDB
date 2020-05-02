#*********************************************************************************************************************
#Author - Vijaya
#This script will operate on AWS DynamoDB to showcase alternate fetch criteria using index
#*********************************************************************************************************************


from __future__ import print_function # Python 2/3 compatibility
import boto3

dynamodb = boto3.resource('dynamodb', region_name='us-east-1')

table = dynamodb.Table('Movies')

table.delete()