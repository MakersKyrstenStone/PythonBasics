class Introducer:
  def __init__(self, name):
      self.name = name
  
  def announce(self):
    return f"I am {self.name}"

  def introduce(self, introducee):
    return f"Hello {introducee}, I am {self.name}!"

introducer = Introducer("Kay")
print(introducer.announce())
# Should print: "I am Kay!"
print(introducer.introduce("Fred"))
# Should print: "Hello Fred, I am Kay!"

class Reminder:
  def __init__(self, name):
      self.name = name
      self.take_action = ""

  def remind_me_to(self, action):
    self.take_action = action
    
  def remind(self):
    return f"{self.name}! {self.take_action}!"

reminder = Reminder("Kay")
reminder2 = Reminder("Kyrsten")
reminder.remind_me_to("Walk the dog")
reminder2.remind_me_to("Catch a Frog")

print(reminder.remind())
# Should print: "Kay! Walk the dog!"
print(reminder2.remind())
