# Maya Material Converter: Universal to Phong

## Description  
This Python script for **Autodesk Maya** converts all materials in a scene—regardless of their type (e.g., `usdPreviewSurface`, `aiStandardSurface`, or custom shaders)—into simple **Phong materials**. The script also preserves existing **texture connections** (like diffuse or base color textures) and reassigns them to the new Phong shader.

---

### Use Case  
I created this script to solve a problem when working with **USDz scenes** opened in Maya. Maya handles the `usdPreviewSurface` shader natively, but textures tend to disappear after converting or exporting the scene. This script converts `usdPreviewSurface` and other complex shaders into simpler **Phong materials**, while ensuring that all texture links remain intact, so you can transfer the scene to **3ds Max** without losing important textures.

---

## Features  
- **Universal Material Support**: Works with all shaders:
  - `usdPreviewSurface`  
  - Arnold's `aiStandardSurface`  
  - Native Maya shaders (Lambert, Blinn, etc.)  
  - Custom or imported plugin-based materials.  
- **Preserves Texture Links**: Transfers textures connected to `color`, `diffuseColor`, or `baseColor`.  
- **Shading Group Management**: Automatically reassigns new Phong materials to existing shading groups.  

---

## Why Use This Script?  
This script simplifies complex shading setups in Maya, especially when dealing with imported assets (USD, Arnold, etc.), making them lightweight and easier to manage.  

It’s ideal for:  
- Rendering with non-plugin renderers that require standard materials.  
- Cleaning up complex or unsupported shaders in a scene.  
- Preparing assets for export with simplified shaders.

---

## Installation  
1. Open Autodesk Maya.  
2. Open the **Script Editor** (`Windows > General Editors > Script Editor`).  
3. Copy and paste the script into the **Python** tab.  
4. Save it as a shelf button or run it directly.

---

## Usage  
1. Load your scene in Maya.  
2. Run the script.  
3. All materials will be converted to **Phong shaders**, and texture links will be transferred.

---

## Example  
### Before  
- Complex shaders like `usdPreviewSurface`, `aiStandardSurface`, or other custom materials.  
- Textures connected to attributes like `baseColor`, `diffuseColor`, or `color`.  

### After  
- All shaders replaced with lightweight **Phong materials**.  
- Texture connections preserved and assigned to the Phong's `color` attribute.  

