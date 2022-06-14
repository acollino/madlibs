"""Madlibs Stories."""

class Story:
    """Madlibs story.

    To  make a story, pass a list of prompts, and the text
    of the template.

        >>> s = Story(["noun", "verb"],
        ...     "I love to {verb} a good {noun}.")

    To generate text from a story, pass in a dictionary-like thing
    of {prompt: answer, promp:answer):

        >>> ans = {"verb": "eat", "noun": "mango"}
        >>> s.generate(ans)
        'I love to eat a good mango.'
    """

    def __init__(self, words, text, author="", title="", icon="story"):
        """Create story with words and template text."""

        self.prompts = words
        self.template = text
        self.author = author
        self.title = title
        self.icon = icon

    def generate(self, answers):
        """Substitute answers into text."""

        text = self.template

        for (key, val) in answers.items():
            text = text.replace("{" + key + "}", val)

        return text

    def generate_multi(self, answers):
        """Substitute MultiDict answers into text."""

        text = self.template

        for key in answers.keys():
            temp_values = answers.getlist(key)
            target = "{" + key + "}"
            while len(temp_values) > 0:
                text = text.replace(
                    target, temp_values.pop(0), 1)
        return text

    def generate_url(self):
        """Generate a url for page navigation"""
        return f"/stories/{self.icon}"


def get_stories():
    basic = Story(
        ["place", "noun", "verb", "adjective", "plural_noun"],
        """Once upon a time in a long-ago {place}, there lived a
       large {adjective} {noun}. It loved to {verb} {plural_noun}.""",
        "Springboard", "Default Story")
    scuba = Story(
        ["faraway_place", "verb_ending_in_ing", "past_tense_verb",
         "noun", "adjective", "article_of_clothing_plural", "adjective",
         "adjective", "land_animal", "water_animal", "large_number", "body_part_plural",
         "color", "adverb_ending_in_ly", "name", "past_tense_verb", "noun"],
        """My family and I went to {faraway_place} for a beach vacation. On our last day 
        we all went scuba {verb_ending_in_ing}. We {past_tense_verb} off the {noun} wearing 
        {adjective} {article_of_clothing_plural}. Under the {adjective} water, I swam 
        ahead of my family—and came face-to-face with a(n) {adjective} creature with the 
        head of a(n) {land_animal} and the body of a(n) {water_animal}! It had {large_number} 
        {body_part_plural} covered in {color} stripes. “Hi,” the creature said 
        {adverb_ending_in_ly}. “My name is {name}.” Then it {past_tense_verb} at me. 
        I turned to get my family's attention but the creature swam away faster 
        than a(n) {noun}! No one believed my story, but that's OK. Maybe I discovered a 
        new species.""", "Kay Boatner", "Scuba Surprise", "scuba")
    dream = Story(
        ["planet", "tool_plural", "verb", "noun_plural", "adverb_ending_in_ly",
         "past_tense_verb", "adjective", "noun", "small_number", "color", "past_tense_verb",
         "animal", "verb_ending_in_ing", "noun_plural", "noun_plural", "noun_plural",
         "piece_of_furniture"],
        """My family joined a tree planting in honor of {planet} Day. Grabbing our 
        {tool_plural}, we walked to the park. “Whatever you do, don't {verb} when you're 
        planting,” the leader said. With our arms full of {noun_plural}, my sister and I 
        ran {adverb_ending_in_ly} down the path to dig our first hole. As we got started, 
        I did exactly what the leader told me not to do: I {past_tense_verb}. Suddenly, a(n) 
        {adjective} {noun} burst from the tree! I stared at it for {small_number} seconds and 
        watched it turn a deep shade of {color}. I was so surprised I {past_tense_verb} like 
        a(n) {animal}. As my sister and I started {verb_ending_in_ing} down the path deeper 
        into the woods, {noun_plural} started springing from everywhere. Then the whole forest 
        filled with {noun_plural} and {noun_plural}. That's when I tripped over a root—and woke 
        up facedown on my {piece_of_furniture}. I must love the Earth. Even my dreams are green!”
        """, "Margaret J. Krauss", "Dreaming Green", "forest")
    garden = Story(
        ["adjective_ending_in_est", "verb_ending_in_ing", "adjective", "noun", "name_1",
         "noun_plural", "name_2", "past_tense_verb", "noun_plural", "past_tense_verb",
         "adjective", "type_of_liquid", "noun", "body_part", "adverb_ending_in_ly", "animal",
         "noun", "name_2", "name_1", "noun"],
        """My friends and I have the {adjective_ending_in_est} job {verb_ending_in_ing} 
         gardens for Mrs. Johnson, the {adjective} lady who lives down the {noun}. One day, 
         while {name_1} pulled {noun_plural} and {name_2} {past_tense_verb} the lawn, I watered 
         the {noun_plural}. Then I had an idea. Wouldn't it be more fun to water my friends 
         instead? But just as I turned the hose on my pals, Mrs. Johnson {past_tense_verb} into 
         the path of the water spray—and got {adjective}. My friends and I froze. Then to our 
         surprise, she yelled, “{type_of_liquid} fight!” She pulled a water {noun} from her back 
         pocket and squirted my {body_part}. Then she {adverb_ending_in_ly} aimed another 
         {animal}-shaped {noun} at {name_2} as {name_1} dived behind a(n) {noun}. Who knew 
         gardening was a contact sport?""", "Sally King", "Water World", "water")
    stories = [basic, scuba, dream, garden]
    return {story.icon: story for story in stories}
