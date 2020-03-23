import types
import colorsys 
import re

def hsv_to_rgb(*args):
    if len(args) == 1:
       h,s,v = args[0]
    else:
       h,s,v = args
    return colorsys.hsv_to_rgb(h,s,v)

def rgb_to_hsv(*args):
    if len(args) == 1:
       r,g,b = args[0]
    else:
       r,g,b = args
    return colorsys.rgb_to_hsv(r,g,b)

def string_to_rgb(s):
    try:
	s = s.lower()
	c = None
	if s in X11COLORS_BY_NAME:
	    c = X11COLORS_BY_NAME[s][3]
	elif (len(s)==4 or len(s)==7) and s[0]=="#":
	    hexpart = s[1:]
	    if len(hexpart)==3:
		hexpart = hexpart[0]+hexpart[0]+hexpart[1]+hexpart[1]+hexpart[2]+hexpart[2]
	    r = int(hexpart[0:2], 16)/255.0
	    g = int(hexpart[2:4], 16)/255.0
	    b = int(hexpart[4:6], 16)/255.0
	    c = [r,g,b]
	else:
	    s = s.replace(',',' ')
	    if "." in s:
		c = map(float,s.split())
	    else:
	        c = map(lambda x: int(x)/255.0, s.split())
	return c
    except:
	return None

def rgb_to_string(rgb):
    return "#%02x%02x%02x"%(round(rgb[0]*255), round(rgb[1]*255), round(rgb[2]*255))

def bwcontrast(rgb):
    '''
    Returns either 0 (signifying black) or 1 (signifying white) depending
    on which contrasts better with the given rgb color.
    Args:
        rgb	(3-vector) The color to contrast with.
    Returns:
        0 (black) or 1 (white)
    '''
    lightness = 0.213*rgb[0] + 0.715*rgb[1] + 0.072*rgb[2]
    if lightness < 0.5:
	return 1
    else:
	return 0

def interpolate( cstart, cend, ncolors ):
    '''
    Returns a list of colors linearly interpolated between two
    specified colors. (In fact, this will linearly interpolate
    between any two vectors - they don't have to be colors or
    even of length 3.)
    Args:
	cstart	(color vector) The color to start at.
	cend	(color vector) The color to end at.
	ncolors	(int) The number of colors in the final list.
		The result always includes cstart and cend, so ncolors
		should be >= 2,
    Returns:
	List of HSV color vectors. cstart is the first element,
	cend is the last.
    '''
    if ncolors < 2:
	return [cstart, cend]
    nsteps = ncolors - 1
    cdelta = []
    for i in range(len(cstart)):
	cdelta.append( float(cend[i]-cstart[i])/nsteps )
    colors = [cstart[:]]
    for i in range(nsteps):
	c = []
	for j in range(len(cstart)):
	    v = cstart[j] + (i+1)*cdelta[j]
	    if v > 1:
		v = math.fmod(v)
	    c.append( v )
	colors.append(c)
    return colors

