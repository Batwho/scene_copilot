'''
python add_more.py --folder {FOLDER} --model {modelname} --api-key {apikey}

check with node transpiler, describe with gemini, append dataset csv

if render crashes or takes too long, prompt user to enter description manually, then get embedding
'''
import os
import sys
import pandas as pd
import google.generativeai as genai
import bpy
import numpy as np
from sentence_transformers import SentenceTransformer
import time

def gemini_obj_desc(blenderfile, skip, use_gpu=False, API_KEY='', max_render_time=120):
    pi = np.pi
    curpath = os.getcwd()
    
    dims = bpy.context.object.dimensions
    maxdim = max(dims)

    # prepare model
    model = genai.GenerativeModel("gemini-1.5-flash")
    genai.configure(api_key=API_KEY)
    prompt = 'The images are all of the same 3D model in against a black background from different angles. Very briefly describe the model whilst ignoring the background.'

    # specify blender file and render format
    bpy.ops.wm.open_mainfile(filepath=blenderfile)
    bpy.context.scene.render.image_settings.file_format = 'PNG'
    
    # Set render settings
    bpy.data.scenes[0].render.engine = "CYCLES"

    if use_gpu:
        # Set the device_type
        bpy.context.preferences.addons[
            "cycles"
        ].preferences.compute_device_type = "CUDA" # or "OPENCL"

        # Set the device and feature set
        bpy.context.scene.cycles.device = "GPU"

        # get_devices() to let Blender detect GPU device
        bpy.context.preferences.addons["cycles"].preferences.get_devices()
        print(bpy.context.preferences.addons["cycles"].preferences.compute_device_type)
        for d in bpy.context.preferences.addons["cycles"].preferences.devices:
            d["use"] = 1 # Using all devices, include GPU and CPU
            print(d["name"], d["use"])
    else: print("Using CPU only...")

    # change render resolution
    bpy.context.scene.render.resolution_x = 1024
    bpy.context.scene.render.resolution_y = 1024

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
    z = [dist,-dist]
    rot = [pi/4, 0, pi/2]

    time_to_render = 0

    for i in range(2):
        for j in range(4):
            start = time.time()

            cam_obj.location = (x[j], y[j], z[i])
            lt_obj.location = (x[j], y[j], z[i])
            cam_obj.rotation_euler = rot
            bpy.ops.render.render(write_still=True)
            
            end = time.time()
            time_to_render = end - start
            if time_to_render > max_render_time and skip: 
                os.remove(f'{curpath}/temp.png')
                print(f'Skipping "{blenderfile}"...\n')
                return 'Too Big, please manually describe'

            img = genai.upload_file(f'{curpath}/temp.png')
            give_to_gemini.append(img)
            rot[2] = rot[2] + pi/2
            
        rot[0] = rot[0] + pi/2
    give_to_gemini.append(prompt)
    response = model.generate_content(give_to_gemini)
    
    for f in genai.list_files(): f.delete()

    os.remove(f'{curpath}/temp.png')

    print(response.text)

    return response.text


def getTextEmbed(text):
    embedder = SentenceTransformer('sentence-transformers/all-MiniLM-L6-v2')
    embedding = embedder.encode(text)
    return embedding

def clear_scene():
    """
    Removes all mesh and text objects from the scene.
    """
    bpy.ops.object.select_all(action='DESELECT')
    
    # Delete all mesh objects
    bpy.ops.object.select_by_type(type='MESH')
    bpy.ops.object.delete()
    
    # Delete all text objects
    bpy.ops.object.select_by_type(type='FONT')
    bpy.ops.object.delete()
    
    # Delete all cameras
    bpy.ops.object.select_by_type(type='CAMERA')
    bpy.ops.object.delete()
    
    # Delete all lights
    bpy.ops.object.select_by_type(type='LIGHT')
    bpy.ops.object.delete()

def create_cube():
    """
    Creates a cube in the scene.
    """
    bpy.ops.mesh.primitive_cube_add(size=2, location=(0, 0, 0))
    cube = bpy.context.active_object
    cube.name = "Material_Cube"
    return cube

def setup_camera():
    """
    Adds a camera to the scene and positions it to point at the cube.
    """
    bpy.ops.object.camera_add(location=(5, -5, 5), rotation=(math.radians(60), 0, math.radians(45)))
    camera = bpy.context.active_object
    bpy.context.scene.camera = camera

def setup_light():
    """
    Adds a light source to illuminate the cube.
    """
    bpy.ops.object.light_add(type='POINT', location=(4, -4, 6))
    light = bpy.context.active_object
    light.data.energy = 1000

def render_material(cube, material, output_path):
    """
    Applies a material to the cube, renders the scene, and saves the image.
    """
    # Apply the material to the cube
    if cube.data.materials:
        cube.data.materials[0] = material
    else:
        cube.data.materials.append(material)

    # Set render settings
    bpy.data.scenes[0].render.engine = "CYCLES"

    # Set the device_type
    bpy.context.preferences.addons[
        "cycles"
    ].preferences.compute_device_type = "CUDA" # or "OPENCL"

    # Set the device and feature set
    bpy.context.scene.cycles.device = "GPU"

    # get_devices() to let Blender detects GPU device
    bpy.context.preferences.addons["cycles"].preferences.get_devices()
    print(bpy.context.preferences.addons["cycles"].preferences.compute_device_type)
    for d in bpy.context.preferences.addons["cycles"].preferences.devices:
        d["use"] = 1 # Using all devices, include GPU and CPU
        print(d["name"], d["use"])
    bpy.context.scene.render.filepath = output_path
    bpy.context.scene.render.resolution_x = 1024
    bpy.context.scene.render.resolution_y = 1024
    bpy.context.scene.render.image_settings.file_format = 'PNG'

    # Render and save image
    bpy.ops.render.render(write_still=True)
    print(f"Rendered {material.name} and saved to {output_path}")

