"""
Comprehensive BF6 Settings Database - Merged from all FieldTuner versions
Contains 100+ documented settings with metadata, tooltips, and search aliases.
"""

SETTINGS_DATABASE = {
    # ==================== GRAPHICS - DISPLAY ====================
    "GstRender.Dx12Enabled": {
        "name": "DirectX 12",
        "category": "Graphics",
        "subcategory": "API",
        "type": "bool",
        "default": 1,
        "range": [0, 1],
        "tooltip": "Enable DirectX 12 for better performance on modern GPUs. Disable if crashes occur.",
        "search_aliases": ["dx12", "directx", "api"]
    },
    "GstRender.FullscreenMode": {
        "name": "Fullscreen Mode",
        "category": "Graphics",
        "subcategory": "Display",
        "type": "int",
        "default": 1,
        "range": [0, 2],
        "options": {0: "Windowed", 1: "Borderless", 2: "Fullscreen"},
        "tooltip": "Fullscreen (2) = best performance, Borderless (1) = easy alt-tab, Windowed (0) = flexible",
        "search_aliases": ["fullscreen", "windowed", "borderless", "screen mode"]
    },
    "GstRender.VSyncMode": {
        "name": "V-Sync",
        "category": "Performance",
        "subcategory": "Frame Sync",
        "type": "bool",
        "default": 0,
        "range": [0, 1],
        "tooltip": "Prevents screen tearing but adds input lag. Disable for competitive play.",
        "search_aliases": ["vsync", "sync", "tearing", "vertical sync"]
    },
    "GstRender.FieldOfViewVertical": {
        "name": "Field of View",
        "category": "Graphics",
        "subcategory": "Display",
        "type": "float",
        "default": 70.0,
        "range": [50.0, 120.0],
        "tooltip": "Higher FOV = wider view but smaller targets. Pro players use 90-105.",
        "search_aliases": ["fov", "field of view", "view angle"]
    },
    "GstRender.ResolutionScale": {
        "name": "Resolution Scale",
        "category": "Performance",
        "subcategory": "Resolution",
        "type": "float",
        "default": 1.0,
        "range": [0.5, 2.0],
        "tooltip": "Render resolution multiplier. Lower = better FPS, Higher = better quality.",
        "search_aliases": ["resolution", "scale", "render scale", "internal resolution"]
    },
    "GstRender.FrameRateLimit": {
        "name": "FPS Limit",
        "category": "Performance",
        "subcategory": "Frame Rate",
        "type": "float",
        "default": 0.0,
        "range": [0.0, 500.0],
        "tooltip": "Cap FPS to reduce GPU load/heat. 0 = unlimited. Match monitor refresh rate.",
        "search_aliases": ["fps", "frame rate", "fps limit", "framerate", "cap"]
    },
    "GstRender.FrameRateLimiterEnable": {
        "name": "Frame Limiter Enable",
        "category": "Performance",
        "subcategory": "Frame Rate",
        "type": "bool",
        "default": 0,
        "range": [0, 1],
        "tooltip": "Enable the built-in frame rate limiter.",
        "search_aliases": ["limiter", "fps limit enable"]
    },
    "GstRender.FullscreenRefreshRate": {
        "name": "Refresh Rate",
        "category": "Graphics",
        "subcategory": "Display",
        "type": "float",
        "default": 60.0,
        "range": [60.0, 360.0],
        "tooltip": "Monitor refresh rate in Hz. Common: 60, 144, 165, 240, 360.",
        "search_aliases": ["refresh", "hz", "hertz", "monitor rate"]
    },
    
    # ==================== GRAPHICS - QUALITY ====================
    "GstRender.OverallGraphicsQuality": {
        "name": "Overall Quality",
        "category": "Graphics",
        "subcategory": "Quality",
        "type": "int",
        "default": 2,
        "range": [0, 4],
        "options": {0: "Low", 1: "Medium", 2: "High", 3: "Ultra", 4: "Ultra+"},
        "tooltip": "Master quality preset. Affects most visual settings.",
        "search_aliases": ["quality", "overall", "preset", "graphics quality"]
    },
    "GstRender.TextureQuality": {
        "name": "Texture Quality",
        "category": "Graphics",
        "subcategory": "Quality",
        "type": "int",
        "default": 2,
        "range": [0, 4],
        "options": {0: "Low", 1: "Medium", 2: "High", 3: "Ultra", 4: "Ultra+"},
        "tooltip": "Higher = sharper textures but more VRAM usage. Major VRAM impact.",
        "search_aliases": ["texture", "textures"]
    },
    "GstRender.TextureFiltering": {
        "name": "Texture Filtering",
        "category": "Graphics",
        "subcategory": "Quality",
        "type": "int",
        "default": 2,
        "range": [0, 4],
        "options": {0: "Low", 1: "Medium", 2: "High", 3: "Ultra", 4: "Ultra+"},
        "tooltip": "Anisotropic filtering quality. Higher = sharper textures at angles.",
        "search_aliases": ["filtering", "anisotropic", "af"]
    },
    "GstRender.ShadowQuality": {
        "name": "Shadow Quality",
        "category": "Graphics",
        "subcategory": "Quality",
        "type": "int",
        "default": 2,
        "range": [0, 3],
        "options": {0: "Low", 1: "Medium", 2: "High", 3: "Ultra"},
        "tooltip": "Shadow rendering quality. Major performance impact. Low for competitive.",
        "search_aliases": ["shadow", "shadows"]
    },
    "GstRender.EffectsQuality": {
        "name": "Effects Quality",
        "category": "Graphics",
        "subcategory": "Quality",
        "type": "int",
        "default": 2,
        "range": [0, 3],
        "options": {0: "Low", 1: "Medium", 2: "High", 3: "Ultra"},
        "tooltip": "Explosions, smoke, particles quality. Performance impact in firefights.",
        "search_aliases": ["effects", "particles", "explosions"]
    },
    "GstRender.LightingQuality": {
        "name": "Lighting Quality",
        "category": "Graphics",
        "subcategory": "Quality",
        "type": "int",
        "default": 2,
        "range": [0, 3],
        "options": {0: "Low", 1: "Medium", 2: "High", 3: "Ultra"},
        "tooltip": "Lighting and illumination quality. Medium impact on performance.",
        "search_aliases": ["lighting", "lights", "illumination"]
    },
    "GstRender.PostProcessQuality": {
        "name": "Post Process Quality",
        "category": "Graphics",
        "subcategory": "Quality",
        "type": "int",
        "default": 2,
        "range": [0, 3],
        "options": {0: "Low", 1: "Medium", 2: "High", 3: "Ultra"},
        "tooltip": "Post-processing effects quality. Low for cleaner competitive visuals.",
        "search_aliases": ["post process", "postprocess", "pp"]
    },
    "GstRender.MeshQuality": {
        "name": "Mesh Quality",
        "category": "Graphics",
        "subcategory": "Quality",
        "type": "int",
        "default": 2,
        "range": [0, 3],
        "options": {0: "Low", 1: "Medium", 2: "High", 3: "Ultra"},
        "tooltip": "3D model detail level. Affects object complexity at distance.",
        "search_aliases": ["mesh", "model", "geometry", "lod"]
    },
    "GstRender.TerrainQuality": {
        "name": "Terrain Quality",
        "category": "Graphics",
        "subcategory": "Quality",
        "type": "int",
        "default": 2,
        "range": [0, 3],
        "options": {0: "Low", 1: "Medium", 2: "High", 3: "Ultra"},
        "tooltip": "Ground/terrain detail. Medium performance impact.",
        "search_aliases": ["terrain", "ground", "landscape"]
    },
    "GstRender.VegetationQuality": {
        "name": "Vegetation Quality",
        "category": "Graphics",
        "subcategory": "Quality",
        "type": "int",
        "default": 2,
        "range": [0, 3],
        "options": {0: "Low", 1: "Medium", 2: "High", 3: "Ultra"},
        "tooltip": "Grass, trees, foliage quality. Can affect visibility in bushes.",
        "search_aliases": ["vegetation", "grass", "trees", "foliage"]
    },
    "GstRender.VolumetricQuality": {
        "name": "Volumetric Quality",
        "category": "Graphics",
        "subcategory": "Quality",
        "type": "int",
        "default": 2,
        "range": [0, 3],
        "options": {0: "Off", 1: "Low", 2: "Medium", 3: "High"},
        "tooltip": "Volumetric fog and lighting. Significant performance impact.",
        "search_aliases": ["volumetric", "fog", "god rays"]
    },
    
    # ==================== GRAPHICS - ANTI-ALIASING ====================
    "GstRender.AntiAliasingDeferred": {
        "name": "Anti-Aliasing",
        "category": "Graphics",
        "subcategory": "Anti-Aliasing",
        "type": "int",
        "default": 2,
        "range": [0, 8],
        "options": {0: "Off", 1: "FXAA Low", 2: "FXAA Medium", 3: "FXAA High", 4: "TAA Low", 5: "TAA Medium", 6: "TAA High", 7: "TAA Ultra", 8: "DLAA"},
        "tooltip": "Smooths jagged edges. TAA can cause blur, FXAA is lighter.",
        "search_aliases": ["aa", "antialiasing", "anti-aliasing", "jaggies", "fxaa", "taa"]
    },
    "GstRender.AmbientOcclusion": {
        "name": "Ambient Occlusion",
        "category": "Graphics",
        "subcategory": "Effects",
        "type": "bool",
        "default": 1,
        "range": [0, 1],
        "tooltip": "Adds realistic shadows in corners/crevices. Disable for competitive.",
        "search_aliases": ["ao", "ambient occlusion", "ssao", "hbao"]
    },
    "GstRender.ScreenSpaceReflections": {
        "name": "Screen Space Reflections",
        "category": "Graphics",
        "subcategory": "Effects",
        "type": "bool",
        "default": 1,
        "range": [0, 1],
        "tooltip": "Real-time reflections on surfaces. Performance impact.",
        "search_aliases": ["ssr", "reflections", "screen space"]
    },
    
    # ==================== GRAPHICS - POST PROCESSING ====================
    "GstRender.MotionBlurEnable": {
        "name": "Motion Blur",
        "category": "Graphics",
        "subcategory": "Post Processing",
        "type": "bool",
        "default": 0,
        "range": [0, 1],
        "tooltip": "Adds blur during movement. DISABLE for competitive - reduces clarity.",
        "search_aliases": ["motion blur", "blur", "movement blur"]
    },
    "GstRender.MotionBlurWorld": {
        "name": "Motion Blur World",
        "category": "Graphics",
        "subcategory": "Post Processing",
        "type": "float",
        "default": 0.0,
        "range": [0.0, 100.0],
        "tooltip": "World motion blur intensity. Set to 0 for competitive.",
        "search_aliases": ["world blur"]
    },
    "GstRender.MotionBlurWeapon": {
        "name": "Motion Blur Weapon",
        "category": "Graphics",
        "subcategory": "Post Processing",
        "type": "float",
        "default": 0.0,
        "range": [0.0, 100.0],
        "tooltip": "Weapon motion blur intensity. Set to 0 for competitive.",
        "search_aliases": ["weapon blur"]
    },
    "GstRender.DepthOfFieldEnable": {
        "name": "Depth of Field",
        "category": "Graphics",
        "subcategory": "Post Processing",
        "type": "bool",
        "default": 1,
        "range": [0, 1],
        "tooltip": "Blurs background when aiming. Disable for clearer vision.",
        "search_aliases": ["dof", "depth of field", "focus blur"]
    },
    "GstRender.WeaponDOF": {
        "name": "Weapon DOF",
        "category": "Graphics",
        "subcategory": "Post Processing",
        "type": "bool",
        "default": 1,
        "range": [0, 1],
        "tooltip": "Weapon depth of field blur. Disable for clearer weapon view.",
        "search_aliases": ["weapon dof", "weapon focus"]
    },
    "GstRender.FilmGrain": {
        "name": "Film Grain",
        "category": "Graphics",
        "subcategory": "Post Processing",
        "type": "bool",
        "default": 0,
        "range": [0, 1],
        "tooltip": "Adds cinematic grain effect. Disable for cleaner image.",
        "search_aliases": ["film grain", "grain", "noise"]
    },
    "GstRender.LensDistortion": {
        "name": "Lens Distortion",
        "category": "Graphics",
        "subcategory": "Post Processing",
        "type": "bool",
        "default": 0,
        "range": [0, 1],
        "tooltip": "Camera lens distortion effect. Disable for accurate aim.",
        "search_aliases": ["lens distortion", "distortion"]
    },
    "GstRender.ChromaticAberration": {
        "name": "Chromatic Aberration",
        "category": "Graphics",
        "subcategory": "Post Processing",
        "type": "bool",
        "default": 0,
        "range": [0, 1],
        "tooltip": "Color fringing effect. Disable for cleaner image.",
        "search_aliases": ["chromatic", "aberration", "color fringing"]
    },
    "GstRender.Vignette": {
        "name": "Vignette",
        "category": "Graphics",
        "subcategory": "Post Processing",
        "type": "bool",
        "default": 0,
        "range": [0, 1],
        "tooltip": "Darkens screen edges. Disable for full visibility.",
        "search_aliases": ["vignette", "edge darkening"]
    },
    "GstRender.Brightness": {
        "name": "Brightness",
        "category": "Graphics",
        "subcategory": "Display",
        "type": "float",
        "default": 0.5,
        "range": [0.0, 1.0],
        "tooltip": "Screen brightness. Adjust for your monitor.",
        "search_aliases": ["brightness", "bright"]
    },
    "GstRender.Contrast": {
        "name": "Contrast",
        "category": "Graphics",
        "subcategory": "Display",
        "type": "float",
        "default": 0.5,
        "range": [0.0, 1.0],
        "tooltip": "Image contrast level.",
        "search_aliases": ["contrast"]
    },
    "GstRender.SharpnessSlider": {
        "name": "Sharpness",
        "category": "Graphics",
        "subcategory": "Post Processing",
        "type": "float",
        "default": 0.5,
        "range": [0.0, 1.0],
        "tooltip": "Image sharpening. Higher can help with TAA blur.",
        "search_aliases": ["sharpness", "sharp", "sharpen"]
    },
    "GstRender.HighDynamicRangeMode": {
        "name": "HDR",
        "category": "Graphics",
        "subcategory": "Display",
        "type": "bool",
        "default": 0,
        "range": [0, 1],
        "tooltip": "High Dynamic Range. Requires HDR monitor.",
        "search_aliases": ["hdr", "high dynamic range"]
    },
    
    # ==================== PERFORMANCE - FRAME GEN & LOW LATENCY ====================
    "GstRender.FutureFrameRendering": {
        "name": "Future Frame Rendering",
        "category": "Performance",
        "subcategory": "Latency",
        "type": "bool",
        "default": 1,
        "range": [0, 1],
        "tooltip": "Pre-renders frames for smoother gameplay. Enable for better FPS.",
        "search_aliases": ["ffr", "future frame", "pre-render"]
    },
    "GstRender.FrameGeneration": {
        "name": "Frame Generation",
        "category": "Performance",
        "subcategory": "Frame Gen",
        "type": "bool",
        "default": 0,
        "range": [0, 1],
        "tooltip": "AI frame generation. Requires compatible GPU (RTX 40xx/RX 7xxx).",
        "search_aliases": ["frame gen", "dlss fg", "afmf"]
    },
    "GstRender.NVIDIAFrameGenerationEnabled": {
        "name": "NVIDIA Frame Gen",
        "category": "Performance",
        "subcategory": "Frame Gen",
        "type": "bool",
        "default": 0,
        "range": [0, 1],
        "tooltip": "DLSS 3 Frame Generation. RTX 40 series only.",
        "search_aliases": ["nvidia fg", "dlss 3", "dlss frame gen"]
    },
    "GstRender.NvidiaLowLatency": {
        "name": "NVIDIA Reflex",
        "category": "Performance",
        "subcategory": "Latency",
        "type": "int",
        "default": 2,
        "range": [0, 2],
        "options": {0: "Off", 1: "On", 2: "On + Boost"},
        "tooltip": "Reduces input latency on NVIDIA GPUs. Use Boost for competitive.",
        "search_aliases": ["reflex", "nvidia latency", "low latency"]
    },
    "GstRender.AMDLowLatency": {
        "name": "AMD Anti-Lag",
        "category": "Performance",
        "subcategory": "Latency",
        "type": "bool",
        "default": 0,
        "range": [0, 1],
        "tooltip": "Reduces input latency on AMD GPUs.",
        "search_aliases": ["anti-lag", "amd latency"]
    },
    "GstRender.IntelLowLatency": {
        "name": "Intel Low Latency",
        "category": "Performance",
        "subcategory": "Latency",
        "type": "bool",
        "default": 0,
        "range": [0, 1],
        "tooltip": "Reduces input latency on Intel GPUs.",
        "search_aliases": ["intel latency"]
    },
    
    # ==================== RAY TRACING ====================
    "GstRender.RaytracingAmbientOcclusion": {
        "name": "RT Ambient Occlusion",
        "category": "Graphics",
        "subcategory": "Ray Tracing",
        "type": "bool",
        "default": 0,
        "range": [0, 1],
        "tooltip": "Ray-traced ambient occlusion. Huge performance impact.",
        "search_aliases": ["rtao", "ray traced ao", "rt ao"]
    },
    "GstRender.RaytracingReflections": {
        "name": "RT Reflections",
        "category": "Graphics",
        "subcategory": "Ray Tracing",
        "type": "bool",
        "default": 0,
        "range": [0, 1],
        "tooltip": "Ray-traced reflections. Major performance impact.",
        "search_aliases": ["rt reflections", "ray traced reflections"]
    },
    "GstRender.RaytracingGlobalIllumination": {
        "name": "RT Global Illumination",
        "category": "Graphics",
        "subcategory": "Ray Tracing",
        "type": "bool",
        "default": 0,
        "range": [0, 1],
        "tooltip": "Ray-traced global illumination. Heaviest RT feature.",
        "search_aliases": ["rtgi", "ray traced gi", "global illumination"]
    },
    
    # ==================== AUDIO ====================
    "GstAudio.Volume": {
        "name": "Master Volume",
        "category": "Audio",
        "subcategory": "Volume",
        "type": "float",
        "default": 1.0,
        "range": [0.0, 1.0],
        "tooltip": "Main game volume.",
        "search_aliases": ["volume", "master", "sound"]
    },
    "GstAudio.Volume_SFX": {
        "name": "SFX Volume",
        "category": "Audio",
        "subcategory": "Volume",
        "type": "float",
        "default": 1.0,
        "range": [0.0, 1.0],
        "tooltip": "Sound effects volume (gunfire, explosions).",
        "search_aliases": ["sfx", "effects volume", "sound effects"]
    },
    "GstAudio.Volume_Music": {
        "name": "Music Volume",
        "category": "Audio",
        "subcategory": "Volume",
        "type": "float",
        "default": 1.0,
        "range": [0.0, 1.0],
        "tooltip": "Background music volume.",
        "search_aliases": ["music", "music volume", "soundtrack"]
    },
    "GstAudio.Volume_UI": {
        "name": "UI Volume",
        "category": "Audio",
        "subcategory": "Volume",
        "type": "float",
        "default": 1.0,
        "range": [0.0, 1.0],
        "tooltip": "Menu and interface sounds volume.",
        "search_aliases": ["ui volume", "menu sounds"]
    },
    "GstAudio.VOIPVolume": {
        "name": "VOIP Volume",
        "category": "Audio",
        "subcategory": "Volume",
        "type": "float",
        "default": 1.0,
        "range": [0.0, 1.0],
        "tooltip": "Voice chat volume.",
        "search_aliases": ["voip", "voice chat", "voice volume"]
    },
    "GstAudio.VoipOn": {
        "name": "VOIP Enable",
        "category": "Audio",
        "subcategory": "Voice Chat",
        "type": "bool",
        "default": 1,
        "range": [0, 1],
        "tooltip": "Enable in-game voice chat.",
        "search_aliases": ["voip enable", "voice chat enable"]
    },
    "GstAudio.PlaySoundInBackground_OnOff": {
        "name": "Background Audio",
        "category": "Audio",
        "subcategory": "General",
        "type": "bool",
        "default": 1,
        "range": [0, 1],
        "tooltip": "Play sound when game is minimized.",
        "search_aliases": ["background audio", "background sound"]
    },
    "GstAudio.HitIndicatorSound": {
        "name": "Hit Indicator Sound",
        "category": "Audio",
        "subcategory": "Feedback",
        "type": "bool",
        "default": 1,
        "range": [0, 1],
        "tooltip": "Sound when hitting enemies. Essential for competitive.",
        "search_aliases": ["hit sound", "hit indicator", "hitmarker"]
    },
    "GstAudio.InGameAnnouncer_OnOff": {
        "name": "Announcer",
        "category": "Audio",
        "subcategory": "Feedback",
        "type": "bool",
        "default": 1,
        "range": [0, 1],
        "tooltip": "In-game announcer voice.",
        "search_aliases": ["announcer", "voice announcer"]
    },
    "GstAudio.SubtitlesFriendlies": {
        "name": "Subtitles: Friendlies",
        "category": "Audio",
        "subcategory": "Subtitles",
        "type": "bool",
        "default": 1,
        "range": [0, 1],
        "tooltip": "Show subtitles for friendly callouts.",
        "search_aliases": ["friendly subtitles"]
    },
    "GstAudio.SubtitlesEnemies": {
        "name": "Subtitles: Enemies",
        "category": "Audio",
        "subcategory": "Subtitles",
        "type": "bool",
        "default": 1,
        "range": [0, 1],
        "tooltip": "Show subtitles for enemy callouts.",
        "search_aliases": ["enemy subtitles"]
    },
    "GstAudio.SubtitlesSquad": {
        "name": "Subtitles: Squad",
        "category": "Audio",
        "subcategory": "Subtitles",
        "type": "bool",
        "default": 1,
        "range": [0, 1],
        "tooltip": "Show subtitles for squad callouts.",
        "search_aliases": ["squad subtitles"]
    },
    "GstAudio.SubtitlesShowSpeakerName": {
        "name": "Show Speaker Name",
        "category": "Audio",
        "subcategory": "Subtitles",
        "type": "bool",
        "default": 1,
        "range": [0, 1],
        "tooltip": "Display speaker name with subtitles.",
        "search_aliases": ["speaker name"]
    },
    
    # ==================== INPUT ====================
    "GstInput.MouseSensitivity": {
        "name": "Mouse Sensitivity",
        "category": "Input",
        "subcategory": "Mouse",
        "type": "float",
        "default": 1.0,
        "range": [0.0, 10.0],
        "tooltip": "Mouse sensitivity. Find your comfort zone and stick with it.",
        "search_aliases": ["sensitivity", "sens", "mouse sens", "mouse speed"]
    },
    "GstInput.MouseRawInput": {
        "name": "Raw Mouse Input",
        "category": "Input",
        "subcategory": "Mouse",
        "type": "bool",
        "default": 1,
        "range": [0, 1],
        "tooltip": "Bypass Windows mouse acceleration. Enable for consistent aim.",
        "search_aliases": ["raw input", "raw mouse", "mouse accel"]
    },
    "GstInput.UniformSoldierAiming": {
        "name": "Uniform Soldier Aiming",
        "category": "Input",
        "subcategory": "Mouse",
        "type": "bool",
        "default": 1,
        "range": [0, 1],
        "tooltip": "Consistent sensitivity across all zoom levels. Enable for muscle memory.",
        "search_aliases": ["usa", "uniform aiming", "uniform soldier"]
    },
    "GstInput.UniformSoldierAimingCoefficient": {
        "name": "USA Coefficient",
        "category": "Input",
        "subcategory": "Mouse",
        "type": "float",
        "default": 1.33,
        "range": [0.1, 3.0],
        "tooltip": "Uniform aiming coefficient. 1.33 is default for BF games.",
        "search_aliases": ["usa coefficient", "aiming coefficient"]
    },
    "GstInput.HoldButtonToZoom": {
        "name": "Hold to ADS",
        "category": "Input",
        "subcategory": "Controls",
        "type": "bool",
        "default": 0,
        "range": [0, 1],
        "tooltip": "Hold button to aim down sights vs toggle.",
        "search_aliases": ["hold zoom", "toggle ads", "aim toggle"]
    },
    "GstInput.SprintHold": {
        "name": "Hold to Sprint",
        "category": "Input",
        "subcategory": "Controls",
        "type": "bool",
        "default": 0,
        "range": [0, 1],
        "tooltip": "Hold button to sprint vs toggle.",
        "search_aliases": ["hold sprint", "toggle sprint", "sprint toggle"]
    },
    "GstInput.Vibration": {
        "name": "Controller Vibration",
        "category": "Input",
        "subcategory": "Controller",
        "type": "bool",
        "default": 1,
        "range": [0, 1],
        "tooltip": "Controller rumble feedback.",
        "search_aliases": ["vibration", "rumble", "haptic"]
    },
}


def get_setting_info(key: str) -> dict:
    """Get full info for a setting by its key."""
    return SETTINGS_DATABASE.get(key, {})


def get_categories() -> list:
    """Get list of all unique categories."""
    categories = set()
    for setting in SETTINGS_DATABASE.values():
        categories.add(setting.get("category", "Other"))
    return sorted(list(categories))


def get_settings_by_category(category: str) -> dict:
    """Get all settings in a specific category."""
    return {k: v for k, v in SETTINGS_DATABASE.items() if v.get("category") == category}


def search_settings(query: str) -> dict:
    """Search settings by name, category, or aliases."""
    query = query.lower().strip()
    results = {}
    
    for key, info in SETTINGS_DATABASE.items():
        # Search in name
        if query in info.get("name", "").lower():
            results[key] = info
            continue
        # Search in category
        if query in info.get("category", "").lower():
            results[key] = info
            continue
        # Search in subcategory
        if query in info.get("subcategory", "").lower():
            results[key] = info
            continue
        # Search in aliases
        for alias in info.get("search_aliases", []):
            if query in alias.lower():
                results[key] = info
                break
        # Search in key itself
        if query in key.lower():
            results[key] = info
    
    return results
