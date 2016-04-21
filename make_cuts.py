from notcher import *
from layout import *
from slicer import *
from flexurizer import *
from test_slices import *
from util import *

# https://pypi.python.org/pypi/svgwrite/
import svgwrite

def make_cuts(stlFile, svgOutput):
	slices = slice(stlFile, 2/10)
	# slices = test_box() # placeholder
	notches = notch(slices)
	# # flexures = flexurize(slices)

	for currentSlice in slices:
	 	slice_notches = notches[currentSlice]
	# 	#slice_flexures = flexures[slice]
	 	currentSlice.segments.extend(slice_notches)
	# 	#slice.segments.extend(slice_flexures)

	segments = layout(slices, 10, 400)
	
	svg = svgwrite.Drawing(svgOutput, profile='tiny')
	for segment in segments:
		svg.add(svg.line(
						mult(segment[0], 2), 
						mult(segment[1], 2), 
						stroke=svgwrite.rgb(0, 0, 0, '%'), 
						stroke_width=2))
	svg.save()

make_cuts('pug.stl', 'test.svg')