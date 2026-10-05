# Susulung king Pyalung: final defense deck

Nine-slide HTML presentation for the Practical Research 1 final defense (Psychology Group, HAU 12 - Aaron), built from the final LAS Findings and Discussion and the script doc.

## Use it

Open `Susulung-king-Pyalung-Final-Defense.html` in Chrome or Edge. It is one self-contained file (fonts, seals, QR, sound effects and music are embedded), so it runs offline. Copy it to both the primary and the backup laptop and plug in the speaker.

**One click per presenter.** Each click brings in the next presenter's part; the slide then builds by itself, timed to the script. Shared slides (4 and 8) take one more click when the second presenter starts.

| Input | Action |
|---|---|
| Click, `→`, `Space`, `PgDn` (clickers work) | Next presenter or slide |
| Right-click, `←`, `PgUp` | Back |
| `1`–`9` | Jump to a slide, fully built and silent (for Q&A) |
| `Home` | Restart from the lobby (resets music and timer) |
| `P` | Presenter view: scripts, cues, word counts, pace timer |
| `F` | Full screen |
| `G` | Slide picker |
| `M` | Music on or off |
| `[` `]` | Music quieter or louder |
| `S` | All sound on or off |
| `R` | Replay the current slide |
| `E` / `V` | Evidence panel / full reference list |
| `T` | Start or pause the timer |

`Ctrl+P` prints every slide fully built, one per page (use "Save as PDF" for a static backup).

## The opening skit (slide 1)

The deck opens on a lobby screen. The operator clicks the **main** screen (not the presenter window), so the browser allows sound:

1. **Click 1:** game sounds play over about 8 s (Welcome to Mobile Legends, Double Kill, Triple Kill, Maniac) while a clock on the phone screen races from 10:47 PM to 2:16 AM. The gamer plays; the mother walks in on "Maniac".
2. **Click 2, the instant she grabs the phone:** "Defeat". Mother: *"Ilang oras ka na diyan?! Alas-dos na!"* Then the catchphrase appears word by word as the psychologist says it: *"Ma'am, it was never about the clock. Hindi ilang oras, kundi kung naiilang ang bata sa kanyang mundo, kaya sa laro nagtatago."* Everyone faces the panel: *"Not how many hours they play, but how uneasy they feel each day."*
3. **Click 3:** the title appears and quiet background music starts.

The music fades out automatically on slide 9 (a soft "Victory" plays) and stays off for Q&A, including any number-key jumps.

## Edit it

Edit `deck.src.html`, then run `python3 build.py` to rebuild the single file. Scripts, cues and timings live in the `NOTES` array; per-slide animation timings are the `data-t` attributes (milliseconds after the click). Slide 3's dots and slide 4's coverage dots come from the coding workbook (Interviewees 1 to 7, 203 extracts).

## Check before the defense

- Rehearse the skit with the real speaker: set the laptop volume so the announcer is clear, then use `[` and `]` so the music is just noticeable under speech.
- Click once on the main window before starting; a click made only in the presenter window may not unlock sound.
- The guidelines mention PowerPoint files; confirm with the adviser that an HTML deck is accepted. The printed PDF is a fallback.
- The QR code opens `https://q.me-qr.com/qqtihfix`; confirm it lands on references only.
- If a presenter changes their script in the script doc, update the matching `NOTES` entry.

## LAS files

The final LAS are the Google Docs "LAS Findings (final)" and "LAS Discussion (final)" in the DEADLINES folder on Drive. The `.docx` files in `LAS-revised/` are earlier six-participant drafts, kept for reference only.
