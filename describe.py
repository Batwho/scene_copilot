import os
import sys
import pandas as pd
import pygsheets as pyg
import google.generativeai as genai
import PIL.Image as pim
import bpy
import numpy as np

def gemini_desc(blenderfile):
    pi = np.pi
    curpath = os.getcwd()
    
    maxdim = 0

    dims = bpy.context.object.dimensions
    maxdim = max(dims)

    # prepare model
    model = genai.GenerativeModel("gemini-1.5-flash")
    genai.configure(api_key=os.environ['GEM_KEY'])
    prompt = 'The images are all of the same 3D model in against a black background from different angles. Very briefly describe the model whilst ignoring the background.'

    # specify blender file and render format
    bpy.ops.wm.open_mainfile(filepath=blenderfile)
    bpy.context.scene.render.image_settings.file_format = 'PNG'
    # bpy.context.preferences.addons['cycles'].preferences.compute_device_type = 'GPU'
    # bpy.context.preferences.addons['cycles'].preferences.devices['GPU'].use = True
    bpy.context.scene.cycles.device = 'GPU'

    # choose render destination
    bpy.context.scene.render.filepath = f'{curpath}/temp' 

    # create camera
    cam_data = bpy.data.cameras.new("Camera")
    cam_data.lens = 18

    # place camera
    cam_obj = bpy.data.objects.new("Camera", cam_data)

    # link camera to scene
    bpy.context.scene.collection.objects.link(cam_obj)

    # set camera as active
    bpy.context.scene.camera = cam_obj

    # create light so camera can see
    lt_data = bpy.data.lights.new(name="Light", type="POINT")
    lt_data.energy = 3000

    # create light object with light data
    lt_obj = bpy.data.objects.new(name="Light", object_data=lt_data)

    # link light object and make it active
    bpy.context.collection.objects.link(lt_obj)
    bpy.context.view_layer.objects.active = lt_obj
    
    give_to_gemini = []

    dist = maxdim * 2
    dist = max(2, dist)

    x = [dist,0,-dist,0]
    y = [0,dist,0,-dist]
    z = [dist,0,-dist]
    rot = [pi/4, 0, pi/2]

    for i in range(3):
        for j in range(4):
            cam_obj.location = (x[j], y[j], z[i])
            lt_obj.location = (x[j], y[j], z[i])
            cam_obj.rotation_euler = rot
            bpy.ops.render.render(write_still=True)
            img = genai.upload_file(f'{curpath}/temp.png')
            
            give_to_gemini.append(img)
            rot[2] = rot[2] + pi/2
        rot[0] = rot[0] + pi/4
    give_to_gemini.append(prompt)
    response = model.generate_content(give_to_gemini)
    
    for f in genai.list_files():
        f.delete()

    os.remove(f'{curpath}/temp.png')

    return response.text

n = len(sys.argv)
if n != 2:
    print("Please use the format: 'python create_csv.py [DIRECTORY OF PYTHON OBJECTS]")
    exit()
path = sys.argv[1]

desc = []
embed = []

# go thru every object in specified directory and get desciption
for object in os.listdir(path):
    # render 12 images
    desc.append(gemini_desc(f'{path}/{object}'))

    # remove files from model prompt
    for f in genai.list_files():
        print("\t", f.name)

print('\n\nResponses')
for idx, text in enumerate(desc):
    print(f'{idx}: {text}')

# df = pd.DataFrame(columns=['object', 'code', 'desc', 'embed'])


# addtodf = dict({'object': objects, 'path': paths})

# df = pd.DataFrame(addtodf)

# df.to_csv(path_or_buf='dataset.csv')
