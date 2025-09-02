from PIL import Image, ImageDraw, ImageFont, ImageFilter, ImageEnhance

# Canvas size
WIDTH, HEIGHT = 1280, 720

# Base gradient background
base = Image.new("RGB", (WIDTH, HEIGHT), (20, 20, 20))
draw = ImageDraw.Draw(base)

# Gradient
for y in range(HEIGHT):
    shade = int(20 + (y / HEIGHT) * 40)
    draw.line([(0, y), (WIDTH, y)], fill=(shade, shade, shade))

# Blur + dark
bg = base.filter(ImageFilter.GaussianBlur(25))
bg = ImageEnhance.Brightness(bg).enhance(0.6)
draw = ImageDraw.Draw(bg)

# Frosted panel
PANEL_W, PANEL_H = 900, 600
PANEL_X = (WIDTH - PANEL_W) // 2
PANEL_Y = (HEIGHT - PANEL_H) // 2
PANEL_TRANSPARENCY = 70
PANEL_CORNER_RADIUS = 40

panel = Image.new("RGBA", (PANEL_W, PANEL_H), (255, 255, 255, PANEL_TRANSPARENCY))
mask = Image.new("L", (PANEL_W, PANEL_H), 0)
mask_draw = ImageDraw.Draw(mask)
mask_draw.rounded_rectangle((0, 0, PANEL_W, PANEL_H), radius=PANEL_CORNER_RADIUS, fill=255)
bg.paste(panel, (PANEL_X, PANEL_Y), mask)

draw = ImageDraw.Draw(bg)

# Fonts
try:
    title_font = ImageFont.truetype("arial.ttf", 50)
    artist_font = ImageFont.truetype("arial.ttf", 28)
except:
    title_font = ImageFont.load_default()
    artist_font = ImageFont.load_default()

# Text
draw.text((PANEL_X + 400, PANEL_Y + 40), "Now Playing", fill="#AAAAAA", font=artist_font)
draw.text((PANEL_X + 400, PANEL_Y + 80), "No Song Available", fill="white", font=title_font)
draw.text((PANEL_X + 400, PANEL_Y + 150), "Apple Music Style", fill="#CCCCCC", font=artist_font)

# Progress bar
BAR_WIDTH = PANEL_W - 100
BAR_HEIGHT = 4
BAR_X = PANEL_X + 50
BAR_Y = PANEL_Y + PANEL_H - 150
draw.rounded_rectangle([(BAR_X, BAR_Y), (BAR_X + BAR_WIDTH, BAR_Y + BAR_HEIGHT)],
                       radius=BAR_HEIGHT//2, fill="#666666")
draw.rounded_rectangle([(BAR_X, BAR_Y), (BAR_X + BAR_WIDTH//3, BAR_Y + BAR_HEIGHT)],
                       radius=BAR_HEIGHT//2, fill="#FA233B")

# Time text
draw.text((BAR_X, BAR_Y + 10), "0:00", fill="white", font=artist_font)
draw.text((BAR_X + BAR_WIDTH - 60, BAR_Y + 10), "--:--", fill="white", font=artist_font)

# Controls (Shapes instead of unicode)
CONTROLS_SIZE = 70
CONTROLS_SPACING = 120
CONTROLS_Y = BAR_Y + 60

# Previous (triangle left)
cx = PANEL_X + (PANEL_W // 2) - CONTROLS_SIZE - CONTROLS_SPACING
cy = CONTROLS_Y
draw.ellipse([(cx, cy), (cx + CONTROLS_SIZE, cy + CONTROLS_SIZE)], fill="white")
draw.polygon([(cx+45, cy+20), (cx+25, cy+35), (cx+45, cy+50)], fill="#222222")

# Play (triangle right)
cx = PANEL_X + (PANEL_W // 2)
cy = CONTROLS_Y
draw.ellipse([(cx, cy), (cx + CONTROLS_SIZE, cy + CONTROLS_SIZE)], fill="white")
draw.polygon([(cx+25, cy+20), (cx+25, cy+50), (cx+50, cy+35)], fill="#222222")

# Next (triangle right)
cx = PANEL_X + (PANEL_W // 2) + CONTROLS_SPACING
cy = CONTROLS_Y
draw.ellipse([(cx, cy), (cx + CONTROLS_SIZE, cy + CONTROLS_SIZE)], fill="white")
draw.polygon([(cx+25, cy+20), (cx+25, cy+50), (cx+50, cy+35)], fill="#222222")

# Save
path = "/mnt/data/failed_apple.png"
bg.save(path)
print("Saved at:", path)
