from typing import Any, Dict
from loguru import logger

class Formatter:
    """
    Formatter class to format the response based on the inference and data.
    """


    def format(self, data: Dict[str, Any], inference: Dict[str, Any]) -> dict:
        """
        Format the response using the given data and inference information.

        :param data: The data containing records to process.
        :param inference: Inference details including main entity and operation kind.
        :return: Formatted response dictionary.
        """

        logger.info("Processing output using inference details")

        response = {}
        self.main_entity = inference.get("main_entity", "")
        self.kind = inference.get("operation_kind", "")
        self.general_message = inference.get("general_message", "Unable to process question, try again")
        self.next_questions = inference.get("next_questions", [])

        # Extract results from data records
        results = [record["fields"] for record in data.get("records", [])]

        response["content"] = self.general_message

        if len(results) == 0:
            response["content"]= "Sorry, I couldn't find any details regarding this"

        response["main_entity"] = self.main_entity
        response["main_format"] = self.kind
        response["role"] = "assistant"
        response["data"]= results

        return response
