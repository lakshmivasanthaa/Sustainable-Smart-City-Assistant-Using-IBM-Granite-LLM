import json
import os

# Define the path to the feedback log JSON file
FEEDBACK_FILE = os.path.join("app", "data", "feedback_log.json")

# ✅ Save feedback from the user
def save_feedback(user, category, message):
    feedback = {
        "user": user,
        "category": category,
        "message": message
    }

    # If file doesn't exist, create it with an empty list
    if not os.path.exists(FEEDBACK_FILE):
        with open(FEEDBACK_FILE, "w") as f:
            json.dump([], f)

    # Read existing feedback data
    with open(FEEDBACK_FILE, "r") as f:
        try:
            data = json.load(f)
        except json.JSONDecodeError:
            data = []

    # Append new feedback
    data.append(feedback)

    # Save updated feedback list back to the file
    with open(FEEDBACK_FILE, "w") as f:
        json.dump(data, f, indent=2)

# ✅ Get all feedback entries (for router or dashboard display)
def get_all_feedback():
    if not os.path.exists(FEEDBACK_FILE):
        return []

    with open(FEEDBACK_FILE, "r") as f:
        try:
            return json.load(f)
        except json.JSONDecodeError:
            return []
