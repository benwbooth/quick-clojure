quick-clojure
=============

Run clojure scripts and lein commands quickly using a persistent nREPL session. Heavily inspired by [grenchman](http://leiningen.org/grench.html). This script differs in grenchman in several ways: it is written in Python, so no compiling or downloading platform-specific binaries is required. Also, the script automatically starts a headless nREPL server if none is currently running (however, see the *Caveats* section below).

Installation
============

```pip install quick-clojure```

Usage
=====

The ```quick-clojure``` python package installs the ```quick```, ```quick-exec```, and ```quick-exec-p``` commands. ```quick``` is the main script. ```quick-exec``` and ```quick-exec-p``` are the equivalents of the ```lein-exec``` and ```lein-exec-p``` scripts. They are there for you to use in shebang lines. (See the excellent [lein-exec plugin](https://github.com/kumarshantanu/lein-exec) for more information).

```
Commands:

  eval          FORM                             Evals given form.
  repl          [PORT]                           Connects a repl to a running nREPL server.
  run           NAMESPACE[/FUNCTION] [ARGS...]   Runs existing defn.
  lein          [TASK ARGS...]                   Runs a Leiningen task.
  start         [PORT]                           Start a nREPL server.
  kill          [PORT]                           Kill a running nREPL server.
  restart       [PORT]                           Restart a running nREPL server.

Running with no arguments will read code from stdin.
```

Tips
======

[Repload](https://github.com/john2x/repload) Integration: You can force the server to run ```(repload)``` before each command by setting the ```REPLOAD``` environment variable. This should automatically reload any user-defined symbols. It should be useful if you're writing and testing development code.

You can set the ```DEBUG``` environment variable to debug nREPL message. The orange ones are client -> server messages, the red ones are server -> client messages.

Caveats
=========

There is currently a race condition when starting up the nREPL server for the first time, which could result in multiple nREPL servers starting up, only one of which is referenced by the ```~/.lein/.repl-port``` file. So if you are planning on running a bunch of code in parallel, start the server first with a ```quick start``` command, at least until I figure out how to fix it. Patches welcome :)

Right now returning an exit code using ```leiningen.core.main/exit``` results in a "Suppressed exit" message. The workaround is to use ```(throw (ex-info nil {:exit-code 0 :suppress-msg true}))``` to exit the script instead.

Also, stack traces for uncaught exceptions are currently written to the server's stderr instead of the client's, meaning that you may not see them. The workaround is to catch all exceptions at the top-level of your script and print the stack trace yourself. 

I have a pull request at [leiningen #1440](https://github.com/technomancy/leiningen/pull/1440) to fix these issues. It's my understanding that grenchman currently has the same issues, but the pull request should fix the problem for both the quick and grenchman projects.

Bugs
=========

I'm sure there are lots of them :) If you find any please write an issue or pull request so I can fix them.

