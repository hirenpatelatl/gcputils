from gcputils import get_cluster_create_json
import conf

cluster_create_json_default = {
  'clusterName': 'foocluster-2', 
  'projectId': 'foo', 
  'config': {
    'gceClusterConfig': {
      'zoneUri': 'https://www.googleapis.com/compute/v1/projects/foo/zones/us-east1-b'
      }}}


def test_get_cluster_create_json():
  assert get_cluster_create_json(conf.project, conf.cluster_name, conf.zone)==cluster_create_json_default
