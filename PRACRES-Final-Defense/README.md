# Susulung king Pyalung: final defense deck

Nine-slide HTML presentation for the Practical Research 1 final defense (Psychology Group, HAU 12 - Aaron), built from the design brainstorm, the LAS Findings, and the Final Defense Scripts doc.

## Use it

Open `Susulung-king-Pyalung-Final-Defense.html` in Chrome or Edge. It is one self-contained file (fonts, seals and QR are embedded), so it runs offline. Copy it to both the primary and the backup laptop.

| Key | Action |
|---|---|
| `→` `Space` `PgDn` or click | Next step or slide (clickers work) |
| `←` `PgUp` | Back one step |
| `1`–`9` | Jump to a slide, fully built (for Q&A) |
| `P` | Presenter view: scripts, cues, word counts, pace timer |
| `F` | Full screen |
| `G` | Slide picker |
| `R` | Replay the current slide from its first step |
| `E` | Evidence and scope panel (optional, for Q&A) |
| `V` | Full reference list inside the file |
| `T` | Start or pause the timer |

Nothing advances on its own. Presenter view opens a second window, so allow pop-ups for the file. Drag it to the laptop screen and put the main window on the projector.

`Ctrl+P` prints every slide fully built, one per page (use "Save as PDF" for a static backup).

## Edit it

Edit `deck.src.html`, then run `python3 build.py` to rebuild the single file. Scripts, cues and timings live in the `NOTES` array near the bottom of the source.

## Check before the defense

- The guidelines mention PowerPoint files; confirm with the adviser that an HTML deck is accepted. The printed PDF is a fallback.
- The QR code is the one from the proposal deck. It opens `https://q.me-qr.com/qqtihfix`; confirm it lands on references only, not the shared research folder.
- Presenter view flags every script that differs from the script doc: Leon's was drafted (his section was empty), Matthew's was shortened to fit 75 words, Michan's was rewritten to match the final SSOP 2 themes, Chase's no longer says "verified", Rinoa's says "Luzon", and Wohan's quote includes "simply".
- Test on the classroom projector: contrast, text size, and the clicker.

## LAS files

The final LAS are the Google Docs "LAS Findings (final)" and "LAS Discussion (final)" in the DEADLINES folder on Drive. They cover seven psychologists (Q-CLZ-01 is Interviewee 7) and 203 extracts. The `.docx` files in `LAS-revised/` are earlier six-participant drafts, kept for reference only; do not upload them.
