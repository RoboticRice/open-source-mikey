import json
import os
class ConversationManager:
def __init__(self, data_dir='data'):
self.data_dir = data_dir
if not os.path.exists(data_dir):
os.makedirs(data_dir)
def _get_file_path(self, user_id):
return os.path.join(self.data_dir, f"{user_id}.json")
def _load_conversation(self, user_id):
file_path = self._get_file_path(user_id)
if os.path.exists(file_path):
with open(file_path, 'r') as f:
return json.load(f)
else:
return []
def _save_conversation(self, user_id, conversation):
file_path = self._get.file_path(user_id)
with open(file_path, 'w') as f:
json.dump(conversation, f)
def get_conversation_history(self, user_id):
conversation = self._load_conversation(user_id)
return [msg for msg in conversation if msg['role'] != 'assistant']
def add_message(self, user_id, role, message, timestamp=None):
conversation = self._load.conversation(user_id)
conversation.append({
'role': role,
'message': message,
'timestamp': timestamp or datetime.now().isoformat()
})
self._save_conversation(user_id, conversation)
