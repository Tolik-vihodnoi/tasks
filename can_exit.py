labirint1 = [
  [0, 1, 1, 1, 1, 1, 1],
  [0, 0, 1, 1, 0, 1, 1],
  [1, 0, 0, 0, 0, 1, 1],
  [1, 1, 1, 1, 0, 0, 1],
  [1, 1, 1, 1, 1, 0, 0]
]

labirint2 = [
  [0, 1, 1, 1, 1, 1, 1],
  [0, 0, 1, 0, 0, 1, 1],
  [1, 0, 0, 0, 0, 1, 1],
  [1, 1, 0, 1, 0, 0, 1],
  [1, 1, 0, 0, 1, 1, 1]
]

labirint3 = [
  [0, 1, 1, 1, 1, 0, 0],
  [0, 0, 0, 0, 1, 0, 0],
  [1, 1, 1, 0, 0, 0, 0],
  [1, 1, 1, 1, 1, 1, 0],
  [1, 1, 1, 1, 1, 1, 1]
]

labirint4 = [
  [0, 1, 1, 1, 1, 0, 0],
  [0, 0, 0, 0, 1, 0, 0],
  [1, 1, 1, 0, 0, 0, 0],
  [1, 0, 0, 0, 1, 1, 0],
  [1, 1, 1, 1, 1, 1, 0]
]



def can_exit(labirint: list, pos_current={'x': 0, 'y': 0}):
    x = pos_current['x']
    y = pos_current['y']
    labirint[y][x] += 1
    if x == len(labirint[0]) - 1 and y == len(labirint) - 1:
        return print('Success')
    for dx, dy  in ((0,-1), (0,1), (-1,0), (1,0)):
        if 0 <= x+dx < len(labirint[0]) and 0 <= y+dy < len(labirint) and \
                labirint[y+dy][x+dx] == 0:
            print(f"current position x={x+dx}, y={y+dy}")
            can_exit(labirint, pos_current={'x': x+dx, 'y': y+dy})




can_exit(labirint1)
can_exit(labirint2)
can_exit(labirint3)
can_exit(labirint4)