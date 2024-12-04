find -s ../mysite  | sed -e "s;[^/]*/;|____ ;g;s;____ |; |;g;s; | ;   ;g;s/^|//g"
