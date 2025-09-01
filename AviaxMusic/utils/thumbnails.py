import os
import re
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
PANEL_TRANSPARENCY = 50
PANEL_CORNER_RADIUS = 30

# Thumbnail settings
THUMB_SIZE = 280
THUMB_X = PANEL_X + 40
THUMB_Y = PANEL_Y + 40
THUMB_CORNER_RADIUS = 15

# Text settings next to thumbnail
TEXT_X = THUMB_X + THUMB_SIZE + 30
TEXT_Y = THUMB_Y + 20
TITLE_WIDTH = PANEL_W - TEXT_X - 40

# Metadata settings
META_Y = TEXT_Y + 80
META_FONT_SIZE = 24
META_SPACING = 30

# Vega title settings
VEGA_TITLE_Y = META_Y + META_SPACING + 30
VEGA_TITLE_FONT_SIZE = 30

# Progress bar settings
BAR_WIDTH = PANEL_W - 100
BAR_HEIGHT = 8
BAR_X = PANEL_X + 50
BAR_Y = THUMB_Y + THUMB_SIZE + 40
PROGRESS = 0.5

# Volume bar settings
VOLUME_BAR_WIDTH = 100
VOLUME_BAR_HEIGHT = 4
VOLUME_BAR_X = PANEL_X + PANEL_W - VOLUME_BAR_WIDTH - 150
VOLUME_BAR_Y = BAR_Y + 30
VOLUME_LEVEL = 0.7

# Controls settings
CONTROLS_WIDTH = BAR_WIDTH + 50
CONTROLS_HEIGHT = 60
CONTROLS_X = BAR_X - 15
CONTROLS_Y = BAR_Y + BAR_HEIGHT + 55

# New image settings
NEW_IMG_PATH = "VeGa/assets/ee.png"
NEW_IMG_WIDTH = 320
NEW_IMG_HEIGHT = 80
NEW_IMG_X = CONTROLS_X + (CONTROLS_WIDTH - NEW_IMG_WIDTH) // 2
NEW_IMG_Y = CONTROLS_Y + CONTROLS_HEIGHT + 15

EXTRA_IMG_PATH = "VeGa/assets/ggg.png"
EXTRA_IMG_WIDTH = 100
EXTRA_IMG_HEIGHT = 115
EXTRA_IMG_X = PANEL_X + PANEL_W - EXTRA_IMG_WIDTH - 40
EXTRA_IMG_Y = PANEL_Y + 40

# Font paths
TITLE_FONT_PATH = "VeGa/assets/thumb/font2.ttf"
REGULAR_FONT_PATH = "VeGa/assets/thumb/font.ttf"

# Border colors
BORDER_COLORS = [
    "#FF0000", "#CD5C5C", "#DC143C", "#FF6347", "#FF4500", "#FF69B4", "#FF1493",
    "#0000FF", "#1E90FF", "#4169E1", "#4682B4", "#00BFFF", "#87CEEB", "#7FFFD4",
    "#00FF00", "#32CD32", "#006400", "#2E8B57", "#3CB371", "#90EE90", "#98FB98",
    "#FFFF00", "#FFD700", "#FFA500", "#FF8C00", "#FFDAB9", "#F0E68C",
    "#800080", "#9932CC", "#8A2BE2", "#9370DB", "#FFC0CB", "#DB7093", "#C71585",
    "#FFFFFF", "#F5F5F5", "#DCDCDC", "#A9A9A9", "#696969", "#000000",
    "#FF00FF", "#00FFFF", "#40E0D0", "#4B0082", "#FFD700", "#C0C0C0", "#B8860B",
]

