import requests
from requests.auth import HTTPBasicAuth
import json


def getAccessToken(client_id,client_secret):
    headers = {'Content-Type': 'application/x-www-form-urlencoded'}
    response = requests.post("https://debris-prod.auth.eu-central-1.amazoncognito.com/oauth2/token?scope=https://api.leanspace.io/READ&grant_type=client_credentials",
    headers=headers,
    auth=HTTPBasicAuth(client_id, client_secret));
    jsonResponse = response.json();
    return jsonResponse.get('access_token');

def createAsset(access_token):
    headers = {'Content-Type': 'application/json',
    'Authorization':'Bearer '+access_token}
    data = '{"name":"tutorialAsset","description":"tutorialAsset","kind":"GENERIC","type":"ASSET","parentNodeId":""}'
    response = requests.post(
        url="https://api.leanspace.io/asset-repository/nodes",
        headers=headers,
        data=data)
    return response.json();

def getAssetTree(access_token):
    headers = {'Content-Type': 'application/json',
    'Authorization':'Bearer '+access_token}
    params = (
        ('query', ''),
        ('resources', 'NODE'),)
    response = requests.get(
        url='https://api.leanspace.io/asset-repository/tree',
        headers=headers,
        params=params)
    return response.json();  

def getAssetMetric(access_token):
    headers = {'Content-Type': 'application/json',
    'Authorization':'Bearer '+access_token}
    params = (
        ('query', ''),
        ('resources', 'NODE'),)
    response = requests.get(
        url='https://api.leanspace.io/asset-repository/metrics',
        headers=headers,
        params=params)
    return response.json();  

def getStreams(access_token):
    headers = {'Content-Type': 'application/json',
    'Authorization':'Bearer '+access_token}
    params = (
        ('query', ''),
        ('resources', 'NODE'),)
    response = requests.get(
        url='https://api.leanspace.io/streams-repository/streams',
        headers=headers,
        params=params)
    return response.json();

def FetchStreams(access_token, stream_id:str):
    headers = {'Content-Type': 'application/json',
    'Authorization':'Bearer '+access_token}
    params = (
        ('query', ''),
        ('resources', 'NODE'),)
    response = requests.get(
        url='https://api.leanspace.io/streams-repository/streams/'+stream_id,
        headers=headers,
        params=params)
    return response.json(); 

def FetchPath(access_token, stream_id:str, path:str):
    headers = {'Content-Type': 'application/json',
    'Authorization':'Bearer '+access_token}
    params = (
        ('query', ''),
        ('resources', 'NODE'),)
    response = requests.get(
        url='https://api.leanspace.io/streams-repository/streams/'+stream_id+'/'+path,
        headers=headers,
        params=params)
    return response.json();  

def GetMetric(metric_id:str, tenantId='debris'):

    client_id = '7kl5gul58apdl64alp78r2mr9b'
    client_secret = 'f7f8feet0l3ja9nep8gj83nstunernqtm5ds8tglutvcd0tfp98'

    metric_id = metric_id.replace('-','_')

    access_token = getAccessToken(client_id=client_id, client_secret=client_secret)
    metric_id = metric_id.replace('-','_')

    def GetQuery(metric_id:str, tenantId:str):
        data = {
        "query": {
            "dimensions": [
             f"telemetry_{tenantId}.d_{metric_id}"
            ],
            "timeDimensions": [
                {
                    "dimension": f"telemetry_{tenantId}.timestamp",
                    "granularity": "hour",
                    "dateRange": [
                        "2021-06-10T11:09:48.171913300Z",
                        "2021-11-16T11:10:48.171913300Z",
                    ]
                }
            ],
            "filters": [
                {
                    "operator": "set",
                    "member": f"telemetry_{tenantId}.d_{metric_id}"
                }
            ],
            "ungrouped": False,
            "order": {
                "telemetry_debris.timestamp": "desc"
            },
            "limit": 100
        }}
        return data

    # param = {"query":{"dimensions": [f"telemetry_debris.d_{metric_id}"]}}

    headers = {'Content-Type': 'application/json',
    'Authorization':'Bearer '+ access_token}
    response = requests.post(
        url='https://api.leanspace.io/analytics/v1/load',
        headers=headers,
        # params=param,
        data=json.dumps(GetQuery(metric_id, tenantId)))
    response.raise_for_status()
    return response.json()




def GetQuery(metric_id:str, tenantId:str):
        data = {
        "query": {
            "dimensions": [
             f"telemetry_{tenantId}.d_{metric_id}"
            ],
            "timeDimensions": [
                {
                    "dimension": f"telemetry_{tenantId}.timestamp",
                    "granularity": "hour",
                    "dateRange": [
                        "2021-06-10T11:09:48.171913300Z",
                        "2021-11-16T11:10:48.171913300Z",
                    ]
                }
            ],
            "filters": [
                {
                    "operator": "set",
                    "member": f"telemetry_{tenantId}.d_{metric_id}"
                }
            ],
            "ungrouped": False,
            "order": {
                "telemetry_debris.timestamp": "desc"
            },
            "limit": 10000
        }}
        return data

global client_id, client_secret

client_id = '7kl5gul58apdl64alp78r2mr9b'
client_secret = 'f7f8feet0l3ja9nep8gj83nstunernqtm5ds8tglutvcd0tfp98'
