import math
import random

def drawGraphtoCanvas(canvas, edges, node, size):
    coords = []
    centers = []

    items = []
    lines = []
    vertexes = []
    v_names = []
    w_names = []

    edge = len(edges)

    (cX, cY) = (size / 2, size / 2)
    bigRad = cX - cX / 10
    r = 20
    rad = math.radians(270)
    difRad = math.radians(360.0 / node)

    # find the center coordinates of the nodes
    for i in range(node):
        x = math.cos(rad) * bigRad + cX - r
        y = math.sin(rad) * bigRad + cY - r
        centers.append((x + r / 2, y + r / 2))
        coords.append((x, y, x + r, y + r))  # x0, y0, x1, y1
        rad += difRad

    # draw the edges between the nodes that we found before
    for i in range(edge):
        lines.append(canvas.create_line(centers[edges[i][0]], centers[edges[i][1]], width=2, fill="blue"))
        [x1,y1] = centers[edges[i][0]]
        [x2,y2] = centers[edges[i][1]]
        m1 = (x1 + x2) / 2 + random.randint(-10 , 10)
        m2 = (y1 + y2) / 2 + random.randint(-10 , 10)
        w_names.append(canvas.create_text(m1, m2, text=str(edges[i][2]), activefill="purple"))
    items.append(lines)
    # draw the nodes
    for i in range(node):
        vertexes.append(canvas.create_oval(coords[i], fill="cyan", outline="cyan"))
        v_names.append(canvas.create_text(coords[i][0] + r/2, coords[i][1] + r/2, text=str(i), activefill="red"))

    items.append(vertexes)
    items.append(v_names)
    return  items