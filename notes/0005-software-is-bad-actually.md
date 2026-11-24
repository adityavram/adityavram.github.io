---
title: Software is bad, actually
date: 2026-11-23
tags: [software, engineering, simplicity]
status: public
---

Software is a place where things break in ways the person running it does not understand. We treat it as good, but more software is not good. That is exponentially more true with agentic codebases. The ideal is short and easy to understand, and it does exactly what the business or the person needs.

## Where more breaks

More code is more surface area for bugs. Most failures are in how one line meets the next, not in the line itself. No one running the software holds a million-line codebase in their head. The bug lives in the gap between what any one person understands and what the code actually does. This is not a feeling. It is structural: the probability a codebase behaves as its author intended falls as it grows, because the assumptions any one line depends on spread across more lines than any one person tracks.

## The agentic multiplier

A coding agent makes this worse. Give an agent a 50-line problem and it returns a 1000-line solution. The agent piles on error handling for cases that will never happen, logging no one reads, config no one sets, and abstraction layers the core logic does not need. The aggregate is 20 times the code, and no one can hold it in their head. The agent optimizes for "looks thorough" because that rates well, not for "does the job" — the same failure mode as the verbose-writing agent, and for the same reason: the model cannot see the whole from inside the generation.

## Why agents cannot clean it up

You might think the answer is to keep agents always on and let them clean up the software. That won't work. The agents fail too. They cause infrastructure overload, and the cost is too high. But the main reason is that continuous rolling outages are continuous outages. The root cause of the software outage is a different outage each time. It is still a user-facing outage. The agent that cleans up is part of the same failure surface. It is not a repair layer above it.

## Less is more

qmail is a mail server D. J. Bernstein wrote in the 1990s. It is roughly a fifth the size of sendmail and had one remote security hole in its first seven years. Bernstein offered $500 for any remote hole; sendmail had many. Less code, fewer places to fail.

The first grep, written by Doug McIlroy in 1973, was a few hundred lines. It did one thing: print lines matching a pattern. The grep on a modern Linux distribution is larger by orders of magnitude. The job did not get orders of magnitude bigger. The original did the job.

Slack desktop, in its early Electron versions, used roughly a gigabyte of RAM to run one chat application. The same application as a terminal client — weechat, irrsi — uses megabytes. Electron bundles a full browser and a JavaScript runtime to do one task, because writing it as a web page was faster to ship. More software, more memory, no more capability.

## The ideal

The ideal is not less than this, and not more. A 50-line script that does the job beats a 1000-line program that does the job and six other things. The six other things are where the bugs live, and none of them is the job.
