print("Once upon a time...")
######
# TREENODE CLASS
######
class TreeNode:
  def __init__(self, story_piece):
    self.story_piece = story_piece
    self.choices = []
    print("initializing story...")
  
  def add_child(self, node):
    self.node = node
    self.choices.append(self.node)
  
  def traverse(self):
    story_node = self
    print(story_node.story_piece)
    while len(story_node.choices) > 0:
      user_choice = input("Enter 1 or 2 to continue the story: ")
      if int(user_choice) in [1,2]:
        chosen_index = int(user_choice) - 1
        chosen_child = story_node.choices[chosen_index]
        print(chosen_child.story_piece)
      else:
        print("Choose one from the options: 1 or 2 ")
      story_node = chosen_child
  
  def former_traverse(self):
    nodes_to_visit = [self]
    while len(nodes_to_visit) > 0:
      current_node = nodes_to_visit.pop(0)
      print(current_node.story_piece)
      nodes_to_visit += current_node.choices

# print(user_choice)

######
# VARIABLES FOR TREE
######
story_piece_1 = """ You are in a forest clearing. There is a path to the left.
A bear emerges from the trees and roars!
Do you:
1 ) Roar back!
2 ) Run to the left...
"""

story_piece_2 = """
The bear is startled and runs away.
Do you:
1 ) Shout 'Sorry bear!'
2 ) Yell 'Hooray!'
"""

story_piece_3 = """
You come across a clearing full of flowers.
The bear follows you and asks 'what gives?'
Do you:
1 ) Gasp 'A talking bear!'
2 ) Explain that the bear scared you.
"""

story_piece_4 = """
The bear returns and tells you it's been a rough week.
After making peace with a talking bear, he shows you the way out of the forest.

YOU HAVE ESCAPED THE WILDERNESS.
"""

story_piece_5 = """
The bear returns and tells you that bullying is not okay before leaving you alone in the wilderness

YOU HAVE ANOTHER ANIMAL SAVE YOU.
"""

story_piece_6 = """
The bear is unamused. After smelling the flowers, it turns around and leaves you alone.

YOU HAVE ANOTHER ANIMAL SAVE YOU.
"""

story_piece_7 = """
The bear understands and apologizes for startling you.
Your new friend shows you a path leading out of the forest.

YOU HAVE ESCAPED THE WILDERNESS.
"""

story_root = TreeNode(story_piece_1)
choice_a = TreeNode(story_piece_2)
choice_b = TreeNode(story_piece_3)
choice_a_1 = TreeNode(story_piece_4)
choice_a_2 = TreeNode(story_piece_5)
choice_b_1 = TreeNode(story_piece_6)
choice_b_2 = TreeNode(story_piece_7)

story_root.add_child(choice_a)
story_root.add_child(choice_b)
choice_a.add_child(choice_a_1)
choice_a.add_child(choice_a_2)
choice_b.add_child(choice_b_1)
choice_b.add_child(choice_b_2)
######
# TESTING AREA
######
# print(story_root.story_piece)
# story_root.traverse()

story_root.former_traverse()