from gcputils import exec_job
import conf

exec_job(conf.project, conf.zone, conf.cluster_name, conf.bucket_name, 
			conf.queryJob, conf.queryString)