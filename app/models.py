class Pitch:

    all_pitches = []

    def __init__(self,title,category,content,date_created,upvotes = 0,downvotes = 0):
        self.title = title
        self.category = category
        self.content = content
        self.date_created = date_created
        self.upvotes = upvotes
        self.downvotes = downvotes

    def save_pitch(self):
        Pitch.all_pitches.append(self)

    @classmethod
    def clear_pitches(cls):
        Pitch.all_pitches.clear()


# class User:
#     def __init__(self,username,email,password):
#         self.username = username
#         self.email = email
#         self.password = password
