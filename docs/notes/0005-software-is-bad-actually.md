
Software is a place where something can break, in a way the person running it does not understand. We treat it as good, but more software is not good. That is exponentially more true in a world of agentic codebases. The ideal is short and easy to understand, and it does exactly what the business or the person needs.

## Where more breaks

More code is more surface area for bugs. Every line is a place something can fail, and most failures are not in the line itself but in the way it meets the next one. The person running the software does not understand the whole, because no person can hold a million-line codebase in their head. The bug lives in the gap between what any one person understands and what the code actually does. This is not a feeling. It is structural: the probability that a codebase behaves as its author intended falls as the codebase grows, because the assumptions any one line depends on are spread across more lines than any one person tracks.

## The agentic multiplier

A coding agent makes this worse in a particular way. Give an agent a 50-line problem and it returns a 1000-line solution. The agent piles on error handling for cases that will never happen, logging no one reads, config no one sets, and abstraction layers the core logic does not need. The aggregate is 20 times the code for the same job, and no one can hold it in their head. The agent optimizes for "looks thorough" because thorough is what rates well, not for "does the job" — the same failure mode as the verbose-writing agent, and for the same reason: the model cannot see the whole from inside the generation.

## Less is more

qmail is a mail server D. J. Bernstein wrote in the 1990s. It is roughly a fifth the size of sendmail, the dominant server of the era, and it had one remote security hole in its first seven years. Bernstein offered $500 for any remote hole. sendmail had many. Less code, fewer places to fail.

The first grep, written by Doug McIlroy in 1973, was a few hundred lines. It did one thing: print lines matching a pattern. The grep on a modern Linux distribution is larger by orders of magnitude. The job did not get orders of magnitude bigger. The original did the job.

Slack desktop, in its early Electron versions, used roughly a gigabyte of RAM to run one chat application. The same application as a terminal client — weechat, irrsi — uses megabytes. Electron bundles a full browser and a JavaScript runtime to do one task, because writing it as a web page was faster to ship. More software, more memory, no more capability.

## The ideal

The ideal is not less than this, and not more. A 50-line script that does the job beats a 1000-line program that does the job and six other things. The six other things are where the bugs live, and none of them is the job.
