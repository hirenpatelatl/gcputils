from gcputils import list_clusters
import conf
import json

expected_output == {

u'clusters': 
	[{
		u'status': {u
			'state': u'RUNNING', u'stateStartTime': u'2017-07-09T23:54:29.207Z'}, 
		u'clusterUuid': u'6b8463ec-814e-4414-b0b7-572af67af1fd', 
		u'clusterName': u'cluster-3', 
		u'projectId': u'ambient-hulling-161217', 
		u'metrics': {u
			'yarnMetrics': {
				u'yarn-containers': u'0', 
				u'yarn-memory-mb-configured': u'24576', 
				u'yarn-virtual-cores-used': u'0', 
				u'yarn-memory-mb-used': u'0', 
				u'yarn-virtual-cores-configured': u'8', 
				u'yarn-nodes': u'2'}, 
			u'hdfsMetrics': {
				u'dfs-nodes-decommissioning': u'0', 
				u'dfs-present-capacity': u'1004578562048', 
				u'dfs-remaining': u'1004578512896', 
				u'dfs-nodes-running': u'2', 
				u'dfs-nodes-decommissioned': u'0', 
				u'dfs-used': u'49152', 
				u'dfs-capacity': u'1056621535232'}}, 
		u'statusHistory': [{
			u'state': u'CREATING', u'stateStartTime': u'2017-07-09T23:52:55.225Z'}], 
		u'config': {u'masterConfig': {u'machineTypeUri': u'https://www.googleapis.com/compute/v1/projects/ambient-hulling-161217/zones/us-east1-b/machineTypes/n1-standard-4', u'diskConfig': {u'bootDiskSizeGb': 500}, u'numInstances': 1, u'instanceNames': [u'cluster-3-m'], u'imageUri': u'https://www.googleapis.com/compute/v1/projects/cloud-dataproc/global/images/dataproc-1-1-20170626-125907'}, u'softwareConfig': {u'imageVersion': u'1.1.34', u'properties': {u'mapred:yarn.app.mapreduce.am.resource.cpu-vcores': u'2', u'yarn:yarn.scheduler.minimum-allocation-mb': u'1024', u'spark:spark.executor.memory': u'5586m', u'mapred:mapreduce.reduce.cpu.vcores': u'2', u'mapred:mapreduce.reduce.memory.mb': u'6144', u'distcp:mapreduce.reduce.memory.mb': u'6144', u'distcp:mapreduce.map.memory.mb': u'3072', u'mapred:yarn.app.mapreduce.am.resource.mb': u'6144', u'mapred:mapreduce.map.memory.mb': u'3072', u'mapred:mapreduce.reduce.java.opts': u'-Xmx4915m', u'yarn:yarn.nodemanager.resource.memory-mb': u'12288', u'spark:spark.driver.memory': u'3840m', u'spark:spark.executor.cores': u'2', u'distcp:mapreduce.reduce.java.opts': u'-Xmx4915m', u'yarn:yarn.scheduler.maximum-allocation-mb': u'12288', u'mapred:yarn.app.mapreduce.am.command-opts': u'-Xmx4915m', u'spark:spark.driver.maxResultSize': u'1920m', u'distcp:mapreduce.map.java.opts': u'-Xmx2457m', u'mapred:mapreduce.map.cpu.vcores': u'1', u'spark:spark.yarn.am.memory': u'5586m', u'mapred:mapreduce.map.java.opts': u'-Xmx2457m', u'spark:spark.yarn.executor.memoryOverhead': u'558', u'spark:spark.yarn.am.memoryOverhead': u'558'}}, u'workerConfig': {u'machineTypeUri': u'https://www.googleapis.com/compute/v1/projects/ambient-hulling-161217/zones/us-east1-b/machineTypes/n1-standard-4', u'diskConfig': {u'bootDiskSizeGb': 500}, u'numInstances': 2, u'instanceNames': [u'cluster-3-w-0', u'cluster-3-w-1'], u'imageUri': u'https://www.googleapis.com/compute/v1/projects/cloud-dataproc/global/images/dataproc-1-1-20170626-125907'}, u'configBucket': u'dataproc-c63c892b-4520-4cfb-a7f9-974f20818902-us', u'gceClusterConfig': {u'networkUri': u'https://www.googleapis.com/compute/v1/projects/ambient-hulling-161217/global/networks/default', u'serviceAccountScopes': [u'https://www.googleapis.com/auth/bigquery', u'https://www.googleapis.com/auth/bigtable.admin.table', u'https://www.googleapis.com/auth/bigtable.data', u'https://www.googleapis.com/auth/cloud.useraccounts.readonly', u'https://www.googleapis.com/auth/devstorage.full_control', u'https://www.googleapis.com/auth/devstorage.read_write', u'https://www.googleapis.com/auth/logging.write'], u'zoneUri': u'https://www.googleapis.com/compute/v1/projects/ambient-hulling-161217/zones/us-east1-b'}}}]}


cluster_list = list_clusters(conf.project)
print(cluster_list)