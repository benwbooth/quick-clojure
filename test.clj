#!/usr/bin/env quick-exec
(println "Hello World!")
(println "Press ENTER") (read-line)
(println "Hello World!")
;(leiningen.core.main/exit 3)
;(throw (ex-info nil {:exit-code 0 :suppress-msg true}))
(throw (ex-info "SomeException" {}))
