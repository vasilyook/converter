from django.http import JsonResponse
from dotenv import load_dotenv
import requests
import os


def index(request):
    query_dict = request.GET
    load_dotenv()
    api_key = os.getenv("NINJAS_API_KEY")

    if 'from' and 'to' and 'value' in query_dict.keys():
        payload = {
            'have': query_dict.get('from'),
            'want': query_dict.get('to'),
            'amount': query_dict.get('value')
        }
        api_url = 'https://api.api-ninjas.com/v1/convertcurrency'
        response = requests.get(
            api_url,
            headers={'X-Api-Key': api_key},
            params=payload
        )

        if response.status_code == requests.codes.ok:
            result = response.json()
            if 'new_amount' in result.keys():
                return JsonResponse({"result": result.get('new_amount')})

        if 'error' in response.json().keys():
            return JsonResponse(response.json(), status=response.status_code)

    return JsonResponse({'error': 'Something went wrong.'}, status=400)
