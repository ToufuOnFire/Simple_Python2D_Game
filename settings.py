import os

# ウインドウの横幅
WIDTH = 1024
# ウインドウの高さ
HEIGHT = 768
# FPS(Frames Per Second)
FPS = 60#← youtube版はなくてもいいかもね
# タイトル
TITLE = "TOUFU"
# 重力
GRAVITY = 1
# ジャンプ力
JUMP_POWER = -18
# 背景色 RGB 0から255
BG_COLOR = (75, 10, 243)
# テキストカラー
TEXT_COLOR = (255, 255, 255)
# フォント
TEXT_FONT = None
# グリッドのラインカラー
GRID_COLOR = (200, 200, 200)
# ディレクトリを設定
BASE_DIR = os.path.dirname(__file__)
# 画像のディレクトリを設定
IMG_DIR = os.path.join(BASE_DIR, "imgs")
# サウンドのディレクトリを設定
SOUND_DIR = os.path.join(BASE_DIR, "sound")
# ゲームオーバーBGM
GAMEOVER_BGM = "maou_se_8bit21_gameover.mp3"
# ゲームクリアBGM
GAMECLEAR_BGM = "maou_game_jingle01_stageclear.mp3"
# プレイヤー用のスプライトシートのディレクトリを指定
PLAYER_SPRITESHEET_DIR = os.path.join(IMG_DIR, "toufu_chan2.png")
# ブロック用のスプライトシートのディレクトリを指定
BLOCK_SPRITESHEET_DIR = os.path.join(IMG_DIR, "tiles_spritesheet.png")
# 敵のスプライトシートのディレクトリを指定
ENEMY_SPRITESHEET_DIR = os.path.join(IMG_DIR, "spritesheet_jumper.png")
# オブジェクトサイズ
OBJECT_SIZE = 32
# プレイヤー横幅
PLAYER_WIDTH = 32
# プレイヤー縦幅
PLAYER_HEIGHT = int(PLAYER_WIDTH * 1.45)
# プレイヤースピード
SPEED = 10