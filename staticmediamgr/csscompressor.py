#! /usr/bin/env python
"""
CSS Compressor

:author: Corey Oordt <coordt@washingtontimes.com>
copyright (c) 2009 The Washington Times
Code licensed under the new BSD license

This code is ported from YUI Compressor
"""
import re

def remove_comments(css):
    # compile the comment block using the flags multiline and dotall so that
    # the dot will see newlines
    comment_block = re.compile(r'/\*.*?\*/', re.M|re.S)
    
    comment_line = re.compile(r'//.*')
    new_css = comment_block.sub(r'', css)
    return comment_line.sub(r'', new_css)

def normalize_whitespace(css):
    """
    Convert all whitespace, including line endings, to a single space
    """
    return re.sub(r'\s+', ' ', css)

def convert_boxmodelhack(css):
    """
    Make a pseudo class for the Box Model Hack: "\"}\""
    """
    return re.sub(r'"\\"}\\""', '___PSEUDOCLASSBMH___', css)

def restore_boxmodelhack(css):
    """Replace the pseudo class for the Box Model Hack"""
    return re.sub('___PSEUDOCLASSBMH___', '"\\"}\\""', css)


def remove_extra_spaces(css):
    """
    Remove the spaces before the things that should not have spaces before them.
    But, be careful not to turn "p :link {...}" into "p:link{...}"
    Swap out any pseudo-class colons with the token, and then swap back.
    """
    pattern = re.compile(r"(^|\})(([^\{:])+:)+([^\{]*\{)")
    repl_colons = lambda x: x.group(0).replace(':', '___PSEUDOCLASSCOLON___')
    new_css = pattern.sub(repl_colons, css)
    new_css = re.sub(r"\s+([!{};:>+\(\)\],])", '\g<1>', new_css)
    new_css = new_css.replace('___PSEUDOCLASSCOLON___', ':')
    
    # Remove the spaces after the things that should not have spaces after them.
    return re.sub(r"([!{}:;>+\(\[,])\s+", "\g<1>", new_css)


def add_missing_semicolon(css):
    return re.sub(r"([^;\}])}", "\g<1>;}", css)

def minify_zeros(css):
    # Replace 0(px,em,%) with 0.
    new_css = re.sub(r"([\s:])(0)(px|em|%|in|cm|mm|pc|pt|ex)", "\g<1>\g<2>", css)
    
    # Replace 0 0 0 0; with 0.
    new_css = re.sub(r":\s*0\s+0\s+0\s+0\s*;?", ":0;", new_css)
    new_css = re.sub(r":\s*0\s+0\s+0\s*;?", ":0;", new_css)
    new_css = re.sub(r":\s*0\s+0\s*;?", ":0;", new_css)
    
    # Replace background-position:0; with background-position:0 0;
    new_css = new_css.replace("background-position:0;", "background-position:0 0;")
    
    # Replace 0.6 to .6, but only when preceded by : or a white-space
    return re.sub(r"(:|\s)0+\.(\d+)", "\g<1>.\g<2>", new_css)

def shorten_colors(css):
    # Shorten colors from rgb(51,102,153) to #336699
    # This makes it more likely that it'll get further compressed in the next step.
    pattern = re.compile(r"rgb\s*\(\s*(\d+),\s*(\d+),\s*(\d+)\s*\)")
    int2hex = lambda x: ("0%s" % hex(x)[2:])[-2:]
    convert_nums = lambda x: '#%s%s%s' % (int2hex(int(x.group(1))), int2hex(int(x.group(2))), int2hex(int(x.group(3))))
    new_css = pattern.sub(convert_nums, css)
    
    # Shorten colors from #AABBCC to #ABC. Note that we want to make sure
    # the color is not preceded by either ", " or =. Indeed, the property
    #     filter: chroma(color="#FFFFFF");
    # would become
    #     filter: chroma(color="#FFF");
    # which makes the filter break in IE.
    pattern = re.compile(r"(?<!=\")#([0-9a-f])\1([0-9a-f])\2([0-9a-f])\3", re.I)
    return pattern.sub('#\g<1>\g<2>\g<3>', new_css)

def remove_empty_rules(css):
    return re.sub(r"[^\}]+\{;?\}", "", css)

def replace_multiple_semicolons(css):
    return re.sub(r";;+", ';', css)

def compress_css(css):
    new_css = remove_comments(css)
    new_css = normalize_whitespace(new_css)
    new_css = convert_boxmodelhack(new_css)
    new_css = remove_extra_spaces(new_css)
    new_css = add_missing_semicolon(new_css)
    new_css = minify_zeros(new_css)
    new_css = shorten_colors(new_css)
    new_css = remove_empty_rules(new_css)
    new_css = replace_multiple_semicolons(new_css)
    new_css = restore_boxmodelhack(new_css)
    
    return new_css.strip()

def compress_cssfile(cssfilepath):
    csscontent = open(cssfilepath).read()
    return compress_css(csscontent)


if __name__ == "__main__":
    import sys
    
    if len(sys.argv) > 1:
        try:
            print compress_cssfile(sys.argv[1])
        except Exception, e:
            print e
            sys.exit()