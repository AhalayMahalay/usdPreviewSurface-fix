import maya.cmds as cmds

def convert_all_materials_to_phong():
    """
    Converts all materials of any type (including usdPreviewSurface, Arnold, etc.) to Phong materials,
    while preserving texture connections.
    """
    # List all shading engines
    shading_engines = cmds.ls(type="shadingEngine")

    # Keep track of converted materials to avoid duplicates
    converted_materials = {}

    for sg in shading_engines:
        # Find the material connected to the shading group's surfaceShader slot
        surface_shader = cmds.listConnections(f"{sg}.surfaceShader", source=True, destination=False)
        if not surface_shader:
            continue

        old_material = surface_shader[0]

        # Skip if already converted
        if old_material in converted_materials:
            continue

        # Create a new Phong material
        phong_material = cmds.shadingNode("phong", asShader=True, name=f"{old_material}_phong")

        # Copy texture connections (attempt to transfer textures from color/diffuse attributes)
        copy_texture_connections(old_material, phong_material)

        # Reassign the new Phong material to the shading group
        cmds.connectAttr(f"{phong_material}.outColor", f"{sg}.surfaceShader", force=True)

        # Track the conversion
        converted_materials[old_material] = phong_material

        print(f"Converted {old_material} to {phong_material}")

    print("All materials successfully converted to Phong materials.")

def copy_texture_connections(old_material, new_material):
    """
    Copies texture connections from the old material to the new Phong material.
    Searches common attributes like color, diffuseColor, etc.
    """
    # List of common attributes where textures might be connected
    color_attributes = ["color", "diffuseColor", "baseColor", "diffuse"]

    for attr in color_attributes:
        # Check if the attribute exists on the old material
        if cmds.attributeQuery(attr, node=old_material, exists=True):
            # Check for connected texture
            connections = cmds.listConnections(f"{old_material}.{attr}", source=True, destination=False)
            if connections:
                texture_node = connections[0]
                # Connect the texture to the new Phong material's color
                cmds.connectAttr(f"{texture_node}.outColor", f"{new_material}.color", force=True)
                print(f"Transferred texture from {old_material}.{attr} to {new_material}.color")
                return  # Stop after transferring the first valid connection

# Run the script
convert_all_materials_to_phong()
