import google.generativeai as genai
from django.conf import settings
import logging

logger = logging.getLogger(__name__)

def get_flashcard_explanation(question, answer, context=""):
    """
    Generates a short, encouraging explanation for why an answer is correct
    using Google Gemini.
    """
    if not settings.GEMINI_API_KEY:
        logger.warning("GEMINI_API_KEY not found in settings.")
        return "AI explanation unavailable (API Key missing)."

    try:
        genai.configure(api_key=settings.GEMINI_API_KEY)
        model = genai.GenerativeModel('gemini-pro')

        prompt = f"""
        You are a warm, encouraging, and expert Google Cloud Platform tutor.
        
        The student is studying flashcards.
        Question: "{question}"
        Correct Answer: "{answer}"
        Context/Topic: "{context}"

        Please explain CLEARLY and CONCISELY (max 2 sentences) why this is the correct answer.
        Focus on the 'why'. Do not just repeat the answer.
        Use a friendly emoji or two if appropriate.
        """

        response = model.generate_content(prompt)
        
        if response and response.text:
            return response.text.strip()
        else:
            return "Could not generate an explanation at this time."

    except Exception as e:
        logger.error(f"Error generating AI explanation: {e}")
        return "AI is taking a quick nap. Try again later!"
