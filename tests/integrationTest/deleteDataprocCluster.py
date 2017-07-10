from gcputils import delete_cluster
import conf

delete_cluster(conf.project, conf.cluster_name)