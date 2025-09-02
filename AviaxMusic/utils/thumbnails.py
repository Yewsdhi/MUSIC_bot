import os
import random
import aiofiles
import aiohttp
from PIL import Image, ImageDraw, ImageEnhance, ImageFilter, ImageFont
from youtubesearchpython.__future__ import VideosSearch
from config import FAILED

# Constants
CACHE_DIR = "cache"
os.makedirs(CACHE_DIR, exist_ok=True)

# Main image dimensions
IMG_WIDTH, IMG_HEIGHT = 1280, 720

# Panel settings
PANEL_W, PANEL_H = 900, 600
PANEL_X = (IMG_WIDTH - PANEL_W) // 2
PANEL_Y = (IMG_HEIGHT - PANEL_H) // 2
PANEL_TRANSPARENCY = 70
PANEL_CORNER_RADIUS = 40

# Thumbnail settings
THUMB_SIZE = 320
THUMB_X = PANEL_X + 50
THUMB_Y = PANEL_Y + 80
THUMB_CORNER_RADIUS = 20

# Text settings
TEXT_X = THUMB_X + THUMB_SIZE + 40
TEXT_Y = THUMB_Y + 20
TITLE_WIDTH = PANEL_W - TEXT_X - 40

TITLE_FONT_PATH = "VeGa/assets/thumb/font2.ttf"
REGULAR_FONT_PATH = "VeGa/assets/thumb/font.ttf"

TITLE_FONT_SIZE = 50
ARTIST_FONT_SIZE = 28

# Progress bar
BAR_WIDTH = PANEL_W - 100
BAR_HEIGHT = 4
BAR_X = PANEL_X + 50
BAR_Y = PANEL_Y + PANEL_H - 150
PROGRESS = 0.35
PROGRESS_COLOR = "#FA233B"  # Apple Music red

# Controls
CONTROLS_SIZE = 70
CONTROLS_SPACING = 120
CONTROLS_Y = BAR_Y + 60

async def get_thumb(videoid: str) -> str:
    cache_path = os.path.join(CACHE_DIR, f"{videoid}_apple.png")
    if os.path.exists(cache_path):
        return cache_path

    # YouTube video data fetch
    results = VideosSearch(f"https://www.youtube.com/watch?v={videoid}", limit=1)
    try:
        results_data = await results.next()
        result_items = results_data.get("result", [])
        if not result_items:
            raise ValueError("No results found.")
        data = result_items[0]
        thumbnail = data.get("thumbnails", [{}])[0].get("url", FAILED)
        duration = data.get("duration")
        channel = data.get("channel", {}).get("name", "Unknown Artist")
        title = data.get("title", "Unknown Title")
    except Exception:
        thumbnail, duration, channel, title = FAILED, None, "Unknown Artist", "Unknown Title"

    is_live = not duration or str(duration).strip().lower() in {"", "live", "live now"}
    duration_text = "Live" if is_live else duration or "Unknown"

    # Download thumbnail
    thumb_path = os.path.join(CACHE_DIR, f"thumb_{videoid}.jpg")
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(thumbnail) as resp:
                if resp.status == 200:
                    async with aiofiles.open(thumb_path, "wb") as f:
                        await f.write(await resp.read())
    except Exception:
        return FAILED

    # Create blurred background
    base = Image.open(thumb_path).resize((IMG_WIDTH, IMG_HEIGHT)).convert("RGBA")
    blurred_bg = base.filter(ImageFilter.GaussianBlur(20))
    darkened_bg = ImageEnhance.Brightness(blurred_bg).enhance(0.5)

    # Frosted glass panel
    panel_area = darkened_bg.crop((PANEL_X, PANEL_Y, PANEL_X + PANEL_W, PANEL_Y + PANEL_H))
    overlay = Image.new("RGBA", (PANEL_W, PANEL_H), (255, 255, 255, PANEL_TRANSPARENCY))
    frosted = Image.alpha_composite(panel_area, overlay)

    mask = Image.new("L", (PANEL_W, PANEL_H), 0)
    draw_mask = ImageDraw.Draw(mask)
    draw_mask.rounded_rectangle((0, 0, PANEL_W, PANEL_H), radius=PANEL_CORNER_RADIUS, fill=255)
    darkened_bg.paste(frosted, (PANEL_X, PANEL_Y), mask)

    draw = ImageDraw.Draw(darkened_bg)

    # Album art
    thumb = Image.open(thumb_path).resize((THUMB_SIZE, THUMB_SIZE))
    thumb_mask = Image.new("L", (THUMB_SIZE, THUMB_SIZE), 0)
    thumb_draw = ImageDraw.Draw(thumb_mask)
    thumb_draw.rounded_rectangle((0, 0, THUMB_SIZE, THUMB_SIZE), radius=THUMB_CORNER_RADIUS, fill=255)
    darkened_bg.paste(thumb, (THUMB_X, THUMB_Y), thumb_mask)

    # Load fonts
    try:
        title_font = ImageFont.truetype(TITLE_FONT_PATH, TITLE_FONT_SIZE)
        artist_font = ImageFont.truetype(REGULAR_FONT_PATH, ARTIST_FONT_SIZE)
    except:
        title_font = ImageFont.load_default()
        artist_font = ImageFont.load_default()

    # Text
    title = trim_to_width(title, title_font, TITLE_WIDTH)
    draw.text((TEXT_X, TEXT_Y), "Now Playing", fill="#AAAAAA", font=artist_font)
    draw.text((TEXT_X, TEXT_Y + 40), title, fill="white", font=title_font)
    draw.text((TEXT_X, TEXT_Y + 120), channel, fill="#CCCCCC", font=artist_font)

    # Progress bar
    progress_width = int(BAR_WIDTH * PROGRESS)
    draw.rounded_rectangle([(BAR_X, BAR_Y), (BAR_X + BAR_WIDTH, BAR_Y + BAR_HEIGHT)],
                           radius=BAR_HEIGHT//2, fill="#666666")
    draw.rounded_rectangle([(BAR_X, BAR_Y), (BAR_X + progress_width, BAR_Y + BAR_HEIGHT)],
                           radius=BAR_HEIGHT//2, fill=PROGRESS_COLOR)

    # Time
    draw.text((BAR_X, BAR_Y + 10), "0:00", fill="white", font=artist_font)
    draw.text((BAR_X + BAR_WIDTH - artist_font.getlength(duration_text), BAR_Y + 10),
              duration_text, fill="white", font=artist_font)

    # Controls
    symbols = ["⏮", "▶", "⏭"]
    for i, symbol in enumerate(symbols):
        cx = PANEL_X + (PANEL_W // 2) - CONTROLS_SIZE - CONTROLS_SPACING + i * (CONTROLS_SPACING)
        cy = CONTROLS_Y
        draw.ellipse([(cx, cy), (cx + CONTROLS_SIZE, cy + CONTROLS_SIZE)], fill="white")
        draw.text((cx + CONTROLS_SIZE//2 - 15, cy + CONTROLS_SIZE//2 - 20),
                  symbol, fill="#222222", font=title_font)

    darkened_bg.save(cache_path)
    return cache_path

def trim_to_width(text: str, font: ImageFont.FreeTypeFont, max_w: int) -> str:
    ellipsis = "…"
    if font.getlength(text) <= max_w:
        return text
    for i in range(len(text) - 1, 0, -1):
        if font.getlength(text[:i] + ellipsis) <= max_w:
            return text[:i] + ellipsis
    return ellipsis