def gemini_mat_desc(api_key='', use_gpu=True, filename=''):

    bpy.ops.wm.open_mainfile(filepath=filename)

    # Path to save each render
    output_path = os.path.join(os.getcwd(), "temp.png")

    # Clear scene of any existing objects
    clear_scene()

    # Create a cube object
    cube = create_cube()
    
    # prepare model
    model = genai.GenerativeModel("gemini-1.5-flash")
    genai.configure(api_key=api_key)
    
    # Set up camera and light for visibility
    setup_camera()
    setup_light()

    embedder = SentenceTransformer('sentence-transformers/all-MiniLM-L6-v2')
    names = []
    descs = []
    embeds = []

    # Cycle through each material in the .blend file
    for material in bpy.data.materials:
        render_material(cube, material, output_path)
        
        # upload image to gemini and get a response
        img = genai.upload_file(f'temp.png')
        prompt = f'This is an image of a material applied to a cube in blender. Please describe a brief description of the material and no other information. You may use the name of the material, {material.name}, as a hint as to what the material is supposed to look like, but note that it might be misleading. If the materials appears to be missing (typically will be all pink), simply say "error" and nothing else.'
        response = model.generate_content([img, prompt])

        print(material.name + ":" + response.text)

        # clear files from gemini
        for f in genai.list_files():
            f.delete()
        
        names.append(material.name)
        descs.append(response.text)
        embedding = embedder.encode(response.text)
        embeds.append(embedding)
    
    df = pd.DataFrame(dict({'name': names, 'desc': descs, 'embed': embeds}))
    df.to_csv(path_or_buf=filename[:-6] + '.csv', index=False)
    return filename[:-6] + '.csv'

def main():
    i = 1
    skip = True
    use_gpu = True
    type = ''
    folder = ''
    outcsv = ''
    api_key = os.environ['GEM_KEY']
    max_render_time = 300
    while(i < len(sys.argv)):
        arg = sys.argv[i]
        match arg:
            case '--input-folder':
                i += 1
                folder = sys.argv[i]
            case '--no-skip':
                skip = False
            case '--materials':
                type = 'material'
                csvs = []
            case '--max-render-time':
                i += 1
                max_render_time = int(sys.argv[i])
            case '--api-key':
                i += 1
                api_key = sys.argv[i]
            case '--no-gpu':
                use_gpu = False
            case _:
                outcsv = sys.argv[i]
        i += 1

    if (outcsv == '' or folder == '') and type != 'material': 
        print('add_more.py usage:\npython add_more.py [--input-folder [FOLDER] | --no-skip | --materials | --max-render-time [TIME IN SECONDS] | --no-gpu | --api-key [GEMINI API KEY] | [OUTPUT CSV NAME]]')
        exit()
    elif outcsv[-4:] != '.csv':
        print('Error: output csv name must end in ".csv"')
        print('add_more.py usage:\npython add_more.py [--input-folder [FOLDER] | --no-skip | --materials | --max-render-time [TIME IN SECONDS] | --no-gpu | --api-key [GEMINI API KEY] | [OUTPUT CSV NAME]]')
        exit()

    try:
        files = os.listdir(folder)
        files = [file for file in files if file[-5:] != '.blend']
        print(files)
    except:
        print(f'Error: {folder} could not be accessed')
    
    # build csv
    df = pd.DataFrame(columns=['name', 'embed', 'desc'])

    issues = 0 # this value will be used to tell the user how many assets have issues describing
    for file in files:
        blenderfile = os.path.join(folder, file)

        if type == 'material':
            csvs.append(gemini_mat_desc(api_key=api_key, use_gpu=use_gpu, outcsv=outcsv, filename=blenderfile))

        else:
            desc = gemini_obj_desc(blenderfile, skip, use_gpu=use_gpu, API_KEY=api_key, max_render_time=max_render_time)

            if desc == 'Too Big, please manually describe':
                issues += 1
                embed = ''
            else: embed = getTextEmbed(desc)

    if type == 'material':
        dataframes = []

        for file_path in csvs:
            df = pd.read_csv(file_path)
            dataframes.append(df)
            os.remove(file_path)

        df = pd.concat(dataframes, ignore_index=True)

    try:
        df.to_csv(path_or_buf=outcsv)
        print(f'Created {outcsv}')
    except:
        print(f'something went wrong creating {outcsv}')
    df.loc[len(df)] = [file[:-6], desc, embed]
        
    

    if issues > 0:
        print(f'{issues} asset(s) were unable to be described automatically, please run "python manual_describe.py {outcsv}" to manually describe error-causing assets')

    


if __name__ == "__main__":
    main()
    
    
