def ask_questions():
    # :def ask_questions(): Prompts the user with learning preference questions.
    responses = {}
    questions = {
        "prefers_diagrams": "Do you prefer diagrams and visual aids?",
        "takes_detailed_notes": "Do you usually take detailed notes?",
        "likes_charts": "Do you like using charts and graphs?",
        "remembers_faces": "Do you tend to remember faces?",
        "enjoys_discussions": "Do you enjoy discussions and group work?",
        "learns_from_lectures": "Do you learn well from lectures?",
        "talks_things_through": "Do you often talk things through to understand them?",
        "remembers_names": "Do you tend to remember names?",
        "learns_by_doing": "Do you learn best by doing things yourself?",
        "enjoys_hands_on_activities": "Do you enjoy hands-on activities?",
        "likes_moving_around": "Do you like to move around while learning?",
        "gestures_when_speaking": "Do you often gesture when you speak?",
    }
    for key, question in questions.items():
        responses[key] = input(f"{question} (yes/no): ").lower() == "yes"
    return responses 


def infer_learning_style(responses, rules):
    # :def infer_learning_style(): Infers learning style based on responses and rules.
    for rule in rules:
        if "IF" in rule and all(responses.get(condition, False) for condition in rule["IF"]):
            return rule["THEN"]  
    return "Could not determine a specific learning style." 


def suggest_content(learning_style):
    # :def suggest_content(): Suggests learning content based on the inferred style.
    suggestions = {
        "Visual": ["Diagrams", "Infographics", "Videos", "Mind Maps"],
        "Auditory": ["Podcasts", "Audiobooks", "Discussions", "Lectures"],
        "Kinesthetic": ["Hands-on projects", "Simulations", "Role-playing", "Experiments"],
        "Visual/Auditory": ["Video lectures", "Presentations with audio", "Group discussions with visual aids"],
        "Visual/Kinesthetic": ["Interactive simulations", "Building models based on diagrams"],
        "Auditory/Kinesthetic": ["Discussions with physical demonstrations", "Role-playing activities"],
        "Unclear": ["Try a variety of methods to see what works best for you!"],
        "Could not determine a specific learning style.": ["Try a variety of methods to see what works best for you!"]
    }
    return suggestions.get(learning_style, ["No specific suggestions available."]) 


if __name__ == "__main__":
    #Main execution block.
    rules = [
        # Rules for Visual Learners
        {"IF": ["prefers_diagrams", "takes_detailed_notes"], "THEN": "Visual"},
        {"IF": ["likes_charts", "remembers_faces"], "THEN": "Visual"},
        # Rules for Auditory Learners
        {"IF": ["enjoys_discussions", "learns_from_lectures"], "THEN": "Auditory"},
        {"IF": ["talks_things_through", "remembers_names"], "THEN": "Auditory"},
        # Rules for Kinesthetic Learners
        {"IF": ["learns_by_doing", "enjoys_hands_on_activities"], "THEN": "Kinesthetic"},
        {"IF": ["likes_moving_around", "gestures_when_speaking"], "THEN": "Kinesthetic"},
        # Rules for combined learning styles
        {"IF": ["prefers_diagrams", "enjoys_discussions"], "THEN": "Visual/Auditory"},
        {"IF": ["takes_detailed_notes", "learns_by_doing"], "THEN": "Visual/Kinesthetic"},
        {"IF": ["enjoys_discussions", "enjoys_hands_on_activities"], "THEN": "Auditory/Kinesthetic"},
        {"IF": [], "THEN": "Unclear"},  # Default rule
    ]

    print("Welcome to the Learning Style Identifier!")

    user_responses = ask_questions()

    preferred_style = infer_learning_style(user_responses, rules)

    print(f"\nYour preferred learning style seems to be: {preferred_style}")

    suggested_content = suggest_content(preferred_style)

    print("\nHere are some suggested learning content types for you:")
    for item in suggested_content:
        print(f"- {item}")