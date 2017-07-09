gcputils
-------------------------------

## Development Instructions
	conda create -n gcputils python=2.7

	pip install -r requirements.txt
	pip install -upgrade .

## Install gcloud from SDK -> https://cloud.google.com/sdk/docs/quickstart-mac-os-x 
	gcloud init
	gcloud auth 
	gcloud auth application-default login
	gcloud info


## glcoud api reference 
	https://cloud.google.com/sdk/gcloud/reference/
## google-cloud python docs 
	https://googlecloudplatform.github.io/google-cloud-python/stable/

## Setup Google Cloud Project
	create gcloud project
	enable dataproc
	enable bigquery
	enable api's

## bigquery python api reference
	https://github.com/GoogleCloudPlatform/google-cloud-python/tree/master/bigquery

## storage
	https://github.com/GoogleCloudPlatform/google-cloud-python/tree/master/storage

## dataproc
	https://github.com/GoogleCloudPlatform/python-docs-samples/blob/master/dataproc/create_cluster_and_submit_job.py

## Setup Git
	git init
	git add README.md
	git commit -m "first commit"
	git remote add origin git@github.com:hirenpatelatl/gcputils.git
	git push -u origin master