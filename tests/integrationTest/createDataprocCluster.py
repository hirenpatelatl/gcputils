from gcputils import create_cluster
from gcputils import wait_for_cluster_creation
import conf

cluster_create_json, result = create_cluster(conf.project, conf.cluster_name, conf.zone)

print(cluster_create_json)
print(result)

wait_for_cluster_creation(conf.project, conf.cluster_name, conf.zone)

