# coding=utf-8

from mako.template import Template
from mako.runtime import Context
from cStringIO import StringIO


if __name__ == '__main__':
    t = Template('hello ${name}')
    buf = StringIO()
    c = Context(buf, name='2332222')
    t.render_context(c)
    print buf.getvalue()
