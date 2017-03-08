#!/bin/env python
import os, sys
import argparse
import logging
import vtk

global gDB
global gArgs
global gTarget
global gType

def render3DS(fName):
    importer = vtk.vtk3DSImporter()
    importer.ComputeNormalsOn()
    importer.SetFileName(fName)
    importer.Read()
    renWin = importer.GetRenderWindow()
    iren = vtk.vtkRenderWindowInteractor()
    iren.SetRenderWindow(renWin)
    renWin.SetSize(500,500)
    ren = importer.GetRenderer()
    ren.SetBackground(0.1,0.2,0.4)
    iren.Initialize()
    renWin.Render()
    iren.Start()

def renderSTL(fName):
    ren = vtk.vtkRenderer()
    renWin = vtk.vtkRenderWindow()
    renWin.AddRenderer(ren)
    iren = vtk.vtkRenderWindowInteractor()
    iren.SetRenderWindow(renWin)
    style = vtk.vtkInteractorStyleTrackballCamera()
    iren.SetInteractorStyle(style)
    polydata = loadStl(fName)
    ren.AddActor(polyDataToActor(polydata))
    ren.SetBackground(0.1, 0.1, 0.1)
    iren.Initialize()
    renWin.Render()
    iren.Start()

def loadStl(fname):
    reader = vtk.vtkSTLReader()
    reader.SetFileName(fname)
    reader.Update()
    polydata = reader.GetOutput()
    return polydata

def polyDataToActor(polydata):
    mapper = vtk.vtkPolyDataMapper()
    if vtk.VTK_MAJOR_VERSION <= 5:
        mapper.SetInput(polydata)
    else:
        mapper.SetInputData(polydata)
    actor = vtk.vtkActor()
    actor.SetMapper(mapper)
    actor.GetProperty().SetColor(0.5, 0.5, 1.0)
    return actor

def verify():
    global gArgs
    global gDb
    global gTarget
    global gType

    parser = argparse.ArgumentParser(description='qds_render')
    parser.add_argument('file', nargs='*', default=None)
    parser.add_argument('-v', '--verbose', dest='verbose', action = 'store_true', default=False, help='Verbose mode')
    gArgs = parser.parse_args()
    gTarget = ' '.join(gArgs.file)
    log_level = logging.INFO
    if gArgs.verbose:
        log_level = logging.DEBUG
    if not gTarget:
        parser.print_help()
        exit()
    logging.basicConfig(level=log_level)
    gDb = logging.getLogger(__name__)
    filename, file_extension = os.path.splitext(gTarget)

    if file_extension == '.stl' or file_extension == '.STL':
        gType = 1;
    elif file_extension == '.3ds' or file_extension == '.3DS':
        gType = 2;
    else:
        parser.print_help()
        exit()

def main():
    global gTarget
    if gType == 1 :
        renderSTL(gTarget)
    elif gType == 2:
        render3DS(gTarget)

if __name__ == '__main__':
    verify()
    main()
