import os
import pytest
import requests
from dotenv import load_dotenv

# Загрузка переменных из .env файла
load_dotenv()

# Переменные окружения
token = os.getenv("GITHUB_TOKEN")
user = os.getenv("GITHUB_USERNAME")
repo = os.getenv("REPO_NAME")

# URL для API
api_url = "https://api.github.com"
headers = {"Authorization": f"token {token}", "Accept": "application/vnd.github.v3+json"}


@pytest.fixture
def github_api():
    """Фикстура для работы с API GitHub"""
    return {
        "api_url": api_url,
        "headers": headers,
        "user": user,
        "repo": repo
    }


def create_repo(api):
    """Создание репозитория"""
    url = f"{api['api_url']}/user/repos"
    data = {"name": api['repo'], "description": "Тест", "private": False}
    r = requests.post(url, json=data, headers=api['headers'])
    assert r.status_code == 201, f"Ошибка при создании репозитория: {r.json().get('message')}"
    print(f"Репозиторий {api['repo']} успешно создан.")


def check_repo(api):
    """Проверка существования репозитория"""
    url = f"{api['api_url']}/repos/{api['user']}/{api['repo']}"
    r = requests.get(url, headers=api['headers'])
    assert r.status_code == 200, f"Репозиторий не найден: {r.json().get('message')}"
    print(f"Репозиторий {api['repo']} найден.")


def delete_repo(api):
    """Удаление репозитория"""
    url = f"{api['api_url']}/repos/{api['user']}/{api['repo']}"
    r = requests.delete(url, headers=api['headers'])
    assert r.status_code == 204, f"Ошибка при удалении репозитория: {r.json().get('message')}"
    print(f"Репозиторий {api['repo']} успешно удален.")


def test_github_repo_operations(github_api):
    """Тестирование операций с репозиторием на GitHub"""
    # Создание репозитория
    create_repo(github_api)

    # Проверка репозитория
    check_repo(github_api)

    # Удаление репозитория
    delete_repo(github_api)

