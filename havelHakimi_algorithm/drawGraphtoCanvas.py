import math

def drawGraphtoCanvas(canvas, edges, node, size):
    coords = []
    centers = []
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
        canvas.create_line(centers[edges[i][0]], centers[edges[i][1]], width=2, fill="blue")
    # draw the nodes
    for i in range(node):
        canvas.create_oval(coords[i], fill="cyan", outline="cyan")
        canvas.create_text(coords[i][0] + r/2, coords[i][1] + r/2, text=str(i), activefill="red")