__X11COLORS__ = \
'''aliceblue	#f0f8ff	240,248,255
antiquewhite	#faebd7	250,235,215
aqua	#00ffff	0,255,255
aquamarine	#7fffd4	127,255,212
azure	#f0ffff	240,255,255
beige	#f5f5dc	245,245,220
bisque	#ffe4c4	255,228,196
black	#000000	0,0,0
blanchedalmond	#ffebcd	255,235,205
blue	#0000ff	0,0,255
blueviolet	#8a2be2	138,43,226
brown	#a52a2a	165,42,42
burlywood	#deb887	222,184,135
cadetblue	#5f9ea0	95,158,160
chartreuse	#7fff00	127,255,0
chocolate	#d2691e	210,105,30
coral	#ff7f50	255,127,80
cornflowerblue	#6495ed	100,149,237
cornsilk	#fff8dc	255,248,220
crimson	#dc143c	220,20,60
cyan	#00ffff	0,255,255
darkblue	#00008b	0,0,139
darkcyan	#008b8b	0,139,139
darkgoldenrod	#b8860b	184,134,11
darkgray	#a9a9a9	169,169,169
darkgreen	#006400	0,100,0
darkgrey	#a9a9a9	169,169,169
darkkhaki	#bdb76b	189,183,107
darkmagenta	#8b008b	139,0,139
darkolivegreen	#556b2f	85,107,47
darkorange	#ff8c00	255,140,0
darkorchid	#9932cc	153,50,204
darkred	#8b0000	139,0,0
darksalmon	#e9967a	233,150,122
darkseagreen	#8fbc8f	143,188,143
darkslateblue	#483d8b	72,61,139
darkslategray	#2f4f4f	47,79,79
darkslategrey	#2f4f4f	47,79,79
darkturquoise	#00ced1	0,206,209
darkviolet	#9400d3	148,0,211
deeppink	#ff1493	255,20,147
deepskyblue	#00bfff	0,191,255
dimgray	#696969	105,105,105
dimgrey	#696969	105,105,105
dodgerblue	#1e90ff	30,144,255
firebrick	#b22222	178,34,34
floralwhite	#fffaf0	255,250,240
forestgreen	#228b22	34,139,34
fuchsia	#ff00ff	255,0,255
gainsboro	#dcdcdc	220,220,220
ghostwhite	#f8f8ff	248,248,255
gold	#ffd700	255,215,0
goldenrod	#daa520	218,165,32
gray	#808080	128,128,128
green	#008000	0,128,0
greenyellow	#adff2f	173,255,47
grey	#808080	128,128,128
honeydew	#f0fff0	240,255,240
hotpink	#ff69b4	255,105,180
indianred	#cd5c5c	205,92,92
indigo	#4b0082	75,0,130
ivory	#fffff0	255,255,240
khaki	#f0e68c	240,230,140
lavender	#e6e6fa	230,230,250
lavenderblush	#fff0f5	255,240,245
lawngreen	#7cfc00	124,252,0
lemonchiffon	#fffacd	255,250,205
lightblue	#add8e6	173,216,230
lightcoral	#f08080	240,128,128
lightcyan	#e0ffff	224,255,255
lightgoldenrodyellow	#fafad2	250,250,210
lightgray	#d3d3d3	211,211,211
lightgreen	#90ee90	144,238,144
lightgrey	#d3d3d3	211,211,211
lightpink	#ffb6c1	255,182,193
lightsalmon	#ffa07a	255,160,122
lightseagreen	#20b2aa	32,178,170
lightskyblue	#87cefa	135,206,250
lightslategray	#778899	119,136,153
lightslategrey	#778899	119,136,153
lightsteelblue	#b0c4de	176,196,222
lightyellow	#ffffe0	255,255,224
lime	#00ff00	0,255,0
limegreen	#32cd32	50,205,50
linen	#faf0e6	250,240,230
magenta	#ff00ff	255,0,255
maroon	#800000	128,0,0
mediumaquamarine	#66cdaa	102,205,170
mediumblue	#0000cd	0,0,205
mediumorchid	#ba55d3	186,85,211
mediumpurple	#9370db	147,112,219
mediumseagreen	#3cb371	60,179,113
mediumslateblue	#7b68ee	123,104,238
mediumspringgreen	#00fa9a	0,250,154
mediumturquoise	#48d1cc	72,209,204
mediumvioletred	#c71585	199,21,133
midnightblue	#191970	25,25,112
mintcream	#f5fffa	245,255,250
mistyrose	#ffe4e1	255,228,225
moccasin	#ffe4b5	255,228,181
navajowhite	#ffdead	255,222,173
navy	#000080	0,0,128
oldlace	#fdf5e6	253,245,230
olive	#808000	128,128,0
olivedrab	#6b8e23	107,142,35
orange	#ffa500	255,165,0
orangered	#ff4500	255,69,0
orchid	#da70d6	218,112,214
palegoldenrod	#eee8aa	238,232,170
palegreen	#98fb98	152,251,152
paleturquoise	#afeeee	175,238,238
palevioletred	#db7093	219,112,147
papayawhip	#ffefd5	255,239,213
peachpuff	#ffdab9	255,218,185
peru	#cd853f	205,133,63
pink	#ffc0cb	255,192,203
plum	#dda0dd	221,160,221
powderblue	#b0e0e6	176,224,230
purple	#800080	128,0,128
red	#ff0000	255,0,0
rosybrown	#bc8f8f	188,143,143
royalblue	#4169e1	65,105,225
saddlebrown	#8b4513	139,69,19
salmon	#fa8072	250,128,114
sandybrown	#f4a460	244,164,96
seagreen	#2e8b57	46,139,87
seashell	#fff5ee	255,245,238
sienna	#a0522d	160,82,45
silver	#c0c0c0	192,192,192
skyblue	#87ceeb	135,206,235
slateblue	#6a5acd	106,90,205
slategray	#708090	112,128,144
slategrey	#708090	112,128,144
snow	#fffafa	255,250,250
springgreen	#00ff7f	0,255,127
steelblue	#4682b4	70,130,180
tan	#d2b48c	210,180,140
teal	#008080	0,128,128
thistle	#d8bfd8	216,191,216
tomato	#ff6347	255,99,71
turquoise	#40e0d0	64,224,208
violet	#ee82ee	238,130,238
wheat	#f5deb3	245,222,179
white	#ffffff	255,255,255
whitesmoke	#f5f5f5	245,245,245
yellow	#ffff00	255,255,0
yellowgreen	#9acd32	154,205,50
'''

X11COLORS = map(lambda x:x.split('\t'), __X11COLORS__.strip().split('\n'))
X11COLORS_BY_NAME = {}
for clr in X11COLORS:
    clr[2] = map(int, clr[2].split(','))
    clr.append([ clr[2][0]/255.0, clr[2][1]/255.0, clr[2][2]/255.0 ])
    X11COLORS_BY_NAME[ clr[0] ] = clr