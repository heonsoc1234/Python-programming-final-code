import pygame
import sys
import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))

pygame.init()

#화면 설정
WIDTH = 1000
HEIGHT = 700
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

#이미지
start_background = pygame.image.load("start_background.png").convert()
background = pygame.image.load("background.png").convert()

q1_background = pygame.image.load("Q1.png").convert()
q2_background = pygame.image.load("Q2.png").convert()
q3_background = pygame.image.load("Q3.png").convert()

q1_question = pygame.image.load("Q1_Q.png").convert_alpha()
q2_question = pygame.image.load("Q2_Q.png").convert_alpha()
q3_question = pygame.image.load("Q3_Q.png").convert_alpha()

original_e = pygame.image.load("e.png").convert_alpha()
original_g = pygame.image.load("g.png").convert_alpha()
original_b = pygame.image.load("b.png").convert_alpha()

#e,b,g png 크기 키우는 코드
e_img = pygame.transform.scale(original_e, (int(original_e.get_width() * 1.5), int(original_e.get_height() * 1.5)))
g_img = pygame.transform.scale(original_g, (int(original_g.get_width() * 1.5), int(original_g.get_height() * 1.5)))
b_img = pygame.transform.scale(original_b, (int(original_b.get_width() * 1.5), int(original_b.get_height() * 1.5)))

#결과 화면 이미지
end_img = pygame.image.load("end.png").convert_alpha()
end_clear_img = pygame.image.load("end_clear.png").convert_alpha()

#OX 퀴즈 버튼 이미지
o1_img = pygame.transform.scale(pygame.image.load("O1.png").convert_alpha(), (200, 200))
o2_img = pygame.transform.scale(pygame.image.load("O2.png").convert_alpha(), (200, 200))
x1_img = pygame.transform.scale(pygame.image.load("X1.png").convert_alpha(), (200, 200))
x2_img = pygame.transform.scale(pygame.image.load("X2.png").convert_alpha(), (200, 200))

#애니메이션용 캐릭터 이미지
player_up1 = pygame.transform.scale(pygame.image.load("up1.png").convert_alpha(), (64, 64))
player_up2 = pygame.transform.scale(pygame.image.load("up2.png").convert_alpha(), (64, 64))
player_up3 = pygame.transform.scale(pygame.image.load("up3.png").convert_alpha(), (64, 64))
player_up4 = pygame.transform.scale(pygame.image.load("up4.png").convert_alpha(), (64, 64))

player_down1 = pygame.transform.scale(pygame.image.load("down1.png").convert_alpha(), (64, 64))
player_down2 = pygame.transform.scale(pygame.image.load("down2.png").convert_alpha(), (64, 64))
player_down3 = pygame.transform.scale(pygame.image.load("down3.png").convert_alpha(), (64, 64))
player_down4 = pygame.transform.scale(pygame.image.load("down4.png").convert_alpha(), (64, 64))

player_left1 = pygame.transform.scale(pygame.image.load("left1.png").convert_alpha(), (64, 64))
player_left2 = pygame.transform.scale(pygame.image.load("left2.png").convert_alpha(), (64, 64))
player_left3 = pygame.transform.scale(pygame.image.load("left3.png").convert_alpha(), (64, 64))
player_left4 = pygame.transform.scale(pygame.image.load("left4.png").convert_alpha(), (64, 64))

player_right1 = pygame.transform.scale(pygame.image.load("right1.png").convert_alpha(), (64, 64))
player_right2 = pygame.transform.scale(pygame.image.load("right2.png").convert_alpha(), (64, 64))
player_right3 = pygame.transform.scale(pygame.image.load("right3.png").convert_alpha(), (64, 64))
player_right4 = pygame.transform.scale(pygame.image.load("right4.png").convert_alpha(), (64, 64))

current_player_image = player_down1

#게임 변수 설정
current_scene = "start"

player_x = 468
player_y = 318

camera_x = 500
camera_y = 482

speed = 5

q1_state = "ready"
q2_state = "ready"
q3_state = "ready"

q1_clear = False
q2_clear = False
q3_clear = False

