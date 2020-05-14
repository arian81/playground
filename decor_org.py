def decor(func):
  def wrap():
    print("diccccccccccccccccccccccccckkkk")
    func()
    print("fuuuuuuuuuuuuuuuuuuuuuuuuuuckkkk")
  return wrap

def print_text():
  print("pussssssssssssssssssssyyyyyyyyyy")

decorated = decor(print_text)
decorated()
