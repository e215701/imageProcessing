import cv2

# 画像を読み込む
image = cv2.imread('./../photo/p3.jpeg')

# 画像を３カケル３のモザイクタイルに分割
tile_size = (image.shape[1] // 3, image.shape[0] // 3)

# タイルのリストを作成
tiles = []
for y in range(3):
    for x in range(3):
        tile = image[y * tile_size[1]: (y + 1) * tile_size[1], x * tile_size[0]: (x + 1) * tile_size[0]]
        tiles.append(tile)

# 順番に反転
for i, tile in enumerate(tiles):
    # タイルを左右反転
    flipped_tile = cv2.flip(tile, 1)

    # 反転したタイルを表示
    cv2.imshow('Flipped Tile', flipped_tile)
    cv2.waitKey(5000)

# 全てのウィンドウを閉じる
cv2.destroyAllWindows()
