from flask import Flask, request, render_template
from stories import Story, get_stories

app = Flask(__name__)

story_example = Story(
    ["place", "noun", "verb", "adjective", "plural_noun"],
    """Once upon a time in a long-ago {place}, there lived a
       large {adjective} {noun}. It loved to {verb} {plural_noun}."""
)

story_list = get_stories()


@app.route("/")
def home_page():
    return render_template("index.html", stories=story_list.values())

@app.route("/prompts/<chosen_story>")
def story_prompts(chosen_story):
    return render_template("prompts.html", story=story_list.get(chosen_story))

@app.route("/story/<chosen_story>")
def show_story(chosen_story):
    user_input = request.args
    generated_story = story_list.get(chosen_story).generate_multi(user_input)
    return render_template("story.html", story=generated_story)
