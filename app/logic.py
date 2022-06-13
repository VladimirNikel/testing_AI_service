from transformers import BlenderbotTokenizer, BlenderbotForConditionalGeneration
from transformers import Conversation, ConversationalPipeline
from typing import Tuple, Any

blenderbot = {
    '90m': 'facebook/blenderbot-90M',
    '400m': 'facebook/blenderbot-400M-distill',
    '1b': 'facebook/blenderbot-1B-distill',
    '3b': 'facebook/blenderbot-3B'
}
mname = blenderbot.get('400m')
model = BlenderbotForConditionalGeneration.from_pretrained(mname)
tokenizer = BlenderbotTokenizer.from_pretrained(mname)

from_memory = [
        ['user', "Hello, my friend!"],
        ['bot', "Hi, dear! How are you?"],
        ['user', "Oh, I'm fine! Where did you fly today?"],
        ['bot', "I landed in the Dominican Republic today. It's sunny here today."],
        ['user', "Ohh, cool! What are your plans for today?"],
        ['bot', "I'd like to go out for a drink and a dance. Find myself a companion for the evening."],
        ['user', "When do you go swimming? And when are you coming home?"],
        ['bot', "At night I'll go swimming naked. And I'll be back home in a month and a half, "
                "since I still have four countries to visit."],
        ['user', "What countries have you yet to visit?"]
    ]


async def init_new_dialogue() -> Tuple[Any, Any]:
    conversation = Conversation()
    for index, message in enumerate(from_memory):
        if message[0] == 'bot':
            conversation.append_response(response=message[1])
        else:
            conversation.add_user_input(text=message[1])
            if not index+1 == len(from_memory):
                conversation.mark_processed()

    return conversation, ConversationalPipeline(model=model, tokenizer=tokenizer)
