from ding_dong_props import *
font.init()


clock = time.Clock()
f_type = font.Font(None, 36)
text = f_type.render(str(winner) + ' поздравляем!!!', 1, IDK)

game = True
game_over = False

bg = transform.scale(image.load('xd.png'), WNDS_SIZE)
ball_s = transform.scale(image.load('squigglebob.png'), (50, 50))

left = stick('kanye_gaming.jpg', 2, 0, WNDS_SIZE[1] / 2)
right = stick('kanye_gaming.jpg', 2, WNDS_SIZE[0] - SPR_SIZE[0], WNDS_SIZE[1] / 2)
ball = gamesprite('squigglebob.png', 2, 250, 250)
ball.image = ball_s
while game:
    for ev in event.get():
        if ev.type == QUIT:
            game = False
    
    if not game_over:
        wnd.blit(bg, (0,0))
        left.update_pos('left')
        right.update_pos('right')
        winner = ball.move(left, right)
        left.render()
        right.render()
        ball.render()
        if winner == 1 or winner == 2:
            game_over = True

    if game and game_over:
        wnd.blit(bg, (0,0))
        wnd.blit(text, (250, 250))
        text = f_type.render(str(winner) + '-ый (ой) поздравляем!!!', True, IDK)
    
    clock.tick(60)
    display.update()