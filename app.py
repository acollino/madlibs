from flask import Flask, request, render_template, flash, redirect
from stories import Story, get_stories
import os

app = Flask(__name__)
app.secret_key = os.getenv("SECRET_KEY", "dev_default")

story_list = get_stories()


@app.route("/")
def home_page():
    return render_template("index.html", stories=story_list.values())

@app.route("/prompts/<chosen_story>")
def story_prompts(chosen_story):
    if chosen_story not in story_list:
        flash("You requested a story that doesn't exist!")
        return redirect("/")
    else:
        return render_template("prompts.html", story=story_list.get(chosen_story))

@app.route("/story/<chosen_story>")
def show_story(chosen_story):
    if chosen_story not in story_list:
        flash("You requested a story that doesn't exist!")
        return redirect("/")
    elif len(request.args) == 0 or len(list(request.args.values())) == 0:
            flash("You did not fill in all of the prompts!")
            return redirect(f"/prompts/{chosen_story}")
    else:
        generated_story = story_list.get(chosen_story).generate_multi(request.args)
        return render_template("story.html", story=generated_story)

@app.errorhandler(404)
def page_not_found(e):
    flash("Something went wrong there, so you've been returned to the main page.")
    flash(f"This was the error: {e}")
    return redirect("/")