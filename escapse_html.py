    # Implement the function escape_html(s), which replaces:
    # > with &gt;
    # < with &lt;
    # " with &quot;
    # & with &amp;
def escape_html(s):
    for (i, o) in ( ("&", "&amp;"),
                    (">", "&gt;"),
                    ("<", "&lt;"),
                    ('"', "&quote;")):
        s = s.replace(i, o)
    return s

#version2
"""
import cgi

def escape_html(s):
    return cgi.escape(s, quote = True)
"""
