# [AI] Session Log

## [AI] Attribution Convention
[AI] Lines marked `[AI]` were written by the AI assistant.
[AI] Lines marked `[LC]` were written by me (Luis Chavez).
[AI] Unmarked lines are mine by default.

---

## [AI] Entry Template

[AI] Copy the block below for each new log entry.

```
### [LC] Entry — <date/time>

**Time / what I was doing:**


**What happened (error, success, decision):**


**What I asked AI, and what I did with the answer (used it, adapted it, rejected it):**


**What I'd tell a freshman about this:**

```

---

### [LC] Entry — 2026-07-15


**Time / what I was doing:**
4:30 PM: I was writing a simple test post request to the llama server on my machine.

**What happened (error, success, decision):**
I ran into some syntax and python specific errors, including .venv setup and installation mishaps.
I wrote main.py post request on my own and had Sonnet 5 review it. I'm not as experienced in python as I am in Rust/C++
so my simple function had many errors. I had a timeout bug, didn't set the timeout past the default (5 seconds) so timeout happened before
the model could respond.
I got it working shortly on my own after a little review and a few claude questions.

**What I asked AI, and what I did with the answer (used it, adapted it, rejected it):**
I asked claude about the errors, it provided me with a details 5 item list about each issue.
I attempted fixing the issues based on claude's response and reviewed some docs for POST syntax.
I accepted all of the AIs advice about syntax, I rejected its incorrect advice about the .venv as it was missing context. (wrong directory)

**What I'd tell a freshman about this:**
Making sure you understand every line of your code starts like this (especially with new concepts). Writing ugly functions, they break, you fix them and ask questions when you get stuck. Claude could've done this in seconds, but by doing this myself and having it review, I have the foundation.
Don't build your projects on a fragile base of understanding from reading output, have a strong foundation (for me it's writing new
concepts entirely on my own) (method might change/update in later entries).

