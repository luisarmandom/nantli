# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.forms import FormValidationAction
import random


class ActionHelloWorld(Action):

    def name(self) -> Text:
        return "action_hello_world"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        dispatcher.utter_message(text="Hello World!")

        return []

class ValidateUserMood(FormValidationAction):

    def name(self) -> Text:
         return "validate_user_mood"

    @staticmethod
    def userMood_db() -> List[Text]:
        """Database of supported user moods."""

        return [
            "feliz",
            "ansiedad",
            "triste",
            "molesto",
            "molesta",
            "enojado"
        ]

    def validate_userMood(
        self,
        value: Text,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> Dict[Text, Any]:
        """Validate pizzaSize value."""

        if value.lower() in self.userMood_db():
            # validation succeeded, set the value of the "cuisine" slot to value
            return {"userMood": value}
        else:
            dispatcher.utter_message(response="utter_unkown_mood")
            # validation failed, set this slot to None, meaning the
            # user will be asked for the slot again
            return {"userMood": None}