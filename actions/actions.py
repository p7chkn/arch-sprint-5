from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher

class ActionPerformanceInfo(Action):
    def name(self) -> Text:
        return "action_performance_info"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(text="Для улучшения производительности можно использовать кэширование, оптимизацию запросов и балансировку нагрузки.")
        return []

# Add other custom actions here
