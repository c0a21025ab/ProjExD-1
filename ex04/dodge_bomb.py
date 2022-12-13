import pygame as pg
import sys
import random
import time


def check_bound(obj_rct, scr_rct):
    # 第一引数　こうかとｎrectまたは爆弾rect
    # 第二引数　スクリーンrect
    #　範囲内：+1/範囲外：-1
    yoko, tate = +1, +1
    if obj_rct.left < scr_rct.left or scr_rct.right < obj_rct.right:
        yoko = -1
    if obj_rct.top < scr_rct.top or scr_rct.bottom < obj_rct.bottom:
        tate = -1
    return yoko, tate


def main():
    bgn = time.time()
    clock = pg.time.Clock()

    mode_2bomb = False # 爆弾２個モード変数


    pg.display.set_caption("逃げろ！こうかとん")
    scrn_sfc = pg.display.set_mode((1600,900))
    scrn_rct = scrn_sfc.get_rect()
    pgbg_sfc = pg.image.load("fig/pg_bg.jpg")
    pgbg_rct = pgbg_sfc.get_rect()

    # (new)着弾時切り替え用の画像サーフェイスの作成
    end_sfc = pg.image.load("fig/bakuhatu.png")
    end_sfc = pg.transform.rotozoom(end_sfc, 0, 2.0)
    end_sfc = pg.transform.scale(end_sfc, (500, 500)) # 画像を縮小
    end_rct = end_sfc.get_rect()
    end_rct.center = 900, 400
    ##


    tori_sfc = pg.image.load("fig/6.png")
    tori_sfc = pg.transform.rotozoom(tori_sfc, 0, 2.0)
    tori_rct = tori_sfc.get_rect()
    tori_rct.center = 900, 400
    scrn_sfc.blit(tori_sfc, tori_rct)

    bomb_sfc = pg.Surface((20,20))
    bomb_sfc.set_colorkey((0,0,0))
    pg.draw.circle(bomb_sfc, (255, 0, 0,), (10, 10), 10)
    bomb_rct = bomb_sfc.get_rect()
    bomb_rct.centerx = random.randint(0, scrn_rct.width)
    bomb_rct.centery = random.randint(0, scrn_rct.height)
    scrn_sfc.blit(bomb_sfc, bomb_rct)

    # (new)爆弾ふやす
    bomb2_sfc = pg.Surface((20,20))
    bomb2_sfc.set_colorkey((0,0,0))
    pg.draw.circle(bomb2_sfc, (255, 0, 0,), (10, 10), 10)
    bomb2_rct = bomb_sfc.get_rect()
    bomb2_rct.centerx = random.randint(0, scrn_rct.width)
    bomb2_rct.centery = random.randint(0, scrn_rct.height)
    ##



    vx, vy = +1, +1
    vx2, vy2 = +1, +1

    while True:
        scrn_sfc.blit(pgbg_sfc, pgbg_rct)
        for event in pg.event.get():
            if event.type == pg.QUIT:
                return

        key_dct = pg.key.get_pressed() #辞書型
        if key_dct[pg.K_UP]:
            tori_rct.centery -= 1
        if key_dct[pg.K_DOWN]:
            tori_rct.centery += 1
        if key_dct[pg.K_LEFT]:
            tori_rct.centerx -= 1
        if key_dct[pg.K_RIGHT]:
            tori_rct.centerx += 1
        if check_bound(tori_rct, scrn_rct) != (+1, +1):
            # どこかしらはみ出ていたら
            if key_dct[pg.K_UP]:
                tori_rct.centery += 1
            if key_dct[pg.K_DOWN]:
                tori_rct.centery -= 1
            if key_dct[pg.K_LEFT]:
                tori_rct.centerx += 1
            if key_dct[pg.K_RIGHT]:
                tori_rct.centerx -= 1

        # キー入力によるモード切り替え
        if key_dct[pg.K_2]:
            mode_2bomb = True
        if key_dct[pg.K_1]:
            mode_2bomb = False
        
        scrn_sfc.blit(tori_sfc, tori_rct)
        bomb_rct.move_ip(vx, vy)
        scrn_sfc.blit(bomb_sfc, bomb_rct)
        
        yoko, tate = check_bound(bomb_rct, scrn_rct)
        vx *= yoko
        vy *= tate
        # (new)キー２が入力されたときに爆弾を二つに増やす
        if mode_2bomb:
            scrn_sfc.blit(bomb2_sfc, bomb2_rct)
            bomb2_rct.move_ip(vx2, vy2)
            yoko, tate = check_bound(bomb2_rct, scrn_rct)
            vx2 *= yoko
            vy2 *= tate
        ##

        if tori_rct.colliderect(bomb_rct) or (tori_rct.colliderect(bomb2_rct) and mode_2bomb):
            # (new)こうかとんが爆弾に触れた位置で画像を切り替える
            end_rct.centerx = tori_rct.centerx # こうかとんの位置と等しくする
            end_rct.centery = tori_rct.centery
            scrn_sfc.blit(end_sfc, end_rct)
            ##

            # (new)こうかとんが爆弾に触れるとGAME OVER と表示させる
            font = pg.font.Font(None, 200)
            text = font.render("GAME OVER", True, (255,0,0))
            scrn_sfc.blit(text, [400, 400])

            # (new)経過時間表示
            font = pg.font.Font(None, 100)
            end = time.time()
            ever_time = end - bgn
            time_text = font.render(f"time:{round(ever_time)} ", True, (255,0,0))
            scrn_sfc.blit(time_text, [0, 0])

            pg.display.update()
            time.sleep(3) #　画像切り替え3秒後にウィンドウを閉じる
            ##
            return
        
       

        pg.display.update()
        clock.tick(1000)



    


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()