# 애니메이션 타이머 변수
walk_count = 0

#구역 및 장애물 설정(상호작용 구역, 제한구역 등등)
rect1 = pygame.Rect(770, 300, 500, 80)     
rect2 = pygame.Rect(1250, 500, 230, 150)   
rect3 = pygame.Rect(500, 500, 230, 150)    
rect4 = pygame.Rect(880, 900, 230, 150)    

wall1 = pygame.Rect(895, 640, 220, 130)
wall2 = pygame.Rect(350, 800, 400, 80)

#메인 게임 루프
running = True
while running:
    
    all_quizzes_cleared = False
    if q1_clear == True and q2_clear == True and q3_clear == True:
        all_quizzes_cleared = True

    #이벤트 처리
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        if current_scene == "start":
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    current_scene = "main"
                    camera_x = 500         
                    camera_y = 482

        elif current_scene == "Q1":
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a: q1_state = "o_selected"
                elif event.key == pygame.K_d: q1_state = "x_selected"
                
                if event.key == pygame.K_SPACE:
                    if q1_state == "o_selected":
                        q1_clear = True
                        current_scene = "main"
                        camera_x = 500
                        camera_y = 482
                    elif q1_state == "x_selected":
                        current_scene = "game_over"
                
                if event.key == pygame.K_ESCAPE:
                    current_scene = "main"

        elif current_scene == "Q2":
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a: q2_state = "o_selected"
                elif event.key == pygame.K_d: q2_state = "x_selected"
                
                if event.key == pygame.K_SPACE:
                    if q2_state == "o_selected":
                        current_scene = "game_over"
                    elif q2_state == "x_selected":
                        q2_clear = True
                        current_scene = "main"
                        camera_x = 500
                        camera_y = 482
                
                if event.key == pygame.K_ESCAPE:
                    current_scene = "main"

        elif current_scene == "Q3":
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a: q3_state = "o_selected"
                elif event.key == pygame.K_d: q3_state = "x_selected"
                
                if event.key == pygame.K_SPACE:
                    if q3_state == "o_selected":
                        current_scene = "game_over"
                    elif q3_state == "x_selected":
                        q3_clear = True
                        current_scene = "main"
                        camera_x = 500
                        camera_y = 482
                
                if event.key == pygame.K_ESCAPE:
                    current_scene = "main"

        elif current_scene == "game_over" or current_scene == "game_clear":
            if event.type == pygame.KEYDOWN:
                running = False

    #키보드 상태 처리
    if current_scene == "main":
        keys = pygame.key.get_pressed()
        
        old_camera_x = camera_x
        old_camera_y = camera_y

        is_moving = False

        #애니메이션 반복
        if keys[pygame.K_w]:
            camera_y -= speed
            is_moving = True
            frame = (walk_count // 7) % 4
            if frame == 0: current_player_image = player_up1
            elif frame == 1: current_player_image = player_up2
            elif frame == 2: current_player_image = player_up3
            elif frame == 3: current_player_image = player_up4

        elif keys[pygame.K_s]:
            camera_y += speed
            is_moving = True
            frame = (walk_count // 7) % 4
            if frame == 0: current_player_image = player_down1
            elif frame == 1: current_player_image = player_down2
            elif frame == 2: current_player_image = player_down3
            elif frame == 3: current_player_image = player_down4

        elif keys[pygame.K_a]:
            camera_x -= speed
            is_moving = True
            frame = (walk_count // 7) % 4
            if frame == 0: current_player_image = player_left1
            elif frame == 1: current_player_image = player_left2
            elif frame == 2: current_player_image = player_left3
            elif frame == 3: current_player_image = player_left4

        elif keys[pygame.K_d]:
            camera_x += speed
            is_moving = True
            frame = (walk_count // 7) % 4
            if frame == 0: current_player_image = player_right1
            elif frame == 1: current_player_image = player_right2
            elif frame == 2: current_player_image = player_right3
            elif frame == 3: current_player_image = player_right4

        #캐릭터가 움직일 때만 프레임 타이머 가동
        if is_moving == True:
            walk_count += 1
        else:
            walk_count = 0

        #캐릭터 충돌 계산용 실제 월드 좌표 상자
        player_actual_rect = pygame.Rect(camera_x + player_x + 32, camera_y + player_y + 58, 1, 1)

        is_collided = False

        #사각형 벽 충돌
        if player_actual_rect.colliderect(wall1) or player_actual_rect.colliderect(wall2):
            is_collided = True

        #원형 벽 2개 충돌
        dist1 = (player_actual_rect.x - 500)**2 + (player_actual_rect.y - 1100)**2
        if dist1 <= 180**2:
            is_collided = True
            
        dist2 = (player_actual_rect.x - 1400)**2 + (player_actual_rect.y - 1000)**2
        if dist2 <= 150**2:
            is_collided = True

        #엔딩 구역 차단
        if all_quizzes_cleared == False:
            if player_actual_rect.colliderect(rect1):
                is_collided = True

        if is_collided == True:
            camera_x = old_camera_x
            camera_y = old_camera_y

        #이벤트 구역 상호작용
        if player_actual_rect.colliderect(rect1) and all_quizzes_cleared == True:
            current_scene = "game_clear"
        elif player_actual_rect.colliderect(rect2):
            current_scene = "Q1"
        elif player_actual_rect.colliderect(rect3):
            current_scene = "Q2"
        elif player_actual_rect.colliderect(rect4):
            current_scene = "Q3"

        #카메라 고정
        if camera_x < 0: camera_x = 0
        if camera_x > 1000: camera_x = 1000
        if camera_y < 0: camera_y = 0
        if camera_y > 800: camera_y = 800

    #화면 그리기
    if current_scene == "start":
        screen.blit(start_background, (0, 0))

    elif current_scene == "main":
        screen.blit(background, (-camera_x, -camera_y))
        screen.blit(current_player_image, (player_x, player_y))

    elif current_scene in ["Q1", "Q2", "Q3"]:
        if current_scene == "Q1":
            screen.blit(q1_background, (0, 0))
            q_x = 500 - (q1_question.get_width() // 2)
            screen.blit(q1_question, (q_x, 80))
            alpha_x = 500 - (e_img.get_width() // 2)
            alpha_y = 450 - (e_img.get_height() // 2)
            screen.blit(e_img, (alpha_x, alpha_y)) 
            active_state = q1_state
        elif current_scene == "Q2":
            screen.blit(q2_background, (0, 0))
            q_x = 500 - (q2_question.get_width() // 2)
            screen.blit(q2_question, (q_x, 80))
            alpha_x = 500 - (g_img.get_width() // 2)
            alpha_y = 450 - (g_img.get_height() // 2)
            screen.blit(g_img, (alpha_x, alpha_y)) 
            active_state = q2_state
        elif current_scene == "Q3":
            screen.blit(q3_background, (0, 0))
            q_x = 500 - (q3_question.get_width() // 2)
            screen.blit(q3_question, (q_x, 80))
            alpha_x = 500 - (b_img.get_width() // 2)
            alpha_y = 450 - (b_img.get_height() // 2)
            screen.blit(b_img, (alpha_x, alpha_y)) 
            active_state = q3_state

        #OX 버튼 그리기
        button_o = o1_img
        button_x = x1_img
        if active_state == "o_selected":
            button_o = o2_img
        elif active_state == "x_selected":
            button_x = x2_img

        screen.blit(button_o, (150, 480))
        screen.blit(button_x, (650, 480))

    #게임 오버 화면 중앙에 고정
    elif current_scene == "game_over":
        screen.fill((0, 0, 0))
        over_x = 500 - (end_img.get_width() // 2)
        over_y = 350 - (end_img.get_height() // 2)
        screen.blit(end_img, (over_x, over_y))

    #게임 클리어 화면 중앙에 고정
    elif current_scene == "game_clear":
        screen.fill((0, 0, 0))
        clear_x = 500 - (end_clear_img.get_width() // 2)
        clear_y = 350 - (end_clear_img.get_height() // 2)
        screen.blit(end_clear_img, (clear_x, clear_y))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()