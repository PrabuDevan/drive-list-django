from django.http import JsonResponse
import json
import requests


def get_drive_files(request):
    if request.method == 'POST':
        body = json.loads(request.body)
        print(body)
        url = 'https://content.googleapis.com/drive/v3/files'
        params = {
            'pageSize': 10,
            'fields': "nextPageToken, files(id, name, shared, size, createdTime, modifiedTime)",
            'key': 'AIzaSyCZpskkk3ggfa7TRxf4kFC5BcvPaueMAGY'
        }
        headers = {'Authorization': f'Bearer {body["access_token"]}'}
        r = requests.get(url, params=params, headers=headers)
        files = r.json()
        print(files)
        return JsonResponse(files, safe=False)


def get_next_page(request):
    if request.method == 'POST':
        body = json.loads(request.body)
        print(body)
        url = 'https://content.googleapis.com/drive/v3/files'
        params = {
            'pageSize': 10,
            'pageToken': body["nextPageToken"],
            'fields': "nextPageToken, files(id, name, shared, size, createdTime, modifiedTime)",
            'key': 'AIzaSyCZpskkk3ggfa7TRxf4kFC5BcvPaueMAGY'
        }
        headers = {'Authorization': f'Bearer {body["access_token"]}'}
        r = requests.get(url, params=params, headers=headers)
        files = r.json()
        print(files)
        return JsonResponse(files, safe=False)
