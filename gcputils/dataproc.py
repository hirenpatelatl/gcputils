import os

from google.cloud import storage
import googleapiclient.discovery

REGION = 'global'
DEFAULT_FILENAME = 'pyspark_sort.py'
dataproc = googleapiclient.discovery.build('dataproc', 'v1')


# [START create_cluster]
def create_cluster(project, cluster_name, zone):
    print('Creating cluster.')
    print(project, cluster_name, zone)

    # dataproc = get_client()

    cluster_create_json = get_cluster_create_json(project, cluster_name, zone)

    result = dataproc.projects().regions().clusters().create(
        projectId=project,
        region=REGION,
        body=cluster_create_json).execute()
    return cluster_create_json, result

# [END create_cluster]

def get_zone_uri(project,zone):
  return \
    'https://www.googleapis.com/compute/v1/projects/{}/zones/{}'.format(
        project,zone)

def get_cluster_create_json(project, cluster_name, zone):
  return {
    'projectId': project,
    'clusterName': cluster_name,
    'config': {
        'gceClusterConfig': {
            'zoneUri': get_zone_uri(project,zone)
        }
    }
  }

def list_clusters(project):
    result = dataproc.projects().regions().clusters().list(
        projectId=project,
        region=REGION).execute()
    return result

def wait_for_cluster_creation(project, cluster_name, zone):
    print('Waiting for cluster creation')

    while True:
        result = dataproc.projects().regions().clusters().list(
            projectId=project,
            region=REGION).execute()
        cluster_list = result['clusters']
        cluster = [c
                   for c in cluster_list
                   if c['clusterName'] == cluster_name][0]
        if cluster['status']['state'] == 'ERROR':
            raise Exception(result['status']['details'])
        if cluster['status']['state'] == 'RUNNING':
            print("Cluster created.")
            break


# [START list_clusters_with_detail]
def list_clusters_with_details(project):
    result = dataproc.projects().regions().clusters().list(
        projectId=project,
        region=REGION).execute()
    cluster_list = result['clusters']
    for cluster in cluster_list:
        print("{} - {}"
              .format(cluster['clusterName'], cluster['status']['state']))
    return result
# [END list_clusters_with_detail]


def get_cluster_id_by_name(cluster_list, cluster_name):
    """Helper function to retrieve the ID and output bucket of a cluster by
    name."""
    cluster = [c for c in cluster_list if c['clusterName'] == cluster_name][0]
    return cluster['clusterUuid'], cluster['config']['configBucket']


# [START delete]
def delete_cluster(project, cluster):
    print('Tearing down cluster')
    result = dataproc.projects().regions().clusters().delete(
        projectId=project,
        region=REGION,
        clusterName=cluster).execute()
    return result
# [END delete]


# [START wait]
def wait_for_job(project, job_id):
    print('Waiting for job to finish...')
    while True:
        result = dataproc.projects().regions().jobs().get(
            projectId=project,
            region=REGION,
            jobId=job_id).execute()
        # Handle exceptions
        if result['status']['state'] == 'ERROR':
            raise Exception(result['status']['details'])
        elif result['status']['state'] == 'DONE':
            print('Job finished')
            return result
# [END wait]

# [START submit_pyspark_job]
def submit_job(project, cluster_name, bucket_name, job_type, filename):
    """Submits the Pyspark job to the cluster, assuming `filename` has
    already been uploaded to `bucket_name`"""

    job_details = job_details_json(
        project, cluster_name, bucket_name, job_type, filename)

    result = dataproc.projects().regions().jobs().submit(
        projectId=project,
        region=REGION,
        body=job_details).execute()
    job_id = result['reference']['jobId']
    print('Submitted job ID {}'.format(job_id))
    return job_id
# [END submit_pyspark_job]

def job_details_json(project, cluster_name, bucket_name, job_type, payload):
    if job_type=="pyspark":
      jobAttribute="pysparkJob"
      FileUriPrefix = "mainPython"

    if job_type=="hive":
      jobAttribute="hiveJob"
      FileUriPrefix = "query"

    if job_type=="pyspark" or job_type=="hive":
      job_body = {
                '{}FileUri'.format(FileUriPrefix): 
                    'gs://{}/{}'.format(bucket_name, payload)
            }   

    if job_type=="query":
      jobAttribute = "hiveJob"
      job_body = {
          'queryList': {
          'queries': 
              [
                '{}'.format(payload)
              ]
          }
      }   

    return {
        'projectId': project,
        'job': {
            'placement': {
                'clusterName': cluster_name
            },
            '{}'.format(jobAttribute): job_body
        }
    }

def get_file(filename):
    f = open(filename, 'r')
    return f, os.path.basename(filename)


def upload_file(project, bucket_name, filename, file):
    """Uploads the PySpark file in this directory to the configured
    input bucket."""
    print('Uploading file to GCS')
    client = storage.Client(project=project)
    bucket = client.get_bucket(bucket_name)
    blob = bucket.blob(filename)
    blob.upload_from_file(file)


def download_output(project, cluster_id, output_bucket, job_id):
    """Downloads the output file from Cloud Storage and returns it as a
    string."""
    print('Downloading output file')
    client = storage.Client(project=project)
    bucket = client.get_bucket(output_bucket)
    output_blob = (
        'google-cloud-dataproc-metainfo/{}/jobs/{}/driveroutput.000000000'
        .format(cluster_id, job_id))
    return bucket.blob(output_blob).download_as_string()

def exec_job(project, zone, cluster_name, bucket_name, job_type, payload):

    cluster_list = list_clusters_with_details(
        project)['clusters']

    (cluster_id, output_bucket) = (
        get_cluster_id_by_name(cluster_list, cluster_name))
    # [START call_submit_pyspark_job]
    if(job_type!="query"):
      file, filename = get_file(payload)
      upload_file(project, bucket_name,
                        filename, file)
      file.close()
      job_id = submit_job(
          project, cluster_name, bucket_name, job_type, filename)
    
    if(job_type=="query"):
      job_id = submit_job(
          project, cluster_name, bucket_name, job_type, payload)
    # [END call_submit_pyspark_job]
    wait_for_job(project, job_id)

    output = download_output(project, cluster_id, output_bucket, job_id)
    print('Received job output {}'.format(output))
    return output
    
