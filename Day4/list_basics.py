# lists_basics.py
# goal: create, access, and change list items

colors = ["red", "green", "blue", "yellow", "black"]

print("original list:", colors)

# indexing forward
print("first color (index 0):", colors[0])
print("third color (index 2):", colors[2])

# indexing backward
print("last color (index -1):", colors[-1])
print("second to last (index -2):", colors[-2])

# changing an item
colors[1] = "purple"   # change green to purple
print("after change:", colors)

# adding items
colors.append("pink")           # add to the end
colors.insert(2, "orange")      # insert at index 2
print("after adding:", colors)

# removing items
colors.remove("black")          # remove by value
popped = colors.pop()           # remove last item
print("after removing:", colors)
print("popped item was:", popped)

