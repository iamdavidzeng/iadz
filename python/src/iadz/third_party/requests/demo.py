import os
import base64
import requests


class Mixpanel(object):
    # only for export
    ENDPOINT = "https://data-eu.mixpanel.com/api/2.0/export/"

    # not for export
    # ENDPOINT = 'https://mixpanel.com/api'
    VERSION = "2.0"

    def __init__(self, api_secret):
        self.api_secret = api_secret
        self.connection_times = 0

    # @retry(stop=stop_after_attempt(5), wait=wait_fixed(2), reraise=True)
    def _request(self, url, params, headers):
        response = requests.get(url, params, headers=headers)
        print(f"request url: {response.url}")
        if response.status_code != 200:
            print(f"response error: {response.text} {response.url}")
            raise ConnectionError(response.text)

        return response.text

    def request(self, params):
        """
        methods - List of methods to be joined, e.g. ['events', 'properties', 'values']
                will give us http://mixpanel.com/api/2.0/events/properties/values/
        params - Extra parameters associated with method
        """
        # params['format'] = format

        request_url = self.ENDPOINT

        auth = base64.b64encode(self.api_secret).decode("utf8")
        headers = {
            "Authorization": "Basic {encoded_secret}".format(encoded_secret=auth)
        }

        return self._request(request_url, params, headers)


if __name__ == "__main__":
    api = Mixpanel(api_secret=os.getenv("MIXPANEL_SECRET_API_DSH").encode("utf-8"))
    data = api.request({
        "from_date": "2022-03-01",
        "to_date": "2022-03-02"
    })
    print(data)
