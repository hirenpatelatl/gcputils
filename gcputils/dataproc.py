import os

from google.cloud import storage
import googleapiclient.discovery

REGION = 'global'

def create_json(): 
    return {
    "projectId": "ambient-hulling-161217",
    "clusterName": "cluster-1",
    "config": {
      "configBucket": "",
      "gceClusterConfig": {
        "zoneUri": "https://www.googleapis.com/compute/v1/projects/ambient-hulling-161217/zones/us-east1-b",
        "networkUri": "https://www.googleapis.com/compute/v1/projects/ambient-hulling-161217/global/networks/default"
      },
      "masterConfig": {
        "numInstances": 1,
        "machineTypeUri": "https://www.googleapis.com/compute/v1/projects/ambient-hulling-161217/zones/us-east1-b/machineTypes/n1-standard-1",
        "diskConfig": {
          "bootDiskSizeGb": 500,
          "numLocalSsds": 0
        }
      },
      "workerConfig": {
        "numInstances": 2,
        "machineTypeUri": "https://www.googleapis.com/compute/v1/projects/ambient-hulling-161217/zones/us-east1-b/machineTypes/n1-standard-1",
        "diskConfig": {
          "bootDiskSizeGb": 500,
          "numLocalSsds": 0
        }}}}



# [START create_cluster]
def create_cluster(dataproc, project, cluster_name, zone):
    print('Creating cluster.')
    zone_uri = \
        'https://www.googleapis.com/compute/v1/projects/{}/zones/{}'.format(
            project, zone)
    cluster_data = {
        'projectId': project,
        'clusterName': cluster_name,
        'config': {
            'gceClusterConfig': {
                'zoneUri': zone_uri
            }
        }
    }
    result = dataproc.projects().regions().clusters().create(
        projectId=project,
        region=REGION,
        body=cluster_data).execute()
    return result
# [END create_cluster]
    


