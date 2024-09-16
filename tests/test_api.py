import os
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
head1ers = {"Authorization": f"token {token}", "Accept": "application/vnd.github.v3+json"}

def cr_repo():
    """Создание репозитория"""
    url = f"{api_url}/user/repos"
    data = {"name": repo, "description": "Тест", "private": False}
    r = requests.post(url, json=data, headers=headers)
    print(f"Репозиторий {repo} {'успешно создан.' if r.status_code == 201 else 'Ошибка: ' + r.json().get('message')}")

def ch_repo():
    """Проверка репозитория"""
    url = f"{api_url}/repos/{user}/{repo}"
    r = requests.get(url, headers=headers)
    print(f"Репозиторий {repo} {'найден.' if r.status_code == 200 else 'Не найден: ' + r.json().get('message')}")

def de_repo():
    """Удаление репозитория"""
    url = f"{api_url}/repos/{user}/{repo}"
    r = requests.delete(url, headers=headers)
    print(f"Репозиторий {repo} {'удален.' if r.status_code == 204 else 'Ошибка: ' + r.json().get('message')}")

if __name__ == "__main__":
    cr_repo()  # Создание
    ch_repo()  # Проверка
    de_repo()  # Удаление