async def get_thumb(videoid: str) -> str:
    cache_path = os.path.join(CACHE_DIR, f"{videoid}_custom.png")
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
        views = data.get("viewCount", {}).get("short", "Unknown Views")
        channel = data.get("channel", {}).get("name", "Unknown Channel")
        title = data.get("title", "Unknown Title")
    except Exception:
        thumbnail, duration, views, channel, title = FAILED, None, "Unknown Views", "Unknown Channel", "Unknown Title"

    is_live = not duration or str(duration).strip().lower() in {"", "live", "live now"}
    duration_text = "Live" if is_live else duration or "Unknown Duration"

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

    # Create base image with blurred background
    base = Image.open(thumb_path).resize((IMG_WIDTH, IMG_HEIGHT)).convert("RGBA")
    blurred_bg = base.filter(ImageFilter.GaussianBlur(15))
    darkened_bg = ImageEnhance.Brightness(blurred_bg).enhance(0.7)

    # Create frosted glass panel with random colored border
    panel_area = darkened_bg.crop((PANEL_X, PANEL_Y, PANEL_X + PANEL_W, PANEL_Y + PANEL_H))
    overlay = Image.new("RGBA", (PANEL_W, PANEL_H), (255, 255, 255, PANEL_TRANSPARENCY))
    frosted = Image.alpha_composite(panel_area, overlay)
    
    # Create mask for rounded corners
    mask = Image.new("L", (PANEL_W, PANEL_H), 0)
    draw_mask = ImageDraw.Draw(mask)
    draw_mask.rounded_rectangle((0, 0, PANEL_W, PANEL_H), radius=PANEL_CORNER_RADIUS, fill=255)
    
    # Paste the frosted panel onto the background
    darkened_bg.paste(frosted, (PANEL_X, PANEL_Y), mask)

    # Add colored border to panel
    border_draw = ImageDraw.Draw(darkened_bg)
    border_color = random.choice(BORDER_COLORS)
    border_draw.rounded_rectangle(
        [(PANEL_X - 5, PANEL_Y - 5), (PANEL_X + PANEL_W + 5, PANEL_Y + PANEL_H + 5)],
        radius=PANEL_CORNER_RADIUS + 5,
        outline=border_color,
        width=5
    )

    # Add thumbnail with rounded corners
    thumb = Image.open(thumb_path).resize((THUMB_SIZE, THUMB_SIZE))
    thumb_mask = Image.new("L", (THUMB_SIZE, THUMB_SIZE), 0)
    thumb_draw = ImageDraw.Draw(thumb_mask)
    thumb_draw.rounded_rectangle((0, 0, THUMB_SIZE, THUMB_SIZE), radius=THUMB_CORNER_RADIUS, fill=255)
    darkened_bg.paste(thumb, (THUMB_X, THUMB_Y), thumb_mask)

    # Add white border around thumbnail
    border_draw.rounded_rectangle(
        [(THUMB_X - 2, THUMB_Y - 2), (THUMB_X + THUMB_SIZE + 2, THUMB_Y + THUMB_SIZE + 2)],
        radius=THUMB_CORNER_RADIUS,
        outline="white",
        width=2
    )

    # Load fonts
    try:
        title_font = ImageFont.truetype(TITLE_FONT_PATH, 42)
        meta_font = ImageFont.truetype(REGULAR_FONT_PATH, META_FONT_SIZE)
        vega_font = ImageFont.truetype(REGULAR_FONT_PATH, VEGA_TITLE_FONT_SIZE)
    except:
        title_font = ImageFont.load_default()
        title_font.size = 42
        meta_font = ImageFont.load_default()
        meta_font.size = META_FONT_SIZE
        vega_font = ImageFont.load_default()
        vega_font.size = VEGA_TITLE_FONT_SIZE

    # Draw title next to thumbnail
    title = trim_to_width(title, title_font, TITLE_WIDTH)
    border_draw.text((TEXT_X, TEXT_Y), title, fill="white", font=title_font)

    # Draw metadata
    border_draw.text((TEXT_X, META_Y), channel, fill="#cccccc", font=meta_font)
    border_draw.text((TEXT_X, META_Y + META_SPACING), 
                    f"Spotify | {views}", fill="white", font=meta_font)

    # Draw Vega title
    vega_title = "VEGA I MUSIC"
    border_draw.text((TEXT_X, VEGA_TITLE_Y), vega_title, fill="white", font=vega_font)

    # Draw progress bar
    progress_width = int(BAR_WIDTH * PROGRESS)
    border_draw.rounded_rectangle(
        [(BAR_X, BAR_Y), (BAR_X + BAR_WIDTH, BAR_Y + BAR_HEIGHT)],
        radius=BAR_HEIGHT//2,
        fill="#555555"
    )
    border_draw.rounded_rectangle(
        [(BAR_X, BAR_Y), (BAR_X + progress_width, BAR_Y + BAR_HEIGHT)],
        radius=BAR_HEIGHT//2,
        fill="white"
    )
    
    # Draw progress time
    current_time = "00:00"
    total_time = duration_text if not is_live else "Live"
    border_draw.text((BAR_X, BAR_Y + BAR_HEIGHT + 10), current_time, fill="white", font=meta_font)
    border_draw.text((BAR_X + BAR_WIDTH - meta_font.getlength(total_time), BAR_Y + BAR_HEIGHT + 10), 
                    total_time, fill="white", font=meta_font)

    # Add controls (play/pause buttons)
    try:
        controls_img = Image.open("VeGa/assets/icons.png").resize(
            (CONTROLS_WIDTH, CONTROLS_HEIGHT)).convert("RGBA")
        darkened_bg.paste(controls_img, (CONTROLS_X, CONTROLS_Y), controls_img)
    except:
        pass

    # Add new image below controls
    try:
        new_img = Image.open(NEW_IMG_PATH).resize(
            (NEW_IMG_WIDTH, NEW_IMG_HEIGHT)).convert("RGBA")
        darkened_bg.paste(new_img, (NEW_IMG_X, NEW_IMG_Y), new_img)
    except:
        pass

    try:
        extra_img = Image.open(EXTRA_IMG_PATH).resize(
            (EXTRA_IMG_WIDTH, EXTRA_IMG_HEIGHT)).convert("RGBA")
        darkened_bg.paste(extra_img, (EXTRA_IMG_X, EXTRA_IMG_Y), extra_img)
    except:
        pass

    darkened_bg.save(cache_path)
    return cache_path

def trim_to_width(text: str, font: ImageFont.FreeTypeFont, max_w: int) -> str:
    ellipsis = "ـ"
    if font.getlength(text) <= max_w:
        return text
    for i in range(len(text) - 1, 0, -1):
        if font.getlength(text[:i] + ellipsis) <= max_w:
            return text[:i] + ellipsis
    return ellipsis