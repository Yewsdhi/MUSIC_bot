<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8" />
<meta name="viewport" content="width=device-width,initial-scale=1" />
<title>Music Thumbnail Card</title>
<link href="https://fonts.googleapis.com/css2?family=Poppins:wght@400;600&family=Great+Vibes&display=swap" rel="stylesheet">
<style>
  :root{
    --bg:#eef0f4;
    --card:#ffffff;
    --text:#222;
    --muted:#9aa3b2;
    --accent:#7c4dff;       /* left */
    --accent-2:#c084fc;     /* right */
    --radius:22px;
    --shadow: 0 18px 40px rgba(0,0,0,.15), 0 2px 6px rgba(0,0,0,.08);
  }
  *{box-sizing:border-box}
  body{
    margin:0;
    min-height:100dvh;
    display:grid;
    place-items:center;
    background:
      radial-gradient(60% 60% at 50% 0%, rgba(0,0,0,.06), transparent 60%) ,
      var(--bg);
    font-family: Poppins, system-ui, -apple-system, Segoe UI, Roboto, Arial, sans-serif;
  }

  .card{
    width:min(92vw, 360px);
    background:var(--card);
    border-radius:var(--radius);
    box-shadow:var(--shadow);
    overflow:hidden;
    position:relative;
  }

  .cover{
    height:180px;
    background:url("https://images.unsplash.com/photo-1503342394128-c104d54dba01?q=80&w=1200&auto=format&fit=crop") center/cover no-repeat;
    border-top-left-radius:var(--radius);
    border-top-right-radius:var(--radius);
  }

  .body{
    padding:18px 20px 22px;
  }

  .title{
    text-align:center;
    font-family:"Great Vibes", cursive;
    font-size:34px;
    line-height:1;
    color:#000;
    text-shadow:0 3px 10px rgba(0,0,0,.15);
    margin:8px 0 18px;
  }

  /* progress */
  .bar-wrap{
    height:10px;
    border-radius:999px;
    background:linear-gradient(90deg, rgba(0,0,0,.06) 0 100%);
    position:relative;
    overflow:hidden;
    margin:0 auto 22px;
    width:82%;
  }
  .bar{
    position:absolute; inset:0;
    --p: 38%; /* progress % */
    background:
      linear-gradient(90deg, var(--accent), var(--accent-2)) 0/var(--p) 100% no-repeat,
      linear-gradient(#e6e9ef,#e6e9ef);
  }

  /* controls */
  .controls{
    display:flex; align-items:center; justify-content:center; gap:28px;
    margin:8px 0 4px;
  }
  .btn{
    width:44px; height:44px; display:grid; place-items:center;
    border:none; background:transparent; cursor:pointer;
    transition:transform .14s ease;
  }
  .btn:active{ transform:scale(.96) }

  .play{
    width:60px; height:60px; border-radius:50%;
    background:#111; color:#fff;
    box-shadow:0 10px 18px rgba(0,0,0,.25);
  }
  .meta{
    text-align:center;
    font-size:13px; color:var(--muted);
    margin-top:8px;
  }

  /* subtle top highlight like the mockup */
  .glow{
    position:absolute; inset:0;
    pointer-events:none;
    background:
      radial-gradient(120px 38px at 50% 180px, rgba(0,0,0,.18), transparent 70%);
    border-radius:var(--radius);
  }

  /* utility: hide focus ring outline but keep accessibility */
  .btn:focus-visible{ outline:2px solid #000; outline-offset:3px }
  .play:focus-visible{ outline-color:#7c4dff }
</style>
</head>
<body>

  <div class="card">
    <div class="cover" role="img" aria-label="Album cover"></div>

    <div class="body">
      <div class="title">Dream Music</div>

      <div class="bar-wrap" aria-label="progress">
        <div class="bar"></div>
      </div>

      <div class="controls" aria-label="player controls">
        <!-- back -->
        <button class="btn" aria-label="Previous">
          <svg width="28" height="28" viewBox="0 0 24 24" fill="currentColor" aria-hidden="true">
            <path d="M6 6h2v12H6zM20 18l-10-6 10-6v12z"/>
          </svg>
        </button>

        <!-- play -->
        <button class="btn play" aria-label="Play">
          <svg width="26" height="26" viewBox="0 0 24 24" fill="currentColor" aria-hidden="true">
            <path d="M8 5v14l11-7z"/>
          </svg>
        </button>

        <!-- next -->
        <button class="btn" aria-label="Next">
          <svg width="28" height="28" viewBox="0 0 24 24" fill="currentColor" aria-hidden="true">
            <path d="M16 6h2v12h-2zM4 18l10-6L4 6v12z"/>
          </svg>
        </button>
      </div>

      <div class="meta">@Dream_with_Music_Bot</div>
    </div>

    <div class="glow"></div>
  </div>

</body>
</html>
