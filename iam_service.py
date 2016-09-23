
"""Module to interact with Google Cloud Platform IAM."""

from apiclient import discovery
from oauth2client.client import GoogleCredentials


def _iam_service():
  """List the keys for a service account.
  Returns:
    An apiclient service object.
  """
  credentials = GoogleCredentials.get_application_default()
  return discovery.build(serviceName='iam', 
                         version='v1',
                         credentials=credentials)

def list_keys(project_id, service_account_id):
  """List the keys for a service account.
  Args:
    project_id: String of a project id.  Should contain the specified service
        account.
    service_account_id: String of a service account id.  Should be in the
        specified project.
  Returns:
    Dict of a newly created instance of ServiceAccountKey.
  """
  full_name = 'projects/{0}/serviceAccounts/{1}'.format(project_id,
                                                        service_account_id)
  keys = _iam_service().projects().serviceAccounts().keys()
  request = keys.list(name=full_name)
  return request.execute()
  