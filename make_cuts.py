from notcher import *
from layout import *
from slicer import *
from flexurizer import *
from test_slices import *
from vector import *
from output_svg import *
from read_ini import *
from visualizer import *
import sys


def make_cuts(stlFile, svgOutput, iniParamsFile):
	params = get_params(iniParamsFile)
	
	sliceDensity = params['slice_density']
	stl_scale = params['stl_scale']
	material_thickness = params['material_thickness']
	layout_margin = params['layout_margin']
	layout_width = params['layout_width']
	flexure_to_flexure_gap = params['flexure_to_flexure_gap']
	flexure_width = params['flexure_width']
	flexure_to_edge = params['flexure_to_edge']

	print("SLICING")
	slices = slice(stlFile, sliceDensity, stl_scale)

	print("GENERATING NOTCHES")
	(notches, notchLabels) = notch(slices)
	
	print("GENERATING FLEXURES")
	flexures = flexurize(slices, material_thickness, flexure_to_flexure_gap, flexure_width, flexure_to_edge)

	print("GENERATING LAYOUT")
	offsets = layout(slices, layout_margin, layout_width)
	
	print("GENERATING SVG")
	output_svg(svgOutput, slices, notches, notchLabels, material_thickness, flexure_width, flexures, offsets)

	print("VISUALIZING")
	visualizer(slices, notches, flexures)

if len(sys.argv) != 4:
	print("Usage: python make_cuts.py stl_file_path svg_output_file_path ini_param_file_path")
else:
	stlFile = sys.argv[1]
	svgOutput = sys.argv[2]
	iniFile = sys.argv[3]
	make_cuts(stlFile, svgOutput, iniFile)

# make_cuts('stl-files/cube.stl', 'svg-files/cube.svg')
# make_cuts('stl-files/chair.stl', 'svg-files/chair.svg') # http://www.thingiverse.com/thing:141703
# make_cuts('stl-files/rhino.stl', 'svg-files/rhino.svg')
# make_cuts('stl-files/bunny.stl', 'svg-files/bunny.svg')
# make_cuts('stl-files/sphere.stl', 'svg-files/sphere.svg')
# make_cuts('stl-files/pug.stl', 'svg-files/pug.svg')
# make_cuts('stl-files/heart.stl', 'svg-files/heart.svg')