from gcputils import job_details_json
import conf

spark_job_json = {
  'projectId': 'foo', 
  'job': {'pysparkJob': 
    {'mainPythonFileUri': 'gs://foobucket/fooSparkFile.py'}, 
    'placement': 
    {'clusterName': 'foocluster-2'}}}

hive_job_json = {
  'projectId': 'foo', 
  'job': {'hiveJob': 
    {'queryFileUri': 'gs://foobucket/fooQueryFile.sql'}, 
    'placement': 
    {'clusterName': 'foocluster-2'}}}

query_job_json = {
  'projectId': 'foo', 
  'job': {'hiveJob': {
      "queryList": {
        "queries": [
          "show databases;"
        ]
      }
    }, 
    'placement': 
    {'clusterName': 'foocluster-2'}}}

def test_spark_job_details_json():
  assert job_details_json(
      conf.project, conf.cluster_name, conf.bucket_name, 
      conf.sparkJob, conf.spark_file_name)==spark_job_json

def test_hive_job_details_json():
  assert job_details_json(
      conf.project, conf.cluster_name, conf.bucket_name, 
      conf.hiveJob, conf.hive_file_name)==hive_job_json

def test_hive_job_details_json():
  assert job_details_json(
      conf.project, conf.cluster_name, conf.bucket_name, 
      conf.queryJob, conf.queryString)==query_job_json

