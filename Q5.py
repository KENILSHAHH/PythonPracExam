print("Input x1,y1,x2,y2,x3,y3,x4,y4:")
x1, y1,x2, y2, x3, y3, x4, y4 = map(float, input().split())
print('PQ and RS are parallel.' if abs((x2 - x1)*(y4 - y3) - (x4 - x3)*(y2 - y1)) < 1e-10 else 'PQ and RS are not parallel')

