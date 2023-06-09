import os
import requests
from dotenv import load_dotenv, find_dotenv


class Translator:

    def __init__(self):
        self.key = self.get_key()

    def get_key(self):
        load_dotenv(find_dotenv())
        OAuth_token = os.environ.get('AOuth_token')

        headers = {
            'Content-Type': 'application/x-www-form-urlencoded',
        }

        data = '{"yandexPassportOauthToken":"OAuth_token"}'.replace(
                                                            'OAuth_token',
                                                            OAuth_token)

        response = requests.post(
            'https://iam.api.cloud.yandex.net/iam/v1/tokens',
            headers=headers,
            data=data)

        json_response = response.json()
        return json_response['iamToken']

    def translate(self, text):
        load_dotenv(find_dotenv())
        IAM_TOKEN = self.key
        folder_id = os.environ.get('folder_id')
        target_language = 'ru'
        source_language = 'en'
        # source_language = 'zh'
        texts = text

        body = {
            "sourceLanguageCode": source_language,
            "targetLanguageCode": target_language,
            "texts": texts,
            "folderId": folder_id,
        }

        headers = {
            "Content-Type": "application/json",
            "Authorization": "Bearer {0}".format(IAM_TOKEN)
        }

        response = requests.post(
            'https://translate.api.cloud.yandex.net/translate/v2/translate',
            json=body,
            headers=headers
        )

        print(response.text)
        data = response.json()
        lst = data['translations']
        translation = lst[0]

        return translation['text']
