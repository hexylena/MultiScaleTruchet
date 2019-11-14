import random


def header(author, title, width=1000, height=1000):
    return f"""<?xml version="1.0" encoding="utf-8"?>
    <svg
    xmlns:dc="http://purl.org/dc/elements/1.1/"
    xmlns:cc="http://creativecommons.org/ns#"
    xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#"
    xmlns:svg="http://www.w3.org/2000/svg"
    xmlns="http://www.w3.org/2000/svg"
    xmlns:sodipodi="http://sodipodi.sourceforge.net/DTD/sodipodi-0.dtd"
    xmlns:inkscape="http://www.inkscape.org/namespaces/inkscape"
    height="{height}"
    version="1.1"
    viewBox="0 0 {width} {height}"
    width="{width}"
    id="svg802"
    sodipodi:docname="out.svg"
    inkscape:version="0.92.3 (2405546, 2018-03-11)">
    >

<sodipodi:namedview
   pagecolor="#ffffff"
   bordercolor="#666666"
   borderopacity="1"
   objecttolerance="10"
   gridtolerance="10"
   guidetolerance="10"
   inkscape:pageopacity="0"
   inkscape:pageshadow="2"
   inkscape:window-width="1920"
   inkscape:window-height="1080"
   id="namedview1385"
   showgrid="false"
   inkscape:pagecheckerboard="true"
   inkscape:zoom="0.295"
   inkscape:cx="369.49153"
   inkscape:cy="430.50847"
   inkscape:window-x="0"
   inkscape:window-y="0"
   inkscape:window-maximized="0"
   inkscape:current-layer="svg802" />

    <metadata
        id="metadata808">
        <rdf:RDF>
        <cc:Work
            rdf:about="">
            <dc:format>image/svg+xml</dc:format>
            <dc:type
            rdf:resource="http://purl.org/dc/dcmitype/StillImage" />
            <dc:title></dc:title>
            <dc:creator>
            <cc:Agent>
                <dc:title>{author}</dc:title>
            </cc:Agent>
            </dc:creator>
            <dc:description>{title}</dc:description>
        </cc:Work>
        </rdf:RDF>
    </metadata>
    """


def footer():
    return "</svg>"


def random_color():
    return "".join([hex(random.choice(range(16)))[2] for _ in range(6)])
