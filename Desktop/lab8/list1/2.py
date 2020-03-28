def common_end(a, b):
  for i in range(len(a)):
    for j in range(len(b)):
      if(a[len(a) - 1] == b[len(b) - 1] or a[0] == b[0]):
        return True
  return False
