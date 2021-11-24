def merge_asc(list1, list2):
  newlist = []
  index1 = 0
  index2 = 0
  newlist1 = []
  newlist2 = []

  newlist1.append(list1)
  newlist2.append(list2)

  while index1 < len(newlist1) and index2 < len(newlist2):
    if newlist1[index1] > newlist2[index2]:
      newlist.append(newlist2[index2])
      index2 += 1
    elif newlist1[index1] < newlist2[index2]:
      newlist.append(newlist1[index1])
      index1 += 1
    else:
      newlist.append(newlist1[index1])
      newlist.append(newlist2[index2])
      index1 += 1
      index2 += 1

  if index1 < len(newlist1):
    for i in range(index1, len(newlist1) - 1):
      newlist.append(newlist1[i])
  elif index2 < len(newlist2):
    for i in range(index2, len(newlist2) -1):
      newlist.append(newlist2[i])
  
  return newlist


def whole_merge_asc(items):
  listofitems = []
  item = []

  for i in range(len(items) - 1):
    item = items[i]
    listofitems.append(item)

  while len(listofitems) != 1:
    index = 0
    while index < len(listofitems) - 1:
      newlist = merge_asc(listofitems[index], listofitems[index + 1])
      listofitems[index] = newlist
      listofitems[index + 1] = None
      index += 1

  return listofitems


items = [4, 56, 23 ,7 ,34 ,546 ,32 ,1 ,44 ,76 ,5 ,89 ,100 ,3 ,99 ,12 ,7 ,18]

print(whole_merge_asc(items))