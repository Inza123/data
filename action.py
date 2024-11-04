import requests
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher

class ActionManageRepositories(Action):
    def name(self) -> str:
        return "action_manage_repositories"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: dict) -> list:
        action = tracker.get_slot("action")
        repo_name = tracker.get_slot("repo_name")
        token = "yhijidoquejiodijoeqijofjejiofhjojio"  # Replace with your GitHub token
        headers = {'Authorization': f'token {token}'}
        username = "hello"  # Your GitHub username

        if action == "list":
            response = requests.get(f'https://api.github.com/users/{username}/repos', headers=headers)
            repos = response.json()
            repo_list = [repo['name'] for repo in repos]
            dispatcher.utter_message(text=f"Here are your repositories: {', '.join(repo_list)}")
        elif action == "create":
            response = requests.post(f'https://api.github.com/user/repos', headers=headers, json={'name': repo_name})
            if response.status_code == 201:
                dispatcher.utter_message(text=f"The repository '{repo_name}' has been created successfully.")
            else:
                dispatcher.utter_message(text="There was an error creating the repository.")
        elif action == "delete":
            response = requests.delete(f'https://api.github.com/repos/{username}/{repo_name}', headers=headers)
            if response.status_code == 204:
                dispatcher.utter_message(text=f"The repository '{repo_name}' has been deleted successfully.")
            else:
                dispatcher.utter_message(text="There was an error deleting the repository.")
        else:
            dispatcher.utter_message(text="I'm sorry, I don't understand that action.")

        return []
