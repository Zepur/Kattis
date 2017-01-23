moves = [str(s) for s in input()]
ball = ['x', '-', '-']

for i in range(len(moves)):
    if moves[i] == 'A':
        ball[0], ball[1] = ball[1], ball[0]
    elif moves[i] == 'B':
        ball[1], ball[2] = ball[2], ball[1]
    else:
        ball[0], ball[2] = ball[2], ball[0]

print(str(int(ball.index('x'))+1))
