from gcputils import dataproc
from gcputils import create_json

create_cluster_json = {
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
      }
    }
  }
}

def test_dataproc():
    assert dataproc.create_json()==create_cluster_json

def test_create_json():
	assert create_json()==create_cluster_json