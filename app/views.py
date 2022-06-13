from aioflask import jsonify
import logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(name)s - %(message)s",)

from app import app
from app.logic import init_new_dialogue


@app.route('/', methods=['GET', 'POST'])
async def new_message():
    try:
        conversation, nlp = await init_new_dialogue()
        result = nlp([conversation], do_sample=False, max_length=1000)
        message = list(result.iter_texts())[-1][1]
        return jsonify({
            'text': message
        }), 200

    except (ValueError, KeyError, TypeError) as error:
        logging.exception(f"error: {error}")
        return jsonify({
            'error': str(error)
        }), 400
