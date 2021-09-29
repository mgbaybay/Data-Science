colors = ["red", "blue", "green", "yellow"]
print(colors)

temp = colors[1]
colors[1] = colors[2]
colors[2] = temp
print(colors)

removed_color = colors.pop(-1)
colors.insert(1, "orange")
colors.insert(2, removed_color)
colors.append("violet")
print(colors)