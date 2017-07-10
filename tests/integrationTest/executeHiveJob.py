from gcputils import exec_job
import conf
import os

file_location = '{}/{}'.format(os.getcwd(),conf.hive_file_name)

exec_job(conf.project, conf.zone, conf.cluster_name, conf.bucket_name, conf.hiveJob, file_location)