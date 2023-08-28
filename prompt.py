import gpt_config
import openai


class Prompt():
    def __init__(self, model, story) -> None:
        self.model = model
        self.story = story

        self.message = [
        {
            "role" : "system",
            "content" : gpt_config.SYSTEM
        },
        {
            "role": "user",
            "content": gpt_config.USER1
        },
        {
                "role": "assistant",
                "content": gpt_config.ASSISTANT1
        },
        {
            "role": "user",
            "content": gpt_config.USER2
        },
        {
                "role": "assistant",
                "content": gpt_config.ASSISTANT2
        },
        {
            "role": "user",
            "content": gpt_config.USER3
        },
        {
                "role": "assistant",
                "content": gpt_config.ASSISTANT3
        }
        ]

    def set_model(self):
        response = openai.ChatCompletion.create(
            model=self.model,
            messages = self.message
            )

        answer = response.choices[0].message.content
        return answer

    def generate(self):
        #assistant = self.set_model()
        self.message.append(
            {
                "role": "user",
                "content": self.story
            }
        )

        response = openai.ChatCompletion.create(
            model=self.model,
            messages = self.message
            )

        answer = response.choices[0].message.content
        return answer

