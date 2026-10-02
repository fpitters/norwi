# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Overview

Norwi is a small desktop Norwegian→English translator. It translates the current X11/system text selection and shows the result in a Tkinter window. There is no build system, linter, or test framework configured.

## Commands

- Setup: `python -m venv venv && source venv/bin/activate && pip install googletrans==4.0.2` (a `venv/` already exists locally and is gitignored)
- Run the app: `python norwi.py` (highlight some Norwegian text in any app first; the script reads it via `root.selection_get()` at startup and raises a `TclError` if nothing is selected)
- `test.py` is not a test suite. It is a standalone demo script that calls the live Google Translate API through `googletrans` (needs network). Run it with `python test.py`.

## Architecture

Everything lives in `norwi.py`, which runs top to bottom with no functions:
1. Creates a `googletrans.Translator`. In googletrans 4.x the API is async, so the single call is wrapped in `asyncio.run(...)`.
2. Creates the Tk root, then reads the current selection and translates it with `src='no', dest='en'`.
3. Renders the result in a read-only `ScrolledText` and enters `mainloop()`.

`test.py` shows the preferred async usage (`async with Translator(raise_exception=True)`), which `norwi.py` does not currently use.
