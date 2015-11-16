from .rest import RestClient


class DeviceCredentials(object):

    """Auth0 connection endpoints

    Args:
        domain (str): Your Auth0 domain, e.g: 'username.auth0.com'

        jwt_token (str): An API token created with your account's global
            keys. You can create one by using the token generator in the
            API Explorer: https://auth0.com/docs/api/v2
    """

    def __init__(self, domain, jwt_token):
        self.domain = domain
        self.client = RestClient(jwt=jwt_token)

    def _url(self, id=None):
        url = 'https://%s/api/v2/device-credentials' % self.domain
        if id is not None:
            return url + '/' + id
        return url

    def get(self, user_id, client_id, type, fields=[], include_fields=True):
        """
        Args:
            user_id (str): The user_id of the devices to retrieve.

            client_id (str): The client_id of the devices to retrieve.

            type (str): The type of credentials (public_key, refresh_token).

            fields (list, optional): A list of fields to include or exclude
                (depending on include_fields) from the result, empty to
                retrieve all fields

            include_fields (bool, optional): True if the fields specified are
                to be excluded from the result, false otherwise
                (defaults to true)
        """

        params = {
            'fields': ','.join(fields) or None,
            'include_fields': str(include_fields).lower(),
            'user_id': user_id,
            'client_id': client_id,
            'type': type,
        }
        return self.client.get(self._url(), params=params)

    def create(self, body):
        return self.client.post(self._url(), data=body)

    def delete(self, id):
        return self.client.delete(self._url(id))
