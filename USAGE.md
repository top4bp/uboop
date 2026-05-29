# Using uboop

uboop is a Boop-like scratchpad for Ubuntu: paste text, run an action on it, get the result.

## Launch

```bash
python main.py
```

A window opens with a single large text editor.

## Basic Workflow

1. **Type or paste** any text into the editor.
2. **Press `Ctrl+K`** to open the command palette.
3. **Search** for an action by name (e.g. `camel`, `json`, `sha256`).
4. **Double-click** the action (or select it and press Enter) to run it.
5. The editor content is **replaced** with the result.

That's it — the same editor is both your input and output.

## Tips

- Actions run on the **entire editor contents**, not a selection.
- Want to chain actions? Just open the palette again (`Ctrl+K`) and pick another.
- Made a mistake? Use `Ctrl+Z` to undo the replacement.
- Drag the custom title bar to move the window; use its buttons to minimize/maximize/close.

## A Few Example Actions

| You have… | Try the action… | You get… |
|---|---|---|
| `hello world` | Camel Case | `helloWorld` |
| `{"b":1,"a":2}` | Format JSON / Sort JSON | indented JSON |
| `password123` | SHA256 Hash / MD5 Hash | the hash digest |
| `hello` | Base64 Encode / Base64 Decode | base64 round-trip |
| Lines of text | Sort Lines / Reverse Lines / Remove Duplicate Lines | reordered/cleaned lines |
| A JWT token | JWT Decode | decoded header & payload |
| `<xml>...</xml>` | Minify XML | single-line XML |
| `[{"a":1},{"a":2}]` | JSON to CSV / CSV to JSON | tabular conversion |
| (empty) | Random UUID / Random Hex Color / Random String | generated value |

Browse the full list inside the palette — just open it and scroll.

## Adding Your Own Action

1. Create a new file in `app/actions/`, e.g. `shout.py`.
2. Subclass `Action`:

   ```python
   from .base import Action

   class ShoutAction(Action):
       name = "Shout"
       def run(self, text: str) -> str:
           return text.upper() + "!!!"
   ```

3. Restart the app — the action is auto-discovered and shows up in the palette.

## Shortcuts

| Shortcut | What it does |
|---|---|
| `Ctrl+K` / `Ctrl+Shift+P` | Open command palette |
| `↑` / `↓` / `PgUp` / `PgDn` | Move selection in the palette |
| `Enter` | Run the highlighted action |
| `Esc` | Close command palette |
| `Ctrl+Z` / `Ctrl+Y` | Undo / redo (including action results) |
| `Ctrl+Q` | Quit |

